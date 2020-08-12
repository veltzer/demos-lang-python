found = True
while found:
    input_string = input('Please give me some digits... \n')
    found = False
    for character in input_string:
        if character < '0' or character > '9':
            # we have a non digit!
            print('Error, you gave me non digits')
            found = True
            break
print('starting real work on', input_string)
