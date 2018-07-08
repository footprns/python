#!/usr/bin/env python3
# create empty tuple tuple=()
def tuple():
    t = ('Norwey', 4.953, 3)
    print(t[0])
    print(2)
    print(len(t))
    for item in t:
        print(item)
    a = ((220, 284), (1184, 1210), (2620, 2924), (5020, 5564))
    for item in a:
        print(item)

def minmax(items):
    return min(items), max(items)

def tuple_unpacking(items):
    lower, upper = minmax(items)
    print(lower)
    print(upper)


if __name__ == '__main__':
    tuple() # The 0th arg is the module filename
