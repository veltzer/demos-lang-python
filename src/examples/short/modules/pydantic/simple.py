from pydantic import BaseModel


# Define a data model
class User(BaseModel):
    name: str
    age: int
    email: str
    is_admin: bool = False


# Create an instance of the model from a dictionary
user_data = {
    'name': 'John Doe',
    'age': 30,
    'email': 'john@example.com'
}

user = User(**user_data)
print(user)
# Output: User(name='John Doe', age=30, email='john@example.com', is_admin=False)

# Access the fields
print(user.name)  # Output: John Doe
print(user.age)   # Output: 30
print(user.email)  # Output: john@example.com
print(user.is_admin)  # Output: False

# Modify the fields
user.is_admin = True
print(user)
# Output: User(name='John Doe', age=30, email='john@example.com', is_admin=True)

# Create an instance with validation errors
try:
    invalid_user = User(name='Alice', age='invalid', email='alice@example.com')
except ValueError as e:
    print(e)
    # Output: 1 validation error for User
    #   age
    #     value is not a valid integer (type=type_error.integer)
