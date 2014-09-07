#!/usr/local/bin/python
import sys

text = open(sys.argv[1], "r").read().split(" ")
print len(text)
