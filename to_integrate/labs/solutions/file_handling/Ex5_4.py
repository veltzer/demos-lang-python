#! /usr/bin/python
# Chapter 5 Exercise 4

import os
import shelve

start_time = 0
LOOP_COUNT = 200
words = []
words_dict = {}
########################################################
# TIMER FUNCTIONS
def start_timer():
    global start_time
    (utime, stime) = os.times()[0:2]
    start_time = utime + stime

def end_timer(txt):
    (utime, stime) = os.times()[0:2]
    end_time = utime + stime
    print('{0:<12}: {1:01.3f} seconds'.format(txt, end_time - start_time))

def load_data():
    global words
    words = open('words').read().split('\n')

########################################################
### TODO: USER FUNCTIONS
# Each function should return the line number
def brute_force():
    global words
    for pos in range(0, len(words)):
        if words[pos] == 'Zulu':
            break

    # return the line number
    return pos + 1


def index():
    global words
    return words.index('Zulu') + 1


def infunc():
    global words
    if 'Zulu' in words:
        return 1
    else:
        return 0


def dictionary():
    global words_dict
    return words_dict['Zulu'] + 1

def shelve_func():
    global shelve_dict
    return shelve_dict['Zulu'] + 1


########################################################
# MAIN

load_data()

# Brute force
start_timer()
for i in range(0, LOOP_COUNT):
    line = brute_force()

end_timer('Brute_force')
print('Brute_force line number:', line)
line = 0

# index
start_timer()
for i in range(0, LOOP_COUNT):
    line = index()

end_timer('Index')
print('Index line number:', line)
line = 0

# in
start_timer()
for i in range(0, LOOP_COUNT):
    line = infunc()

end_timer('In')
line = 0

# Create a dictionary from the words list
i = 0
start_timer()

# TODO: Create a dictionary called words_dict
for key in words:
    words_dict[key] = i
    i += 1

for i in range(0, LOOP_COUNT):
    line = dictionary()

end_timer('Dictionary')
print('Dictionary line number:', line)
line = 0

i = 0
start_timer()
shelve_dict = shelve.open('shelve_dict')

for key in words:
    shelve_dict[key] = i
    i += 1

end_timer('Shelve creation')


start_timer()

for i in range(0, LOOP_COUNT):
    line = shelve_func();

shelve_dict.close()
end_timer('Shelved dictionary')

print('Dictionary line number: ', line)
