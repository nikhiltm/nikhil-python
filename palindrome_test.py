import random
testword = open("wordfile2.txt").read().splitlines()
def swap(s, x, y):
    z = s[x]
    s[x] = s[y]
    s[y] = z
        
def reverse(s):
    l = list(s)
    for x in range(0, len(l)):
        y = len(l) - 1 - x
        if y <= x:
            break
        swap(l, x, y)
    h = "".join(l)
    return h
        
def test(s):
    reverse(s)
    if s == reverse(s):
       print("This string is a palindrome")
    else:
        print("This string is not a palindrome")

for i in range(0, len(testword)):
    inputword = testword[i]
    print(inputword)
    test(inputword)

