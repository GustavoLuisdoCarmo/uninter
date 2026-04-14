soma = 0
MenorNumero = 100
MaiorNumero = 0

while True:

    numero = float(input("informe um número de 1 a 100: "))

    if numero < 0:
        print("informe outro número. nmrl")
        continue
    elif numero == 0:
        break
    elif numero > 100:
        print("muito grande, tem que ser menor que 100.")
        continue
    else:
        soma = soma + numero
        if numero > MaiorNumero:
            MaiorNumero = numero

        if (numero != 0) and (numero < MenorNumero):
            MenorNumero = numero

print(f"\n\nA soma de todos os numeros é: {soma}")
print(f"o maior numero de todos os numeros que você digitou com muita criatividade foi: {MaiorNumero}")
print(f"o menor e mais paia numero que você colocou foi: {MenorNumero}")
