import random

print("WELCOME TO THE 2048 GAME")
print("GET 2048 ON YOUR BOARD TO WIN THE GAME")
print("GOOD LUCK")
def box(space):
    print("-"*17)
    print("|",space[0][0],"|",space[0][1],"|",space[0][2],"|",space[0][3],"|")
    print("-"*17)
    print("|",space[1][0],"|",space[1][1],"|",space[1][2],"|",space[1][3],"|")
    print("-"*17)
    print("|",space[2][0],"|",space[2][1],"|",space[2][2],"|",space[2][3],"|")
    print("-"*17)
    print("|",space[3][0],"|",space[3][1],"|",space[3][2],"|",space[3][3],"|")
    print("-"*17)

space = [[" "," "," "," "],
         [" "," "," "," "],
         [" "," "," "," "],
         [" "," "," "," "]]


def swipe_left(space):
    for j in range(0,4):
        for i in range(2,-1,-1):
            if space[j][i] == " ":
                space[j][i] = space[j][i+1]
                space[j][i+1] = " "
            elif space[j][i] == space[j][i+1]:
                space[j][i] = space[j][i] + space[j][i+1]
                space[j][i+1] = " "
    for m in range(2):
        for k in range(0,4):
            for l in range(2,-1,-1):
                if space[k][l] == " ":
                    space[k][l] = space[k][l+1]
                    space[k][l+1] = " "

def swipe_right(space):
    for j in range(0,4):
        for i in range(1,4):
            if space[j][i] == " ":
                space[j][i] = space[j][i-1]
                space[j][i-1] = " "
            elif space[j][i] == space[j][i-1]:
                space[j][i] = space[j][i] + space[j][i-1]
                space[j][i-1] = " "
    for m in range(2):
        for k in range(0,4):
            for l in range(1,4):
                if space[k][l] == " ":
                    space[k][l] = space[k][l-1]
                    space[k][l-1] = " "

def swipe_up(space):
    for j in range(2,-1,-1):
        for i in range(0,4):
            if space[j][i] == " ":
                space[j][i] = space[j+1][i]
                space[j+1][i] = " "
            elif space[j][i] == space[j+1][i]:
                space[j][i] = space[j][i] + space[j+1][i]
                space[j+1][i] = " "
    for m in range(2):
        for k in range(2,-1,-1):
            for l in range(0,4):
                if space[k][l] == " ":
                    space[k][l] = space[k+1][l]
                    space[k+1][l] = " "

def swipe_down(space):
    for j in range(1,4):
        for i in range(0,4):
            if space[j][i] == " ":
                space[j][i] = space[j-1][i]
                space[j-1][i] = " "
            elif space[j][i] == space[j-1][i]:
                space[j][i] = space[j][i] + space[j-1][i]
                space[j-1][i] = " "
    for m in range(2):
        for k in range(1,4):
            for l in range(0,4):
                if space[k][l] == " ":
                    space[k][l] = space[k-1][l]
                    space[k-1][l] = " "

def rand_val():
    r1 = random.randint(0,3)
    r2 = random.randint(0,3)
    return r1,r2


def add_val(space):
    while True:
        r1,r2 = rand_val()
        if space[r1][r2]!= " ":
            r1,r2 = rand_val()
        elif space[r1][r2]== " ":
            space[r1][r2] = 2
            break
    
def count_loss(loss):
    if space[0][0]!=" " and space[0][1]!=" " and space[0][2]!=" " and space[0][3]!=" " and space[1][0]!=" " and space[1][1]!=" " and space[1][2]!=" " and space[1][3]!=" " and space[2][0]!=" " and space[2][1]!=" " and space[2][2]!=" " and space[2][3]!=" " and space[3][0]!=" " and space[3][1]!=" " and space[3][2]!=" " and space[3][3]!=" " :
        loss = loss + 1
        print(" ")
        print("End of Empty Boxes")
        print("Alas! You Lost")
    else:
        loss = 0
    return loss

def count_win(space,win):
    for i in range(0,4):
        for j in range(0,4):
            if space[i][j] == 2048:
                win = 1
                print("Congratulations You have won it")
            else:
                win = 0
    return win
            
while True:
    loss = 0
    win = 0
    add_val(space)
    box(space)
    ch = int(input("Enter the operation : 1-left; 2-right; 3-up; 4-down : "))
    if ch==1:
        swipe_left(space)
    elif ch==2:
        swipe_right(space)
    elif ch==3:
        swipe_up(space)
    elif ch==4:
        swipe_down(space)
    else:
        print("Wrong input entered")
    w = count_win(space,win)
    lo = count_loss(loss)
    if w!=0 or lo!=0:
        break
    
print("\n")
print("THANKS FOR PLAYING THE GAME")