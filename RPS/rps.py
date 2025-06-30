import random
import os
import pickle
from typing import Dict, Tuple, Optional

class GameData:
    
    def __init__(self, name: str, wins: int = 0, losses: int = 0, ties: int = 0):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.ties = ties


class RockPaperScissors:
    
    def __init__(self):
        
        self.name = ""
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
        
    def start(self):

        print("Welcome to Rock, Paper, Scissors!\n")
        while True:
            print("1. Start New Game")
            print("2. Load Game")
            print("3. Quit\n")
            
            choice = self.get_valid_input("Enter choice: ", range(1, 4))
            
            if choice == 1:
                self.new_game()
            elif choice == 2:
                self.load_game()
            elif choice == 3:
                break
    
    def new_game(self):
        

        self.name = input("\nWhat is your name? ")
        self.wins = 0
        self.losses = 0
        self.ties = 0
        print(f"\nHello {self.name}. Let's play!\n")
        self.play()
    
    def load_game(self):

        self.name = input("\nWhat is your name? ")
        filename = f"{self.name}.rps"
        
        try:
            if os.path.exists(filename):
                with open(filename, "rb") as file:
                    game_data = pickle.load(file)
                    self.name = game_data.name
                    self.wins = game_data.wins
                    self.losses = game_data.losses
                    self.ties = game_data.ties
                print(f"\nWelcome back {self.name}. Let's play!\n")
                self.play()
            else:
                print(f"\n{self.name}, your game could not be found.")
        except Exception as e:
            print(f"\n{self.name}, your game could not be found.")
            print(f"Error: {str(e)}")
    
    def play(self):
        
        round_number = self.wins + self.losses + self.ties + 1
        
        while True:
            print(f"Round {round_number}\n")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors\n")
            
            user_choice = self.get_valid_input("What will it be? ", range(1, 4))
            comp_choice = random.randint(1, 3)
            
            user_choice_name = self.choices[user_choice]
            comp_choice_name = self.choices[comp_choice]
            
            result = self.determine_winner(user_choice, comp_choice)
            
            if result == "win":
                print(f"\nYou chose {user_choice_name}. The computer chose {comp_choice_name}. You win!")
                self.wins += 1
            elif result == "lose":
                print(f"\nYou chose {user_choice_name}. The computer chose {comp_choice_name}. You lose!")
                self.losses += 1
            else:  # tie
                print(f"\nYou chose {user_choice_name}. The computer chose {comp_choice_name}. It's a tie!")
                self.ties += 1
            
            print("\nWhat would you like to do?\n")
            print("1. Play Again")
            print("2. View Statistics")
            print("3. Quit\n")
            
            choice = self.get_valid_input("Enter choice: ", range(1, 4))
            
            if choice == 1:
                round_number += 1
                print()  # Add a blank line for better formatting
            elif choice == 2:
                self.display_statistics()
            elif choice == 3:
                self.save_game()
                break
    
    def determine_winner(self, user_choice: int, comp_choice: int) -> str:
       
        if user_choice == comp_choice:
            return "tie"
        
        # Rock beats Scissors, Scissors beats Paper, Paper beats Rock
        if (user_choice == 1 and comp_choice == 3) or \
           (user_choice == 3 and comp_choice == 2) or \
           (user_choice == 2 and comp_choice == 1):
            return "win"
        else:
            return "lose"
    
    def display_statistics(self):
        """Display the game statistics."""
        print(f"\n{self.name}, here are your game play statistics...")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        print(f"Ties: {self.ties}\n")
        
        win_loss_ratio = 0.0
        if self.losses > 0:
            win_loss_ratio = self.wins / self.losses
        
        print(f"Win/Loss Ratio: {win_loss_ratio:.2f}\n")
    
    def save_game(self):
        """Save the game data to a file."""
        try:
            game_data = GameData(self.name, self.wins, self.losses, self.ties)
            with open(f"{self.name}.rps", "wb") as file:
                pickle.dump(game_data, file)
            print(f"\n{self.name}, your game has been saved.")
        except Exception as e:
            print(f"\nSorry {self.name}, the game could not be saved.")
            print(str(e))
    
    def get_valid_input(self, prompt: str, valid_range) -> int:
      
        while True:
            try:
                user_input = input(prompt)
                user_choice = int(user_input)
                if user_choice in valid_range:
                    return user_choice
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a number.")


if __name__ == "__main__":
    game = RockPaperScissors()
    game.start()
