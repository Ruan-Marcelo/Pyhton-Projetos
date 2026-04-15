#pip install pandas
#pip install openpyxl
import pandas as pd
import openpyxl

arquivo = 'opinioes.xlsx'
df = pd.read_excel(arquivo)

cont = 1
for index, row in df.iterrows():
    print(row['Produto'], ' - ', row['Opiniao'])