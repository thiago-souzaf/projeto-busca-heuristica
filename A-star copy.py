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
D =[[ 0, 10,  -1,   -1,   -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 
    [10, 0,   8.5,  -1,   -1, -1, -1, -1, 10, 3.5, -1, -1, -1, -1], 
    [-1, 8.5, 0,    6.3,  -1, -1, -1, -1, 9.4, -1, -1, -1, 18.7, -1], 
    [-1, -1,  6.3,  0,    13, -1, -1, 15.3, -1, -1, -1, -1, 12.8, -1], 
    [-1, -1,  -1,   13,   0, 3, 2.4, 30, -1, -1, -1, -1, -1, -1], 
    [-1, -1,  -1,   -1,   3, 0, -1, -1, -1, -1, -1, -1, -1, -1], 
    [-1, -1,  -1,   -1,   2.4, -1, 0, -1, -1, -1, -1, -1, -1, -1], 
    [-1, -1,  -1,   15.3, 30, -1, -1, 0, 9.6, -1, -1, 6.4, -1, -1], 
    [-1, 10,  9.4,  -1,   -1, -1, -1, 9.6, 0, -1, 12.2, -1, -1, -1], 
    [-1, 3.5, -1,   -1,   -1, -1, -1, -1, -1, 0, -1, -1, -1, -1], 
    [-1, -1,  -1,   -1,   -1, -1, -1, -1, 12.2, -1, 0, -1, -1, -1], 
    [-1, -1,  -1,   -1,   -1, -1, -1, 6.4, -1, -1, -1, 0, -1, -1], 
    [-1, -1,  18.7, 12.8, -1, -1, -1, -1, -1, -1, -1, -1, 0, 5.1], 
    [-1, -1,  -1,   -1,   -1, -1, -1, -1, -1, -1, -1, -1, 5.1, 0]]

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

class Node:
    def __init__(self, station, parent, line_color):
        self.parent = parent
        self.station = station
        self.line_color = line_color

        self.g = 0
        self.h = 0
        self.f = 0

    def __str__(self):
        return f"(Estação: E{self.station+1}; f: {self.f}; g: {self.g};  Parent node: {self.parent}; cor da linha: {self.line_color})"
    def __repr__(self):
        return f"(Estação: E{self.station+1}; f: {self.f}; g: {self.g};  Parent node: {self.parent}; cor da linha: {self.line_color})"


def calcularHeuristica(estacao_atual, estacao_final) -> int:
    """ 
    Função para calcular a heurística da estacao atual até a estação destino seguindo uma linha reta.

    Args:
        estacao_atual: indice da estacao atual do nó
        estacao_final: indice da estacao de destino final

    Returns: 
        Retorna quantos minutos levam para percorrer a distância em linha reta
    """

    km = H[estacao_atual][estacao_final]
    min = transformarKilometroEmMinutos(km)
    return min

def transformarKilometroEmMinutos(km):
    # Considera velocidade média de 30km/h
    minutos = km*2
    return minutos

def astar (start_station, end_station):
    
    # Create start node
    start_node = Node(start_station, None, None)

    fronteira = []
    visitados = []

    fronteira.append(start_node)

    while len(fronteira) > 0:
        # Seleciona o primeiro nó da fronteira
        fronteira.sort(key=lambda x: x.f)
        current_node = fronteira.pop(0)
        visitados.append(current_node)
        

        # Testa se o nó selecionado é estado final
        if current_node.station == end_station:
            path = []
            current = current_node
            while current is not None:
                path.append((current.station+1, current.g))
                current = current.parent
            return path[::-1] # Return reversed path
        

        # Gera um novo conjunto de estados
        children = []
        for i in range (14):
            line_color = L[current_node.station][i]
            if line_color != 0:
                new_node = Node(i, current_node, line_color)
                new_node.g = current_node.g + transformarKilometroEmMinutos(D[current_node.station][new_node.station])

                # Soma 4 no gasto se estiver fazendo baldeação
                if current_node.line_color and current_node.line_color != line_color: new_node.g += 4

                new_node.h = calcularHeuristica(new_node.station, end_station)

                new_node.f = new_node.g + new_node.h

                children.append(new_node)
        
        # Verifica os children gerados
        for child in children:

            # Boolean para determinar se o child vai ser inserido ou não na fronteira com base nos nós visitados e nós na fronteira
            is_better = True
            
            # Child já está nos nós visitados
            for node_visitado in visitados:
                if child.station == node_visitado.station: is_better = False

            # Child já está na fronteira
            for node_fronteira in fronteira:
                if child.station == node_fronteira.station and child.line_color == node_fronteira.line_color and child.g > node_fronteira.g:
                    is_better = False

            # Insere os nós gerados na fronteira
            if is_better: fronteira.append(child)


def main():

    # estacao_partida = int(input('Estação de partida: '))-1
    # estacao_final = int(input('Estação destino: '))-1

    start = 13
    end = 1
    path = astar(start, end)
    print(path)


if __name__ == "__main__":
    main()
