def create_file():
    filename = input("Enter file name: ")

    try:
        # 'x' mode creates a new file and fails if it already exists
        with open(filename, "x"):
            print("File created successfully.")
    except FileExistsError:
        print("File already exists.")

    # Return filename so other functions can use it
    return filename


def write_file(filename):
    data = input("Enter content to write: ")

    try:
        # 'w' mode overwrites the file if it exists
        with open(filename, "w") as f:
            f.write(data)
        print("Data written successfully.")
    except Exception as e:
        print("Error:", e)


def read_file(filename):
    try:
        # 'r' mode reads file content
        with open(filename, "r") as f:
            content = f.read()
        
        print("\nFile Content:\n", content)
    
    except FileNotFoundError:
        print("File not found.")


def append_file(filename):
    data = input("Enter content to append: ")

    try:
        # 'a' mode appends data to the end of the file
        with open(filename, "a") as f:
            f.write("\n" + data)
        print("Data appended successfully.")
    except Exception as e:
        print("Error:", e)

def file_menu():
    filename = None  #Stores currently selected/created file

    while True:
        print("\nFile Operations:\n"
              "1. Create a new file\n"
              "2. Write to a file\n"
              "3. Read from a file\n"
              "4. Append to a file\n"
              "5. Back")

        try:
            sub_choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input!")
            continue

        # Create file and store filename
        if sub_choice == 1:
            filename = create_file()

        # Write to file (only if file exists)
        elif sub_choice == 2:
            if filename:
                write_file(filename)
            else:
                print("Please create/select a file first.")

        # Read file content
        elif sub_choice == 3:
            if filename:
                read_file(filename)
            else:
                print("Please create/select a file first.")

        # Append data to file
        elif sub_choice == 4:
            if filename:
                append_file(filename)
            else:
                print("Please create/select a file first.")

        # Exit menu
        elif sub_choice == 5:
            print("Exiting sub menu...")
            break

        else:
            print("Invalid choice")