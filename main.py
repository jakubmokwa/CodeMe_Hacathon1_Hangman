import random


def get_random_word(word_list):
    return random.choice(word_list)


def game_round(word_list, num_of_rounds, game_word):
    pass


def main():
    word_list = ['pizza', 'empire', 'stellar', 'starfish', 'supremacy', 'federation', 'origin', 'battleship']
    num_of_rounds = 12
    game_word = get_random_word(word_list)
    game_round(word_list, num_of_rounds, game_word)


main()
