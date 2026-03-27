nuns = []
par = 0
impar = 0

while len(nuns) < 5:
    try:
        num = int(input(f"Digite o {len(nuns) + 1}° número: "))
        nuns.append(num)
        
        
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
            
    except ValueError:
        print("Por favor, digite apenas números inteiros.")

print(f"Números digitados: {nuns}")
print(f"Pares: {par} | Ímpares: {impar}")
