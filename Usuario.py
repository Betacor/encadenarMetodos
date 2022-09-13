class Usuario:		
    nombre_banco = "Banco de Chile"		
    def __init__(self, nombre):
        self.nombre = nombre
        self.balance = 0


    def hacer_deposito(self, deposito):
        self.balance += deposito
        return self

    def hacer_retiro(self, giro):
        self.balance -= giro
        return self

    def mostrar_balance_usuario(self):
        print(f"El balance de {self.nombre} es {self.balance} pesos.")
        return self

    def transferir_dinero(self, transferencia, usuario):
        self.balance -= transferencia
        usuario.balance += transferencia
        print(f"{self.nombre} ha realizado una transferencia de {transferencia} pesos. Su saldo ahora es de {self.balance} pesos.")







        #DUDAS
        #agregar vinculacion con carlos: 
        #print(f"{self.nombre} ha realizado una transferencia de {transferencia} pesos de {CLIENTE?}. Su saldo ahora es {self.balance} pesos.")
        #como referirme a carlos, si self.nombre se refiere a Alicia
        




