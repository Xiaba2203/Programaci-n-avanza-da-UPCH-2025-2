from E1_Account import Account
a1 = Account("Juan", "001", 1000)  # crea cuenta
a2 = Account("Maria", "002", 500)  # crea cuenta
a1.deposit(200)  # deposita
a1.withdraw(100)  # retira
a2.deposit(300)  # deposita
a2.withdraw(1000)  # intenta retiro
a1.dump()  # muestra datos
a2.dump()  # muestra datos
