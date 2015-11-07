__author__ = 'Leria'

with open ('yazkora.txt', 'r+') as ds:
    txt = ds.read()
    s = txt.partition(".")
    s = list(s)
    for char in s:
        if char == '.':
            s.remove(char)
    dict1 = {}
    for elt in s:
        temp = elt.split(' ')
        for x in temp:
            if x[-2:] == 'yo':
                print(x, sep='')

