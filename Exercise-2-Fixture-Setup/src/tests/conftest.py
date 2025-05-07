import pytest
from conta import Conta
from banco import Banco
from agencia import Agencia
from transacao import Entrada
from dinheiro  import Moeda, Dinheiro

@pytest.fixture
def conta() -> Conta:
  banco = Banco("Banco UFSC", Moeda.BRL)
  agencia = Agencia("CTC", 1234, banco)
  conta = Conta("Henrique", 123,  agencia)
  dinheiro = Dinheiro(Moeda.BRL, 100, 50)
  transacao_entrada = Entrada(dinheiro)
  conta.adicionar_transacao(transacao_entrada)
  return conta