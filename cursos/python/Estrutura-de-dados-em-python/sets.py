set1 = ({1, 2, 3, 4})
set2 = set([2, 90, 8, 5])

print(type(set1))
print(type(set2))

# Adicionando dados

set1.add(40)
print(set1)

set2.add(65)
print(set2)

# Atualizando dados

set1.update([10, 8, 67])
print(set1)

set2.update([22, 33, 78])
print(set2)

# Remoção de dados
# O método discard, só faz uma remoção por vez

set1.discard(8)
print(set1)

set2.discard(78)
print(set2)

# Operações matemáticas
# União

set_novo1 = ({1, 2, 3})
set_novo2 = set([4, 5, 6])

print(set_novo1.union(set_novo2))

# Interseção

set_novo3 = ({4, 7, 8})
set_novo4 = set([4, 5, 6])

print(set_novo3.intersection(set_novo4))

# Diferença

print(set_novo3.difference(set_novo4))

# Diferença simétrica

print(set_novo3.symmetric_difference(set_novo4))
