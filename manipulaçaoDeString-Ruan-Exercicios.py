nome_completo = input("Digite seu nome completo: ")

split = nome_completo.lower().split(" ")
print(split)

nome = input("Digite seu nome completo: ")
partes = nome.split()
primeiro_nome = partes[0].lower()
print( "Login Gerado", primeiro_nome)

placa = input("Digite a placa: ").replace(" ", "")

if len(placa) == 7 and placa.isalnum():
    print("Placa valida")
else:
    print("Placa não valida")

print(placa.upper())
print(len(placa.upper()))

# comentario = input("Digite um comentario: ").strip()
# comentario_final = comentario.replace("ODIO", "***")
# tamanho = len(comentario_final)

# if comentario_final.isupper():
#   print("Comentario considerado grito")
# else:
#   print("Comentario não considerado grito")

# print(comentario_final)
# print(tamanho)


comentario = input("Digite um comentario: ").strip()
comentario_final = comentario.replace("ODIO", "***")
print("comentario tratado: ",comentario_final)
print("quantidade:", len(comentario_final))
if comentario_final.isupper():
  print("Comentario considerado grito")
else:
  print("Comentario normaç")
