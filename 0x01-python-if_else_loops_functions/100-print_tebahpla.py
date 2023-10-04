#!/usr/bin/python3
for c in range(ord('Z'), ord('A')-1, -1):
    print("{:c}".format(c if c % 2 else c + 32), end="")
