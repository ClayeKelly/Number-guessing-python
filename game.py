import random


def print_title():
    print("""
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    |                                       |
    |       Welcome to Number Guessing!     |
    |            Calculator and More!       |
    |              By [Claye Kelly]         |
    |                                       |
    |_______________________________________|
    """)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: Division by zero is not allowed.")
        return None

def number_guessing_game():
    number_to_guess = random.randint(1, 10)
    guesses = 0

    while True:
        user_guess = int(input("Guess a number between 1 and 10: "))
        guesses += 1

        if user_guess < number_to_guess:
            print("Your guess is too low. Try again.")
        elif user_guess > number_to_guess:
            print("Your guess is too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} in {guesses} attempts.")
            break

def calculator():
    operation = ""
    num1 = 0
    num2 = 0

    while True:
        num1 = float(input("Enter the first number: "))
        if num1 is not None:
            break

    operation = input("Enter an operator (+, -, *, /): ")

    num2 = float(input("Enter the second number: "))

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        print("Invalid operator. Please use one of the following operators: +, -, *, /")
        calculator()
        return

    print(f"The result of {num1} {operation} {num2} is {result}")

def game_loop():
    print_title()
    choice = input("Do you want to play the number guessing game or use the calculator? (g/c): ")

    if choice == "g":
        number_guessing_game()
    elif choice == "c":
        calculator()
    else:
        print("Invalid input. Please try again.")
        game_loop()

if __name__ == "__main__":
    game_loop()



