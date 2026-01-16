class BankAccount:
    def __init__(self, account_number, initial_balance=0, branch_name="Main Branch"):
        self.account_number = account_number  # public
        self.__balance = initial_balance #only for class
        self._branch_name=branch_name  # for class and subclasses     
    def get_balance(self):
        return self.__balance
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount. Balance cannot be negative.")

account=BankAccount("123456789", 1000)
#account.__balance = 5000  # This will not change the actual balance
account.set_balance(1000)
print(account.account_number);
#print(account.__balance ) # This will raise an AttributeError
print(account.get_balance());