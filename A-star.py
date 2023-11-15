# MATRIZ COM DISTANCIAS EM LINHA RETA
H = (
#	 E1    E2    E3    E4    E5    E6     E7    E8    E9    E10   E11   E12   E13   E14
    (0,    10,   18.5, 24.8, 36.4, 38.8,  35.8, 25.4, 17.6, 9.1,  16.7, 27.3, 27.6, 29.8),# E1
    (10,   0,    8.5,  14.8, 26.6, 29.1,  26.1, 17.3, 10,   3.5,  15.5, 20.9, 19.1, 21.8),# E2
    (18.5, 8.5,  0,    6.3,  18.2, 20.6,  17.6, 13.6, 9.4,  10.3, 19.5, 19.1, 12.1, 16.6),# E3
    (24.8, 14.8, 6.3,  0,    12,   14.4,  11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4),# E4
    (36.4, 26.6, 18.2, 12,   0,    3,     2.4,  19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9),# E5
    (38.8, 29.1, 20.6, 14.4, 3,    0,     3.3,  22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2),# E6
    (35.8, 26.1, 17.6, 11.5, 2.4,  3.3,   0,    20,   23,   27.3, 34.2, 25.7, 12.4, 15.6),# E7
    (25.4, 17.3, 13.6, 12.4, 19.4, 22.3,  20,   0,    8.2,  20.3, 16.1, 6.4,  22.7, 27.6),# E8
    (17.6, 10,   9.4,  12.6, 23.3, 25.7,  23,   8.2,  0,    13.5, 11.2, 10.9, 21.2, 26.6),# E9
    (9.1,  3.5,  10.3, 16.7, 28.2, 30.3,  27.3, 20.3, 13.5, 0,    17.6, 24.2, 18.7, 21.2),# E10
    (16.7, 15.5, 19.5, 23.6, 34.2, 36.7,  34.2, 16.1, 11.2, 17.6, 0,    14.2, 31.5, 35.5),# E11
    (27.3, 20.9, 19.1, 18.6, 24.8, 27.6,  25.7, 6.4,  10.9, 24.2, 14.2, 0,    28.8, 33.6),# E12
    (27.6, 19.1, 12.1, 10.6, 14.5, 15.2,  12.4, 22.7, 21.2, 18.7, 31.5, 28.8, 0,    5.1), # E13
    (29.8, 21.8, 16.6, 15.4, 17.9, 18.2,  15.6, 27.6, 26.6, 21.2, 35.5, 33.6, 5.1,  0)    # E14
    )

# MATRIZ COM DISTÂNCIAS REAIS
D = [[0, 10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 
 [10, 0, 8.5, -1, -1, -1, -1, -1, 10, 3.5, -1, -1, -1, -1], 
 [-1, 8.5, 0, 6.3, -1, -1, -1, -1, 9.4, -1, -1, -1, 18.7, -1], 
 [-1, -1, 6.3, 0, 13, -1, -1, 15.3, -1, -1, -1, -1, 12.8, -1], 
 [-1, -1, -1, 13, 0, 3, 2.4, 30, -1, -1, -1, -1, -1, -1], 
 [-1, -1, -1, -1, 3, 0, -1, -1, -1, -1, -1, -1, -1, -1], 
 [-1, -1, -1, -1, 2.4, -1, 0, -1, -1, -1, -1, -1, -1, -1], 
 [-1, -1, -1, 15.3, 30, -1, -1, 0, 9.6, -1, -1, 6.4, -1, -1], 
 [-1, 10, 9.4, -1, -1, -1, -1, 9.6, 0, -1, 12.2, -1, -1, -1], 
 [-1, 3.5, -1, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, -1], 
 [-1, -1, -1, -1, -1, -1, -1, -1, 12.2, -1, 0, -1, -1, -1], 
 [-1, -1, -1, -1, -1, -1, -1, 6.4, -1, -1, -1, 0, -1, -1], 
 [-1, -1, 18.7, 12.8, -1, -1, -1, -1, -1, -1, -1, -1, 0, 5.1], 
 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 5.1, 0]]

# AZUL     1
# AMARELA  2
# VERDE    3
# VERMELHA 4
# TABELA DE LIGAÇÕES, REPRESENTANDO TAMBEM A COR DA LINHA É FEITA A LIGAÇÃO
L = [
#	E0  E1 E2 E3 E4 E5 E6 E7 E8 E9 E10 E11 E12 E13
	(0, 1,  0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  0),# E0
	(1, 0,  1, 0, 0, 0, 0, 0, 2,  2,  0,  0,  0,  0),# E1
	(0, 1,  0, 1, 0, 0, 0, 0, 4,  0,  0,  0,  4,  0),# E2
	(0, 0,  1, 0, 1, 0, 0, 3, 0,  0,  0,  0,  3,  0),# E3
	(0, 0,  0, 1, 0, 1, 2, 2, 0,  0,  0,  0,  0,  0),# E4
	(0, 0,  0, 0, 1, 0, 0, 0, 0,  0,  0,  0,  0,  0),# E5
	(0, 0,  0, 0, 2, 0, 0, 0, 0,  0,  0,  0,  0,  0),# E6
	(0, 0,  0, 3, 2, 0, 0, 0, 2,  0,  0,  3,  0,  0),# E7
	(0, 2,  4, 0, 0, 0, 0, 2, 0,  0,  4,  0,  0,  0),# E8
	(0, 2,  0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  0),# E9
	(0, 0,  0, 0, 0, 0, 0, 0, 4,  0,  0,  0,  0,  0),# E10
	(0, 0,  0, 0, 0, 0, 0, 3, 0,  0,  0,  0,  0,  0),# E11
	(0, 0,  4, 3, 0, 0, 0, 0, 0,  0,  0,  0,  0,  3),# E12
	(0, 0,  0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  3,  0) # E13
	]
inicio = int(input('Estação de partida: '))-1
final = int(input('Estação destino: '))-1

fronteira = []
visitados = [0]*14
resposta = []
trocasDeEstacao  = 0
km = 0

def caminho(a):
    while a[3][2] != -1:
        resposta.append(a[3][2])
        a = a[3]

def sucessoresDe(a):
    for i in range (0, 14):
        if(L[a[2]][i] != 0 and visitados[a[2]] == 0):
            g = converterParaMinutos(a[3][1] + D[a[2]][i])
            h = converterParaMinutos(H[i][final])
            pai = a
            linha = L[a[2]][i]
            if(a[4] != linha):
                h += 4
            s = [h+g, g, i, pai, linha]
            fronteira.append(s)
    visitados[a[2]] = 1


def converterParaMinutos(x):
    mins = x*2
    return mins

def printarFronteira():
    print("FRONTEIRA:")
    for i in range(0, len(fronteira)):
        if(visitados[fronteira[i][2]] == 0):
            print(f'E{fronteira[i][2]+1}')
    print()
    


def estrela():
    k = 0
    while k > -1:	
        for i in range(0, len(fronteira)):
            if(visitados[fronteira[i][2]] == 0):
                break
        if(fronteira[i][2] == final):
            visitados[fronteira[i][2]] = 1
            resposta.append(fronteira[i][2])
            caminho(fronteira[i])
            break
        sucessoresDe(fronteira[i])
        fronteira.sort(key=lambda fronteira: fronteira[0])
        printarFronteira()
        k += 1

V = [0, 0, -1, -1, -1]
# E = [f, g, indiceEstacao, pai, corDaLinha]
a = [converterParaMinutos(H[inicio][final]), 0, inicio, V, None]
fronteira.append(a)
printarFronteira()
estrela()

respostaFinal = resposta[::-1]
print("-"*30)
print("Caminho percorrido: ")
for i in range(0, len(respostaFinal)):
    if i == 0:
       print(f"Saindo da estação E{respostaFinal[i]+1}")
       km += (D[respostaFinal[i]][respostaFinal[i+1]])
    elif i == len(respostaFinal)-1:
        print(f'Chegando na Estação E{respostaFinal[i]+1}')
    else:
        print(f"Passando por E{respostaFinal[i]+1}")
        km += (D[respostaFinal[i]][respostaFinal[i+1]])
        if L[respostaFinal[i-1]][respostaFinal[i]] != L[respostaFinal[i]][respostaFinal[i+1]]:
            trocasDeEstacao+=1
            print(">>Baldeação<<")

print(f'Tempo gasto no total: {converterParaMinutos(km) + trocasDeEstacao*4:.2f} minutos')
