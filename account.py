class Account:
    def __init__(self, name):
        self.name = name
        self.deposit = []
        self.withdrawal = []
        self.loans = []
        self.paid_loan = []
        self.transfer = []
        self.amount_received = []

    def get_balance(self):
        balance = 0
        for x in self.deposit:
            balance += x
        for l in self.loans:
            balance += l
        for y in self.withdrawal:
            balance -= y
        for a in self.amount_received:
            balance += a
        return balance

    def deposits(self,amount):
        if amount > 0 :
            self.deposit.append(amount)
            self.balance = self.get_balance()
        else:
            print('You do not have enough money in your account\n')
            exit
        return f'{self.name} you have deposited {amount} KES in your account,\nyour new balance is {self.balance} KES\n'
    
    def withdraws(self,amount):
        if amount < self.get_balance():
            self.withdrawal.append(amount)
            self.balance = self.get_balance()
        else:
            return 'You do not have enough money in your account\n'
        return f'{self.name} you have withdrawn {amount} KES from your account,\nyour new balance is {self.get_balance()} KES\n'
    
    def request_loan(self,loan):
        if loan > 0:
            self.loans.append(loan)
        else:
            return 'Your loan request has been denied\n'
        return f'{self.name} your loan request of {loan} KES has been approved,\nyour new balance is {self.get_balance()} KES\n'
    
    def repay_loan(self,loan):
        if loan <= self.get_balance():
            total_loan = sum(self.loans) - sum(self.paid_loan)
            if loan <= total_loan:
                self.withdrawal.append(loan)
                self.paid_loan.append(loan)
                print(f"You have successfully repaid {loan} KES from your loan")
        else:
            print("You don't have enough balance to pay the loan") 
        return f'your new balance is {self.get_balance()} KES\n'     

    def get_account_statement(self):
        total_deposits = 0
        total_withdrawals = 0
        total_loans = 0
        total_money_received = 0
        print(f"Hello {self.name}, here is your account statement.")
        for amount in self.deposit:
             total_deposits += amount
             print(f"Deposited: {amount} KES")
        for amount in self.withdrawal:
            total_withdrawals += amount
            print (f"Withdrew: {amount} KES")
        for loan in self.loans:
            total_loans += loan
            print(f"Borrowed: {loan} KES")
        for amount in self.amount_received:
            total_money_received += amount
            print(f"Received: {amount} KES")
        print(f"Current balance: {self.get_balance()} KES\n")

    def interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        self.deposit.append(interest)
        return f"Interest of {interest:.1f} was added to your account's balance, your new balance is {self.balance:.1f} KES"

    def transfer_funds(self, amount, receiver):
        if amount > 0 and self.get_balance() >= amount:
            self.withdrawal.append(amount)
            self.transfer.append((amount, receiver.name))
            receiver.amount_received.append(amount)
            print(f"Transferred {amount} KES to {receiver.name}")
        else:
            print(f'Failed to transfer {amount}')
        return f'{self.name} your new balance is {self.get_balance()} KES\n'  
    
    def receive_funds(receiver,sender):
        if sender.transfer_funds():
            for a in sender.transfer:
                receiver.balance += a
            print(receiver.balance)
            
    def freeze_account(self):
         self.account_frozen = True
         print(f"{self.name}, your account has been successfully frozen.")

    def unfreeze_account(self):
        self.account_frozen = False
        print( f"{self.name}, your account now active.")
    
    def set_min_balance(self,amount):
        self.min_balance = amount
        return f"The minimum withdrawing amount now is {self.min_balance}"
    
    def close_account(self):
        close = input()
        print(f"Are you sure you want to close your account ?",close)
        if close == "yes":
            self.balance = 0
            self.deposits = []
            self.withdrawals = []
            self.loan = 0
            print("Your account has been closed")
        else:
            print("Account closing cancelled")

account1 = Account("Akeza")
account2 = Account("Saloi")
print("Your account balance is",account1.get_balance(),"KES")
print(account1.request_loan(1000))
print(account2.deposits(1000))
print(account1.deposits(2000))
print(account1.withdraws(200))
print(account1.withdraws(10))
print(account1.request_loan(500))
print(account1.repay_loan(200))
print(account1.transfer_funds(500,account2))
account1.get_account_statement()
account2.get_account_statement()
account2.freeze_account()
account1.unfreeze_account()
print(account2.interest())
print(account2.set_min_balance(500))


