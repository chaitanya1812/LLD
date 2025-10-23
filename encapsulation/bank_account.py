class BankAccount():
    def __init__(self):
        self.__balance = 0.0 # private : completely private
        # for educational purpose
        self._balance = 0.0 # Protected : intended to be private but not enforced
        self.balance = 0.0 # Public: normal public variable

    # public method to modify data
    def deposit(self, amt):
        if amt <= 0:
            raise ValueError("amount must be positive")
        self.__balance += amt
        self._balance += amt
        self.balance += amt
    
    # public method to modify data
    def withdraw(self, amt):
        if amt <= 0:
            raise ValueError("amount must be positive")
        if amt > self.__balance:
            raise ValueError("Insufficient balance")
        self.__balance -= amt
        self._balance -= amt
        self.balance -= amt
    
    # accessing private variable using getters: read-only access
    def get_balance(self):
        return self.__balance

    # # public method to modify data: set private variable __balance using setter
    def set_balance(self, amt):
        self.__balance = amt
        # for educational purpose
        self._balance = amt
        self.balance = amt



        