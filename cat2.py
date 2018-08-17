#!/usr/bin/python
import sys

if len(sys.argv) != 2:
  print("USAGE cat.py filename")
  quit()

#Get file name
ifile = sys.argv[1]
oldfile = open(ifile).read().splitlines()
nfile = open("newfile.txt", "w")

#replace parts in lines
for line in oldfile:
  nfile.write(line.replace('/../../..', '/../meta-openbmc') + "\n")
nfile.close()

ofile = open("newfile.txt").read().splitlines()
for line in ofile:
  print line	
