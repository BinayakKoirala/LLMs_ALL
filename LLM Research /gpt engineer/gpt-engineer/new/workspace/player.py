class Player:
    def __init__(self, name):
        self.name = name
    
    def get_guess(self):
        while True:
            try:
                guess = int(input("Enter your guess: "))
                return guess
            except ValueError:
                print("Invalid input. Please enter a valid number.")
