import pytest
from banco import Banco

class Test_Banco:
  @pytest.fixture
  def banco(self) -> Banco:
    return Banco("Banco UFSC", "R$")
  
  def test_moeda_banco(self, banco: Banco):
    # IMPLICIT FIXTURE SETUP
    # EXERCISE SUT
    moeda = banco.moeda

    # RESULT VERIFICATION
    assert moeda == "R$"

  def test_criar_agencia(self, banco: Banco):
    # IMPLICIT FIXTURE SETUP
    # EXERCISE SUT
    agencia = banco.criar_agencia("CTC")

    # RESULT VERIFICATION
    assert agencia.nome == "CTC"

  def test_obter_agencias(self, banco: Banco):
    # IMPLICIT FIXTURE SETUP
    # INLINE FIXTURE SETUP
    banco.criar_agencia("CTC")

    # EXERCISE SUT
    agencias = banco.obter_agencias()

    # RESULT VERIFICATION
    assert len(agencias) == 1

  def test_obter_uma_agencia(self, banco: Banco):
    # IMPLICIT FIXTURE SETUP
    # INLINE FIXTURE SETUP
    banco.criar_agencia("CTC")

    # EXERCISE SUT
    agencia = banco.obter_agencia("CTC")

    # RESULT VERIFICATION
    assert agencia.nome == "CTC"