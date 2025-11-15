from E1 import Account2
b1 = Account2("Luis", "003", 2000)  # crea cuenta
b2 = Account2("Ana", "004", 1500)  # crea cuenta
print(b1.get_name(), b1.get_no(), b1.get_balance())  # muestra datos
b1.set_name("Carlos")  # cambia nombre
b1.set_no("009")  # cambia nro
b1.set_balance(5000)  # cambia saldo
print(b1.get_name(), b1.get_no(), b1.get_balance())  # muestra cambios
