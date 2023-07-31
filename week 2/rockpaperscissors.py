import tkinter as tk 
import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!" 
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') 
        or (user_choice == 'paper' and computer_choice == 'rock') or 
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!" 
    else:
        return "Computer wins!"
def play_game():
    user_choice = user_choice_var.get()
    computer_choice = get_computer_choice()
    result = determine_winner (user_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
# Create the main window

window = tk.Tk()
window. title("Rock, Paper, Scissors")
# Create the user choice label and dropdown
user_choice_label = tk. Label (window, text="Choose:") 
user_choice_label.pack()
user_choice_var = tk.StringVar (window)
user_choice_var.set ('rock')
user_choice_dropdown = tk. OptionMenu (window, user_choice_var, 'rock', 'paper', 'scissors')
user_choice_dropdown.pack()
# Create the play button
play_button = tk.Button (window, text="Play", command=play_game) 
play_button.pack()
# Create the result label
result_label = tk.Label (window, text="") 
result_label. pack()
# Start the Tkinter event Loop
window.mainloop ()