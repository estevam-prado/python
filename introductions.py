# EXERCÍCIO 1 // IMPRIMA "OLÁ MUNDO!"
print("Olá Mundo!")

# EXERCÍCIO 2 // SOLICITE 3 NÚMEROS E IMPRIMA A SOMA DESTES
x = int(input("Digite um número inteiro:"))
y = int(input("Digite outro número inteiro:"))
z = int(input("Digite um último número inteiro:"))
n = x + y + z
print("A soma destes números é", str(n), ".")

# EXERCÍCIO 3 // SOLICITE O NOME DE UMA FRUTA E IMPRIMA UMA FRASE MOSTRANDO TAL FRUTA
fruta = input("Digite o nome de uma fruta:")
print("A fruta digita foi:", fruta, ".")

# EXERCÍCIO 4 // TRANSFORME A DISTÂNCIA DE UMA CIDADE EM KM PARA METROS
dist = float(input("Digite a distância de uma cidade em km:"))
metros = dist * 1000
print("A distância em metros é:", str(metros), ".")

# EXERCÍCIO 5 // CALCULE A MÉDIA DE DUAS NOTAS
np1 = float(input("Digite a nota da prova 1:"))
np2 = float(input("Digite a nota da prova 2:"))
media = (np1 + np2) / 2
print("A média final foi: ", str(media), ".")

# EXERCÍCIO 6 // CALCULE A ÁREA DE UM QUADRADAO A PARTIR DE SEU LADO
lado = float(input("Digita o tamanho do lado do quadrado:"))
area = lado ** 2
print("A área do quadrado é:", str(area), ".")

# EXERCÍCIO 7 // CALCULE A ÁREA DE UM CÍRCULO A PARTIR DE SEU RAIO
raio = float(input("Digite o tamanho do raio do círculo:"))
cirArea = raio ** 2 * 3.1415
print("A área do circulo é:", str(cirArea), ".")

# EXERCÍCIO 8 // TRANSFORME A TEMPERATURA DE FAHRENHEIT PARA CELSIUS
fahr = float(input("Digite a temperatura em Fahrenheit:"))
cel = 5 * ((fahr - 32) / 9)
print("A temperatura em Celsius é ", str(cel), "°.")

# EXERCÍCIO 9 // TRANSFORME A TEMPERATURA DE CELSIUS PARA FAHRENHEIT
tempC = float(input("Digite a temperatura em Celsius:"))
tempF = (tempC * 9 / 5) + 32
print("A temperatura em Fahrenheit é", str(tempF), "°.")

# EXERCÍCIO 10 // CALCULE A MÉDIA DE 3 ALTURAS
alt1 = float(input("Digite a altura da primeira pessoa:"))
alt2 = float(input("Digite a altura da segunda pessoa:"))
alt3 = float(input("Digite a altura da terceira pessoa:"))
altMedia = (alt1 + alt2 + alt3) / 3
print("A média das alturas é: ", str(altMedia), ".")

# EXERCÍCIO 11 // CÁLCULOS ENTRE 3 NÚMEROS INTEIROS
n1 = int(input("Digite o primeiro número inteiro:"))
n2 = int(input("Digite o segundo número inteiro:"))
n3 = int(input("Digite o terceiro número inteiro:"))
res1 = n1 % n2
res2 = n2 ** n3
res3 = n1 / n3 + n2
print("Resultado 1:", str(res1), ", Resultado 2:", str(res2), ", Resultado 3:", str(res3), ".")

# EXERCÍCIO 12 // CÁLCULO DE PESO IDEAL BASEADO NA ALTURA
altura = float(input("Digite a altura:"))
sexo = input("Masculino ou Feminino?")
if sexo == "Masculino" or sexo == "masculino":
    pesoIdeal = (72.7 * altura) - 58
elif sexo == "Feminino" or sexo == "feminino":
    pesoIdeal = (62.1 * altura) - 44.7
print("O peso ideal é", str(pesoIdeal), ".")

# EXERCÍCIO 13 // CÁLCULO DA HIPOTENUSA
cat1 = float(input("Digite o valor do primeiro cateto:"))
cat2 = float(input("Digite o valor do segundo cateto:"))
hip = (cat1 ** 2 + cat2 ** 2) ** 0.5
print("A hipotenusa deste triângulo é:", str(hip), ".")

# EXERCÍCIO 14 // SEPARAÇÃO DA PARTE INTEIRA E O RESTO DA DIVISÃO
nmb1 = int(input("Digite o primeiro número inteiro:"))
nmb2 = int(input("Digite o segundo número inteiro:"))
div = nmb1 // nmb2
rest = nmb1 % nmb2
print("Divisão:", str(div), ", Resto:", str(rest), ".")
