print("Welcome to ATM")
balance = 1000
while True:
    print("\nYour balance:", balance)
    print("To check balance press 1")
    print("To deposit money press 2")
    print("To withdraw money press 3")
    print("To exit press 4")
    
    b = int(input("Choose a number: "))

    if b == 1:
        print("Your balance =", balance)
    
    elif b == 2:
        c = float(input("Enter amount to deposit: "))
        balance += c
        print("Your new balance is", balance)
    
    elif b == 3:
        d = float(input("Enter amount to withdraw: "))
        if d > balance:
            print("Error: Insufficient balance")
        else:
            balance -= d
            print("Withdrawal successful. Remaining balance is", balance)
    
    elif b == 4:
        print("Thank you for using the ATM. Goodbye!")
        break 
    
    else:
        print("Invalid choice. Please try again.")
