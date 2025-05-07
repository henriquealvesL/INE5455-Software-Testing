import pytest
from agencia import Agencia

class Test_Agencia:
  @pytest.fixture
  def agencia(self) -> Agencia:
    return Agencia("CTC", 1234, "Banco UFSC")
  
  def test_nome_banco(self, agencia: Agencia): 
    # IMPLICIT FIXTURE SETUP
    # EXERCISE SUT
    nome_banco = agencia.banco

    # RESULT VERIFICATION
    assert nome_banco == "Banco UFSC"

  def test_obter_identificador(self, agencia: Agencia):  
    # IMPLICIT FIXTURE SETUP
    # EXERCISE SUT
    digito = agencia.obter_identificador()

    # RESULT VERIFICATION
    assert digito == "1234"

  def test_criar_conta(self, agencia: Agencia):
    # IMPLICIT FIXTURE SETUP
    # EXERCISE SUT
    conta = agencia.criar_conta("Henrique")

    # RESULT VERIFICATION
    assert conta.titular == "Henrique"

  def test_verificar_contas_agencia(self, agencia: Agencia):
    #IMPLICIT FIXTURE SETUP
    # INLINE FIXTURE SETUP
    agencia.criar_conta("Henrique")
    # EXERCISE SUT
    contas = agencia.obter_contas()
    # RESULT VERIFICATION
    assert len(contas) == 1

