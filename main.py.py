customers = []

while True:

    print("\n===== HOTEL MANAGEMENT SYSTEM =====")
    print("1. Add Customer")
    print("2. Show Customers")
    print("3. Book Room")
    print("4. Food Bill")
    print("5. Checkout")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Add customer
    if choice == 1:

        name = input("Enter customer name: ")
        phone = input("Enter phone number: ")

        customer = {
            "name": name,
            "phone": phone,
            "room": 0,
            "room_bill": 0,
            "food_bill": 0
        }

        customers.append(customer)

        print("Customer added successfully!")

    # Show customers
    elif choice == 2:

        if len(customers) == 0:
            print("No customers found.")

        else:
            print("\n----- CUSTOMER DETAILS -----")

            for customer in customers:
                print("Name:", customer["name"])
                print("Phone:", customer["phone"])
                print("Room:", customer["room"])
                print("Room Bill:", customer["room_bill"])
                print("Food Bill:", customer["food_bill"])
                print("---------------------------")

    # Book room
    elif choice == 3:

        if len(customers) == 0:
            print("Please add a customer first.")

        else:

            name = input("Enter customer name: ")

            found = False

            for customer in customers:

                if customer["name"] == name:

                    room = int(input("Enter room number: "))

                    print("\nRoom Types")
                    print("1. Single - Rs. 1500")
                    print("2. Double - Rs. 2500")
                    print("3. Deluxe - Rs. 3500")

                    room_type = int(input("Choose room type: "))

                    if room_type == 1:
                        customer["room_bill"] = 1500

                    elif room_type == 2:
                        customer["room_bill"] = 2500

                    elif room_type == 3:
                        customer["room_bill"] = 3500

                    else:
                        print("Invalid room type.")
                        break

                    customer["room"] = room

                    print("Room booked successfully!")

                    found = True
                    break

            if found == False:
                print("Customer not found.")

    # Food bill
    elif choice == 4:

        name = input("Enter customer name: ")

        found = False

        for customer in customers:

            if customer["name"] == name:

                print("\nFood Menu")
                print("1. Breakfast - Rs. 150")
                print("2. Lunch - Rs. 250")
                print("3. Dinner - Rs. 300")

                food = int(input("Choose food: "))

                if food == 1:
                    customer["food_bill"] += 150

                elif food == 2:
                    customer["food_bill"] += 250

                elif food == 3:
                    customer["food_bill"] += 300

                else:
                    print("Invalid choice.")
                    break

                print("Food added successfully!")

                found = True
                break

        if found == False:
            print("Customer not found.")

    # Checkout
    elif choice == 5:

        name = input("Enter customer name: ")

        found = False

        for customer in customers:

            if customer["name"] == name:

                total = customer["room_bill"] + customer["food_bill"]

                print("\n========== BILL ==========")
                print("Customer:", customer["name"])
                print("Room:", customer["room"])
                print("Room Bill: Rs.", customer["room_bill"])
                print("Food Bill: Rs.", customer["food_bill"])
                print("--------------------------")
                print("Total Bill: Rs.", total)
                print("==========================")

                found = True
                break

        if found == False:
            print("Customer not found.")

    # Exit
    elif choice == 6:

        print("Thank you!")
        break

    else:
        print("Invalid choice.")
