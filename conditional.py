# EXERCÍCIO 1 // DETERMINAÇÃO SE O NÚMERO É PAR OU ÍMPAR
n = int(input("Digite um número inteiro: "))
det = n % 2

if det == 0:
    res = "par"
else: res = "impar"

print("O número é ", res, ".")

# EXERCÍCIO 2 // ESCRITA EM ORDEM CRESCENTE E DECRESCENTE EM SEGUIDA
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print(n1, n2, n2, n1)
elif n2 > n1:
    print(n2, n1, n1, n2)
else: print("Os dois números são iguais.")

# EXERCÍCIO 3 // DETERMINAÇÃO DO NÚMERO MAIOR/MENOR
nmb1 = int(input("Digite o primeiro número: "))
nmb2 = int(input("Digite o segundo número: "))

if nmb1 > nmb2:
    print('"', str(nmb1), '" é maior e "', str(nmb2), '" é menor.')
elif nmb2 > nmb1:
    print('"', str(nmb2), '" é maior e "', str(nmb1), '" é menor.')
else: print("Os dois números são iguais.")

# EXERCÍCIO 4 // DETERMINAÇÃO DO MENOR ENTRE 3 NÚMEROS
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

if x < y and x < z:
    menor = x
elif y < x and y < z:
    menor = y
else: menor = z

print(menor, "é o menor número")

# EXERCÍCIO 5 // CÁLCULO DO PREÇO A SER PAGO
uni = int(input("Digite a quantidade de produtos comprados: "))

if uni >= 20:
    preço = 10.9
else: preço = 12.9
pgmt = uni * preço

print("Deverá ser pago R$", pgmt, ".")

#EXERCÍCIO 6 // DETERMINE SE O PRIMEIRO NÚMERO É MÚLTIPLO DO SEGUNDO
num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro:"))

if num1 % num2 == 0:
    print("O primeiro número é múltiplo do segundo.")
else: (print("O primeiro número não é múltiplo do segundo."))

# EXERCÍCIO 7 // DETERMINE SE DETERMINADA LETRA É VOGAL OU CONSOANTE
a = input("Digite uma letra:")

if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
    print("A letra digitada é uma vogal.")
else: print("A letra digitada é uma consoante.")

# EXERCÍCIO 8 // RELACIONAMENTO DE NÚMERO COM DIA DA SEMANA
num = float(input("Digite um número de 1 a 7:"))

if num == 1:
    print("Domingo.")
elif num == 2:
    print("Segunda.")
elif num == 3:
    print("Terça.")
elif num == 4:
    print("Quarta.")
elif num == 5:
    print("Quinta.")
elif num == 6:
    print("Sexta.")
elif num == 7:
    print("Sábado.")
else: print("Valor inválido.")

# EXERCÍCIO 9 // OPERAÇÃO MATEMÁTICA UTILIZANDO 'match-case'
nmr1 = float(input("Digite o primeiro número:"))
nmr2 = float(input("Digite o segundo número:"))
opr = input("Digite uma operação matemática (+, -, *, /):")

match opr:
    case "+":
        resultado = nmr1 + nmr2
        print(resultado)
    case "-":
        resultado = nmr1 - nmr2
        print(resultado)
    case "*":
        resultado = nmr1 * nmr2
        print(resultado)
    case "/":
        resultado = nmr1 / nmr2
        print(resultado)
    case _:
        print("Operação Inválida.")
 
# EXERCÍCIO 10 // DETERMINAÇÃO DO VALOR A SER PAGO (VARIÁVEL)
mor = float(input("Quantos kg de morango?"))
maça = float(input("Quantos kg de maçã?"))

if mor > 5 or maça > 5 or mor + maça > 5:
    pMorVar = 15.20
    pMaçaVar = 7.50
elif mor < 5 or maça < 5 or mor + maça < 5:
    pMorVar = 19.50
    pMaçaVar = 8.80

frutasTotal = mor + maça
preçoMor = mor * pMorVar
preçoMaça = maça * pMaçaVar
preçoTotal = preçoMor + preçoMaça

if mor > 8 or maça > 8 or mor + maça > 8 or preçoTotal > 25:
    preçoTotal = preçoTotal - (preçoTotal * 0.1)

print("Você comprou", str(frutasTotal), "kgs de fruta e deve pagar R$", str(preçoTotal))

# EXERCÍCIO 11 // DETERMINAÇÃO DA MÉDIA, CONCEITO, E SITUAÇÃO DE APROVADO/REPROVADO DE DETERMINADO ALUNO
np1 = float(input("Digite a nota da prova 1:"))
np2 = float(input("Digite a nota da prova 2:"))
media = (np1 + np2) / 2

if media < 4:
    conceito = "E"
    resultado = "REPROVADO"
elif media >= 4 and media < 6:
    conceito = "D"
    resultado = "REPROVADO"
elif media >= 6 and media < 7.5:
    conceito = "C"
    resultado = "APROVADO"
elif media >= 7.5 and media < 9:
    conceito = "B"
    resultado = "APROVADO"
elif media >= 9:
    conceito = "A"
    resultado = "APROVADO"

print("Nota 1:", str(np1), ", Nota 2:", str(np2), ", Média:", str(media), ", Conceito:", conceito, ", Resultado:", resultado, ".")

# EXERCÍCIO 12 // VERIFICAÇÃO SE UM NÚMERO DE TRÊS DÍGITOS É DE DÍGITOS CRESCENTES
number = int(input("Digite um número de 3 dígitos:"))

if str(number) in '123456789':
    print("O número contêm dígitos crescentes.")
else: print("O número não contêm dígitos crescentes.")
