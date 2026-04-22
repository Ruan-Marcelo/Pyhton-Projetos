#pip install pandas
#pip install openpyxl
import pandas as pd
import openpyxl
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import time 

def analyze_sentiment(endpoint, credential, frases):
    text_analytics_client = TextAnalyticsClient(endpoint, credential)
    response = text_analytics_client.analyze_sentiment(frases, language="pt")
    result = [doc for doc in response if not doc.is_error]
    return result 

credential = AzureKeyCredential("your_key_here")
endpoint='your_endpoint_here'

arquivo = 'opinioes.xlsx'
df = pd.read_excel(arquivo)

cont = 1
dic_info = {
    'pasta carbonara':[0,0],
    'risotto':[0,0],
    'pizza margherita':[0,0]
}

frases = []
qtd = 0
qtd_analyze = 0
for index, row in df.iterrows():
    frases.append(row['Opiniao'])
    qtd += 1
    qtd_analyze += 1
    print(f'Analisando: {qtd}')

    if qtd == 10:
        ret_analyze = analyze_sentiment(endpoint,credential,frases)
        for ret in ret_analyze:            
            if ret.confidence_scores.positive >= 0.5:
                dic_info[row['Produto']][0] += ret.confidence_scores.positive   # soma scores positivos
                dic_info[row['Produto']][1] += 1       # soma quantidades de opiniões    

        frases = []
        qtd = 0
        time.sleep(1)


medias = [
    dic_info['pasta carbonara'][0] / dic_info['pasta carbonara'][1],
    dic_info['risotto'][0] / dic_info['pasta carbonara'][1],
    dic_info['pizza margherita'][0] / dic_info['pasta carbonara'][1]
]

print(f'Medias de pontuções => Pasta carbonara: {medias[0]} / Risotto: {medias[1]} / Pizza margherita: {medias[2]}')
pos_maior = medias.index(max(medias))
print(f'Prato sugerido: {list(dic_info.keys())[pos_maior]}')