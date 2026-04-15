import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

endpoint = 'https://language60914924.cognitiveservices.azure.com/'
key = '1pPmwys2kCuKFFa80VRt9cuD7mt4mAsG2RhTFVjqfvxJeTx0lHiyJQQJ99CDACYeBjFXJ3w3AAAaACOG0rsq'

text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

documents = [
    'O ambiente estava maravilhoso',
    'O produto é ruim e não presta'    
]


result = text_analytics_client.analyze_sentiment(documents, show_opinion_mining=True)
docs = [doc for doc in result if not doc.is_error]

print("Let's visualize the sentiment of each of these documents")
for idx, doc in enumerate(docs):
    print(f"Document text: {documents[idx]}")
    print(f"Overall sentiment: {doc.sentiment}")