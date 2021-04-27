# (if <condition>: <expression1> else: <expression2>)

# Primeiramente, a <condition> é avaliada.

# Se a <condition> receber True, <expression1> é validada e retorna o resultado;

# Se a <condition> receber False, <expression2> é validada e retorna o resultado.


num = 6
if(num % 2 == 0):
    s = 'par'
else:
    s = 'impar'

s = "par" if num % 2 == 0 else 'impar'
print("O número digitado é", s)
