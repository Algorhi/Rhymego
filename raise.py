#!/usr/bin/env python3
a = int(input("please input a:\n"))
if a > 0:
    print('this is running!',a)
else:
    print("number {:2.3f}".format(a))
    raise Exception("a > 0")
