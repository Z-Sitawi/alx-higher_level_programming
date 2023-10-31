#!/usr/bin/python3
for x in range(-122, -96):
    print("{:c}".format(-x) if x in range(-122, -96, 2)
          else "{:s}".format(chr(-x)).upper(), end="")
