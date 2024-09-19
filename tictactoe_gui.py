from tkinter import *
from tkinter import messagebox
from functools import partial

main = Tk()
main.geometry("300x300")
main.title("Tic Tac Toe")
main.configure(bg="#f0f0f0")  

field = [' '] * 9
current_player = 'X'
buttons = []

def btn_click(index):
    global current_player
    if field[index] == ' ':
        field[index] = current_player
        buttons[index].config(text=current_player, bg='lightblue' if current_player == 'X' else 'lightcoral', state=DISABLED)
        if check_winner(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif ' ' not in field:
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X'


def check_winner(player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
        (0, 4, 8), (2, 4, 6)             
    ]
    for a, b, c in win_conditions:
        if field[a] == field[b] == field[c] == player:
            return True
    return False

def reset_game():
    global field, current_player
    field = [' '] * 9
    current_player = 'X'
    for button in buttons:
        button.config(text=' ', bg='lightgray', state=NORMAL)


frame = Frame(main, bg="#f0f0f0")
frame.pack(pady=10)

for i in range(9):
    button = Button(frame, text=' ', font=("Arial", 20), width=5, height=2, bg='lightgray', fg='black', command=partial(btn_click, i))
    row, col = divmod(i, 3)
    button.grid(row=row, column=col, padx=5, pady=5)
    buttons.append(button)

reset_button = Button(main, text="Reset Game", font=("Arial", 14), bg='lightgreen', command=reset_game)
reset_button.pack(pady=10)

main.mainloop()
