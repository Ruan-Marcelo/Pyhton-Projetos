print("Atividade - Valor total de uma compta com deconto");

valor1 = float(input("Digite o valor da primeira compra: "));

valor2 = float(input("Digite o valor da segunda compra: "));

valor_total = valor1 + valor2;

desconto = float(input("Digite o valor do desconto em %: "));

desconto = valor_total * (desconto / 100)

print(f"O valor total da compra é de: {valor_total}")
print(f"O valor do desconto é de: {desconto}")

valor_final = valor_total - desconto

print(f"O valo final da compra com o desconto aplicado foi de: {valor_final}")

print("Atividade - IMC");

peso = float(input("Digite seu peso em quilogramas: "));

altura = float(input("Digite a sua altura em metros: "));

imc = peso / (altura * altura);

print("Seu IMC é de:", round(imc));

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Você está no peso normal.")
elif 25 <= imc < 30:
    print("Você está acima do peso (Sobrepeso).")
elif 30 <= imc < 35:
    print("Você está na Obesidade Grau I.")
elif 35 <= imc < 40:
    print("Você está na Obesidade Grau II.")
else:
    print("Você está na Obesidade Grau III (Mórbida).")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("A sua média final é de:", round(media,2))

numero1 = int(input("Digite um número: "));
numero2 = int(input("Digite outro número: "));

soma = numero1 + numero2;

print(f"A soma dos dois numeros é: {soma}")

diferenca = numero1 - numero2;

print(f"A diferença entre o número 1 e o número 2 é de: {diferenca}")

produto = numero1 * numero2;

print(f"O produto entre o número 1 e o número 2 é de: {produto}")

divisao = numero1 // numero2;

if numero1 == 0 or numero2 == 0:
   print("Não é possível calcular a divisão por zero.")
else:
   print(f"A divisão entre o número 1 e o número 2 é de:", round(divisao,2))

resto = numero1 % numero2;

print(f"O resto da divisão entre o número 1 e o número 2 é de: {resto}");

nome = input("Digite seu nome Completo: ");
idade = int(input("Digite a idade atual: "));

idade_em_5 = idade + 5;

print(f"Após 5 anos você {nome} tera {idade_em_5}");

from datetime import date

nome = input("Digite seu nome Completo: ");
ano_nascimento = int(input("Digite o ano de nascimento: "));


ano_atual = date.today().year;
idade_atual = ano_atual - ano_nascimento;
idade_futura = idade_atual + 5;

print(nome,"daqui 5 anos terá", idade_futura, "anos. ");

