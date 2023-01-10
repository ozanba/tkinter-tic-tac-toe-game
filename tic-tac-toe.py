from tkinter import *
import random
from tkmacosx import Button
root = Tk()

root.title("Tic-Tac-Toe XOX")

def o_first_clicked():

    x_first_button.grid_forget()
    o_first_button.grid_forget()
    random_button.grid_forget()
    decide_who_first.grid_forget()
     
    global first_player
    global second_player
    first_player = "O"
    second_player = "X"
    game()

def x_first_clicked():
    
    x_first_button.grid_forget()
    o_first_button.grid_forget()
    random_button.grid_forget()
    decide_who_first.grid_forget()
    global first_player
    global second_player
    first_player = "X"
    second_player = "O"
    game()

def random_clicked():
  
   
    global first_player
    global second_player
    randomN = random.randrange(1,3)
    if randomN ==1:
        first_player = "X"
        second_player = "O"
    elif randomN ==2:
        first_player = "O"
        second_player = "X"
        
    x_first_button.grid_forget()
    o_first_button.grid_forget()
    random_button.grid_forget()
    decide_who_first.grid_forget()
    game()

def multiplayer():
    global decide_who_first
    global x_first_button
    global o_first_button
    global random_button
    
    #delete main screen
    ask_game_mode.grid_forget()
    single_player_button.grid_forget()
    multiplayer_button.grid_forget()
    #Print
    decide_who_first= Label(root, text="How to decide who is first ",font=('Times',24))
    decide_who_first.grid(row=0, column=0, columnspan=3)
    x_first_button= Button(root, text="X",font=('Times',24), command=x_first_clicked)
    x_first_button.grid(row=1, column=0)
    o_first_button= Button(root, text="O",font=('Times',24), command=o_first_clicked)
    o_first_button.grid(row=1, column=1)
    random_button = Button(root, text="Random",font=('Times',24), command=random_clicked)
    random_button.grid(row=1, column=2)

def clear_board():
    b1["state"] = "normal"
    b2["state"] = "normal"
    b3["state"] = "normal"
    b4["state"] = "normal"
    b5["state"] = "normal"
    b6["state"] = "normal"
    b7["state"] = "normal"
    b8["state"] = "normal"
    b9["state"] = "normal"
    
    b1["text"] = " "
    b2["text"] = " "
    b3["text"] = " "
    b4["text"] = " "
    b5["text"] = " "
    b6["text"] = " "
    b7["text"] = " "
    b8["text"] = " "
    b9["text"] = " "
    
    
    b1["bg"] = "white"
    b2["bg"] = "white"
    b3["bg"] = "white"
    b4["bg"] = "white"
    b5["bg"] = "white"
    b6["bg"] = "white"
    b7["bg"] = "white"
    b8["bg"] = "white"
    b9["bg"] = "white"
       
def game():
    heights= 100
    widths=200
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    b1 = Button(text=" ", font=("Helvetica", 24), height=heights, width=widths, command= lambda: b_click(b1) )
    b2 = Button(text=" ", font=("Helvetica", 24), height=heights, width=widths, command= lambda: b_click(b2) )
    b3 = Button(text=" ", font=("Helvetica", 24), height=heights, width=widths, command= lambda: b_click(b3) )
    b4 = Button(text=" ", font=("Helvetica", 24), height=heights, width=widths, command= lambda: b_click(b4) )
    b5 = Button(text=" ", font=("Helvetica", 24), height=heights, width=widths, command= lambda: b_click(b5) )
    b6 = Button(text=" ", font=("Helvetica", 24), height=heights, width=widths, command= lambda: b_click(b6) )
    b7 = Button(text=" ", font=("Helvetica", 24), height=heights, width=widths, command= lambda: b_click(b7) )
    b8 = Button(text=" ", font=("Helvetica", 24), height=heights, width=widths, command= lambda: b_click(b8) )
    b9 = Button(text=" ", font=("Helvetica", 24), height=heights, width=widths, command= lambda: b_click(b9) )
    b1.grid(row=0, column=0)    
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    
    b4.grid(row=1, column=0)    
    b5.grid(row=1, column=1)    
    b6.grid(row=1, column=2)  
      
    b7.grid(row=2, column=0)    
    b8.grid(row=2, column=1)    
    b9.grid(row=2, column=2)
    
    global second_player_wins
    global first_player_wins
    score_board= Label(text="Score Board", font=("Times", 24), )
    score_board.grid(row=0, column=4, columnspan=3)   
    
    first_player_wins = Label(text="%s First Player:0"%first_player,font=("Times", 24),)
    second_player_wins =Label(text="%s Second Player:0"%second_player,font=("Times", 24),)
    
    first_player_wins.grid(row=1, column=4, sticky='w')
    second_player_wins.grid(row=2, column=4)
    #clear button
    clear_button = Button(text="Clear board", padx=30,pady=30, command=clear_board)
    clear_button.grid(row=1, column=5)
    
def b_disable():
    b1["state"] = "disabled"
    b2["state"] = "disabled"
    b3["state"] = "disabled"
    b4["state"] = "disabled"
    b5["state"] = "disabled"
    b6["state"] = "disabled"
    b7["state"] = "disabled"
    b8["state"] = "disabled"
    b9["state"] = "disabled"

global second_player_win
global first_player_win

second_player_win = 0
first_player_win = 0

def checkwin():
    global second_player_win 
    global first_player_win
    if b1["text"]== first_player and b2["text"]== first_player and b3["text"]== first_player:
        b_disable()
        b1["bg"] = "green"
        b2["bg"] = "green"
        b3["bg"] = "green"
        first_player_win = first_player_win +1
    elif b1["text"]== second_player and b2["text"]== second_player and b3["text"]== second_player:
        b_disable()
        b1["bg"] = "green"
        b2["bg"] = "green"
        b3["bg"] = "green"
        second_player_win = second_player_win +1
    elif b4["text"]== first_player and b5["text"]== first_player and b6["text"]== first_player:
        b_disable()
        b4["bg"] = "green"
        b5["bg"] = "green"
        b6["bg"] = "green"
        first_player_win = first_player_win +1
    elif b4["text"]== second_player and b5["text"]== second_player and b6["text"]== second_player:
        b_disable()
        b4["bg"] = "green"
        b5["bg"] = "green"
        b6["bg"] = "green"
        second_player_win = second_player_win +1
    elif b7["text"]== first_player and b8["text"]== first_player and b9["text"]== first_player:
        b_disable()
        b7["bg"] = "green"
        b8["bg"] = "green"
        b9["bg"] = "green"
        first_player_win = first_player_win +1
    elif b7["text"]== second_player and b8["text"]== second_player and b9["text"]== second_player:
        b_disable()
        b7["bg"] = "green"
        b8["bg"] = "green"
        b9["bg"] = "green"
        second_player_win = second_player_win +1
    elif b1["text"]== second_player and b5["text"]== second_player and b9["text"]== second_player:
        b_disable()
        b1["bg"] = "green"
        b5["bg"] = "green"
        b9["bg"] = "green"
        second_player_win = second_player_win +1
    elif b1["text"]== first_player and b5["text"]== first_player and b9["text"]== first_player:
        b_disable()
        b1["bg"] = "green"
        b5["bg"] = "green"
        b9["bg"] = "green"
        first_player_win = first_player_win +1
    elif b3["text"]== second_player and b5["text"]== second_player and b7["text"]== second_player:
        b_disable()
        b3["bg"] = "green"
        b5["bg"] = "green"
        b7["bg"] = "green"
        second_player_win = second_player_win +1,
    elif b3["text"]== first_player and b5["text"]== first_player and b7["text"]== first_player:
        b_disable()
        b3["bg"] = "green"
        b5["bg"] = "green"
        b7["bg"] = "green"
        first_player_win = first_player_win +1
    elif b1["text"]== first_player and b4["text"]== first_player and b7["text"]== first_player:
        b_disable()
        b1["bg"] = "green"
        b4["bg"] = "green"
        b7["bg"] = "green"  
        first_player_win = first_player_win +1 
    elif b1["text"]== second_player and b4["text"]== second_player and b7["text"]== second_player:
        b_disable()
        b1["bg"] = "green"
        b4["bg"] = "green"
        b7["bg"] = "green"   
        second_player_win = second_player_win +1
    elif b2["text"]== first_player and b5["text"]== first_player and b8["text"]== first_player:
        b_disable()
        b2["bg"] = "green"
        b5["bg"] = "green"
        b8["bg"] = "green" 
        first_player_win = first_player_win +1  
    elif b2["text"]== second_player and b5["text"]== second_player and b8["text"]== second_player:
        b_disable()
        b2["bg"] = "green"
        b5["bg"] = "green"
        b8["bg"] = "green"  
        second_player_win = second_player_win +1 
    elif b3["text"]== first_player and b6["text"]== first_player and b9["text"]== first_player:
        b_disable()
        b3["bg"] = "green"
        b6["bg"] = "green"
        b9["bg"] = "green"  
        first_player_win = first_player_win +1   
    elif b3["text"]== second_player and b6["text"]== second_player and b9["text"]== second_player:
        b_disable()
        b3["bg"] = "green"
        b6["bg"] = "green"
        b9["bg"] = "green"
        second_player_win = second_player_win +1  
    
    
    first_player_wins["text"]= "%s First Player: %d" % (first_player,first_player_win ) 
    second_player_wins["text"]= "%s Second Player: %d" % (second_player,second_player_win)   
    
         
    
#main screen
ask_game_mode= Label(root, text="Game Mode",font=('Times', 24) )
ask_game_mode.grid(row=0, column=0, columnspan=2)
#single player button
single_player_button= Button(root, text="Single Player",state="disabled",font=('Times', 24))
single_player_button.grid(row=1, column=0)
#multiplayer button
multiplayer_button= Button(root, text="Multiplayer",font=('Times', 24), command=multiplayer)
multiplayer_button.grid(row=1, column=1)


b_clicked = True 
count_play = 1


def b_click(b):
    global count_play
    global b_clicked 
    

    if b["text"]== " " and b_clicked==True:
        if count_play % 2  == 1:
            b["text"] = first_player
        count_play = count_play + 1
        b_clicked = False
        checkwin()
    
    if b["text"]== " " and b_clicked==False:

        b["text"] = second_player
        count_play = count_play + 1
        b_clicked = True
        checkwin()
        
root.mainloop()