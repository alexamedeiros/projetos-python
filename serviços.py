
#criando uma lista uma lista inicial com alguns serviços# 1. Criando uma lista inicial com alguns serviços
servicos = ["Manicure", "Pedicure", "Esmaltação em Gel", "Blindagem"]

print("--- Lista Inicial de Serviços ---")
# Mostrando cada serviço um por um
for servico in servicos:
    print(f"- {servico}")

# 2. Adicionando um novo item na lista (simulando um cadastro)
novo_servico = "Spa dos Pés"
servicos.append(novo_servico)
novo_servico = "Esmaltação em Gel"
servicos.append(novo_servico)

print("\n--- Lista Atualizada com Novo Serviço ---")
# Mostrando a lista atualizada
for servico in servicos:
    print(f"- {servico}")

# 3. Mostrando o total de serviços cadastrados
total = len(servicos)
print(f"\nTotal de serviços disponíveis: {total}")

#removendo um serviço da lista pelo nome 
servicos.remove("Manicure")
print("\n--- Lista Após Remover a Manicure---")
for servico in servicos:
    print(f"- {servico}")