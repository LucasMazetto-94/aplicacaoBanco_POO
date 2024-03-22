from datetime import datetime, timedelta
import pytz
from random import randint

class ContaCorrente:
    """
    cria um Objeto ContaCorrente para gerenciar as contas dos clientes

    Attributos:
        nome: Nome do Cliente
        cpf: CPF do Cliente
        agencia: Agencia responsável pela conta do Cliente
        num_conta: Número da conta do Cliente
        saldo: Saldo disponível na conta do cliente
        limete: Limite do cheque especial da conta
        limite_df: O limite difinido através de conta


    """

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self._cpf = cpf
        self._saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.limite_def = None
        self.transacoes = []
        self.cartao_credito = []

    def consultar_saldo (self):
        print('Seu saldo atual é de R$ {:,.2f}'.format(self._saldo))

    def depositar(self, valor):
        self._saldo += valor
        self.consultar_saldo()
        self.transacoes.append((valor, 'Saldo: R$ {:,.2f}'.format(self._saldo), ContaCorrente._data_hora()))

    def _definir_limite(self):
        self.limite_def = - self._saldo * 0.1
        return self.limite_def

    def _limite_conta(self):
        self.limite = self._definir_limite()
        return self.limite

    def sacar(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self.transacoes.append((-valor, 'Saldo: R$ {:,.2f}'.format(self._saldo), ContaCorrente._data_hora()))

    def consultar_limite(self):
        print('Seu limite de Cheque Especial é de R$ {:,.2f}'.format(self._limite_conta()))

    def historico_transacao(self):
        print('Histórico de Transações:')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self.transacoes.append((-valor, 'Saldo: R$ {:,.2f}'.format(self._saldo), ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino.transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))

class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000,9999999999999999)
        self.titular = titular
        self.validade = "{}/{}".format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year+4)
        self.cod_seguranca='{}{}{}'.format(randint(0,9), randint(0,9), randint(0,9))
        self.limite= 1000
        self.conta_corrente= conta_corrente
        conta_corrente.cartao_credito.append(self)






#programa
conta_lucas = ContaCorrente('lucas', '421.149.448-16', '1234', '34062')
cartao_lucas = CartaoCredito('Lucas', conta_lucas)

print(conta_lucas.cartao_credito[0].conta_corrente.num_conta)
print(cartao_lucas.validade)
print(cartao_lucas.numero)
print(cartao_lucas.cod_seguranca)
