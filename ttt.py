# tic tak toe{ai} using minimax algo.....

import tkinter as tk
from tkinter import messagebox
import random

# Initialize the main tkinter window
root = tk.Tk()
root.title("Tic Tac Toe")

# Variable to track current player (X or O)
current_player = "X"
game_over = False

# Create buttons for the Tic Tac Toe grid
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text="", width=10, height=5,background="lavender",
                           font=('Arial', 20, 'bold'),
                           command=lambda r=i, c=j: on_button_click(r, c))
        button.grid(row=i, column=j, padx=5, pady=5)
        row.append(button)
    buttons.append(row)

# Function to handle button click
def on_button_click(row, col):
    global current_player, game_over
    
    if buttons[row][col]["text"] == "" and not game_over:
        buttons[row][col]["text"] = current_player
        if check_winner(current_player):
            messagebox.showinfo("Tic Tac Toe", f"{current_player} Wins Sir!")
            game_over = True
        elif all(buttons[r][c]["text"] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("Tic Tac Toe", "It's a Tie Sir!")
            game_over = True
        else:
            current_player = "O"
            computer_move()

# Function for the computer's move
def computer_move():
    global current_player, game_over
    
    # Simple AI: choose the first available empty cell
    for r in range(3):
        for c in range(3):
            if buttons[r][c]["text"] == "":
                buttons[r][c]["text"] = current_player
                if check_winner(current_player):
                    messagebox.showinfo("Tic Tac Toe", f"{current_player} wins!")
                    game_over = True
                elif all(buttons[row][col]["text"] != "" for row in range(3) for col in range(3)):
                    messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                    game_over = True
                current_player = "X"
                return

# Function to check for a winner
def check_winner(player):
    # Check rows
    for r in range(3):
        if all(buttons[r][c]["text"] == player for c in range(3)):
            return True
    
    # Check columns
    for c in range(3):
        if all(buttons[r][c]["text"] == player for r in range(3)):
            return True
    
    # Check diagonals
    if all(buttons[i][i]["text"] == player for i in range(3)):
        return True
    if all(buttons[i][2-i]["text"] == player for i in range(3)):
        return True
    
    return False

# Start the tkinter main loop
root.mainloop()
