"""
This example shows that you can modify dictionaries values in place
"""

# Dictionary with complex values (lists and dictionaries)
student_data = {
    "Alice": {
        "grades": [85, 92, 78],
        "contact": {"email": "alice@example.com"}
    },
    "Bob": {
        "grades": [76, 88, 94],
        "contact": {"email": "bob@example.com"}
    }
}

# Original data
print("Original:", student_data)

# Modifying a list inside the dictionary
student_data["Alice"]["grades"].append(95)  # Add a new grade
print("After adding grade:", student_data["Alice"]["grades"])

# Modifying a nested dictionary
student_data["Bob"]["contact"]["email"] = "bob.new@example.com"
print("After changing email:", student_data["Bob"]["contact"])

# Final state
print("Final data:", student_data)
