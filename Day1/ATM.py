def withdraw(balance,amount):
    if type(balance) != int or type(amount) != int:
        raise TypeError("Balance Must be a integer")
    
    if amount%100 != 0:
        raise ValueError("Amount must be a multiple of 100")

    if amount <= balance:
        balance = balance-amount
        return balance
    else:
        raise ValueError("There is not enough Balance to withdraw")

def main():
    balance = int(input("Enter Balance: "))
    amount = int(input("Enter Amount: "))
    result = withdraw(balance,amount)
    print(f"Balance Amount is {result}")

main()