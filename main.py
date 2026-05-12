# Import custom utility modules from utils package
from utils import datetime_tools, file_tools, math_tools, random_tools

# Import built-in module for UUID generation
import uuid

# Main loop for the Multi-Utility Toolkit 
while True:
    # Display main menu
    print("===========================")
    print("Welcome to Multi-Utility Toolkit")
    print("===========================")
    print("Choose an Option:\n" \
        "1. Datetime and Time Operations\n" \
        "2. Mathematical Operations\n" \
        "3. Random data Generation\n" \
        "4. Generate Unique Identifiers(UUID)\n" \
        "5. File Operations\n" \
        "6. Explore Module Attributes(dir())\n" \
        "7. Exit")
    print("===========================")

     # Take user input for menu selection
    choice = int(input("Please Enter your choice: "))

    # Option 1: Call datetime utilities menu
    if choice == 1:
        datetime_tools.datetime_menu()
    
    # Option 2: Call mathematical operations menu
    elif choice == 2:
        math_tools.math_menu()
    
    # Option 3: Call random data generation menu
    elif choice == 3:
        random_tools.random_menu()

    # Option 4: Generate a random UUID (version 4)
    elif choice == 4:
        print("Generated UUID", uuid.uuid4())
    
    #Option 5: Call file operations menu
    elif choice == 5:
        file_tools.file_menu()
    
    # Option 6: Dynamically explore attributes of a module using dir()
    elif choice == 6:
        module_name = input("Enter module name (e.g., math, random, utils.math_tools): ")
        try:
            # Dynamically import module by name
            module = __import__(module_name)
            print(dir(module))
        except Exception as e:
            print("Error:", e)
    
     # Option 7: Exit program
    elif choice == 7:
        print("Exiting from the program1!! Goodbye!!!")
        break
    
    # Handle invalid input
    else:
        print("Invalid Input!!!")
