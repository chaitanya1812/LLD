import bank_account as b
def test_bank():
    ba = b.BankAccount()
    print("\ninitial balance :",ba.balance) # accessing public variable
    # print(ba.__balance) # accessing private variable raises no attribute error
    ba.deposit(100) # deposite
    print("after deposit",ba._balance) # accessing protected variable
    ba.set_balance(150) # set balance using setter
    print("after set balance", ba.get_balance()) # balance using getter
