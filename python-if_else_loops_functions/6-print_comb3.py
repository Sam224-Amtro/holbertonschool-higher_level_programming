#!/usr/bin/python3
for k in range(10):
    for j in range(k + 1, 10):
        if k == 8 and j == 9:
            print("{}{}".format(k, j))
        else:
            print("{}{}, ".format(k, j), end="")
