class Budget:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return 'The balance in', self.name, 'is', self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            print('Insufficient Funds')
        else:
            self.balance > amount
            print('Transaction successful')

    def available_balance(self):
        return 'Your available balance in', self.name, 'budget is ', self.balance

    def transfer(self, transfer_amount):
        if self.balance < transfer_amount:
            print('Insufficient Funds')
        else:
            self.balance >= transfer_amount
            destination = input('What category are you transferring to?: \n')
            print('Transaction Successful, your new balance in', self.name, 'budget is', self.balance)


category_one = Budget('Food', 10000)
category_two = Budget('Clothing', 15000)
category_three = Budget('Entertainment', 7000)
