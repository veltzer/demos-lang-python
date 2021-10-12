f = open('ex4.py')
report = {}
lines = f.readlines()
for line in lines:
    for c in line:
        if not (c in [' ', '\n', '\r', '\t']):
            if c in report:
                report[c] += 1
            else:
                report[c] = 1
f = open('ex4.py.report', 'w')
keys = sorted(report.keys())
for c in keys:
    f.write(c)
    f.write(' : ')
    f.write(str(report[c]))
    f.write('\n')
f.close()
