'''
# Tic_Tac_Toe_Game

Tic Tac Toe is a two-player game in which the objective is to take turns and mark the correct spaces in a 3x3 (or larger) grid. 

Minimum of 3 turns required to win or Maxmium 5 turn a player will get.

On technical side side,

We can represent matrix 3 by 3 to represent Tic Tac Toe board via list. Player will get his/her chance turn by Turn

Steps:
    
1. Print the board after every Turn.
2. Print the empty space for Player A and ask where he wants to place 'X'
3. Check the winning position
4. if win, exit the game
5. Else , move to next Game

'''

# Data structure of tic tac Toe board ( 3 * 3 board )

tic_tac_toe_board = [ ['_' for _ in range(3) ] for _ in range(3)]   # Initialize the board with '_'

print(tic_tac_toe_board)

# Function to print the board
def print_tictac_board(tic_tac_toe_board):
    for x in tic_tac_toe_board:
        for i in range(len(x)):
            if i == 2 :
                print(x[i] )
            else :
                print(x[i] , end = '|')


#Function to find the available space:

def find_avail_space_on_tic_tac_board(tic_tac_toe_board):
    avail_space_list = []
    for i in range(len(tic_tac_toe_board)):
        for j in range(len(tic_tac_toe_board[i])):
            if tic_tac_toe_board[i][j] == '_' :
                avail_space = 'R' + str(i+1) + '&C' + str(j+1)
                avail_space_list.append(avail_space)
                
    return avail_space_list
                
# Function to check winning situation

def is_winning(tic_tac_toe_board , symbol):
    
    if ( tic_tac_toe_board[0][0] == symbol ) &  ( tic_tac_toe_board[0][1] == symbol ) &  ( tic_tac_toe_board[0][2] == symbol ):
        return True
    elif ( tic_tac_toe_board[1][0] == symbol ) &  ( tic_tac_toe_board[1][1] == symbol ) &  ( tic_tac_toe_board[1][2] == symbol ):
        return True
    elif ( tic_tac_toe_board[2][0] == symbol ) &  ( tic_tac_toe_board[2][1] == symbol ) &  ( tic_tac_toe_board[2][2] == symbol ):
        return True
    elif ( tic_tac_toe_board[0][0] == symbol ) &  ( tic_tac_toe_board[1][0] == symbol ) &  ( tic_tac_toe_board[2][0] == symbol ):
        return True
    elif ( tic_tac_toe_board[0][1] == symbol ) &  ( tic_tac_toe_board[1][1] == symbol ) &  ( tic_tac_toe_board[2][1] == symbol ):
        return True
    elif ( tic_tac_toe_board[0][2] == symbol ) &  ( tic_tac_toe_board[1][2] == symbol ) &  ( tic_tac_toe_board[2][2] == symbol ):
        return True
    elif ( tic_tac_toe_board[0][0] == symbol ) &  ( tic_tac_toe_board[1][1] == symbol ) &  ( tic_tac_toe_board[2][2] == symbol ):
        return True
    elif ( tic_tac_toe_board[0][2] == symbol ) &  ( tic_tac_toe_board[1][1] == symbol ) &  ( tic_tac_toe_board[2][0] == symbol ):
        return True
    
    return False

# Function to fill the space
def place_symbol_on_tic_tac_board(tic_tac_toe_board , place_selected , symbol ):
    
    # if row is gretear than 3 and less than 1
    if int(place_selected[1]) > 3 or int(place_selected[1]) < 1 :        
        return False
    
    # if col is gretear than 3 and less than 1    
    if int(place_selected[4]) > 3 or int(place_selected[4]) < 1 :
        return False
    
    # check the index from selected available place
    i = int(place_selected[1]) - 1
    j = int(place_selected[4]) - 1
    
    # if blank space
    if tic_tac_toe_board[i][j] == '_' :
        
        tic_tac_toe_board[i][j] = symbol     # place the symbol
        
        return tic_tac_toe_board            # return the board
    else :
        return False
        
    

def play_tic_tac_toe_game():
    print("Welcome To TIC TAC TOE GAME")
    print("---------------------------\n")
    
    # 1. Initialize the board     
    tic_tac_toe_board = [ ['_' for _ in range(3) ] for _ in range(3)]   # Initialize the board with '_'
    
    for i in range(1,25,1):
        
        # 2 . print the board
        print_tictac_board(tic_tac_toe_board)
        print("\n\n")
        print(f"Available space on Tic Tac Toe Board is : {find_avail_space_on_tic_tac_board(tic_tac_toe_board)}\n")
        
        print("\n\n")
        if len(find_avail_space_on_tic_tac_board(tic_tac_toe_board)) == 0 :
            print("Match Draw")
            return
        
        if i % 2 == 0 :
            print("It's Player B's Turn .")
            print("**********************")
            symbol = 'O'
        else :
            print("It's Player A's Turn \n")
            print("**********************")
            symbol = 'X'

        place_selected = input(f"Please Enter where you want to place {symbol} : ")
        
        #result = place_symbol_on_tic_tac_board(tic_tac_toe_board , place_selected , symbol )
            
        #if result:
        if place_symbol_on_tic_tac_board(tic_tac_toe_board , place_selected , symbol ):
            #tic_tac_toe_board = result
            
            if len(find_avail_space_on_tic_tac_board(tic_tac_toe_board)) < 5 :
                if is_winning(tic_tac_toe_board , symbol):
                    if symbol == 'X' :
                        print("Player A WON The Game")
                    else :
                        print("Player B WON The Game")
                    print_tictac_board(tic_tac_toe_board)
                    return                       
        else :
            print("You have choosen wrong place")                   
            i = i -1   

    
    
# Play the game

play_tic_tac_toe_game()