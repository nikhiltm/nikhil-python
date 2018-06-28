l = [23, 87, 15, 34, -74, 63]
def max(x):
    if x[0] > x[1] and x[0] > x[2] and x[0] > x[3] and x[0] > x[4] and x[0] > x[5]:
        print(x[0])
    elif x[1] > x[2] and x[1] > x[3] and x[1] > x[4] and x[1] > x[5]:
        print(x[1])
    elif x[2] > x[3] and x[2] > x[4] and x[2] > x[5]:
        print(x[2])
    elif x[3] > x[4] and x[3] > x[5]:
        print(x[3])
    elif x[4] > x[5]:
        print(x[4])
    else:
        print(x[5])
def min(x):
        if x[0] < x[1] and x[0] < x[2] and x[0] < x[3] and x[0] < x[4] and x[0] < x[5]:
            print(x[0])
        elif x[1] < x[2] and x[1] < x[3] and x[1] < x[4] and x[1] < x[5]:
            print(x[1])
        elif x[2] < x[3] and x[2] < x[4] and x[2] < x[5]:
            print(x[2])
        elif x[3] < x[4] and x[3] < x[5]:
            print(x[3])
        elif x[4] < x[5]:
            print(x[4])
        else:
            print(x[5])
  
total = l[0] + l[1] + l[2] + l[3] + l[4] + l[5] 

n = (int(input("Enter number here: ")))
def find(x):
    if n == x[0]:
        print(str(n) + " was found at index 0")
    elif n == x[1]:
        print(str(n) + " was found at index 1")
    elif n == x[2]:
        print(str(n) + " was found at index 2")
    elif n == x[3]:
        print(str(n) + " was found at index 3")
    elif n == x[4]:
        print(str(n) + " was found at index 4")
    elif n == x[5]:
        print(str(n) + " was found at index 5")
    else:
        print(str(n) + " was not found in the list")