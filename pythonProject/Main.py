class Main:
    pass


from Cliente import Cliente

from Conta import Conta

c1= Cliente("Arthur Ferigra Emidio","1195723-0911")
conta=Conta(c1.get_nome(),6565,0)

conta.deposita(1000)
conta.saque(50)
conta.extrato()





