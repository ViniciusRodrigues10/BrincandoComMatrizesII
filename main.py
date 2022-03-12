matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input())
        linha.append(valor)
    matriz.append(linha)

somaPositivos = somaValoresForaDiagonalPrincipal = denominador = 0
menorValor = matriz[0][0]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] >= 0:
            somaPositivos += matriz[i][j]
            denominador += 1
        if matriz[i][j] < menorValor:
            menorValor = matriz[i][j]
        if i != j:
            somaValoresForaDiagonalPrincipal += matriz[i][j]

delta = 0
if (menorValor % 2) == 0:
    delta = 1

print("{:.2f}".format(somaPositivos / denominador), menorValor, delta, somaValoresForaDiagonalPrincipal)