lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo']

lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)


# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)
#
# print(max(lista_animal))
#
# if 'lobo' in lista_animal:
#     print('existe um lobo na lista')
# else:
#     print('não existe um lobo')
#     lista_animal.append('lobo')
#     print(lista_animal)
#
# lista_animal.pop(0)
# print(lista_animal)
#
#
# lista_animal.remove('elefante')
# print(lista_animal)