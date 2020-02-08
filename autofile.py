#!/usr/bin/env python3

import sys


a = open(sys.argv[1])
s = a.read()
a.close()

b = open(sys.argv[2],'a')
b.write(s)
b.close()



