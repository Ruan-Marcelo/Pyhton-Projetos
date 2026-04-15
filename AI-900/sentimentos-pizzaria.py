import os
import pandas as pd
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

endpoint = 'seu end_point'
key = 'su_key'

text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

arquivo = 'opinioes.xlsx'
df = pd.read_excel(arquivo)

for index, row in df.iterrows():
    texto = row['Opiniao']
    produto = row['Produto']

    result = text_analytics_client.analyze_sentiment([texto], show_opinion_mining=False)
    doc = list(result)[0]

    print(f"Produto: {produto}")
    print(f"Opinião: {texto}")
    print(f"Sentimento: {doc.sentiment}")
    print("-" * 40)