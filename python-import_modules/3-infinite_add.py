#!/usr/bin/python3
import sys

if __name__ == "__main__":
    count = len(sys.argv)
    add = 0

    for k in range(1, count):
        add += int(sys.argv[k])

    print("{}".format(add))
