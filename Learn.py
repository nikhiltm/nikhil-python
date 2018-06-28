import string

file = open("/Users/Nikhil/Documents/Coding/Numbers", "r")
s = file.read()
mylist = string.split(s,',')
x = len(mylist)
for i in range(0, x) :
    print mylist[x-1-i]
    