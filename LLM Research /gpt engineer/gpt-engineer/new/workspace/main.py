from game import Game

def main():
    min_num = 1
    max_num = 100
    max_attempts = 5

    game = Game(min_num, max_num, max_attempts)
    game.start()

if __name__ == "__main__":
    main()
