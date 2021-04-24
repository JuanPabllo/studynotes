# nome_dicionario = {"key":"valor"}
# nome_dicionario = {key:valor}

telefones = {
    "Roberto": "3354-5548",
    "Monica": "1235-8547"
}

print("Numero do Roberto: ", telefones["Roberto"])
print("Numero do Monica: ", telefones["Monica"])

# Métodos

print(telefones.get("Antonio", "Contato inexistente"))

# Adicionando valores

telefones["Yudi"] = "4002-8546"
print(telefones)

# Removendo valores

del telefones["Roberto"]
print(telefones)
