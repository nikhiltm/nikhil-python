import random
import turtle
l = open("wordfile.txt").read().splitlines()
x = l[random.randint(0, len(l)-1)]
h = list(x)
w = ["_", "_", "_", "_", "_", "_", "_"]
errorattempts = 8
prevguessleft = 8
attempts = 0
t = turtle.Turtle()
t.pensize(10)
t.pencolor("black")
t.fd(200)
t.bk(100)
t.lt(90)
t.fd(400)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(50)
t.penup()
t.fd(100)
t.pendown()
t.rt(270)
def hangman(y, s, z):
    result = False
    for i in range(0,len(s)):
        if y == s[i] and y != z[i]:
            z[i] = y
            result = True
        elif y == s[i] and y == z[i]:
            print("You have already guessed that letter")
            result = True
    return result

def guesscheck(result):
    global errorattempts
    global attempts
    if result == True:
        attempts = attempts + 1
        print("You have ", errorattempts, " error attempts left")
    else:
        errorattempts = errorattempts - 1
        attempts = attempts + 1
        if errorattempts == 0:
            print("You have no error attempts left. Game over. The secret word was ", x)
        else:
            print("You have ", errorattempts, " error attempts left")
def drawman():
    global errorattempts
    if errorattempts == 7:
        t.circle(50)
    elif errorattempts == 6:
        t.rt(90)
        t.fd(150)
    elif errorattempts == 5:
        t.lt(45)
        t.fd(100)
        t.penup()
    elif errorattempts == 4:
        t.bk(100)
        t.pendown()
        t.rt(90)
        t.fd(100)
        t.penup()
    elif errorattempts == 3:
        t.bk(100)
        t.lt(45)
        t.bk(75)
        t.pendown()
        t.lt(135)
        t.fd(100)
        t.penup()
    elif errorattempts == 2:
        t.bk(100)
        t.lt(90)
        t.pendown()
        t.fd(100)
        t.penup()
    elif errorattempts == 1:
        t.bk(100)
        t.lt(135)
        t.bk(125)
        t.rt(90)
        t.fd(25)
        t.pendown()
        t.circle(5)
        t.penup()
    elif errorattempts <= 0:
        t.bk(50)
        t.pendown()
        t.circle(5)

       

print(w)
while True:
    a = (input(str("Enter a letter here: ")))
    ret = hangman(a, h, w)
    print(w)
    guesscheck(ret)
    if w == h:
        print("Congratulations! You found the word in ", attempts, " attempts!")
        break
    elif errorattempts <= 0:
        print("You have no more error attempts left. Game over.")
        break
    if  prevguessleft != errorattempts:
        drawman()
        prevguessleft = errorattempts
