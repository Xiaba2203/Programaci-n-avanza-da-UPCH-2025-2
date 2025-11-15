

# Clase Account2 con privados y get/set (ítem 4)
class Account2:
    def __init__(self, name, account_number, initial_amount):  # constructor
        self.__name = name  # privado nombre
        self.__no = account_number  # privado nro
        self.__balance = initial_amount  # privado saldo

    def get_name(self): return self.__name  # devuelve nombre
    def get_no(self): return self.__no  # devuelve nro
    def get_balance(self): return self.__balance  # devuelve saldo
    def set_name(self, name): self.__name = name  # cambia nombre
    def set_no(self, no): self.__no = no  # cambia nro
    def set_balance(self, bal): self.__balance = bal  # cambia saldo


# Clase Account3 con última transacción (ítem 6)
class Account3:
    def __init__(self, name, account_number, initial_amount):  # constructor
        self.__name = name  # privado nombre
        self.__no = account_number  # privado nro
        self.__balance = initial_amount  # privado saldo
        self.__transactions = []  # lista privada

    def deposit(self, amount):  # método depositar
        self.__balance += amount  # suma saldo
        self.__transactions.append(amount)  # guarda mov

    def withdraw(self, amount, limit=3000):  # método retirar
        if self.__balance - amount >= 0 and amount <= limit:  # valida
            self.__balance -= amount  # resta saldo
            self.__transactions.append(-amount)  # guarda mov
        else:
            print("Operación no permitida")  # error

    def last_transaction(self):  # última transacción
        if self.__transactions:  # si hay movimientos
            return self.__transactions[-1]  # devuelve última
        return None  # lista vacía


# Clase Account4 con contador (ítem 8)
class Account4:
    total = 0  # variable de clase

    def __init__(self, name, account_number, initial_amount):  # constructor
        self.__name = name  # privado nombre
        self.__no = account_number  # privado nro
        self.__balance = initial_amount  # privado saldo
        Account4.total += 1  # suma total objetos

    def get_name(self): return self.__name  # devuelve nombre
    def get_no(self): return self.__no  # devuelve nro
    def get_balance(self): return self.__balance  # devuelve saldo
    def set_balance(self, b): self.__balance = b  # cambia saldo

    @classmethod
    def get_total(cls): return cls.total  # devuelve total


# Clase Stock (ítem 12)
class Stock:
    def __init__(self, symbol, name, prev_price, curr_price):  # constructor
        self.__symbol = symbol  # privado símbolo
        self.__name = name  # privado nombre
        self.__previousPrice = prev_price  # precio previo
        self.__currentPrice = curr_price  # precio actual

    def get_symbol(self): return self.__symbol  # devuelve símbolo
    def get_name(self): return self.__name  # devuelve nombre
    def get_previousPrice(self): return self.__previousPrice  # devuelve previo
    def get_currentPrice(self): return self.__currentPrice  # devuelve actual
    def set_previousPrice(self, p): self.__previousPrice = p  # cambia previo
    def set_currentPrice(self, p): self.__currentPrice = p  # cambia actual

    def getChangePercent(self):  # calcula variación
        return (self.__currentPrice - self.__previousPrice) / self.__previousPrice * 100
