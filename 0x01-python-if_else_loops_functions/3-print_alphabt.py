#!/usr/bin/python3
for i in range(97, 123):
    if i is ord('e') or i is ord('q'):
        continue
    else:
        print("{}".format(chr(i)), end="")
