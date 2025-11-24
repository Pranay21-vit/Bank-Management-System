import random
import sys

# Define ANSI color codes for console output
class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    MAGENTA = '\033[95m' # Light Violet
    ENDC = '\033[0m'     # Reset color

def print_colored_header():
    """Prints a custom-colored header banner to the console."""
    
    header_text = f"""
{Colors.BLUE}====================================================
{Colors.MAGENTA} • PROJECT:🏦Renaissance Bank Management Systemk
{Colors.BLUE}---------------------------------------------------
{Colors.GREEN}  • 🪪CREATED BY: PRANAY KOTHARI 25BCE10248
{Colors.BLUE}===================================================={Colors.ENDC}
"""
    # Using sys.stderr or sys.stdout will print to the console
    print(header_text, file=sys.stdout)

# --- Start of running code ---

# **Call the function to print the colored header banner**
print_colored_header()


class Bank():
    Bname = "Renaissance Bank"
    clients = []

    def updateUser(self, client):
        self.clients.append(client)

    def authenticate(self, name, account_number, password):
        auth = False
        for i in self.clients:
            if (i.account["name"] == name and
                i.account["accno"] == account_number and
                i.account["password"] == password):
                auth = True
                return i
        print("Wrong credentials")
        return False

class Client():
    account = {}

    def __init__(self, name, deposit, password):
        self.account["name"] = name
        self.account["deposit"] = deposit
        self.account["accno"] = random.randint(100000, 999999)
        self.account["password"] = password
        print(f"Your account has been created, account number is: {self.account['accno']}")

    def deposit(self, amnt):
        self.account["deposit"] += amnt
        print("Deposit successful")

    def withdraw(self, amnt):
        if self.account["deposit"] >= amnt:
            self.account["deposit"] -= amnt
            print("Withdrawal successful")
        else:
            print("Insufficient funds")

    def check(self):
        print(f"Balance: {self.account['deposit']} rupees")

def main():
    bank = Bank()
    print(f"\nHello and welcome to {bank.Bname}")
    flag = True
    while flag:
        print("""\nWhat would you like to do:
                1.) Create a new account
                2.) Inquire existing account
                3.) Exit""")
        try:
            choice = int(input("Press 1, 2, or 3: "))
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")
            continue
            
        if choice == 1:
            name = input("Enter name: ")
            
            # Simple input validation for deposit
            while True:
                try:
                    deposit = int(input("Enter deposit amount: "))
                    if deposit >= 0:
                        break
                    else:
                        print("Deposit must be a non-negative number.")
                except ValueError:
                    print("Invalid amount. Please enter a number.")
                    
            password = input("Enter password: ")
            client = Client(name, deposit, password)
            bank.updateUser(client)
            
        elif choice == 2:
            name = input("Enter name: ")
            
            # Simple input validation for account number
            while True:
                try:
                    account_number = int(input("Enter account number: "))
                    break
                except ValueError:
                    print("Invalid account number. Please enter a number.")
            
            password = input("Enter password: ")
            current_client = bank.authenticate(name, account_number, password)
            
            if current_client:
                print("""\nWhat would you like to do:
                        1.) Deposit
                        2.) Withdraw
                        3.) Check balance
                        4.) Exit""")
                try:
                    choice = int(input("Press 1, 2, 3, or 4: "))
                except ValueError:
                    print("Invalid input. Please enter 1, 2, 3, or 4.")
                    continue
                    
                if choice == 1:
                    while True:
                        try:
                            amount = int(input("Enter deposit amount: "))
                            if amount >= 0:
                                break
                            else:
                                print("Amount must be non-negative.")
                        except ValueError:
                            print("Invalid amount. Please enter a number.")
                    current_client.deposit(amount)
                    
                elif choice == 2:
                    while True:
                        try:
                            amount = int(input("Enter withdrawal amount: "))
                            if amount >= 0:
                                break
                            else:
                                print("Amount must be non-negative.")
                        except ValueError:
                            print("Invalid amount. Please enter a number.")
                    current_client.withdraw(amount)
                    
                elif choice == 3:
                    current_client.check()
                elif choice == 4:
                    print("Returning to main menu.")
                else:
                    print("Invalid choice. Returning to main menu.")
            else:
                print("Authentication failed.")
        elif choice == 3:
            flag = False
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            
    print("Thank you for using the Renaissance Bank system. Goodbye!")
    return "Bye"

if __name__ == "__main__":
    main()
