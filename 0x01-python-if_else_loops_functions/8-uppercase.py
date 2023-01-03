#!/usr/bin/python3
def uppercase(str):
    for i in str:
        n = ord(i)
        if n >= 97 and n <= 122:
            n -= 32
        print("{:c}".format(n), end="")
    print()
