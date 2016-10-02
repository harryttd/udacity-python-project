# I imported sleep just to add a delay affect.
from time import sleep
import sys

level_1 = '''A common first thing to do in a language is display 'Hello __1__!'
In __2__ this is particularly easy; all you have to do is type in: __3__ "Hello
__1__!" Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the __3__ command, and produces a
program which does something, so it is useful in that capacity. It may seem a
bit odd to do something in a Turing complete language that can be done even
more easily with an __4__ file in a browser, but it's a step in learning __2__
syntax, and that's really its purpose.'''

level_2 = '''A __1__ is created with the def keyword. You specify the inputs a
__1__ takes by adding __2__ separated by commas between the parentheses.
__1__s by default returns __3__ if you don't specify the value to return.
__2__ can be standard data types such as string, integer, dictionary, tuple,
and __4__ or can be more complicated such as objects and lambda functions.'''

level_3 = '''When you create a __1__, certain __2__s are automatically
generated for you if you don't make them manually. These contain multiple
underscores before and after the word defining them. When you write
a __1__, you almost always include at least the __3__ __2__, defining
variables for when __4__s of the __1__ get made. Additionally, you generally
want to create a __5__ __2__, which will allow a string representation of the
method to be viewed by other developers.'''

blanks = ['__1__', '__2__', '__3__', '__4__', '__5__']
level_1_answers = ['World', 'Python', 'print', 'HTML']
level_2_answers = ['function', 'arguments', 'None', 'list']
level_3_answers = ['class', 'method', '__init__', 'instance', '__repr__']


def difficulty():
    """Function asks for user's input to select a difficulty, calls 'amount_of_tries' function, and then calls the 'replace_blank' function."""
    levels = ['easy', 'medium', 'hard']
    choice = raw_input("\nFill in the blanks!\n\nSelect easy, medium, or hard: ").lower()
    while choice not in levels:
        choice = raw_input("Incorrect input, please try again.\n\nSelect easy, medium, or hard: ")
    print "\nYou've chosen %s!\n" % (choice)

    turns = amount_of_tries()
    if choice == 'easy':
        replace_blank(turns, level_1, blanks, level_1_answers)
    elif choice == 'medium':
        replace_blank(turns, level_2, blanks, level_2_answers)
    elif choice == 'hard':
        replace_blank(turns, level_3, blanks, level_3_answers)


def yes_or_no():
    """Function for selecting yes or no when required. Prompts the user for input and returns the input."""
    valid_input = ['y', 'yes', 'n', 'no']
    user_input = raw_input("Type 'y' for Yes or 'n' for No: ").lower()
    while user_input not in valid_input:
        print "\nOops! That was not a valid input. Try again...\n"
        user_input = raw_input("Type 'y' for Yes or 'n' for No: ").lower()
    return user_input


def amount_of_tries():
    """This function allows the user to pick how many tries they would like to have for each blank in the level and returns the amount of tries."""
    print "Would you like to set the amount of tries you get? The default is 3.\n"
    answer = yes_or_no()
    if answer == 'y' or answer == 'yes':
        while ValueError:
            try:
                amount = range(1, 11)  # The user can pick between 1 and 10 tries.
                tries = int(raw_input("Select between 1 and 10 tries: "))
                while tries not in amount:
                    print "\nInvalid number.\n"
                    tries = int(raw_input("Select between 1 and 10 tries: "))
                print "\nOk. You have %s tries per question." % (tries)
                sleep(1)
                return tries
            except ValueError:
                print "Not valid input.\n"

    else:
        tries = 3
        print "\nOk. You have 3 tries per question."
        sleep(1)
        return tries


def replace_blank(turns, level, blanks, answers):
    """Finds each blank in the level and calls the 'user_input' function to replace each blank."""
    print "\nStart with the first blank.\n"
    print level
    for blank in blanks:
        if blank in level:
            len_blank = len(blank)
            # 'index' holds the index of each 'blank' in the 'blanks' list.
            index = blanks.index(blank)
            # 'found' finds where each 'blank' in the level is located.
            found = level.find(blank)
            # 'blank_space' holds the string of each 'blank' in the level.
            blank_space = level[found: found + len_blank]
            level = user_input(turns, blank_space, index, level, answers)
            print level
    print "\nGood job! You Finished!\n"
    sleep(1)
    play_again()


def user_input(turns, blank_space, index, level, answers):
    """Asks for the user's input for each blank. Replaces each blank with the correct input and prints the level."""
    tries = turns
    user_input = raw_input('\nWhat should we substitute for %s? ' % (blank_space)).lower()
    while user_input != answers[index].lower():
        tries -= 1
        if tries > 0:
            print "\nTry again! You have %s more turns!\n" % (tries)
            print level
            user_input = raw_input('\nWhat should we substitute for %s? ' % (blank_space)).lower()
        elif tries == 0:
            print "\nSorry! You failed!\n"
            sleep(1)
            play_again()

    level = level.replace(blank_space, answers[index])
    print "\nYou got the right answer!\n\nContinue!\n"
    return level


def play_again():
    """Allows the user to play again if so desired. Calls 'yes_or_no' function to prompt the user."""
    print "Would you like to play again?\n"
    answer = yes_or_no()
    if answer == 'y' or answer == 'yes':
        difficulty()
    elif answer == 'n' or answer == 'no':
        sys.exit("\nGoodbye!")  # The way my code is now structured (after my first submission), sys.exit() is required to exit the program. Otherwise the program does not exit. I think it has something to do with my 'user_input' function being called in the 'replace_blank' function. I can't fully figure out how to do without sys.exit(). Code needs to be refactored.

difficulty()
