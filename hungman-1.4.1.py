import random

HANGMAN_ASCII_ART=("""
welcome to the game Hangman\n

  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/|

""")
MAX_TRIES=6
num_of_tries = 0
RANDOM_NUMBER=(random.randint(5, 10))
num_of_occurences_in_old_letters_guessed = 0
old_letters_guessed = []
HANGMAN_PHOTOS = {0: "x-------x", \
                1: """
    x-------x
    |
    |
    |
    |
    |
    """, \
                2: """
    x-------x
    |       |
    |       0
    |
    |
    |
    """, \
    3: """
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """, \
            4: """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
    """, \
            5: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """, \
            6: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """
    }

def main():

    global num_of_tries
    global num_of_occurences_in_old_letters_guessed

    def welcome_messege():
        print(HANGMAN_ASCII_ART)
        print("Your max tries are:", MAX_TRIES, "tries")
        global letter_guessed
    
    def print_hangman(num_of_tries):
        print(HANGMAN_PHOTOS[num_of_tries])
    # print_hangman(6)

    def choose_word(file_path, index):
        with open(file_path, "r") as f:
            lines_list = f.read()
            words_list = lines_list.split(" ")
            words_list[-1] = words_list[-1][:-1]
            if index > len(words_list):
                new_index = index % len(words_list)
                return words_list[new_index - 1]
            else:
                return words_list[index - 1]
    # print(choose_word("/home/stav/Documents/Courses/python-course/course-python-projects/hello.txt", 6))
    
    def check_valid_input(letter_guessed, old_letters_guessed): 
        global is_valid
        if len(letter_guessed) > 1:
            is_valid = False
            return is_valid
            print("Please type only english characters here")
        elif letter_guessed.isalpha() == False:
            is_valid = False
            return is_valid
            print("Please type only english characters here")
        elif letter_guessed.lower() in old_letters_guessed:
            is_valid = False
            return is_valid
            print("Please type only english characters here")
        else:
            is_valid = True
            return is_valid
        # print(is_valid)
        # print(letter_guessed)
        # word=input("Please write here the word in the game: ")
        # word_length=len(word)
        # print("_" * word_length)
    # check_valid_input('a', ['a', 'b', 'c'])
    
    def try_update_letter_guessed(letter_guessed, old_letters_guessed):
        if check_valid_input(letter_guessed, old_letters_guessed) == True:
            old_letters_guessed += letter_guessed
            is_valid = True
            return is_valid
            print(old_letters_guessed)
        else:
            is_valid = False
            print("X")
            print(" -> ".join(old_letters_guessed))
            return is_valid
    # try_update_letter_guessed('a', ['k', 'b', 'c'])
    
    def show_hidden_word(secret_word, old_letters_guessed):
        """
        This function shows to the player his progress in the game.
        :parameter name: secret_word - a word that the player should enter
        old_letters_guessed - letters that the player allready guessed
        :type: str, list
        :return: The function returns string that contains letters and underlines.
        :rtype: str
        """
        global guessed_word
        guessed_word = []
        for letter in secret_word:
            guessed_word += ["_"]
        for letter in secret_word:
            if letter in old_letters_guessed:
                indices = [i for i, x in enumerate(secret_word) if x == letter]
                for item in indices:
                    guessed_word[item] = letter
        return ' '.join(guessed_word)
    # print(show_hidden_word("mammals", ["m", "z"]))
    
    def num_of_tries_up():
        global num_of_occurences_in_old_letters_guessed
        if letter_guessed in guessed_word:
            num_of_occurences_in_old_letters_guessed += 1
        num_of_tries = len(old_letters_guessed) - num_of_occurences_in_old_letters_guessed

    def check_win(secret_word, old_letters_guessed):
        global game_win
        """
        This function checks if the player guessed the secret word and won the game
        :parameter name: secret_word, old_letters_guessed
        :type: str, list
        :return: True or False values
        :rtype: bool
        """
        good_guesses = []
        for letter in secret_word:
            if letter in old_letters_guessed:
                good_guesses += [letter]
        if len(good_guesses) == len(secret_word):
            game_win = True
            return game_win
        else:
            game_win = False
            return game_win
    # print(check_win("pizza", ["p", "i", "z", "a", "b"]))

    welcome_messege()
    # while is_valid != True:
    #     print("Please type only english characters here")
    #     letter_guessed = (input("Guess a letter: ")).lower()
    chosen_word = ''
    while len(chosen_word) == 0:
        chosen_word = input("Please enter here the path to the file that you want to choose the word from: ")        
    chosen_index = ''
    while len(chosen_index) == 0:
        chosen_index = int(input("Please enter here the index of the word in this file: "))
    choose_word(chosen_word, chosen_index)
    some_word = choose_word(chosen_word, chosen_index)
    show_hidden_word(some_word, old_letters_guessed)
    print(" ".join(guessed_word))
    def game_begin():
        global num_of_tries
        while (num_of_tries < MAX_TRIES) and (check_win(some_word, old_letters_guessed) == False):
            show_hidden_word(some_word, old_letters_guessed)
            letter_guessed = (input("Guess a letter: ")).lower()
            # check_valid_input(letter_guessed, old_letters_guessed)
            try_update_letter_guessed(letter_guessed, old_letters_guessed)
            print(show_hidden_word(some_word, old_letters_guessed))
            if letter_guessed not in some_word and check_valid_input(letter_guessed, old_letters_guessed) == True:
                num_of_tries += 1
            print_hangman(num_of_tries)
        if num_of_tries == MAX_TRIES:
            print("LOSE")
        else:
            print("WIN")
            # num_of_tries_up()
            # print(old_letters_guessed)
            # num_of_tries_up()
            # print(num_of_tries)

    game_begin()

if __name__ == "__main__":
    main()
