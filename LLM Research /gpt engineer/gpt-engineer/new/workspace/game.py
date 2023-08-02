import random

class Game:
    def __init__(self, min_num, max_num, max_attempts):
        self.min_num = min_num
        self.max_num = max_num
        self.max_attempts = max_attempts
        self.secret_number = self.generate_random_number()
    
    def generate_random_number(self):
        return random.randint(self.min_num, self.max_num)
    
    def validate_guess(self, guess):
        if guess < self.secret_number:
            return "Too low"
        elif guess > self.secret_number:
            return "Too high"
        else:
            return "Correct!"
    
    def start(self):
        print(f"Welcome to the Number Guessing Game! Guess a number between {self.min_num} and {self.max_num}.")
        attempts = 0
        while attempts < self.max_attempts:
            guess = self.get_guess()
            result = self.validate_guess(guess)
            print(result)
            attempts += 1
            if result == "Correct!":
                print("Congratulations! You guessed the correct number.")
                break
            elif attempts == self.max_attempts:
                print(f"Game over! The correct number was {self.secret_number}.")
        self.play_again()
    
    def play_again(self):
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            self.secret_number = self.generate_random_number()
            self.start()
        else:
            print("Thank you for playing!")

    def get_guess(self):
        while True:
            try:
                guess = int(input("Enter your guess: "))
                if self.min_num <= guess <= self.max_num:
                    return guess
                else:
                    print(f"Please enter a number between {self.min_num} and {self.max_num}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
