#! /usr/local/bin/python
# Python 3 version

for line in open('messier.txt'):
    if not line: break
    if line.startswith('M'):
        # Slice each field
        mes_num = line[:6].rstrip()
        com_name = line[6:40].rstrip()
        if not com_name: com_name = 'no name'
        obj_type = line[40:64].rstrip()
        const = line[64:].rstrip()
        print(f"|{mes_num}|{com_name}|{obj_type}|{const}|")

        

