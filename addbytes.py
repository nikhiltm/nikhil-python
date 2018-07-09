#!/usr/bin/python
import sys
import os

if len(sys.argv) != 4:
  print("USAGE addbytes.py filename byte #ofbytes")
  quit()

ifile = sys.argv[1]
hexbyte = int(sys.argv[2])
count = int(sys.argv[3])
f = open(ifile, "a")

#f.seek(0, os.SEEK_END)
#size = f.tell()
#print(size)
#f.seek(size, 0)

for number in range(0, count):  
  f.write(bytearray([hexbyte]))

f.close()
