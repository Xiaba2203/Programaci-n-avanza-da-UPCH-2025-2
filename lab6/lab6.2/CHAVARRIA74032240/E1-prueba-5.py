from E1 import Account4
import random  # para aleatorios
import pickle  # para guardar objetos

N = 3  # cantidad cuentas
cuentas = []  # lista vacía

for i in range(N):  # bucle
    nombre = "C" + str(i)  # nombre
    nro = str(100 + i)  # nro cuenta
    saldo = random.randint(100, 1000)  # saldo
    cuenta = Account4(nombre, nro, saldo)  # crea objeto
    if random.choice([True, False]):  # elige acción
        cuenta.set_balance(cuenta.get_balance() + 100)  # deposita
    else:
        cuenta.set_balance(max(0, cuenta.get_balance() - 50))  # retira
    cuentas.append(cuenta)  # guarda

with open("cuentas.dat", "wb") as f:  # abre archivo
    pickle.dump(cuentas, f)  # guarda lista

del cuentas  # borra de memoria

with open("cuentas.dat", "rb") as f:  # abre archivo
    cuentas = pickle.load(f)  # carga lista

print("Cuentas en memoria:", Account4.get_total())  # muestra total
for c in cuentas:  # recorre lista
    print(c.get_name(), c.get_no(), c.get_balance())  # muestra datos
