"""
This is a fast way to convert numbers with commas in them from string to the right type

References:
- http://stackoverflow.com/questions/6633523/how-can-i-convert-a-string-with-dot-and-comma-into-a-float-number-in-python
"""

str_num = "1,324,432.23"
float_num = float(str_num.replace(",", ""))
print(f"float_num is [{float_num}]")
