import os
from abc import ABC, abstractmethod

class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.customer = []

class Customer:
    def __init__(self, name,customer_id):
        self.name = name
        self.customer_id = customer_id

class Account(ABC):
    def __init__(self, name, customer_id, account_number, account_type, balance):
        super().__init__(name, customer_id)
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def show_balance(self):
        pass

class SavingsAccount(Account):
    def __init__(self, name, customer_id, account_number, account_type, balance):
        super().__init__(name, customer_id, account_number, account_type, balance)

    def deposit(self, amount):
        self.initial_deposit = 500
        self.maitaining_balance = 2000 
        self.withdrawal_limit = 20000

        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance  and amount <= self.withdrawal_limit:
            self.balance -= amount
        else:
            print("exceed withdrawal amount limit")

    def show_balance(self):
        return f"Your Balance: {self.balance}"

class CheckingAccount(Account):
    def __init__(self, name, customer_id, account_number, account_type, balance):
        super().__init__(name, customer_id, account_number, account_type, balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid amount for withdrawal.")

    def show_balance(self):
        return f"Your Balance: {self.balance}"
    
    def close_account(self):
        if self.balance == 0:
            print("Account closed.")

class JointAccount(Account):
    def __init__(self, name, customer_id, account_number, account_type, balance):
        super().__init__(name, customer_id, account_number, account_type, balance)
        self.minimum_initial_deposit = 50000
        self.users = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid amount for withdrawal.")

    def show_balance(self):
        return f"Your Balance: {self.balance}"
    
    def close_account(self):
        if self.balance == 0:
            print("Account closed.")       
        
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class BankUserInterface:
    __users = [] 

    @staticmethod
    def create_account():
        os.system("cls")
        print("CREATE AN ACCOUNT")
        last_name = input("Last Name: ")
        first_name = input("First Name: ")
        middle_name = input("Middle Name: ")
        address = input("Address: ")
        birthdate = input("Birthdate: ")
        gender = input("Gender: ")
        contact_no = input("Contact No: ")
        nationality = input("Nationality: ")
        status = input("Status: ")

        os.system('cls')
        print("\nUser's Input for Verification:")
        print(f"Last Name: {last_name}")
        print(f"First Name: {first_name}")
        print(f"Middle Name: {middle_name}")
        print(f"Address: {address}")
        print(f"Birthdate: {birthdate}")
        print(f"Gender: {gender}")
        print(f"Contact No: {contact_no}")
        print(f"Nationality: {nationality}")
        print(f"Status: {status}")

        confirmation = input("\nConfirm account creation? (y/n): ")
        if confirmation.lower() == "y":
            print("Account is verifying...")
            print("Account is Created.")
            os.system('cls')
            
            # Ask the user to sign up
            sign_up_choice = input("Would you like to sign up now? (y/n): ")
            if sign_up_choice.lower() == "y":
                BankUserInterface.signup()
                os.system('cls')
            
        else:
            print("Account is not verified.")
            input()
            BankUserInterface.create_account()
    
    @staticmethod
    def signup():
        print("SIGN UP")
        username = input("Create Username: ")
        password = input("Create Password: ")
        

        # Check if the username is already taken
        for user in BankUserInterface.__users:
            if user.username == username:
                print("Username already taken. Please choose another one.")
                return

        # If the username is unique, create a new User instance and add it to the list
        os.system('cls')
        new_user = User(username, password)
        BankUserInterface.__users.append(new_user)
        print("Account is created. Press [enter] to continue.")
        input()

    #LOG IN 
    @staticmethod
    def log_in():
        user_name = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        
        account_type = input("Account Type:(Savings/ Checking/ Joint): ")
        if account_type == 'Savings' or 'savings':
            initial_deposit = None
            maintaining_balance = None
            s_choice = None

            while s_choice != '4' :
                os.system('cls')
                print("Savings Account")
                print("[1] Deposit\n[2] Withdrwal\n[3] Check Balance\n[4] Log out")
                initial_deposit = 500
                maintaining_balance = 20000
                s_choice = input("\nEnter Choice: ")

                if s_choice == '1':
                    deposit_amount = float(input("Enter the deposit amount: "))
                    if deposit_amount > 0:
                        initial_deposit += deposit_amount  # Update the balance
                        print(f"Deposited {deposit_amount}.")
                    else:
                     print("Invalid deposit amount.")
 
                elif s_choice == '2':
                    withdrawal_amount = float(input("Enter the withdrawal amount: "))
                    if maintaining_balance >= withdrawal_amount:
                        maintaining_balance -= withdrawal_amount
                        print(f"Withdrew {withdrawal_amount}.")
                    else:
                        print("Insufficient balance.")

                elif s_choice == '3':
                    print(f"Your account balance is {initial_deposit}.")

                elif s_choice == '4':
                    print("Logging out...")
                else:
                    print("Invalid choice. Please choose from 1 to 4.")

        elif account_type == 'Checking' or 'Checking':
            c_initial_deposit = None
            c_choice = None
            c_balance = None

            while c_choice != '4' :
                os.system('cls')
                print("[1] Deposit\n[2] Withdrawal\n[3] Check Balance\n[4] Log out")
                c_initial_deposit = 25000
                c_choice = input("\nEnter Choice: ")

                if c_choice == '1':
                    deposit_amount = float(input("Enter the deposit amount: "))
                    if deposit_amount > 0:
                        c_initial_deposit += deposit_amount  # Update the balance
                        print(f"Deposited {deposit_amount}.")
                    else:
                     print("Invalid deposit amount.")
 
                elif s_choice == '2':
                    withdrawal_amount = float(input("Enter the withdrawal amount: "))
                    if c_balance >= withdrawal_amount:
                        c_balance -= withdrawal_amount
                        print(f"Withdrew {withdrawal_amount}.")
                    else:
                        print("Insufficient balance!")

                elif c_choice == '3':
                    print(f"Your account balance is {c_initial_deposit} PHP.")

                elif c_choice == '4':
                    print("Logging out...")
                else:
                    print("Invalid choice. Please choose from 1 to 4.")


    @staticmethod
    def show_menu():
        choice = None

        while choice != '3':
            os.system('cls')
            print("EA Bank")
            print("[1] Create account\n[2] Login\n[3] Exit")
            choice = input("\nEnter Choice: ")

            if choice == '1':
                BankUserInterface.create_account()
            elif choice == '2':
                BankUserInterface.log_in()
            elif choice == '3':
                print("Exiting the program.")
                break
            else:
                print("ERROR: Invalid choice. Press [enter] to continue.")
                input()


if __name__== '__main__':
    BankUserInterface.show_menu()