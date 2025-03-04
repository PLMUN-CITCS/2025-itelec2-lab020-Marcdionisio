def get_integer_input():
    """Handles user input to obtain an integer."""
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number):
    """Determines if a given number is even or odd."""
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

if __name__ == "__main__":
    user_number = get_integer_input()
    print(check_even_odd(user_number))
