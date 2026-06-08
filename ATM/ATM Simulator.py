# ATM SIMULATOR PROJECT
balance = 10000
pin = 1234
history = []

attempts = 3

while attempts > 0:
    enter_pin = int(input("Enter ATM PIN : "))

    if enter_pin == pin:
        print("Login Successful")
        
        while True:
            print("***** MENU *****")
            print("1.Check Balance")
            print("2. Deposit Money")
            print("3. Withdrow Money")
            print("4.Transaction History")
            print("5.Fast Cash")
            print("6.Change PIN")
            print("7.Mini Statement")


            print("8 Exit")

            choice = input("Enter Your Choice")
            
            if choice == "1":
                print(f"Your Balance is {balance}")


            elif choice == "2":
                amount = int(input("Emter amount to deposite"))

                if amount > 0:
                    balance += amount
                    history.append(f"Deposite {amount}")
                    print(f"{amount} is deposite successfully")
                    print(f"Total balance is {balance}")

                else:
                    print("Invalid Amount")

            elif choice == "3":
                amount = int(input("Enter amount to withdrow: "))

                if amount <= balance:
                    balance -= amount
                    history.append(f"Withdrawn {amount}")
                    print(f"{amount} withdrow Successfully")
                    print(f"Remaining Balance {balance}")

                else:
                    print("Insufficient balance")

            elif choice =="4":
                if len(history) == 0:
                    print("No transactions Found")
                
                else:
                    print("\n----- Transaction History -----")
                    for item in history:
                        print(item)

            elif choice == "5":
                print("1. 500")
                print("2. 1000")
                print("3. 2000")

                fast = input("Choose Amount")

                if fast == "1":
                    amount = 500
                elif fast == "2":
                    amount = 1000
                elif fast == "3":
                    amount = 200
                
                else:
                    print("Invalid Option")
                    continue

                if amount <= balance:
                    balance -= amount
                    history.append(f"fast cash withdrow {amount}")
                    print(f" {amount} is withdrown")

                else:
                    print("Insufficient balance")

            elif choice == "6":
                old_pin= int(input("Enter Old pin"))

                if old_pin == pin:
                    new_pin = int(input("Enter New pin"))
                    pin = new_pin
                    print("Pin changed")
                else:
                    print("Invalid Old Pin")
            elif choice == "7":
                print("****** Mini statement ********")
                if len(history) == 0:
                    print("No history")
                else:
                    for item in history[-5:]:
                        print(item)



            elif choice == "8":
                print("Thank You for using ATM")
                break
            else:
                print("Invalid Choice")
        break

    else:
        attempts -=1
        print(f"Wrong PIN. Attempts Left:{attempts}")
    
if attempts == 0:
    print("ATM Blocke")

