"""
This is an example of why context in lamba matters

In this example we have a list of companies.
Each company is a dict of employees and their salaries.
We would like to find the employee which has the maximal salary
in each company using the 'max' function.

Look at the two examples below which look very similar and try
to explain why the first command doesn't pass lint and the second
does.

Run lint with:
    $ pylint -s n -r n exapmle.py

References:
- https://stackoverflow.com/questions/25314547/cell-var-from-loop-warning-from-pylint
"""

l = [
        # first company
        {
            "mark": 1000,
            "doron": 2000,
        },
        # secnod company
        {
            "yuval": 3000,
            "avi": 4000,
        },
]

# this exapmle does not pass lint
for c in l:
    max_person = max(c.keys(), key=lambda x: c[x])
    print(f"{max_person}")
# this exapmle does pass lint
for c in l:
    max_person = max(c.keys(), key=lambda x, d=c: d[x])
    print(f"{max_person}")
