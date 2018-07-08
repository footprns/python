#!/usr/bin/env python3
import sys
# Learn about default value
def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


if __name__ == '__main__':
    banner(sys.argv[1]) # The 0th arg is the module filename
