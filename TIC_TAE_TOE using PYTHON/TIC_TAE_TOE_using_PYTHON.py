#+++++++++++++++++++global variable++++++++++++++
#game board
board=["_" ,"_","_",
      "_" ,"_","_",
      "_" ,"_","_"]
#if game is still going
game_is_still_going=True
#who won?or tie?
winner=None
#who turn next 
current_player="x"

def dispaly_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])
def play_game():
    #dispaly the board
   dispaly_board()
   while game_is_still_going:
       #handle a single turn to an arbitory player
     handle_turn(current_player)
     #check the game is over
     check_if_game_iz_over()
     #flip to the other player
     flip_player()
     #the game has ended
   if winner=="x"or winner=="o":
        print(winner+"won.")
   elif winner==None:
       print("TIE")
def check_if_game_iz_over():
    check_if_wins()
    check_if_tie()
def check_if_wins():
    #check rows
    #check colums
    #check diagnols
    return
def check_rows():
    return 
def check_coloum():
    return
def check_diagonals():
    return
def check_if_tie():
    
    return
def flip_player():
    return
def handle_turn(player):
    position=input("enter the position from 1-9")
    position=int(position)-1
    board[position]="x"
    dispaly_board()
play_game()