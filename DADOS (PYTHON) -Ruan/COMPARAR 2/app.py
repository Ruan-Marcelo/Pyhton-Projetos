# Abre a planilha Fatura Mensal VDO.xlsx e pega:
# Coluna AZ (quantidade) a partir da linha 3
# Coluna BA (valor) a partir da linha 3
# Nomes de empresas na coluna A, linha 3 em diante
# Abre a planilha Unicom.xlsx, pega nomes das empresas na coluna B, linha 2 em diante
# Faz correspondência fuzzy entre os nomes das duas planilhas usando RapidFuzz
# Insere duas novas colunas após a última coluna da planilha Unicom:
# Quantidade (da coluna AZ)
# Valor (da coluna BA)
# Preenche os valores de acordo com o nome da empresa (com correspondência aproximada)
# Adiciona uma coluna extra indicando qual nome da planilha VDO foi considerado correspondente

# pip install pandas openpyxl rapidfuzz

import pandas as pd
from rapidfuzz import process, fuzz
import re
import unicodedata

# =========================
# ARQUIVOS
# =========================
arquivo_principal = ""
arquivo_secundario = ""

# =========================
# LER PLANILHAS
# =========================
df_principal = pd.read_excel(arquivo_principal)
df_secundario = pd.read_excel(arquivo_secundario)

# =========================
# COMEÇAR DA LINHA 3 DA SECUNDÁRIA
# =========================
df_secundario = df_secundario.iloc[2:].reset_index(drop=True)  # linha 3 em diante

# =========================
# FILTRO DE NOMES E PADRONIZAÇÃO
# =========================
def limpar_nome(texto):
    if pd.isna(texto):
        return ""
    texto = str(texto).lower()
    texto = unicodedata.normalize('NFKD', texto)
    texto = texto.encode('ASCII', 'ignore').decode('utf-8')
    texto = re.sub(r'[^a-z0-9\s]', '', texto)
    remover = ["ltda", "sa", "s a", "me", "eireli", "brasil", "empresa"]
    for palavra in remover:
        texto = texto.replace(palavra, "")
    return texto.strip()

# =========================
# NOMES E VALORES DA PLANILHA SECUNDÁRIA
# =========================
nomes_sec = df_secundario.iloc[:, 0].astype(str).tolist()  # coluna A
nomes_sec_limp = [limpar_nome(x) for x in nomes_sec]

quantidades = df_secundario.iloc[:, 51].tolist()  # coluna AZ
valores = df_secundario.iloc[:, 52].tolist()      # coluna BA

# =========================
# FUNÇÃO PARA BUSCAR VALORES COM CORRESPONDÊNCIA DOS NOMES DAS EMPRESAS
# =========================
def buscar_valores(nome_empresa):
    nome_limpo = limpar_nome(nome_empresa)
    resultado = process.extractOne(
        nome_limpo,
        nomes_sec_limp,
        scorer=fuzz.token_set_ratio
    )
    if resultado:
        melhor_nome, score, indice = resultado
        if score >= 65:
            return quantidades[indice], valores[indice], nomes_sec[indice]  # retorna também o nome correspondente
    return None, None, None

# =========================
# CRIAR NOVAS COLUNAS NA PLANILHA PRINCIPAL
# =========================
ultima_col = df_principal.shape[1]

lista_quantidade = []
lista_valor = []
lista_correspondente = []  # nova lista

# nomes na coluna B, linha 2 em diante
for nome in df_principal.iloc[:, 1]:
    qtd, val, nome_vdo = buscar_valores(nome)
    lista_quantidade.append(qtd)
    lista_valor.append(val)
    lista_correspondente.append(nome_vdo)  # adiciona o nome correspondente

# inserir após a última coluna
df_principal.insert(ultima_col, "Quantidade", lista_quantidade)
df_principal.insert(ultima_col + 1, "Valor", lista_valor)
df_principal.insert(ultima_col + 2, "Nome VDO Correspondente", lista_correspondente)  # nova coluna

# =========================
# SALVAR RESULTADO
# =========================
df_principal.to_excel("atualizado.xlsx", index=False)
print("Planilha atualizada!")