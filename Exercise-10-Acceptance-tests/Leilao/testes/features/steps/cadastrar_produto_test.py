from behave import given, when, then
from src.mercado_leilao import MercadoLeilao

@given('o cadastro do usuario Ernani Cesar foi realizado')
def step_impl(context):
    context.mercado = MercadoLeilao()
    context.mercado.cadastra_usuario("Ernani Cesar", "UFSC", "ernani@posgrad.ufsc.br", "055.761.919-00")

@given('o nome do produto {nome}')
def step_impl(context, nome):
    context.nome_produto = nome

@given('a descricao do produto {descricao}')
def step_impl(context, descricao):
    context.descricao_produto = descricao

@given('e o lance {lance}')
def step_impl(context, lance):
    context.lance = int(lance)

@given('e o cpf do leiloador {cpf}')
def step_impl(context, cpf):
    context.cpf_leiloador = cpf

@given('a data limite e {data_limite}')
def step_impl(context, data_limite):
    context.data_limite = data_limite

@given('{produto} ja foi cadastrado')
def step_impl(context, produto):
    context.mercado.cadastra_produto("cadeira", "gamer", 100, "055.761.919-00", "2025-12-30")

@when('cadastrar o produto')
def step_impl(context):
    try:
        context.mercado.cadastra_produto(
            context.nome_produto,
            context.descricao_produto,
            context.lance,
            context.cpf_leiloador,
            context.data_limite
        )
        context.resultado = "cadastrado com sucesso"
    except Exception as e:
        context.resultado = str(e)

@then('o sistema cadastra com sucesso')
def step_impl(context):
    assert context.resultado == "cadastrado com sucesso"

@then('o sistema mostra a mensagem {mensagem}')
def step_impl(context, mensagem):
    assert context.resultado == mensagem