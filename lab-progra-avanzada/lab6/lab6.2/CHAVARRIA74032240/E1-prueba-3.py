from E1 import Account3
c1 = Account3("Pedro", "005", 3000)  # crea cuenta
c1.deposit(500)  # deposita
c1.withdraw(1000)  # retira
print("Última transacción:", c1.last_transaction())  # muestra última
