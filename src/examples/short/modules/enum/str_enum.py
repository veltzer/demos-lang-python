"""
StrEnum is particularly useful when you need enumerated constants that are also strings,
allowing you to perform string operations while maintaining the readability and type safety of enums.
Its great for cases where you have predefined string constants, like color codes,
HTTP status messages, or configuration options.
"""
from enum import StrEnum


class ColorCode(StrEnum):
    RED = "FF0000"
    GREEN = "00FF00"
    BLUE = "0000FF"
    YELLOW = "FFFF00"
    PURPLE = "800080"


# Using the StrEnum
print(ColorCode.RED)  # Output: ColorCode.RED
print(ColorCode.RED.value)  # Output: FF0000

# Comparison (alphabetical order)
print(ColorCode.GREEN < ColorCode.RED)  # Output: True

# String operations
print(ColorCode.BLUE.lower())  # Output: 0000ff
print(ColorCode.YELLOW.startswith("FF"))  # Output: True

# Iteration
for color in ColorCode:
    print(f"{color.name}: {color.value}")

# Conversion to and from strings
color_code = "800080"
color = ColorCode(color_code)
print(f"Color code {color_code} is {color.name}")  # Output: Color code 800080 is PURPLE

# Using in string formatting
print(f"The hex code for blue is #{ColorCode.BLUE}")  # Output: The hex code for blue is #0000FF
