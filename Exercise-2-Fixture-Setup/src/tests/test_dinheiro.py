import pytest

from dinheiro import Dinheiro, Moeda, ValorMonetario

class Test_Dinheiro:

  @pytest.fixture
  def moeda(self) -> Moeda:
    return Moeda.BRL
  
  @pytest.fixture
  def dinheiro(self, moeda) -> Dinheiro:
    return Dinheiro(moeda, 1000, 1000)
  
  @pytest.fixture
  def valor(self, moeda) -> ValorMonetario:
    return ValorMonetario(moeda, 100)
  
  def test_create_dinheiro(self, moeda: Moeda, dinheiro: Dinheiro):
    # IMPLICIT FIXTURE SETUP
    # EXERCISE SUT
    dinheiro_test = dinheiro

    # RESULT VERIFICATION
    assert dinheiro_test.moeda == moeda

  def test_obter_quantia_em_escala(self,  dinheiro: Dinheiro):
    # IMPLICIT FIXTURE SETUP
    # EXERCISE SUT
    escala = dinheiro.obter_quantia_em_escala()
    # RESULT VERIFICATION
    assert escala == 101000.0

  def test_verificar_dinheiro_zero(self, moeda : Moeda):
    # IMPLICIT FIXTURE SETUP
    #INLINE FIXTURE SETUP
    dinheiro_test = Dinheiro(moeda, 0, 0)
    # EXERCISE SUT
    is_zero = dinheiro_test.zero()
    # RESULT VERIFICATION
    assert is_zero

  def test_formatar_sem_moeda(self, dinheiro: Dinheiro):
    # IMPLICIT FIXTURE SETUP
    # EXERCISE SUT
    formatado = dinheiro.formatar_sem_moeda()
    # RESULT VERIFICATION
    assert formatado == "1010,00"

  def test_formatar_com_moeda(self, dinheiro: Dinheiro):
    # IMPLICIT FIXTURE SETUP
    # EXERCISE SUT
    formatado = dinheiro.formatar_com_moeda()
    # RESULT VERIFICATION
    assert formatado == "1010,00 BRL"

  def test_somar(self, valor: ValorMonetario, dinheiro: Dinheiro):
    # IMPLICIT FIXTURE SETUP
    # EXERCISE SUT
    somado = valor.somar(dinheiro)
    # RESULT VERIFICATION
    assert somado.formatado() == "+1011,00 BRL"

  def test_subtrair(self, valor: ValorMonetario, dinheiro: Dinheiro):
    # IMPLICIT FIXTURE SETUP
    # EXERCISE SUT
    subtraido = valor.subtrair(dinheiro)
    # RESULT VERIFICATION
    assert subtraido.formatado() == "-1009,00 BRL"

  def test_obter_quantia_valor(self, valor: ValorMonetario):
      # IMPLICIT FIXTURE SETUP
    # EXERCISE SUT
    quantia = valor.obter_quantia()
    # RESULT VERIFICATION
    assert quantia.formatado() == "1,00 BRL"

  
  

