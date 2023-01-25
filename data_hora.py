from datetime import datetime
""" print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year) """


"""Recebendo uma data para lançamento de seu app """

""" data_de_lancamento = datetime.strptime(input("Quando devemos Lançar o app "), '%d%m%Y' )
print(data_de_lancamento) """

"""Considerando intervalo entre datas"""

""" data_atual = datetime.now()
intervalo = data_de_lancamento - data_atual

print(f"Temos exatamente o intervalo de {intervalo.days} dias para o lançamento de nosso App") """

"""Desafio !! Crie um programa que calcule quantos dias faltam para a sua data de aniversário """

data_hoje = datetime.now()
data_aniversario = datetime.strptime(input("Digite sua data de aniversário "), "%d%m%Y")

intervalo = data_aniversario - data_hoje
print(f"Faltam extamente {intervalo.days} para o seu aniversário ")
