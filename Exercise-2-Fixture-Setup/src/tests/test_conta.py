from conta import Conta
from transacao import Saida
from dinheiro import Moeda, Dinheiro

class Test_Conta:
  def test_obter_identificador(self, conta: Conta):
    # DELEGATED FIXTURE SETUP

    # EXERCISE SUT
    identificador = conta.obter_identificador()

    # RESULT VERIFICATION
    assert identificador == "0123-8"

  def test_verificar_saldo(self, conta: Conta):
    # DELEGATED FIXTURE SETUP
    # EXERCISE SUT
    saldo = conta.calcular_saldo()
    # RESULT VERIFICATION
    assert saldo.formatado() == "+100,50 BRL"

  def test_saldo_negativo(self, conta: Conta):
    # DELEGATED FIXTURE SETUP
    # INLINE FIXTURE SETUP
    dinheiro = Dinheiro(Moeda.BRL, 200, 50)
    saida = Saida(dinheiro)
    conta.adicionar_transacao(saida)
    # EXERCISE SUT
    saldo = conta.calcular_saldo()
    # RESULT VERIFICATION
    assert saldo.formatado() == "-100,00 BRL"

  def test_saldo_zero(self, conta: Conta):
    # DELEGATED FIXTURE SETUP
    # INLINE FIXTURE SETUP
    dinheiro = Dinheiro(Moeda.BRL, 100, 50)
    saida = Saida(dinheiro)
    conta.adicionar_transacao(saida)
    # EXERCISE SUT
    saldo = conta.calcular_saldo()
    print(saldo)
    # RESULT VERIFICATION
    assert saldo.formatado() == "0,00"

