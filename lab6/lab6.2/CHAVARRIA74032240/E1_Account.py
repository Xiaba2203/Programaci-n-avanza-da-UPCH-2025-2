class Account:
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount, limit=3000):
        if(self.balance - amount >=0 and amount<=limit):
            self.balance -= amount
            #self.transactions.append(-amount)
        else:
            if(self.balance - amount <0):
                print("No tiene suficiente dinero en la cuenta para retirar")
            if(amount>limit):
                print("No puede retirar mas que el límite diario:",limit)

    def dump(self):
        print(self.name, self.no, " balance:",self.balance)
        
