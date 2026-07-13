"""
An airline agent that can buy, return and change flight tickets

We fly to a lot of places, so the agent interviews the passenger about what
they actually want out of a holiday, the climate, what they can afford to
spend once they land, the culture, the language, and narrows the catalogue
down for them rather than reciting it at them.

The agent talks to the human on stdin/stdout and uses strict tools so that
every action it takes arrives as a schema validated object. It loops until
the human is satisfied, at which point the model calls the `done` tool.

The modules you need to install to make this work are `passpy` and `anthropic`
"""

import sys
import itertools
from typing import TypedDict, Callable, Any
import passpy
import anthropic
from anthropic.types import ToolParam, MessageParam, ToolResultBlockParam

MODEL = "claude-opus-4-8"
SYSTEM = """
You are a ticket agent for Fandango Airlines. We fly out of Tel Aviv to many places.
You can search destinations, sell tickets, refund them and change them, using your tools.

Most passengers do not know where they want to go, they only know what they want
out of a holiday. Do not recite the catalogue at them. Interview them instead:
ask about the climate they like, what they want to spend once they land, the sort
of culture they are after, whether the language matters to them, how long a flight
they will tolerate. Ask about ONE thing at a time, in a natural way, and use what
they tell you to narrow the search. Three or four good questions is usually plenty.
When you are down to a handful of candidates, present them with a sentence each
saying why that place fits what the passenger asked for, and let them choose.

Always search before you quote a price, never invent destinations, flights or prices.
When the passenger names the flight they want, act on it, do not ask them to confirm again.
Only ask a question when you genuinely cannot tell which flight or ticket they mean.
When the passenger has nothing more they want, call the `done` tool.
Keep your answers short and friendly.
"""


class Destination(TypedDict):
    flight_id: str
    country: str
    price: int  # the airfare from Tel Aviv, in USD
    hours: float  # how long the flight takes
    climate: str  # tropical, mediterranean, temperate, arid, alpine, cold
    cost_of_living: str  # cheap, moderate, expensive
    culture: str  # beach, nightlife, history, art, food, nature, shopping, spiritual
    language: str


# everywhere we fly out of Tel Aviv
DESTINATIONS: dict[str, Destination] = {
    "Larnaca": {
        "flight_id": "FD100", "country": "Cyprus", "price": 120, "hours": 1.0,
        "climate": "mediterranean", "cost_of_living": "moderate",
        "culture": "beach", "language": "Greek",
    },
    "Athens": {
        "flight_id": "FD110", "country": "Greece", "price": 210, "hours": 2.0,
        "climate": "mediterranean", "cost_of_living": "moderate",
        "culture": "history", "language": "Greek",
    },
    "Rome": {
        "flight_id": "FD120", "country": "Italy", "price": 340, "hours": 3.5,
        "climate": "mediterranean", "cost_of_living": "expensive",
        "culture": "history", "language": "Italian",
    },
    "Barcelona": {
        "flight_id": "FD130", "country": "Spain", "price": 380, "hours": 4.5,
        "climate": "mediterranean", "cost_of_living": "moderate",
        "culture": "art", "language": "Spanish",
    },
    "Lisbon": {
        "flight_id": "FD140", "country": "Portugal", "price": 410, "hours": 5.5,
        "climate": "mediterranean", "cost_of_living": "cheap",
        "culture": "food", "language": "Portuguese",
    },
    "Berlin": {
        "flight_id": "FD150", "country": "Germany", "price": 300, "hours": 4.0,
        "climate": "temperate", "cost_of_living": "moderate",
        "culture": "nightlife", "language": "German",
    },
    "Amsterdam": {
        "flight_id": "FD160", "country": "Netherlands", "price": 330, "hours": 4.5,
        "climate": "temperate", "cost_of_living": "expensive",
        "culture": "art", "language": "Dutch",
    },
    "Prague": {
        "flight_id": "FD170", "country": "Czechia", "price": 260, "hours": 3.5,
        "climate": "temperate", "cost_of_living": "cheap",
        "culture": "history", "language": "Czech",
    },
    "Budapest": {
        "flight_id": "FD180", "country": "Hungary", "price": 240, "hours": 3.0,
        "climate": "temperate", "cost_of_living": "cheap",
        "culture": "nightlife", "language": "Hungarian",
    },
    "Reykjavik": {
        "flight_id": "FD190", "country": "Iceland", "price": 620, "hours": 7.0,
        "climate": "cold", "cost_of_living": "expensive",
        "culture": "nature", "language": "Icelandic",
    },
    "Zurich": {
        "flight_id": "FD200", "country": "Switzerland", "price": 450, "hours": 4.0,
        "climate": "alpine", "cost_of_living": "expensive",
        "culture": "nature", "language": "German",
    },
    "Marrakesh": {
        "flight_id": "FD210", "country": "Morocco", "price": 350, "hours": 5.5,
        "climate": "arid", "cost_of_living": "cheap",
        "culture": "shopping", "language": "Arabic",
    },
    "Cairo": {
        "flight_id": "FD220", "country": "Egypt", "price": 180, "hours": 1.5,
        "climate": "arid", "cost_of_living": "cheap",
        "culture": "history", "language": "Arabic",
    },
    "Dubai": {
        "flight_id": "FD230", "country": "UAE", "price": 400, "hours": 3.5,
        "climate": "arid", "cost_of_living": "expensive",
        "culture": "shopping", "language": "Arabic",
    },
    "Istanbul": {
        "flight_id": "FD240", "country": "Turkey", "price": 220, "hours": 2.0,
        "climate": "temperate", "cost_of_living": "cheap",
        "culture": "food", "language": "Turkish",
    },
    "Tbilisi": {
        "flight_id": "FD250", "country": "Georgia", "price": 230, "hours": 3.0,
        "climate": "temperate", "cost_of_living": "cheap",
        "culture": "food", "language": "Georgian",
    },
    "Goa": {
        "flight_id": "FD260", "country": "India", "price": 540, "hours": 7.5,
        "climate": "tropical", "cost_of_living": "cheap",
        "culture": "beach", "language": "Hindi",
    },
    "Bangkok": {
        "flight_id": "FD270", "country": "Thailand", "price": 680, "hours": 10.0,
        "climate": "tropical", "cost_of_living": "cheap",
        "culture": "food", "language": "Thai",
    },
    "Bali": {
        "flight_id": "FD280", "country": "Indonesia", "price": 790, "hours": 13.0,
        "climate": "tropical", "cost_of_living": "cheap",
        "culture": "spiritual", "language": "Indonesian",
    },
    "Kathmandu": {
        "flight_id": "FD290", "country": "Nepal", "price": 610, "hours": 8.0,
        "climate": "alpine", "cost_of_living": "cheap",
        "culture": "spiritual", "language": "Nepali",
    },
    "Nairobi": {
        "flight_id": "FD300", "country": "Kenya", "price": 700, "hours": 8.0,
        "climate": "temperate", "cost_of_living": "cheap",
        "culture": "nature", "language": "Swahili",
    },
    "Cape Town": {
        "flight_id": "FD310", "country": "South Africa", "price": 850, "hours": 11.0,
        "climate": "mediterranean", "cost_of_living": "moderate",
        "culture": "nature", "language": "English",
    },
    "Rio de Janeiro": {
        "flight_id": "FD320", "country": "Brazil", "price": 980, "hours": 15.0,
        "climate": "tropical", "cost_of_living": "moderate",
        "culture": "beach", "language": "Portuguese",
    },
    "Buenos Aires": {
        "flight_id": "FD330", "country": "Argentina", "price": 1020, "hours": 16.0,
        "climate": "temperate", "cost_of_living": "cheap",
        "culture": "nightlife", "language": "Spanish",
    },
    "Mexico City": {
        "flight_id": "FD340", "country": "Mexico", "price": 890, "hours": 15.0,
        "climate": "temperate", "cost_of_living": "cheap",
        "culture": "food", "language": "Spanish",
    },
    "Havana": {
        "flight_id": "FD350", "country": "Cuba", "price": 940, "hours": 14.0,
        "climate": "tropical", "cost_of_living": "cheap",
        "culture": "nightlife", "language": "Spanish",
    },
    "New York": {
        "flight_id": "FD360", "country": "USA", "price": 720, "hours": 12.0,
        "climate": "temperate", "cost_of_living": "expensive",
        "culture": "art", "language": "English",
    },
    "Tokyo": {
        "flight_id": "FD370", "country": "Japan", "price": 830, "hours": 12.5,
        "climate": "temperate", "cost_of_living": "expensive",
        "culture": "food", "language": "Japanese",
    },
    "Singapore": {
        "flight_id": "FD380", "country": "Singapore", "price": 760, "hours": 11.0,
        "climate": "tropical", "cost_of_living": "expensive",
        "culture": "food", "language": "English",
    },
    "Sydney": {
        "flight_id": "FD390", "country": "Australia", "price": 1250, "hours": 19.0,
        "climate": "temperate", "cost_of_living": "expensive",
        "culture": "beach", "language": "English",
    },
}
# every flight leaves from Tel Aviv, so a flight is just its destination
BY_FLIGHT = {entry["flight_id"]: city for city, entry in DESTINATIONS.items()}
# ticket id -> flight id, the tickets this passenger currently holds
TICKETS: dict[str, str] = {}
NEXT_TICKET = itertools.count(1)


def describe(city: str) -> str:
    """One line describing a destination, the way the agent should see it"""
    entry = DESTINATIONS[city]
    return (
        f"{entry['flight_id']}: {city} ({entry['country']}), {entry['price']} USD,"
        f" {entry['hours']}h flight, {entry['climate']} climate,"
        f" {entry['cost_of_living']} to live, good for {entry['culture']},"
        f" they speak {entry['language']}"
    )


def search_destinations(
    climate: str | None = None,
    cost_of_living: str | None = None,
    culture: str | None = None,
    language: str | None = None,
    max_price: int | None = None,
    max_hours: float | None = None,
) -> str:
    """Search the destinations we fly to, on any combination of attributes"""
    found = [
        describe(city)
        for city, entry in DESTINATIONS.items()
        if (climate is None or entry["climate"] == climate)
        and (cost_of_living is None or entry["cost_of_living"] == cost_of_living)
        and (culture is None or entry["culture"] == culture)
        and (language is None or entry["language"].lower() == language.lower())
        and (max_price is None or entry["price"] <= max_price)
        and (max_hours is None or entry["hours"] <= max_hours)
    ]
    if not found:
        return "nothing we fly to matches all of that, try relaxing one of the criteria"
    return f"{len(found)} destinations match:\n" + "\n".join(found)


def buy_ticket(flight_id: str) -> str:
    """Buy a ticket on a flight and return the new ticket id"""
    if flight_id not in BY_FLIGHT:
        return f"there is no flight {flight_id}"
    ticket_id = f"T{next(NEXT_TICKET):03d}"
    TICKETS[ticket_id] = flight_id
    city = BY_FLIGHT[flight_id]
    return f"bought ticket {ticket_id} to {city} for {DESTINATIONS[city]['price']} USD"


def return_ticket(ticket_id: str) -> str:
    """Return a ticket and refund it"""
    if ticket_id not in TICKETS:
        return f"there is no ticket {ticket_id}"
    city = BY_FLIGHT[TICKETS.pop(ticket_id)]
    return f"returned ticket {ticket_id}, refunded {DESTINATIONS[city]['price']} USD"


def change_ticket(ticket_id: str, flight_id: str) -> str:
    """Move an existing ticket to a different flight, charging the difference"""
    if ticket_id not in TICKETS:
        return f"there is no ticket {ticket_id}"
    if flight_id not in BY_FLIGHT:
        return f"there is no flight {flight_id}"
    old = DESTINATIONS[BY_FLIGHT[TICKETS[ticket_id]]]
    new_city = BY_FLIGHT[flight_id]
    TICKETS[ticket_id] = flight_id
    difference = DESTINATIONS[new_city]["price"] - old["price"]
    return f"moved ticket {ticket_id} to {new_city}, the difference is {difference} USD"


def list_tickets() -> str:
    """Return the tickets the passenger is holding"""
    if not TICKETS:
        return "the passenger holds no tickets"
    return "\n".join(
        f"{ticket_id}: {describe(BY_FLIGHT[flight_id])}"
        for ticket_id, flight_id in TICKETS.items()
    )


def done() -> str:
    """The passenger is satisfied, we are finished"""
    return "finished"


CLIMATES = ["tropical", "mediterranean", "temperate", "arid", "alpine", "cold"]
COSTS = ["cheap", "moderate", "expensive"]
CULTURES = ["beach", "nightlife", "history", "art", "food", "nature", "shopping", "spiritual"]
TOOLS: list[ToolParam] = [
    {
        "name": "search_destinations",
        "description": (
            "Search the destinations we fly to from Tel Aviv. Every argument is a filter"
            " and any of them may be null, so call this with only what the passenger has"
            " actually told you, and call it again as you learn more about them."
        ),
        "strict": True,
        "input_schema": {
            "type": "object",
            "properties": {
                # a nullable enum has to be spelled as "one of the values, or null"
                "climate": {
                    "anyOf": [{"type": "string", "enum": CLIMATES}, {"type": "null"}],
                },
                "cost_of_living": {
                    "anyOf": [{"type": "string", "enum": COSTS}, {"type": "null"}],
                },
                "culture": {
                    "anyOf": [{"type": "string", "enum": CULTURES}, {"type": "null"}],
                },
                "language": {
                    "type": ["string", "null"],
                    "description": "the language spoken there, for example Spanish",
                },
                "max_price": {
                    "type": ["integer", "null"],
                    "description": "the most the passenger will pay for the airfare, in USD",
                },
                "max_hours": {
                    "type": ["number", "null"],
                    "description": "the longest flight the passenger will sit through",
                },
            },
            "required": [
                "climate", "cost_of_living", "culture", "language", "max_price", "max_hours",
            ],
            "additionalProperties": False,
        },
    },
    {
        "name": "buy_ticket",
        "description": "Buy a ticket on a flight for the passenger",
        "strict": True,
        "input_schema": {
            "type": "object",
            "properties": {"flight_id": {"type": "string"}},
            "required": ["flight_id"],
            "additionalProperties": False,
        },
    },
    {
        "name": "return_ticket",
        "description": "Return a ticket the passenger holds and refund them",
        "strict": True,
        "input_schema": {
            "type": "object",
            "properties": {"ticket_id": {"type": "string"}},
            "required": ["ticket_id"],
            "additionalProperties": False,
        },
    },
    {
        "name": "change_ticket",
        "description": "Move a ticket the passenger holds onto a different flight",
        "strict": True,
        "input_schema": {
            "type": "object",
            "properties": {
                "ticket_id": {"type": "string"},
                "flight_id": {"type": "string", "description": "the flight to move the ticket to"},
            },
            "required": ["ticket_id", "flight_id"],
            "additionalProperties": False,
        },
    },
    {
        "name": "list_tickets",
        "description": "List the tickets the passenger currently holds",
        "strict": True,
        "input_schema": {"type": "object", "properties": {}, "additionalProperties": False},
    },
    {
        "name": "done",
        "description": "Call this when the passenger has nothing more that they want",
        "strict": True,
        "input_schema": {"type": "object", "properties": {}, "additionalProperties": False},
    },
]
HANDLERS: dict[str, Callable[..., str]] = {
    "search_destinations": search_destinations,
    "buy_ticket": buy_ticket,
    "return_ticket": return_ticket,
    "change_ticket": change_ticket,
    "list_tickets": list_tickets,
    "done": done,
}

store = passpy.Store()
api_key = store.get_key("keys/claude.ai")
assert api_key is not None
client = anthropic.Anthropic(api_key=api_key.rstrip())

print(f"Fandango Airlines, we fly to {len(DESTINATIONS)} places. Where shall we send you?")
print("(ctrl-d to give up)")
messages: list[MessageParam] = []
finished = False
while not finished:
    try:
        line = input("you> ")
    except EOFError:
        print()
        break
    if not line.strip():
        continue
    messages.append({"role": "user", "content": line})
    # let the agent work until it has nothing left to do but talk back to us
    while True:
        response = client.messages.create(
            model=MODEL,
            max_tokens=2000,
            system=SYSTEM,
            messages=messages,
            tools=TOOLS,
        )
        messages.append({"role": "assistant", "content": response.content})
        for block in response.content:
            if block.type == "text":
                print(f"agent> {block.text}")
        if response.stop_reason != "tool_use":
            break
        results: list[ToolResultBlockParam] = []
        for block in response.content:
            if block.type != "tool_use":
                continue
            # `strict` means the input already validates against the schema
            arguments: dict[str, Any] = {
                key: value for key, value in dict(block.input).items() if value is not None
            }
            result = HANDLERS[block.name](**arguments)
            print(f"[{block.name}({arguments}) -> {result}]", file=sys.stderr)
            results.append({"type": "tool_result", "tool_use_id": block.id, "content": result})
            if block.name == "done":
                finished = True
        messages.append({"role": "user", "content": results})

print("Fandango Airlines thanks you for your custom")
