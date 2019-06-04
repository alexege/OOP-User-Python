class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def make_deposit(self, amount):
        self.balance = self.balance + amount

    def make_withdrawal(self, amount):
        if(amount > self.balance):
            self.balance = self.balance - amount
    
    def display_user_balance(self):
        print(f"{self.name}, Balance: $ {self.balance}")

    def transfer_money(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount

# Create 3 instances of the User class
person1 = User('Alexander', 0)
person2 = User('Kian', 0)
person3 = User('Angelo', 0)

# Have the first user make 3 deposits and 1 withdrawal and then display their balance
person1.make_deposit(100)
person1.make_deposit(100)
person1.make_deposit(100)
person1.make_withdrawal(300)
person1.display_user_balance()

# Have the second user make 2 deposits and 2 widthdrawals and then display their balance
person2.make_deposit(25)
person2.make_deposit(25)
person2.make_withdrawal(10)
person2.make_withdrawal(5)
person2.display_user_balance()

# Have the third user make 1 deposits and 3 withdrawals and then display their balance
person3.make_deposit(450)
person3.make_withdrawal(100)
person3.make_withdrawal(100)
person3.make_withdrawal(100)
person3.display_user_balance()

# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances.
person1.display_user_balance()
person2.display_user_balance()
person1.transfer_money(person2, 50)
person1.display_user_balance()
person2.display_user_balance()
