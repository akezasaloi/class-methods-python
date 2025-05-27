class Account:
    def __init__(self, name):
        self.name = name
        self.deposit = []
        self.withdrawal = []
        self.loans = []
        self.paid_loan = []
    def get_balance(self):
        balance = 0
        for x in self.deposit:
            balance += x
        for l in self.loans:
            balance += l
        for y in self.withdrawal:
            balance -= y
        return balance 
    def deposits(self,amount):
        if amount > 0 :
            self.deposit.append(amount)
            self.balance = self.get_balance()
        else:
            print('You do not have enough money in your account\n')
            exit
        return f'{self.name} you have deposited {amount} KES in your account,\nyour new balance is {self.balance}\n'
    def withdraws(self,amount):
        if amount < self.get_balance():
            self.withdrawal.append(amount)
            self.balance = self.get_balance()
        else:
            return 'You do not have enough money in your account\n'
        return f'{self.name} you have withdrawn {amount} KES from your account,\nyour new balance is {self.get_balance()}\n'
    def request_loan(self,loan):
        if loan > 0:
            self.loans.append(loan)
            self.deposit.append(loan)
            print(f"Loan of ${loan} has been approved and deposited")
        else:
            return 'Your loan request has been denied\n'
        return f'{self.name} your loan request of {loan} KES has been approved,\nyour new balance is {self.get_balance()}\n'
    def repay_loan(self,loan):
        if loan <= self.get_balance():
            total_loan = sum(self.loans) - sum(self.paid_loan)
            if loan <= total_loan:
                self.withdrawal.append(loan)
                self.paid_loan.append(loan)
                print(f"You have successfully repaid {loan} KES from your loan")
        else:
            print("You don't have enough balance to pay the loan") 
        return f'your new balance is {self.get_balance()}\n'     
    def transfer(self, amount, receiver_account):
        if amount > 0 and self.get_balance() >= amount:
            self.withdrawals.append(amount)
            receiver_account.deposits.append(amount)
            self.transfers.append((amount, receiver_account.name))
            receiver_account.received.append((amount, self.name))
            print(f"Transferred ${amount} to {receiver_account.name}")
        else:
            print("Transfer failed: Insufficient balance or invalid amount")
account1 = Account("Akeza")
account2 = Account("Saloi")
account1.get_balance()
print(account1.withdraws(10))
print(account1.request_loan(10000))
print(account1.deposits(1000))
print(account1.withdraws(200))
print(account1.request_loan(500))
print(account1.repay_loan(200))


#  Transfer Funds: Method to transfer funds from one account to an instance of another account.
    # def transfer_funds(self,amount):
    