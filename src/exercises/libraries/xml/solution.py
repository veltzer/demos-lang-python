import xml.dom.minidom

# parse an XML file by name
dom = xml.dom.minidom.parse('data_samples/numbers.xml')

salary_sum = 0
for employee in dom.getElementsByTagName('employee'):
    salary_str = employee.getAttribute('salary')
    salary = int(salary_str)
    salary_sum += salary

print(f"salary_sum is {salary_sum}")
