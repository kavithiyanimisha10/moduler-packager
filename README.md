# Personal Data Collector (Python)

## Overview

This is a simple **Python beginner project** that collects some personal
information from the user and displays it with additional details like
**data type** and **memory address**.

This program demonstrates the use of: - Input and Output - Variables -
Data types (`str`, `int`, `float`) - Type checking using `type()` -
Memory address using `id()` - Basic calculation

------------------------------------------------------------------------

## Code Explanation

### 1. Welcome Message

The program first asks for the user's name and prints a welcome message.

### 2. Collecting Data

The program collects the following information: - Name - Age - Height
(in meters) - Favourite number

Each input is stored in a variable.

### 3. Data Type Usage

Different data types are used:

  Variable   Data Type   Purpose
  ---------- ----------- -------------------------
  Name       String      Stores user's name
  age        Integer     Stores user's age
  height     Float       Stores height in meters
  favnum     Integer     Stores favourite number

### 4. Displaying Type and Memory Address

The program prints: - Value - Data Type using `type()` - Memory Address
using `id()`

Example:

    Your age is 21 years. (<class 'int'> , Memory address : 12345678)

### 5. Birth Year Calculation

The program calculates birth year using:

    birthyear = current_year - age

Then it prints the calculated birth year.

### 6. Ending Message

Finally, the program thanks the user for using the program.

------------------------------------------------------------------------

## How to Run the Program

1.  Install Python (if not installed)
2.  Save the code in a file named:

```{=html}
<!-- -->
```
    personal_data_collector.py

3.  Open terminal or command prompt
4.  Run the program:

```{=html}
<!-- -->
```
    python personal_data_collector.py

------------------------------------------------------------------------

## Example Output

    Welcome ,Here is your personal data collector.Please enter your data below.

    Enter your name : Nimisha
    Enter your age : 20
    Enter your height in meters : 1.6
    Enter your favourite number : 7

    Thank you for giving your personal data.Here is the data we collected.

    Your name is Nimisha.
    Your age is 20 years.
    Your height in meters is 1.6.
    Your favourite number is 7.

    Your birth year is 2006 (based on your age).

------------------------------------------------------------------------

## Learning Purpose

This project is useful for **Python beginners** who want to practice:

-   Taking user input
-   Working with variables
-   Understanding data types
-   Printing formatted output

------------------------------------------------------------------------

## Author

Created as a **Python learning practice project**.
