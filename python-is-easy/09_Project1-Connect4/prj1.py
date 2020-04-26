occupancy=[5,5,5,5,5,5,5]
board=[[" "," "," "," "," "," "," "], [" "," "," "," "," ", " "," "], [" "," "," "," "," ", " "," "], [" "," "," "," "," ", " "," "], [" "," "," "," "," ", " "," "], [" "," "," "," "," ", " "," "]]


def drawBoard():

    colCount=0
    for col in range(12):
        if col%2==0:
            for i in range(7):
                if(i!=6):
                    print(board[colCount][i]+"|", end="")
                else:
                    print(board[colCount][i])
                    colCount+=1
        else:
            for j in range(13):
                print("-", end="")
            print()


def checkWin(symbol):
    #Horizontal check
    #print(board)
    for i in range(6):
        for j in range(5):
            #print(i,j,symbol+"->"+board[i][j])
            if(board[i][j]==symbol):
                #print("Got symbol",i,j,symbol)
                if board[i][j] == symbol and board[i][j+1] == symbol and board[i][j+2] == symbol and board[i][j+3]==symbol:
                    #print("Inside")
                    return 1

    #vertical check
    for i in range(7):
        for j in range(3):
            if(board[j][i]==symbol):
                if board[j][i] == symbol and board[j+1][i] == symbol and board[j+2][i] == symbol and board[j+3][i] == symbol:
                    return 1


    #diagnoal down check
    for i in range(3):
        for j in range(4):
            if board[i][j]==symbol:
                if board[i][j]==symbol and board[i+1][j+1]==symbol and board[i+2][j+2]==symbol and board[i+3][j+3]==symbol:
                    return 1

    #diagnoal up check
    for i in range(5,2,-1):
        for j in range(4):
            if board[i][j]==symbol:
                if board[i][j]==symbol and board[i-1][j+1]==symbol and board[i-2][j+2]==symbol and board[i-3][j+3]==symbol:
                    return 1

def play():
    player="1"
    symbol="X"
    win=0

    while(win!=1):
        col_move=int(input("Player "+player+", select a column: "))
        if(occupancy[col_move-1]!=-1):
            board[occupancy[col_move-1]][col_move-1]=symbol
            occupancy[col_move-1]-=1
            drawBoard()
            win=checkWin(symbol)
            if win==1:
                print("Player "+player+" won the game!")
            if(player=="1"):
                player="2"
                symbol="o"
            else:
                player="1"
                symbol="X"

        else:
            print("Can't insert a coin into this colum as it is full")


drawBoard()
play()
