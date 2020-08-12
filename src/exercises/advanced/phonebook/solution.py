import re


def read_phonebook():
    pb = {}
    for line in open('data.txt'):
        line = line.rstrip()
        mylist = line.split(',')
        pb[mylist[0]] = mylist[1]
    return pb


def print_the_menu():
    print('1) search for a name in the phonebook')
    print('2) delete a name in the phonebook')
    print('3) add a name to the phonebook')
    print('4) edit a name in the phonebook')
    print('5) save and exit')
    print('6) show the phonebook')
    print('7) find entries in phonebook')
    selection = input('please give me your choice: ')
    return selection


def search_for_name():
    name = input('please give me a name to search for: ')
    if name in mypb:
        print('the number is', mypb[name])
    else:
        print('the name', name, 'is not in the phonebook')


def delete_a_name():
    name = input('please give me a name to search for: ')
    if name in mypb:
        del mypb[name]
    else:
        print('the name', name, 'is not in the phonebook')


def add_a_name():
    name = input('please give me a name: ')
    if name in mypb:
        print('sorry, name', name, 'is already in the phonebook...')
        return
    phone = input('please give me a phone: ')
    mypb[name] = phone


def edit_a_name():
    name = input('please give me a name to edit: ')
    if name not in mypb:
        print('sorry, name', name, 'is not in the phonebook...')
        return
    phone = input('please give me a new phone: ')
    mypb[name] = phone


def save():
    f = open('data.txt', 'w')
    for name in mypb:
        f.write(name + ',' + mypb[name] + '\n')
    f.close()
    global done
    done = True


def print_phonebook():
    for name in mypb:
        print('name', name, 'phone', mypb[name])


def find_in_phonebook():
    regexp = input('please give me a regexp: ')
    for name in mypb:
        m = re.search(regexp, name)
        if m is not None:
            print('found', name, 'with phone', mypb[name])


mypb = read_phonebook()
done = False
while not done:
    selection = print_the_menu()
    if selection == '1':
        print('you selected (1)')
        search_for_name()
    elif selection == '2':
        print('you selected (2)')
        delete_a_name()
    elif selection == '3':
        print('you selected (3)')
        add_a_name()
    elif selection == '4':
        print('you selected (4)')
        edit_a_name()
    elif selection == '5':
        print('you selected (5)')
        save()
    elif selection == '6':
        print('you selected (6)')
        print_phonebook()
    elif selection == '7':
        print('you selected (7)')
        find_in_phonebook()
    else:
        print('Sorry, selection ', selection, ' is not supported')
print('after the loop')
