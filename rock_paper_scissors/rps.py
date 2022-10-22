#!/bin/python3
from enum import IntEnum
import random, time

class Game(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

results = {
        Game.Rock : [Game.Scissors],
        Game.Scissors : [Game.Paper],
        Game.Paper : [Game.Rock]
        }

def player_selection():
    options = [f"{option.name} [{option.value}]" for option in Game]
    player_choice = int(input(f"Enter your choice: {options}\n"))    
    player = Game(player_choice)
    print("Computer is thinking...")
    time.sleep(random.randint(1, 5))
    return player

def computer_selection():
    computer_choice = random.randint(0,2)
    computer = Game(computer_choice)
    return computer 

def choose_winner(player, computer):
    computer_won = results[player]
    if player == computer:
       print(f"It's a draw! Both of you selected: {player.name}!")
    elif computer in computer_won:
       print(f"You won! {player.name} beats {computer.name}. Congratulations!")
    else:
        print(f"You lost! {computer.name} beats {player.name}! Try again!")

while True:
    try:
        you = player_selection()
    except ValueError as e:
        choice_range = f"(0, {len(Game) - 1})"
        print(f"You have to pick number in range: {choice_range}.")
        continue
    comp = computer_selection()
    choose_winner(you, comp)

    and_another_one = input("Do you want to play again? Y/N\n")
    if and_another_one.upper() != "Y":
        break
