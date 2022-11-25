# from distutils.command.build import build
# import random
from wonderwords import RandomWord

# SNOWMAN_WORD = "kohlrabi"
SNOWMAN_WRONG_GUESSES = 7
SNOWMAN_MAX_WORD_LENGTH = 8
SNOWMAN_MIN_WORD_LENGTH = 5

# SNOWMAN_1 = '*   *   *  '
# SNOWMAN_2 = ' *   _ *   '
# SNOWMAN_3 = '   _[_]_ * '
# SNOWMAN_4 = '  * (")    '
# SNOWMAN_5 = '  \( : )/ *'
# SNOWMAN_6 = '* (_ : _)  '
# SNOWMAN_7 = '-----------'

SNOWMAN_GRAPHIC = [
    '*   *   *  ',
    ' *   _ *   ',
    '   _[_]_ * ',
    '  * (")    ',
    '  \( : )/ *',
    '* (_ : _)  ',
    '-----------'
]

def print_snowman(wrong_guesses_count):
    for i in range(SNOWMAN_WRONG_GUESSES - wrong_guesses_count,
                SNOWMAN_WRONG_GUESSES):
        print(SNOWMAN_GRAPHIC[i])


#print_snowman(3)

def get_letter_from_user(word_dict, list2):
    """
    Prompts the user to guess a letter, checks that the input is valid, and returns the input string.
    """
    guess = None
    valid_guess = False

    while not valid_guess:
        guess = input("Guess a letter: ")

        if not guess.isalpha() or len(guess)> 1:
            print("Invalid letter! Please enter a single character.")
        elif guess in list2: 
            print("You have already guessed that letter and it's not in the word!")
        elif guess in word_dict and word_dict[guess]:
            print("You have already guessed that letter and it's in the word!")
        else:
            valid_guess = True

    return guess 

def build_word_dict(word):
    word_dict = {}
    for letter in word:
        word_dict[letter] = False
    return word_dict

def print_word_progress_string(word, word_dict):
    progress = ""
    for letter in word:
        if word_dict[letter]:
            progress += letter + " "
        else:
            progress += "_ "
    if progress[-1] == " ":
        progress = progress[0:-1]
        
    print(progress)

def get_word_progress(word, word_dict):
    score = 0
    for letter in word:
        if word_dict[letter]:
            score += 1
    
    return score >= len(word)

def snowman():
    """
    Initiates a game of Snowman.
    """
    r = RandomWord()
    snowman_word = r.word(
      word_min_length=SNOWMAN_MIN_WORD_LENGTH, 
      word_max_length=SNOWMAN_MAX_WORD_LENGTH)

    snowman_dict = build_word_dict(snowman_word)
    #print(snowman_dict)

    wrong_guesses_list = []
    #correct_guesses_list = []

    #correct_guesses = 0
    #wrong_guesses = 0
    

    while len(wrong_guesses_list) < SNOWMAN_WRONG_GUESSES and not get_word_progress(snowman_word, snowman_dict):
        user_input = get_letter_from_user(snowman_dict, wrong_guesses_list)

        if user_input in snowman_dict:
            print("Letter found!")
            snowman_dict[user_input] = True
        else:
            
            print("Letter not found.")
            wrong_guesses_list.append(user_input)
        
        print_snowman(len(wrong_guesses_list))
        print_word_progress_string(snowman_word, snowman_dict)
        print("Wrong guesses: ", wrong_guesses_list)
        
    if get_word_progress(snowman_word, snowman_dict):
        print("Success!")
    else:
        print(f"Too bad! The word was {snowman_word}!")

snowman()


