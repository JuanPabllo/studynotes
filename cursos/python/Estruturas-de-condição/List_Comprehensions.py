# nova_lista = []
# for i in lista_antiga:
#     if filter(i):
#         nova_lista.append(expressions(i))

new_list = [expression(i) for i in old_list if filter(i)]

# Sintaxe
[expressao for item in list if condicao]
for item in list:
    if condicao:
        expressao

nova_lista = [expression(i) for i in lista_antiga if filter(i)]