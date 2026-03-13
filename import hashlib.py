import hashlib
# Importa a biblioteca hashlib, usada para gerar funções de hash 
from google.colab import files
# Importa o módulo files do Google Colab, que permite fazer upload de arquivos do computador

# Upload dos arquivos
files.upload()
# Abre uma janela para o usuário selecionar e enviar arquivos para o ambiente do Colab


def calcular_hash(caminho_arquivo):
    # Define uma função chamada calcular_hash que recebe o caminho/nome do arquivo

    hash_sha256 = hashlib.sha256()
    # Cria um objeto de hash usando o algoritmo SHA-256

    with open(caminho_arquivo, "rb") as arquivo:
        # Abre o arquivo em modo binário 

        for bloco in iter(lambda: arquivo.read(4096), b""):
            # Lê o arquivo em blocos de 4096 bytes até não haver mais dados

            hash_sha256.update(bloco)
            # Atualiza o cálculo do hash com o conteúdo do bloco lido

    return hash_sha256.hexdigest()
    # Retorna o hash final em formato hexadecimal (texto)


arquivo1 = input("Informe o nome do Arquivo 1: ")
# Solicita ao usuário o nome do primeiro arquivo

arquivo2 = input("Informe o nome do Arquivo 2: ")
# Solicita ao usuário o nome do segundo arquivo


try:
    # Inicia um bloco de tratamento de erros

    hash1 = calcular_hash(arquivo1)
    # Calcula o hash do primeiro arquivo

    hash2 = calcular_hash(arquivo2)
    # Calcula o hash do segundo arquivo

    print("\nHash do Arquivo 1:")
    # Exibe o texto indicando o hash do primeiro arquivo

    print(hash1)
    # Mostra o hash calculado do primeiro arquivo

    print("\nHash do Arquivo 2:")
    # Exibe o texto indicando o hash do segundo arquivo

    print(hash2)
    # Mostra o hash calculado do segundo arquivo

    if hash1 == hash2:
        # Compara se os dois hashes são iguais

        print("\nTrabalho plagiado!")
        # Se forem iguais, os arquivos têm o mesmo conteúdo

    else:
        print("\nTrabalho OK")
        # Se forem diferentes, os arquivos não são iguais


except FileNotFoundError:
    # Captura o erro caso algum arquivo não seja encontrado

    print("Erro: Arquivo não encontrado. Verifique o nome informado.")
    # Exibe uma mensagem de erro para o usuário
