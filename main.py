
class bank:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} successfully. New balance : {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance - amount >= 500:
            print(f"Withdrawn {amount} successfully. Current balance: {self.balance}")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Your Account has Rs.{self.balance}.")


user = bank()

print("Welcome to Banking!!")
while True:
    print("1. Create Account \n2. Login \n3. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        Username = input("Enter Your name: ")
        Password = int(input("Enter Your Password: "))
        print("Account created successfully. Please Login for personal banking")
    elif choice == "2":
        Username = input("Enter Your name: ")
        Password = int(input("Enter Your Password: "))
        if Username == "Neethu Mathew" and Password == 12345678:
            print("Login Successfully. \nPlease use our Services ")
            while True:
                print("\n1. Deposit \n2. Withdraw \n3. Check Balance \n4. Logout")
                Services = input("Enter your Option: ")
                if Services == "1":
                    amount = float(input("Enter the amount to be deposited: "))
                    user.deposit(amount)
                elif Services == "2":
                    amount = float(input("Enter the amount to be withdrawn: "))
                    user.withdraw(amount)
                elif Services == "3":
                    user.check_balance()
                elif Services == "4":
                    print("Logged out successfully")
                    break
                else:
                    print("Invalid choice. Please Try again.")
        else:
            print("Incorrect Login Details. Please Login")
    elif choice == "3":
        print("Thank you for using Our Services.")
        break
    else:
        print("Incorrect Login")



