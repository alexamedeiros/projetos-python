import sqlite3
# 1 Conectar ao banco de dados(cria um arquivo chamado"salao.db" automaticamente )
conexao = sqlite3.connect("salao.db")
cursor = conexao.cursor()

# 2 Criar uma tabela para guardar os nossos serviços
cursor.execute("""
CREATE TABLE IF NOT EXISTS servicos(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
nome TEXT
)
""")

# 3 Inserir um serviço de forma definitiva no banco de dados 
novo_servico = "Manicure"
cursor.execute("INSERT INTO servicos(nome) VALUES (?)", (novo_servico,))

#salvar (confirmar) a alteração no banco de dados
conexao.commit()
print("Servicos guardado no banco de dados com sucesso!")

# 4 Comsultar e mostrar o que está guardado no banco de dados 
cursor.execute("SELECT * FROM servicos")
resultados = cursor.fetchall()

print("\n--- Itens salvos no Banco de Dados ---")
for item in resultados:
    print(item)

# 5 Fechar a conexão com o banco 
conexao.close()
