arr=[['','',''],['','',''],['','','']]
plc=0 #to check if the board is full or not
f=0 #flag to check if someone has won or not


def printable(): #function to print the board
    n=0
    global f
    
    #checking for diagonals
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
        #checking for rows and columns
        if arr[row][0]==arr[row][1]==arr[row][2]=='O' or arr[row][0]==arr[row][1]==arr[row][2]=='X' or arr[0][row]==arr[1][row]==arr[2][row]=='O' or arr[0][row]==arr[1][row]==arr[2][row]=='X':
            if arr[row][0]=='O' or arr[0][row]=='O':
                f=1
            else:
                f=2
        print("\n")
        for column in range(0,3):
            #checking for columns
            print(f"\t{arr[row][column]}\t",end="")
            n+=1
            if column!=2:
                print("|",end="")
        print("\n")
        if row!=2:
            print("    -----------------------------------------")


def user_input(n: int): #function to take input from the user
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
    
    
def processing(): #function to process the game
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
