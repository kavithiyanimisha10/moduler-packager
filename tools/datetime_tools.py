# Import required built-in modules
import datetime, time

def datetime_menu():
    def get_valid_date(prompt):
        while True:
            user_input = input(prompt)
            try:
                # Import required built-in modules
                return datetime.datetime.strptime(user_input, "%d-%m-%Y").date() # strp coverts string - date
            except ValueError:
                print("Invalid date! Please use format DD-MM-YYYY (e.g., 25-12-2024).")

    def get_valid_int(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid number! Please enter a valid integer.")
                continue

    # Main loop for datetime menu
    while True:
        print("Datetime and Time Operations:\n" \
        "1. Display current date and time\n" \
        "2. Calculate difference between two dates/times\n" \
        "3. Format date into custom format\n" \
        "4. stopwatch\n" \
        "5. countdown Timer\n" \
        "6. Back to Main menu")

        # Get validated menu choice   
        sub_choice = get_valid_int("Please Enter your choice: ")

        # Option 1: Show current date and time
        if sub_choice == 1: 
            now = datetime.datetime.now()
            print("Current Date & Time: ",now)

        # Option 2: Calculate difference between two dates
        elif sub_choice == 2:
            date1 = get_valid_date("Enter first date (DD-MM-YYYY): ")
            date2 = get_valid_date("Enter second date (DD-MM-YYYY): ")

            # Subtracting dates returns a timedelta objec
            difference = date1 - date2

            # Display absolute difference in days    
            print(f"Difference in days: {abs(difference.days)}")

        # Option 3: Format date in different styles
        elif sub_choice == 3:
            date_obj = get_valid_date("Enter your date (DD-MM-YYYY): ") 
            
            # Format date using strftime()
            print("Format 1: ",date_obj.strftime("%d/%m/%Y"))
            print("Format 2: ",date_obj.strftime("%B %d, %Y"))
            print("Format 3: ",date_obj.strftime("%A, %d %B %Y")) 

        # Option 4: Stopwatch using high-precision timer    
        elif sub_choice == 4:
            input("Press ENTER to start stopwatch...")
            start_time = time.perf_counter()

            input("Press ENTER to stop stopwatch...")
            end_time = time.perf_counter()

            elapsed = end_time - start_time

            print(f"Elapsed time: {elapsed:.2f} seconds")
    
        # Option 5: Countdown timer
        elif sub_choice == 5:
            try: 
                seconds = get_valid_int("Enter time in seconds: ")
            except ValueError:
                print("Invalid number!")
                continue
            
            # Countdown loop
            while seconds > 0:
                print(f"\rTime left: {seconds} sec", end="") # overwrite same line
                time.sleep(1) # wait 1 second
                seconds -= 1

            print("\nTime's up!")

        # Option 6: Exit submenu    
        elif sub_choice == 6:
            print("\n Going back to main menu....")
            break
            
        # Handle invalid menu choice
        else:
            print("Invalid Input. Please enter correct datetime and time operation you want to perform.")