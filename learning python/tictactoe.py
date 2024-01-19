from typing import List
arr=[['','',''],['','',''],['','','']]
plc=0
f=0
def printable():
    n=0
    global f
    if arr[0][0]==arr[1][1]==arr[2][2]=='O' or arr[0][0]==arr[1][1]==arr[2][2]=='X':
        if arr[0][0]=='O':
            f=1
        else:
            f=2
    elif arr[0][2]==arr[1][1]==arr[2][0]=='O' or arr[0][2]==arr[1][1]==arr[2][0]=='X':
        if arr[0][0]=='O':
            f=1
        else:
            f=2
    for row in range(0,3):
        if arr[row][0]==arr[row][1]==arr[row][2]=='O' or arr[row][0]==arr[row][1]==arr[row][2]=='X':
            if arr[row][0]=='O':
                f=1
            else:
                f=2
        print("\n")
        for column in range(0,3):
            if arr[0][column]==arr[1][column]==arr[2][column]=='O' or arr[0][column]==arr[1][column]==arr[2][column]=='X':
                if arr[0][column]=='O':
                    f=1
                else:
                    f=2
            
            print(f"\t{arr[row][column]}\t",end="")
            n+=1
            if column!=2:
                print("|",end="")
        print("\n")
        if row!=2:
            print("    -----------------------------------------")


def user_input(n: int):
    global plc
    ch=int(input("enter the position to place a O at: "))
    if ch<=9 and ch>=1:
        if arr[(ch-1)//3][(ch-1)%3]=='':
            if n==1:
                arr[(ch-1)//3][(ch-1)%3]='O'
                plc+=1
            else:
                arr[(ch-1)//3][(ch-1)%3]='X'
                plc+=1
        else:
            print("enter a valid position!")
            user_input(n)
    else:
        print("enter a valid position!")
        user_input(n)
    
    
def processing():
    global plc
    global f

    while(f==0):
        printable()
        if f==1:
            print("player 1 wins!")
            break
        if f==2:
            print("player 2 wins!")
            break
        user_input(1)
        printable()
        if f==1:
            print("player 1 wins!")
            break
        if f==2:
            print("player 2 wins!")
            break
        if plc==9:
            print("draw!")
            break
        user_input(2)
        

processing()
