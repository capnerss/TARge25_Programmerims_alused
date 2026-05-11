"""
Bank manager.

Konsoolipõhine programm, mis simuleerib lihtsat pangakontot.
Klassid ja objektid: BankAccount klassi loomine mallina ja sellest konkreetse objekti instantseerimine (loomine).
Konstruktorid: Initsialiseerimismeetodi (__init__) kasutamine objekti algseisundi (omaniku nimi, saldo) määramiseks.
Meetodid: Funktsioonide kirjutamine klassi sisse (deposit, withdraw, display_status),
et objekti andmeid turvaliselt muuta ja neile ligi pääseda.
Juhtimisstruktuurid ja loogika: if/else tingimuslausete kasutamine tehingute valideerimiseks (näiteks tagamaks,
 et sa ei saa välja võtta rohkem raha, kui kontol on).
"""


class BankAccount:
    """1. Constructor: Sets up the initial state of the object."""

    def __init__(self, owner, starting_balance=0.0):
        self.owner = owner
        self.balance = starting_balance

    def deposit(self, amount):
        """Adds money with basic validation."""
        if amount > 0:
            self.balance += amount
            print(f"[{self.owner}] Deposited €{amount:.2f}. New balance: €{self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Removes money with logic to check for sufficient funds."""
        if amount > self.balance:
            print(f"[{self.owner}] Withdrawal failed: Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"[{self.owner}] Withdrew €{amount:.2f}. New balance: €{self.balance:.2f}")

    def display_status(self):
        """Displays the object's current state"""
        print(f"--- Account Status ---\nOwner: {self.owner}\nBalance: €{self.balance:.2f}\n----------------------")


if __name__ == "__main__":
    # Create an object
    my_account = BankAccount("Toomas Hendrik", 100.0)
    # Show initial status
    my_account.display_status()
    # Test a successful deposit
    my_account.deposit(50.0)
    # Test a successful withdrawal
    my_account.withdraw(30.0)
    # Test a failing withdrawal (not enough money)
    my_account.withdraw(500.0)
    # Show final status
    my_account.display_status()
