from utilitarios import (
    cadastrar_categoria,
    cadastrar_transacao,
    saldo_total,
)
# categorias
categoria_receitas = cadastrar_categoria('Receitas')
categoria_contas = cadastrar_categoria('Contas Fixas')
categoria_viagens = cadastrar_categoria('Viagens')
categoria_lazer = cadastrar_categoria('Lazer')

# transações
cadastrar_transacao(
    descricao= 'Salario Jan/2024',
    valor= 1000.0,
    categoria= categoria_receitas
)
cadastrar_transacao(
    descricao= 'Mesada',
    valor= 50.0,
    categoria= categoria_contas
)
cadastrar_transacao(
    descricao= 'Ingresso Show',
    valor= -150.0,
    categoria= categoria_lazer
)
cadastrar_transacao(
    descricao= 'Viagem Disney',
    valor= -400.0,
    categoria= categoria_viagens
)
final = saldo_total()

print('Saldo total: ', final)