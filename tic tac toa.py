#tic tac toa python program
#start of the program
import random

##board = ([' ', ' ', ' ', ' ', 'X', 'O', ' ', 'X', ' ', 'O'])
#printing the board in the screen
def drawBoard(board):
    # "board" is a list of 10 strings representing the board (ignore index 0)
   print('   |   |   ')
   print(' ' + board[7] + ' | ' + ' ' + board[8] + ' | ' + board[9])
   print('   |   |   ')
   print('-----------')
   print('   |   |   ')
   print(' ' + board[4] + ' | ' + ' ' + board[5] + ' | ' + board[6])
   print('   |   |   ')
   print('-----------')
   print('   |   |   ')
   print(' ' + board[1] + ' | ' + ' ' + board[2] + ' | ' + board[3])
   print('   |   |   ')

##drawBoard(board)

#letting the player be X or O
def inputPlayerLetter():
    #let the player choose which he wants to be X or O.
    letter = ' '
    while not (letter == 'X' or letter=='O') :
        print("Do you want to be X or O ? ")
        letter = input().upper()
    ##inputPlayerLetter()
    # Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    if letter == 'X' :
        return ('X','O')
    else:
        return ('O','X')

#Deciding who go first.
def whoGoFirst():
    # Randomly choose the player who goes first.
    if random.randint(0,1)== 0:
        return 'computer'
    else:
        return 'player'

#Asking the player to play again.
def playAgain():
    #This function return TRUE if the player wants to play again
    print("Do you want to play again ? yes/no")
    if input().lower().startswith('y'):
        return True
    else:
        print("THANK YOU SO MUCH FOR PLAYING!")

#placing the mark on the board
def makeMove(board, letter, move):
    # The parameters are a list with ten strings named board, one of the player’s letters (either 'X' or 'O') named
    # letter, and a place on the board where that player wants to go (which is an integer from 1 to 9) named move.
    board[move] = letter

#checking if the player has won
def isWinner(bo, le):
    #Given a board and a player's letter, this function return TRUE if the player has won
    #we use bo instead of board and le instead of letter so we don't have to type as much
    #remember, Python doesn’t care what you name your variables. There are eight possible ways to win at Tic Tac Toe.
    return ((bo[7]==le and bo[8]==le and bo[9]==le)or #across the top row
    (bo[4]==le and bo[5]==le and bo[6]==le)or #across the middle row
    (bo[1]==le and bo[2]==le and bo[3]==le)or #across the buttom row
    (bo[7]==le and bo[4]==le and bo[1]==le)or #across the first column
    (bo[8]==le and bo[5]==le and bo[2]==le)or #across middle column
    (bo[9]==le and bo[6]==le and bo[3]==le)or #across the buttom column
    (bo[7]==le and bo[5]==le and bo[3]==le)or #across the backward diagonal
    (bo[9]==le and bo[5]==le and bo[1]==le)) #across the forward diagonal

#Duplicating the board data
def getBoardCopy(board):
    # Make the duplicate of the board list and return it the duplicate
    dupeBoard=[] #creating new list
    for i in board:
        dupeBoard.append(i) #adding items in the duplicating
    return dupeBoard

#checking if a space on the board is free
def isSpaceFree(board, move):
    #this function return true if pass move is free on the passed board
     if board[move] == '':
         return True
     else:
        return False

#letting the player enter their move
def getPlayerMove(board):
    #  Let the player type in their move
    move = ' '  #'1 2 3 4 5 6 7 8 9'.split() evaluates to ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

#choosing a Move  from a list of Moves
def chooseRandomMoveFromList(board, movelist):
    #Return a valid move from a passed list on the passed board
    #Return NONE if there is no valid move.
    possibleMoves=[]
    for i in movelist:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
        if len(possibleMoves)!=0:
            return random.choice(possibleMoves)
        else:
            return None

#CREATING THE ARTIFICIAL INTELLIGENCE
def getComputerMove(board, computerletter):
    # given the board and the computer letter, determine where to moves and return that moves
    if computerletter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

#the computer checks if it can win in one move
    #here is our algorithm for our tic tac toa
    #first check if we can win in next move
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy,computerletter, i)
            if isWinner(copy,computerletter):
                return i

    # the computer check if the player win in one move and if this then block playing in the same moves
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,playerLetter,i)
            if isWinner(copy,playerLetter):
                return i

    #checking the corner,center,side in that order
    #try to take one of the corner if they are free
    move = chooseRandomMoveFromList(board,[1,3,7,9])
    if move != None:
        return move
    #try to take the center, if it is free
    if isSpaceFree(board,5):
        return 5
    #try to take the side, if it is free
    return chooseRandomMoveFromList(board,[2,4,6,8])
    #This function won’t return None because the side spaces are the only spaces that can possibly be left.
    # This ends the getComputerMove() function and the AI algorithm
#checking if the board is full
def isBoardFull(board):
    #return true if every space is taken full, otherwise return false
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False    #As soon as for loops finds a free space on the board (that is, when isSpaceFree(board, i)
            # returns True) the isBoardFull() function will return False.

    return True


#THE START OF THE GAME
print("WELCOME TO TIC TAC TOA!")
while True:
    #reset the board    ,keep looping until the execution encounters a break statement
    theboard = ['']*10

    #deciding the Player's Mark and who goes first
    playerLetter,computerLetter = inputPlayerLetter()
    turn = whoGoFirst()
    print('The '+ turn + ' will go first.')
    gameIsPlaying = True # The gameIsPlaying variable keeps track of whether the game is still being played or if someone
                                                                            # has won or tied.
    #running the player turn
    while gameIsPlaying:
        if turn == 'player':  # Player’s turn.
            drawBoard(theboard)
            move = getPlayerMove(theboard)
            makeMove(theboard, playerLetter, move)

            if isWinner(theboard,playerLetter):
                drawBoard(theboard)
                print("HOORAY!  YOU HAVE WON THE GAME!")
                gameIsPlaying = False
            else:
                if isBoardFull(theboard):
                    drawBoard(theboard)
                    print("THE GAME IS TIE!")
                    break
                else:
                    turn = 'computer'
        #RUNNING THE COMPUTER'S TURN
        else: #COMPUTER'S TURN
            move = getComputerMove(theboard,computerLetter)
            makeMove(theboard,computerLetter, move)
            if isWinner(theboard,computerLetter):
                drawBoard(theboard)
                print('THE COMPUTER HAS BEATEN YOU! YOU LOSE.')
                gameIsPlaying = False
            else:
                if isBoardFull(theboard):
                    drawBoard(theboard)
                    print("THE GAME IS TIE!")
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break


