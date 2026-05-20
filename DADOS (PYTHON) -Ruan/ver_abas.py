import pandas as pd

# Carrega todas as abas do arquivo Excel em um dicionário
arquivo_excel = pd.ExcelFile('')

# Extrai os nomes das abas e converte para uma lista em Python
abas = arquivo_excel.sheet_names

# Exibe a lista de abas
print(abas)