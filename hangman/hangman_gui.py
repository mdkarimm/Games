from tkinter import *
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import random

main = Tk()
main.title("Hangman")
main.geometry("800x600")

image_list = [Image.open(f"images/hangman0{i}.png") for i in range(1, 8)]

image_index = 0
hangman_image = ImageTk.PhotoImage(image_list[image_index])
image_label = Label(main, image=hangman_image)
image_label.image = hangman_image
image_label.place(x=0, y=0)


word_list = ["goodmorning", "hangman", "python", "programming", "tkinter", "challenge", "example"]

def new_game():
    global word, display_word, no_guess
    word = random.choice(word_list).lower()
    display_word = ["_"] * len(word) 
    no_guess = 0
    update_display()

def update_display():
    display_word_text.set(" ".join(display_word))
    hangman_image = ImageTk.PhotoImage(image_list[no_guess])
    image_label.config(image=hangman_image)
    image_label.image = hangman_image

def guess_letter():
    global no_guess
    guess = simpledialog.askstring("Guess", "Guess a letter: ").lower()
    
    if not guess or len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        return
    
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                display_word[i] = guess
        if "_" not in display_word:
            messagebox.showinfo("Hangman", "You win!")
            new_game()
    else:
        no_guess += 1
        if no_guess >= MAX_TRIES:
            messagebox.showinfo("Hangman", "You lose! The word was: " + word)
            new_game()
    
    update_display()

MAX_TRIES = 6
no_guess = 0
word = ""
display_word = []

display_word_text = StringVar()
display_word_text.set(" ".join(display_word))
word_label = Label(main, textvariable=display_word_text, font=("Helvetica", 24))
word_label.place(x=200, y=300)

guess_button = Button(main, text="Guess Letter", command=guess_letter, font=("Helvetica", 14))
guess_button.place(x=350, y=400)

new_game()

main.mainloop()
