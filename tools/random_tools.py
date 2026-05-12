# Import required modules
import random, string

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid Number!!!")

def random_number():
    low = get_valid_int("Enter lower bound value: ")
    high = get_valid_int("Enter higher bound value: ")

    # Validate range
    if low > high:
        print("Lower bound must be less than higher bound")
        return
    
    # Generate random number within range
    print("Random Number: ", random.randint(low,high))

def random_list():
    size = get_valid_int("Enter list size: ")
    low = get_valid_int("Enter min value: ")
    high = get_valid_int("Enter max value: ")

    if low > high:
        print("Invalid Range.")
        return
    
    # Generate list of random numbers
    result = [random.randint(low,high) for _ in range(size)]
    print("Random List: ", result)

def random_password():
    """
    Generates a random password using:
    - Uppercase and lowercase letters
    - Digits
    - Special characters
    """
    length = get_valid_int("Enter password length: ")
    
    # Combine all possible characters
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters to form password
    password = ''.join(random.choice(chars) for _ in range(length))

    print("Generated Password:", password)


def random_otp():
    # Generates a 6-digit One-Time Password (OTP).
    otp = random.randint(100000, 999999)
    print("Generated OTP:", otp)

def random_menu():
    while True:
        print("\nRandom Data Generation:\n"
              "1. Generate Random Number\n"
              "2. Generate Random List\n"
              "3. Create Random Password\n"
              "4. Generate Random OTP\n"
              "5. Back")

        # Validate menu choice
        try:
            sub_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input!")
            continue

        # Call corresponding function    
        if sub_choice == 1:
            random_number()

        elif sub_choice == 2:
            random_list()

        elif sub_choice == 3:
            random_password()

        elif sub_choice == 4:
            random_otp()

        elif sub_choice == 5:
            print("Exiting sub menu...")
            break

        else:
            print("Invalid choice")