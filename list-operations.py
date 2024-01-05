# list comprehension
from functools import reduce

x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]  # [valor_a_adicionar laço condição]
z = [i**2 for i in x if i % 2 == 0]
# print(x)
# print(y)
# print(z)

# Enumerate
lista = ["abacate", "bola", "cachorro"]
for i, nome in enumerate(lista):
    # print(i, nome)
    pass


# filter
def pares(numero_dado):
    if numero_dado % 2 == 0:
        return numero_dado


lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = filter(pares, lista2)
# print(list(lista_pares))

# reduce


def soma(valor1, valor2):
    return valor1 + valor2


lista3 = [1, 3, 5, 10, 20]
somatorio = reduce(soma, lista3)
# print(somatorio)

# map


def dobro(valor_dado):
    return valor_dado * 2


lista4 = [1, 2, 3, 4, 5]
lista_dobrada = map(dobro, lista4)
# print(list(lista_dobrada))

# funções lambda
lista_exemplo = [1, 2, 3, 4, 5]
nova_lista_dobrada = map(lambda i: i*2, lista_exemplo)
# print(list(nova_lista_dobrada))

# zip
lista5 = [1, 2, 3, 4, 5]
lista6 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista7 = ["R$ 2,00", "R$ 5,00", "Não tem preço", "Não tem preço", "Não tem preço"]
for numero, nome, valor in zip(lista5, lista6, lista7):
    print(numero, nome, valor)
