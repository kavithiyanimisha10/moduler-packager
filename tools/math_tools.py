# Import built-in math module for mathematical functions
import math

def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid Number")

def factorial():
    # Convert input to integer (factorial only works on integers)
    n = int(get_valid_number("Enter a non-negative integer:")) 
    if n < 0:
        print("Factorial not defined for negative numbers")
        return
    print("Factorial: ", math.factorial(n))

def compound_interest():
    p = get_valid_number("Principal: ")
    r = get_valid_number("Rate (%): ")
    t = get_valid_number("Time (years): ")

    amount = p * (1 + r /100) ** t
    print(f"Compound Interest Result: {amount:.2f}")

def trignometry():
    angle = get_valid_number("Enter angle in degress: ")
    
    # Convert degrees to radians (required for math functions)
    rad = math.radians(angle)

    print("sin: ",math.sin(rad))
    print("cos: ",math.cos(rad))
    print("tan: ",math.tan(rad))

def area_shapes():
    print("\n1.Circles\n" \
    "2. Rectangle\n" \
    "3. Triangle\n" \
    "4. back to Sub menu")
    while True:
        # Taking shape choice from user        
        choice = int(get_valid_number("Choose Shape:"))

        # Circle area = πr²
        if choice == 1:
            r = get_valid_number("Radius: ")
            print("Area:", math.pi * r * r)

        # Rectangle area = length × width
        elif choice == 2:
            l = get_valid_number("Length: ")
            w = get_valid_number("Width: ")
            print("Area:", l * w)

        # Triangle area = ½ × base × height
        elif choice == 3:
            b = get_valid_number("Base: ")
            h = get_valid_number("Height: ")
            print("Area:", 0.5 * b * h)

        # Exit loop
        elif choice == 4:
            print("Going back to Mathematical Operations Menu....")
            break

        else:
            print("Invalid shape choice")

def math_menu():
    while True:
        print("Mathematical Operations:\n" \
            "1. Calculate Factorial\n" \
            "2. Solve Compound Interest\n" \
            "3. Trigonometric Calculations\n" \
            "4. Area of Geometric Shapes\n" \
            "5. Back to Main menu")

        # Validate menu input
        try:     
            sub_choice = int(input("Please Enter your choice: "))
        except ValueError:
            print("Invalid input!!") 
            continue

        # Call appropriate function based on user choice
        if sub_choice == 1: 
            factorial()

        elif sub_choice == 2:
            compound_interest()

        elif sub_choice == 3:
            trignometry()

        elif sub_choice == 4:
            area_shapes()

        elif sub_choice == 5:
            print("Going back to Main Menu...")
            break
        
        else:
            print("Invalid Choice!!")