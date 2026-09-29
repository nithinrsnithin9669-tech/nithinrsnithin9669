# Hotel Management System

A simple Python-based command-line hotel management system for handling basic hotel operations such as customer registration, room booking, food billing, and checkout. The project is designed as an educational application to demonstrate fundamental Python programming concepts through a practical real-world problem.

## Features

* Adds and stores customer details such as name and phone number.
* Displays customer records currently stored in the system.
* Provides different room types: Single, Double, and Deluxe.
* Calculates room charges based on room type and number of stay days.
* Provides a basic food menu with Breakfast, Lunch, and Dinner.
* Calculates food charges based on the selected food item and quantity.
* Combines room and food charges to generate the final customer bill.
* Validates important inputs such as room selection, food selection, stay duration, and quantity.
* Uses a simple menu-driven interface for easy operation.
* Runs offline using standard Python features without external libraries.

## Room Options

The system provides the following room categories:

| Room Type | Price per day |
| --------- | ------------: |
| Single    |         ₹1500 |
| Double    |         ₹2500 |
| Deluxe    |         ₹3500 |

## Food Menu

The available food options are:

| Food Item | Price |
| --------- | ----: |
| Breakfast |  ₹150 |
| Lunch     |  ₹250 |
| Dinner    |  ₹300 |

## Inputs

The system accepts the following information:

| Input          | Description                     |
| -------------- | ------------------------------- |
| Customer name  | Name of the hotel customer      |
| Phone number   | Customer contact number         |
| Room type      | Single, Double, or Deluxe       |
| Number of days | Duration of the customer's stay |
| Food item      | Breakfast, Lunch, or Dinner     |
| Food quantity  | Number of food items ordered    |

Use the options shown by the program when entering room and food choices.

## Calculations

The room bill is calculated using:

```text
Room Bill = Room Price per Day × Number of Days
```

The food bill is calculated using:

```text
Food Bill = Food Price × Quantity
```

The final bill is calculated as:

```text
Final Bill = Room Bill + Food Bill
```

For example, if a customer stays in a Single room for 2 days:

```text
Room Bill = ₹1500 × 2
          = ₹3000
```

If the customer also orders food costing ₹400:

```text
Final Bill = ₹3000 + ₹400
           = ₹3400
```

## Requirements

* Python 3
* No external Python libraries are required.

## Run

From the folder containing the Python source file, run:

```bash
python hotel_management_system.py
```

Follow the menu displayed by the program and select the required option.

The main menu provides:

```text
1. Add Customer
2. Show Customers
3. Book Room
4. Food Bill
5. Checkout
6. Exit
```

Select the appropriate option to perform the required hotel management operation.

## Project Structure

The program is organized around these functional areas:

* Customer registration and information storage
* Customer record display
* Room booking and room-bill calculation
* Food ordering and food-bill calculation
* Final bill generation
* Input validation
* Menu-driven program control

The project uses Python lists and dictionaries to store customer information during program execution.

## Program Concepts Used

The project demonstrates several fundamental Python concepts:

* Variables and data types
* Lists
* Dictionaries
* Functions
* `if`, `elif`, and `else` statements
* `for` and `while` loops
* User input using `input()`
* Output using `print()`
* Arithmetic operations
* Conditional validation
* Menu-driven programming

## Interpreting Results

The system displays customer information, selected room details, room charges, food charges, and the final amount during checkout.

The final bill represents the basic charges recorded by the program for the selected customer. The project is intended as a simplified hotel management example and does not include advanced hotel operations such as taxes, discounts, online payments, or database storage.

## Troubleshooting

* If Python is not recognized, install Python 3 and make sure it is available in the system PATH.
* If the program does not start, check that you are running the command from the folder containing the Python file.
* If an invalid menu option is entered, select one of the options displayed by the program.
* If an invalid room or food option is entered, enter the option supported by the program.
* Enter positive values for the number of stay days and food quantity.

## Scope

This project is intended for learning and demonstrating basic Python programming concepts through a simple hotel management application.

The current version provides basic customer management, room booking, food billing, and checkout functionality. Customer data is stored only while the program is running.

Possible future improvements include:

* Database integration
* Graphical User Interface (GUI)
* Room availability management
* Customer search and modification
* Tax and discount calculation
* Online payment support
* Receipt generation
* Admin login system
* Permanent customer record storage

