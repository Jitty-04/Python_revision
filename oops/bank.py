# method2 > deposit
# method3 > withdrawal
# method4 > thank you for visiting

class Bank:
    def add_user(self, name, ac_type, balance):
        self.balance = balance
        print('account created successfully')

    def deposit(self, amount):
        self.balance += amount
        print(f'{amount} deposited')

    def withdrawal(self, amount):
        if amount > self.balance:
            print('insufficient balance')
        else:
            self.balance -= amount
            print(f'{amount} debited from account')

    def check_balance(self):
        print(f'your current balance is {self.balance}')

    def greet(self):
        print('thank you for visiting..')

obj = Bank()

obj.add_user('Arun', 'savings', 5000)

obj.deposit(5000)

obj.withdrawal(1000)

obj.check_balance()

obj.greet()
