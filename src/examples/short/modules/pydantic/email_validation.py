from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: EmailStr


# Valid email
valid_user = User(name='John Doe', email='john@example.com')
print(valid_user)
# Output: User(name='John Doe', email=EmailStr('john@example.com'))

# Invalid email
try:
    invalid_user = User(name='Alice', email='invalid_email')
except ValueError as e:
    print(e)
    # Output: 1 validation error for User
    #   email
    #     value is not a valid email address (type=value_error.email)
