vetor = []

while len(vetor) < 8:
    try:
        numero = int(input(f"Digite o {len(vetor) + 1}º número: "))
        vetor.append(numero)
    except ValueError:
        print("Valor inválido digite apenas numeros inteiros.")

print("Vetor na ordem digitada:", vetor)

numerosParaSoma = []

while len(numerosParaSoma) < 10:
    try:
       nums = int(input(f"Digite o {len(numerosParaSoma) + 1}º numero: "))
       numerosParaSoma.append(nums)
       soma = sum(numerosParaSoma)
       print("Soma da truma: ", soma)

    except ValueError:
        print("Valor inválido digite apenas numeros inteiros.")

print("Vetor na ordem digitada:", numerosParaSoma)

for i in range(5):
    valor = int(input("Digite um numero: "))
    soma += valor
print('Soma total: ',soma)

notas = []

while len(notas) < 6:
    try:
        nota = float(input(f"digite o {len(notas) + 1} numero: "))
        notas.append(nota)
        media = sum(notas)/len(notas)
        
        acima = 0
        abaixo = 0
        
        for n in notas:
            if n >= media:
                acima += 1
            else:
                abaixo += 1
            
    except ValueError:
        print("Valor inválido digite apenas numeros inteiros.")

print(f"Média da turma: , {media:.2f}")
print("Acima da média", acima)
print("Abaixo da média", abaixo)
print("Vetor na ordem digitada:", notas)