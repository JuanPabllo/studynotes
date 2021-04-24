# Estas duas listas são simples, e então denominadas de vetores.

listas1 = ["python", "php"]
listas2 = [312.5, 22 + 4j]

# Esta lista é composta, e então considerada uma matriz.
listas3 = [["c#", "go lang"], [40, -8.980]]

# Buscando na lista1 a palavra python
print(listas1[0])
print(listas1[-2])

# Buscando na lista2 o número complexo
print(listas2[1])
print(listas2[-1])

# Agora, vamos buscar na matriz
# Buscando na lista3 a palavra go lang
print(listas3[0][1])

# Buscando o número inteiro positivo
print(listas3[1][0])

# Comprimento de uma lista

print(len(listas1))
print(len(listas2))
# Número de linhas
print(len(listas3))
# Número de colunas
print(len(listas3[0]))
print(len(listas3[1]))

# Valores
# Valor máximo da lista3 coluna
print(max(listas3[1]))

# Valor mínimo da lista3 coluna 1
print(min(listas3[1]))

# soma da lista3 coluna 1
print(sum(listas3[1]))

# Métodos

# Append: Usamos ele para acrescentar um novo dado a lista
# Insert: Usamos ele para acrescentar um novo dado a lista, de acordo com o índice.
# Remove: Remover um dado de acordo com índice.
# Sort: Ordena a lista.
# Reserve: Inverte a posição dos itens
# Count: Número de vezes que um dado aparece na lista

listas1.append("java")
print(listas1)

listas1.insert(1, "c")
print(listas1)

listas1.remove("php")
print(listas1)

# Vamos criar uma nova lista e adicionar diretamente agora, para testar o sort e reverse.

lista_nova = [99, -9, 6.7, 86, 10.6]

# lista_nova.sort()
# print(lista_nova)

lista_nova.reverse()
print(lista_nova)

# Vamos criar nossas últimas listas para usar o método count

ultima_lista1 = [0, 11, 2, "python", "python"]
ultima_lista2 = [11, 22, 45]

print(ultima_lista1.count("python"))
print(ultima_lista2.count("python"))
