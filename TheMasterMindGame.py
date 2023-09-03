import random

colours = ["R", "V", "Y", "G", "B", "P", "I", "O", "A", "M"]
print("\n\n")
print("        ***       Welcome to MasterMind !       ***        \n")
print("There are 8 colours used in this guessing game.......\n")
print("RED : < R | r >")
print("VIOLET : < V | v >")
print("YELLOW : < Y | y >")
print("GREEN : < G | g >")
print("BLUE : < B | b >")
print("PINK : < P | p > ")
print("INDIGO : < I | i > ")
print("ORANGE : < O | o >")
print("AQUA : < A | a >")
print("MAROON : < M | m >\n")
print("To make the game more convenient to play, you can type in the first alphabet of the color you want to choose in either lowercase or uppercase..........")

def print_error_prompt(error_type):
    if error_type == "invalid_length":
        print(f"Invalid guess length. You must guess {codeLength} colors. Remember to use spaces if you're not using them.")
    elif error_type == "invalid_color":
        print("Invalid color in your guess. Use the abbreviations provided.")
    elif error_type == "already_guessed":
        print("You have already guessed that color.")
    elif error_type == "unknown_error":
        print("An unknown error occurred. Please try again.")

while True:
    codeLength = input("Enter the number of colors you want the other person to guess : ")
    if codeLength.isdigit():
        codeLength = int(codeLength)
        if 4 <= codeLength <= 10:
            break
        else:
            print("You can only choose your Code Length between 4 to 10 !!")
    else:
        print("Please enter a valid number between 4 to 10 for the game to continue !!!")

print("Number of the length of code confirmed : " + str(codeLength))

while True:
    tries = input("Enter the number of tries you wish to conclude the game in : ")
    if tries.isdigit():
        tries = int(tries)
        if 1 <= tries <= 30:
            break
        else:
            print("Please keep the number of tries less than 30 for the game to be more enjoyable !!")
    else:
        print("Please enter a valid number for the game to continue !!!")

print("Number of tries confirmed : " + str(tries))

def generateCode():
    code = []

    for x in range(codeLength):
        color = random.choice(colours)
        code.append(color)

    return code

code = generateCode()

def guessCode():
    while True:
        guess = input("Your Guess : ").upper().split(" ")

        if len(guess) != codeLength:
            print_error_prompt("invalid_length")
            continue

        for color in guess:
            if color not in colours:
                print_error_prompt("invalid_color")
                break

        else:
            break

    return guess

def checkCode(Guess, realCode):
    colourCount = {}
    correctPosition = 0
    incorrectPosition = 0

    for color in realCode:
        if color not in colourCount:
            colourCount[color] = 0
        colourCount[color] += 1

    for guessColor, realColor in zip(Guess, realCode):
        if guessColor == realColor:
            correctPosition += 1
            colourCount[guessColor] -= 1

    for guessColor, realColor in zip(Guess, realCode):
        if guessColor in colourCount and colourCount[guessColor] > 0:
            incorrectPosition += 1
            colourCount[guessColor] -= 1

    return correctPosition, incorrectPosition

def game():
    code = generateCode()
    for attempts in range(1, tries + 1):
        Guess = guessCode()
        correctPosition, incorrectPosition = checkCode(Guess, code)

        print(f"Attempt {attempts}: Correct Position: {correctPosition} | Incorrect Position: {incorrectPosition}")

        if correctPosition == codeLength:
            print("Congratulations! You've guessed the secret code correctly!")
            break
    else:
        print("Oops!! You ran out of tries :( .....\nThe code was : ", *code)

if __name__ == "__main__":
    game()
