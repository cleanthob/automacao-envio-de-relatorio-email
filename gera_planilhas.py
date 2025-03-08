import pandas as pd
import numpy as np

# Número de lojas
num_lojas = 25

# Criando dados fictícios para a planilha de desempenho diário
dados = {
    "Data": ["2025-03-08"] * num_lojas,
    "ID Loja": [i + 1 for i in range(num_lojas)],  # Agora inclui ID da loja
    "Faturamento do Dia": np.random.randint(500, 1500, num_lojas),
    "Meta de Faturamento Diário": [1000] * num_lojas,
    "Diversidade de Produtos Vendidos": np.random.randint(2, 6, num_lojas),
    "Meta de Diversidade de Produtos Diário": [4] * num_lojas,
    "Ticket Médio por Venda": np.random.randint(400, 600, num_lojas),
    "Meta de Ticket Médio Diário": [500] * num_lojas,
}

# Criar DataFrame de desempenho
df_desempenho = pd.DataFrame(dados)

# Adicionar coluna de Status de Meta
df_desempenho["Status de Meta"] = np.where(
    (df_desempenho["Faturamento do Dia"] >= df_desempenho["Meta de Faturamento Diário"])
    & (
        df_desempenho["Diversidade de Produtos Vendidos"]
        >= df_desempenho["Meta de Diversidade de Produtos Diário"]
    )
    & (
        df_desempenho["Ticket Médio por Venda"]
        >= df_desempenho["Meta de Ticket Médio Diário"]
    ),
    "Meta Atingida",
    "Meta Não Atingida",
)

# Caminho para salvar a planilha de desempenho
file_path_desempenho = r"Backup arquivos lojas\OnePage_Modelo.xlsx"

# Salvando como Excel
df_desempenho.to_excel(file_path_desempenho, index=False)

# Criando dados fictícios para a planilha de lojas
lojas = {
    "ID Loja": [i + 1 for i in range(num_lojas)],
    "Nome Loja": [f"Loja {i+1}" for i in range(num_lojas)],
}

# Criar DataFrame de lojas
df_lojas = pd.DataFrame(lojas)

# Caminho para salvar a planilha de lojas
file_path_lojas = r"Backup arquivos lojas\Lista_Lojas.xlsx"

# Salvando como Excel
df_lojas.to_excel(file_path_lojas, index=False)

# Número de lojas
num_lojas = 25

# Criando dados fictícios para a planilha de gerentes
gerentes = {
    "ID Loja": [i + 1 for i in range(num_lojas)],
    "Nome Gerente": [f"Gerente {i+1}" for i in range(num_lojas)],
    "Email": [f"testandopython7+{i+1}@gmail.com" for i in range(num_lojas)],
}

# Criar DataFrame de gerentes
df_gerentes = pd.DataFrame(gerentes)

# Caminho para salvar a planilha de gerentes
file_path_gerentes = r"Backup arquivos lojas\Lista_Gerentes.xlsx"

# Salvando como Excel
df_gerentes.to_excel(file_path_gerentes, index=False)

print("Planilhas geradas com sucesso!")
