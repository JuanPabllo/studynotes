import random

# Int
num1 = 300
num2 = -8

print(type(num1))
print(type(num2))

# Float
num3 = 300.5  # número positivo com uma casa decimal
num4 = -433.6750  # número negativo com quatro casas decimais

print(type(num3))
print(type(num4))

# Complex
num5 = 2 + 4j
num6 = 4j
num7 = -10j

print(type(num5))
print(type(num6))
print(type(num7))

# Número aleatório

# Gera um número inteiro aleatório entre 0 e 10
print(random.randint(0, 10))

# Conversões

num8 = 80  # Número do tipo int
num9 = -9.6  # Número do tipo float

print(type(float(num8)))  # Convertendo de int para float
print(type(int(num9)))  # Convertendo de float para int
print(type(complex(num8)))  # Convertendo de int para complex

print(float(num8))
print(int(num9))
print(complex(num8))

# Operações aritméticas
# Operações com int.

print(10 + 9)  # Soma de inteiros
print(9 - 8)  # Subtração de inteiros
print(-9 * -9)  # Multiplicação de inteiros
print(10 / 3)  # Divisão de inteiros
print(10 // 3)  # Parte inteira da divisão entre inteiros
print(10**2)  # Exponenciação entre inteiros
print(10 % 2)  # Resto da divisão entre inteiros

# Operações com float.
print("-----------------------------------")

print(10.5 + 8.2)  # Soma com floats
print(-98.66 - 8.99)  # Subtração com floats
print(27.5 * 3.7)  # Multiplicação com floats
print(99.2 / 3.2)  # Divisão com floats
print(99.2 // 3.2)  # Parte inteira da divisão com floats
print(0.25**2)  # Exponenciação com floats
print(5.0 % 2.5)  # Resto da divisão com floats

# Operações com complex.
print("-----------------------------------")

print(3 + 4j + 3 + 4j)  # Soma com complex
print(2 + 4j - 2 + 8j)  # Subtração com complex
print(-2 + 9j * 16 + 90j)  # Multiplicação com complex
print(2 + 10j / 2j)  # Divisão com complex
print(25 + 2j ** 3 + 2j)  # Exponenciação com complex
