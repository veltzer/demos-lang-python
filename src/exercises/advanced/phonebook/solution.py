import re


def read_phonebook():
    pb = {}
    with open("data.txt") as f:
        for line in f:
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


def search_for_name(mypb):
    name = input('please give me a name to search for: ')
    if name in mypb:
        print('the number is', mypb[name])
    else:
        print('the name', name, 'is not in the phonebook')


def delete_a_name(mypb):
    name = input('please give me a name to search for: ')
    if name in mypb:
        del mypb[name]
    else:
        print(f"the name {name} is not in the phonebook")


def add_a_name(mypb):
    name = input('please give me a name: ')
    if name in mypb:
        print('sorry, name', name, 'is already in the phonebook...')
        return
    phone = input('please give me a phone: ')
    mypb[name] = phone


def edit_a_name(mypb):
    name = input('please give me a name to edit: ')
    if name not in mypb:
        print('sorry, name', name, 'is not in the phonebook...')
        return
    phone = input('please give me a new phone: ')
    mypb[name] = phone


def save(mypb):
    with open("data.txt", "w") as f:
        for name in mypb:
            f.write(name + ',' + mypb[name] + '\n')


def print_phonebook(mypb):
    for name in mypb:
        print('name', name, 'phone', mypb[name])


def find_in_phonebook(mypb):
    regexp = input('please give me a regexp: ')
    for name in mypb:
        m = re.search(regexp, name)
        if m is not None:
            print('found', name, 'with phone', mypb[name])


def main():
    mypb = read_phonebook()
    done = False
    while not done:
        selection = print_the_menu()
        if selection == '1':
            print('you selected (1)')
            search_for_name(mypb)
        elif selection == '2':
            print('you selected (2)')
            delete_a_name(mypb)
        elif selection == '3':
            print('you selected (3)')
            add_a_name(mypb)
        elif selection == '4':
            print('you selected (4)')
            edit_a_name(mypb)
        elif selection == '5':
            print('you selected (5)')
            save(mypb)
        elif selection == '6':
            print('you selected (6)')
            print_phonebook(mypb)
        elif selection == '7':
            print('you selected (7)')
            find_in_phonebook(mypb)
        else:
            print('Sorry, selection ', selection, ' is not supported')
    print('after the loop')


main()
