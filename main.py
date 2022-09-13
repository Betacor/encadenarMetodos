from Usuario import Usuario

alicia = Usuario("Alicia Araya")
bernardo = Usuario("Bernardo Borquez")
carlos = Usuario("Carlos Carmona")

alicia.hacer_deposito(100).hacer_deposito(700).hacer_deposito(1000).hacer_retiro(300).mostrar_balance_usuario()

bernardo.hacer_deposito(800).hacer_deposito(500).hacer_retiro(300).hacer_retiro(100).mostrar_balance_usuario()

carlos.hacer_deposito(3000).hacer_retiro(200).hacer_retiro(500).hacer_retiro(400).mostrar_balance_usuario()

alicia.transferir_dinero(150, carlos)

alicia.mostrar_balance_usuario()
carlos.mostrar_balance_usuario()







