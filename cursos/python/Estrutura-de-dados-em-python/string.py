string1 = 'Hello world'
string2 = "Hello World com python"
string3 = """Hello World com python e três aspas triplas simples"""

print(type(string1))
print(type(string2))
print(type(string3))

# Conversão para String

string4 = 123456
print(type(str(string4)))

# Concatenação

string5 = "Python" + "é legal!"
print(string5)

string6 = "Python é" + " muito" * 3 + " legal"
print(string6)

# Descontruindo uma String

string7 = "python"
print(string7[0])
print(string7[-6])
print(string7[1:5])
print(string7[:4])
print(string7[0:5:2])

# Métodos internos

string8 = "Python4Noobs"
print(len(string8))
print(string8.count("o"))
print(string8.count("o", 3, 7))

# UPPER e LOWER.

print(string7.upper())
print(string7.lower())

# Os métodos: Isalnum, replace e split.
# Isalnum: Retorna true se todos os caracteres forem alfanúmericos.
# replace:Retorna uma nova string substituindo na string a todas as ocorrências de uma string b por uma nova string c.
# split:Separa a string a toda vez que for encontrada uma string b.

string9 = "melancia321"
string10 = "melancia321*%#"
string11 = "Brasil"

print(string9.isalnum())
print(string10.isalnum())

print(string11.replace("s", "z"))
print(string11.split("as"))
