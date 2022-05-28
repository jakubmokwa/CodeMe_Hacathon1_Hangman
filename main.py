import random


def check_guess(word, game_word):
    if len(word) == 1 or len(word) == len(game_word):
        return True
    return False


def get_guess(game_word, num_of_rounds, round_num):
    while True:
        word = input(f"Write your letter or guess the word ({num_of_rounds - round_num} guesses left) -> ")
        if check_guess(word, game_word):
            return word
        else:
            print("Error, your guess isn't a single letter or a word with the same amount of letters as required")


def get_random_word(word_list):
    return random.choice(word_list)


def game_round(num_of_rounds, game_word, player_word):
    round_num = 0
    while round_num < num_of_rounds:
        round_guess = get_guess(game_word, num_of_rounds, round_num)
        round_guess = round_guess.lower()
        if len(round_guess) == 1:
            for index, letter in enumerate(game_word):
                if letter == round_guess:
                    player_word[index] = round_guess
                    round_num -= 1
            if '_' not in player_word:
                print("Player won")
                break
        else:
            if list(round_guess) == game_word:
                print("Player won")
                break
        round_num += 1
        print(*player_word)


def main():
    word_list = ['pizza', 'empire', 'stellar', 'starfish', 'supremacy', 'federation', 'origin', 'battleship']
    num_of_rounds = 12
    game_word = list(get_random_word(word_list))
    player_word = list('_' * len(game_word))
    game_round(num_of_rounds, game_word, player_word)


main()
