"""
This example shows that you cannot use mutable objects as keys in a dict
"""


try:
    # Attempting to use a list as a key
    my_dict = {
        # pylint: disable=unhashable-member
        [1, 2, 3]: "This is a list key"
    }
    print("This won't execute")
except TypeError as e:
    print(f"Error: {e}")

try:
    my_dict = {}
    list_key = [4, 5, 6]
    my_dict[list_key] = "Another list key attempt"
    print("This won't execute")
except TypeError as e:
    print(f"Error: {e}")

tuple_dict = {
    (1, 2, 3): "This is a tuple key",
    (4, 5, 6): "Another tuple key",
}
print("Tuple as key works:", tuple_dict[(1, 2, 3)])


try:
    tuple_dict = {
        ([1,2], [3,4], [5,6]): "Tuple with mutable values"
    }
except TypeError as e:
    print(f"Error: {e}")

try:
    dict_key = {"name": "John"}
    # pylint: disable=unhashable-member
    bad_dict = {dict_key: "Using dict as key"}
    print("This won't execute")
except TypeError as e:
    print(f"Error: {e}")
