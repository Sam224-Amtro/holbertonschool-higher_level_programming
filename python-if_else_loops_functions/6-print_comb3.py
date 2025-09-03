#!/usr/bin/python3
for k in range(10):
    for j in range(k + 1, 10):
        if k == 8 and j == 9:
            print(f"{k}{j}")
        else:
            print(f"{k}{j}, ", end="")
