class Account:
    def __init__(self, name):
        self.name = name
        self.deposit = []
        self.withdrawal = []
        self.loans = []
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
    def request_loan(self,amount):
        if amount < self.get_balance():
            self.loans.append(amount)
            self.balance = self.get_balance()
        else:
            return 'Your loan request has been denied\n'
        return f'{self.name} your loan request of {amount} KES has been approved,\nyour new balance is {self.get_balance()}\n'

  
 
    
account1 = Account("Akeza")
account2 = Account("Saloi")
account1.get_balance()
print(account1.withdraws(10))
print(account1.request_loan(10000))
print(account1.deposits(1000))
print(account1.withdraws(200))
print(account1.request_loan(500))


#  Transfer Funds: Method to transfer funds from one account to an instance of another account.
    # def transfer_funds(self,amount):
    