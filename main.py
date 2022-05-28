import random


def check_guess(word, game_word):
    if len(word) == 1 or len(word) == len(game_word):
        return True
    return False


def get_guess(game_word):
    while True:
        word = input("Write your letter or guess the word (must be the same amount of letters) -> ")
        if check_guess(word, game_word):
            return word
        else:
            print("Error, your guess isn't a single letter or a word with the same amount of letters as required")


def get_random_word(word_list):
    return random.choice(word_list)


def game_round(num_of_rounds, game_word, player_word):
    for i in range(num_of_rounds):
        round_guess = get_guess(game_word)


def main():
    word_list = ['pizza', 'empire', 'stellar', 'starfish', 'supremacy', 'federation', 'origin', 'battleship']
    num_of_rounds = 12
    game_word = get_random_word(word_list)
    player_word = ['_' * len(game_word)]
    game_round(num_of_rounds, game_word, player_word)


main()
