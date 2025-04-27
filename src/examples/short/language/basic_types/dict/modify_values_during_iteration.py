"""
This example shows that you can modify values during iteration
"""

# Dictionary with student scores
student_scores = {
    "Alice": 85,
    "Bob": 76,
    "Charlie": 92
}

print("Original:", student_scores)

# Method 1: Safe modification using items()
for name, score in student_scores.items():
    student_scores[name] = score + 5

print("After bonus:", student_scores)

# Method 2: Using dictionary comprehension (alternative)
student_grades = {name: "Pass" if score >= 80 else "Fail" for name, score in student_scores.items()}

print("Grades:", student_grades)
