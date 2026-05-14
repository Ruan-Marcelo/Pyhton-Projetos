# abrir uma planilha principal
# adicionar uma nova coluna ao lado da coluna Veículos
# pegar os valores da outra planilha
# copiar os dados da coluna P
# começar da linha 3
# preencher a nova coluna automaticamente
# apenas a primeira ocorrência de cada empresa será preenchida
# correção de correspondência fuzzy para melhorar resultados

# pip install pandas openpyxl rapidfuzz

import pandas as pd
from rapidfuzz import process, fuzz
import re
import unicodedata

# =========================
# ARQUIVOS
# =========================

arquivo_principal = "Unicom.xlsx"
arquivo_secundario = "Fatura Mensal VDO.xlsx"

# =========================
# LER PLANILHAS
# =========================

df_principal = pd.read_excel(arquivo_principal)
df_secundario = pd.read_excel(arquivo_secundario)

# =========================
# COMEÇAR DA LINHA 3
# =========================

df_secundario = df_secundario.iloc[2:].reset_index(drop=True)

# =========================
# FUNÇÃO PARA LIMPAR NOMES
# =========================

def limpar_nome(texto):
    if pd.isna(texto):
        return ""
    texto = str(texto).lower()
    # remover acentos
    texto = unicodedata.normalize('NFKD', texto)
    texto = texto.encode('ASCII', 'ignore').decode('utf-8')
    # remover caracteres especiais
    texto = re.sub(r'[^a-z0-9\s]', '', texto)
    # remover palavras comuns, mantendo termos importantes
    remover = ["ltda", "sa", "s a", "me", "eireli", "brasil", "empresa"]
    for palavra in remover:
        texto = texto.replace(palavra, "")
    return texto.strip()

# =========================
# EMPRESAS DA SECUNDÁRIA
# =========================

empresas_secundaria = df_secundario.iloc[:, 0].astype(str).tolist()
empresas_limpas = [limpar_nome(x) for x in empresas_secundaria]

# =========================
# FUNÇÃO PARA BUSCAR VALOR (com token_set_ratio e threshold menor)
# =========================

def buscar_valor(nome_empresa):
    nome_limpo = limpar_nome(nome_empresa)
    
    resultado = process.extractOne(
        nome_limpo,
        empresas_limpas,
        scorer=fuzz.token_set_ratio
    )
    
    if resultado:
        melhor_nome, score, indice = resultado
        if score >= 65:  # threshold reduzido
            valor = df_secundario.iloc[indice, 15]  # coluna P = índice 15
            return valor
    return None

# =========================
# GERAR NOVA COLUNA (APENAS PRIMEIRA OCORRÊNCIA)
# =========================

empresas_preenchidas = set()  # vai guardar nomes já preenchidos

def buscar_valor_unico(nome_empresa):
    nome_limpo = limpar_nome(nome_empresa)
    if nome_limpo in empresas_preenchidas:
        return None
    valor = buscar_valor(nome_empresa)
    if valor is not None:
        empresas_preenchidas.add(nome_limpo)
    return valor

nova_coluna = df_principal.iloc[:, 1].apply(buscar_valor_unico)

# =========================
# INSERIR AO LADO DE VEÍCULOS
# =========================

pos_veiculos = df_principal.columns.get_loc("Veículos")

df_principal.insert(
    pos_veiculos + 1,
    "Quantidade",
    nova_coluna
)

# =========================
# SALVAR
# =========================

df_principal.to_excel("resultado.xlsx", index=False)

print("Dados comparados!")