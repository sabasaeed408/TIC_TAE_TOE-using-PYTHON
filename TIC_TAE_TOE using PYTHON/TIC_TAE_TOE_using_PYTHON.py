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
    global winner
    #check rows
    row_winner=check_rows()
    #check colums
    coloum_winner=check_coloum()
    #check diagnols
    diagnol_winner=check_diagonals()
    if row_winner:
        winner=row_winner
        #there was a win
    elif coloum_winner:
        #there was a win
        winner=coloum_winner
    elif diagnol_winner:
        #there was a win
        winner=diagnol_winner
    else:
        #there was no win
        winner=None
    return
def check_rows():
    global game_is_still_going
    row1=board[0]==board[1]==board[2]!="_"
    row2=board[3]==board[4]==board[5]!="_"
    row3=board[6]==board[7]==board[8]!="_"
    if row1 or row2 or row3:
        game_is_still_going=False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return 
def check_coloum():
    global game_is_still_going
    coloum1=board[0]==board[3]==board[6]!="_"
    coloum2=board[1]==board[4]==board[7]!="_"
    coloum3=board[2]==board[5]==board[8]!="_"
    if coloum1 or coloum2 or coloum3:
        game_is_still_going=False
    if coloum1:
        return board[0]
    elif coloum2:
        return board[1]
    elif coloum3:
        return board[2]
    return
def check_diagonals():
    global game_is_still_going
    diagnol1=board[0]==board[4]==board[8]!="_"
    diagnol2=board[2]==board[4]==board[6]!="_"
    if diagnol1 or diagnol2:
        game_is_still_going=False
    if diagnol1:
        return board[0]
    elif diagnol2:
        return board[2]
    return
def check_if_tie():
    global game_is_still_going
    if "_" not in board:
        game_is_still_going=False

    
    return
def flip_player():
    global current_player
    if current_player=="x":
        current_player="o"
    elif current_player=="o":
        current_player="x"
    return
def handle_turn(player):
    print(player+"turn.")
    position=input("enter the position from 1-9")
    valid=False
    while not valid:
    
       while position not in ["1","2","3","4","5","6","7","8","9"]:
         positon=input("INVALID STATEMENT Choose no from 1to 9 again")
       position=int(position)-1
       if board[position]=="_":
        valid=True
       else:
        print("you can't over write go again")

    board[position]=player
    dispaly_board()


play_game()
