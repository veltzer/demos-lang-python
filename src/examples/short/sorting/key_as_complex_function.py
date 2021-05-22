"""
This is an example of how to write complex functions as key
"""

def my_func(employee_data):
    return employee_data["salary"]


my_list = [
        {
            "name": "mark",
            "salary": 30,
        },
        {
            "name": "avi",
            "salary": 20,
        },
        {
            "name": "yossi",
            "salary": 25,
        },
]
# list.sort is a method that sorts a list *in place* and does not return anything interesting...
my_list.sort(key=my_func)
print(my_list)
