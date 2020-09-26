# Project = Guessing game (user needs to guess a randomly generated number)
# Author = Jordy Zijp
# Class = ID1G4(A)
# Datetime = 24-Sept-2020 00:12

# Importing the module that makes it possible to generate a random value/number
import random

# Minimum and maximum available attempts to guess
min_amount_guesses = 1
max_amount_guesses = 5


# introduction for the player
print("Welcome to this guessing game where you have to guess a secret number."
      "\n======================================================================================")

# Ask user for the amount of guesses that he/she wants
guess_amount = int(input("Tell us how many attempts you want to guess the secret number, choose between "
                         + str(min_amount_guesses) + " and "+ str(max_amount_guesses) + ": \n" "amount of attempts = "))

# Validation check to see if the amount of guesses matches the minimum/maximum amount of guesses
while guess_amount < min_amount_guesses or guess_amount > max_amount_guesses:
    guess_amount = int(input("Invalid input, please choose between: " + str(min_amount_guesses) + " and "
                             + str(max_amount_guesses) + "\n"))

# Minimum and maximum value for the randomly generated  number (given by user)
custom_minimum_number = int(input("Give a minimum value range for the generated number: \n"))
custom_maximum_number = int(input("Give a maximum value range for the generated number: \n"))

# Validation for the minimum number to start the range to generate a number
while custom_minimum_number > custom_maximum_number:
    custom_minimum_number = int(input("The minimum number can not be higher than the maximum number, "
                                      "start again and give a new minimum number: \n"))
    custom_maximum_number = int(input("Give a maximum value range for the generated number: \n"))

# Validation for the maximum number to end the range to generate a number
while custom_maximum_number < custom_minimum_number:
    custom_minimum_number = int(input("The maximum number can not be lower than the minimum number, "
                                      "start again and give a new minimum number: \n"))
    custom_maximum_number = int(input("Give a maximum value range for the generated number: \n"))

# generated random number is filled into this variable
random_number = random.randint(custom_minimum_number, custom_maximum_number)

# Ask user to guess a number
user_guess = int(input("Guess a number between " + str(custom_minimum_number) + " and "
                       + str(custom_maximum_number) + "\n"))

# Initializing the number of guesses
count = guess_amount

# Message that you receive when you guessed the randomly generated number
winner_message = "======================================================================================\n" \
                 "Congratulations! you guessed the secret number, the winning number was: " + str(random_number)

# list that collects the stats
stats_list = ["amount of guesses you needed: ", ]

# Loop to see if the input matches the random number, it tells if it's too low, too high or correct
# Also this loop is calculating the amount of tries because if you exceed the limit the game will stop
while random_number != user_guess:
    count -= 1
    if count == 0:
        print("The amount of guesses is reached, you lost. The secret number was: " + str(random_number))
        break
    if user_guess < random_number:
        print("the guessed number is too low, the amount of guesses left = " + str(count))
        user_guess = int(input("Try another number between: " + str(custom_minimum_number) + " and "
                               + str(custom_maximum_number) + "\n"))
    elif user_guess > random_number:
        print("The guessed number is too high, the amount of guesses left = " + str(count))
        user_guess = int(input("Try another number between: " + str(custom_minimum_number) + " and "
                               + str(custom_maximum_number) + "\n"))
    if random_number == user_guess:
        print(str(winner_message) + "\n")
