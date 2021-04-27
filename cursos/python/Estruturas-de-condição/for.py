fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == 'banana':
#         continue
#     print(x)

# for x in fruits:
#     if x == 'banana':
#         break
#     print(x)

# Função range()

for x in range(2, 30, 3):
    print(x)

# Keyword ELSE
for x in range(6):
    print(x)
else:
    print("Finnaly finished")

adj = ["red", "big", "tasty"]

for x in adj:
    for y in fruits:
        print(x, y)

# Declaração pass

for x in [0, 1, 2]:
    pass
# ter um loop for vazio como esse, geraria um erro sem a instrução pass
