# ATM SIMULATOR PROJECT
balance = 10000
pin = 1234

enter_pin = int(input("enter ATM PIN"))

if enter_pin == pin:
    print("Login Successful")

    while True:
        print("***** MENU *****")
        print("1.Check Balance")
        print("2. Deposit Money")
        print("3. Withdrow Money")
        print("4 Exit")

        choice = input("Enter Your Choice")
         
        if choice == "1":
            print(f"Your Balance is {balance}")


        elif choice == "2":
            amount = int(input("Emter amount to deposite"))

            if amount > 0:
                balance += amount
                print(f"{amount} is deposite successfully")
                print(f"Total balance is {balance}")

            else:
                print("Invalid Amount")

        elif choice == "3":
            amount = int(input("Enter amount to withdrow: "))

            if amount <= balance:
                balance -= amount
                print(f"{amount} withdrow Successfully")
                print(f"Remaining Balance {balance}")

            else:
                print("Insufficient balance")

        elif choice == "4":
            print("Thank You for using ATM")
            break
        else:
            print("Invalid Choice")

else:
    print("Wrong PIN")
