from matrizes import H, D, L
import gui

class Node:
    def __init__(self, station, parent, line_color):
        self.parent = parent
        self.station = station
        self.line_color = line_color

        self.g = 0  # custo
        self.h = 0  # heuristica
        self.f = 0


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
    minutos = km * 2
    return minutos


def printarFronteira(fronteira):
    print("Fronteira:")
    for node in fronteira:
        print(f"-> E{node.station + 1} | f: {node.f:.1f} | g: {node.g:.1f} | Linha {get_color_name(node.line_color)} ")
    print("-" * 50)


def get_color_name(color_number):
    # Faz o mapeamento das cores com os índices
    color_mapping = {
        1 : "Azul",
        2: "Amarela",
        3: "Verde",
        4: "Vermelha"
    }
    return color_mapping.get(color_number, None)


def astar(start_node, end_station):
    fronteira = []
    visitados = []

    fronteira.append(start_node)

    while len(fronteira) > 0:
        # Seleciona o primeiro nó da fronteira
        fronteira.sort(key=lambda x: x.f)
        printarFronteira(fronteira)
        current_node = fronteira.pop(0)
        visitados.append(current_node)

        # Testa se o nó selecionado é estado final
        if current_node.station == end_station:
            path = []
            current = current_node
            while current is not None:
                path.append((current.station + 1, current.g))
                current = current.parent
            return path[::-1]  # Return reversed path

        # Gera um novo conjunto de estados
        children = []
        for i in range(14):
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

            # Child já está na fronteira, chegando na mesma linha
            for node_fronteira in fronteira:
                if child.station == node_fronteira.station and child.line_color == node_fronteira.line_color and child.g > node_fronteira.g:
                    is_better = False

            # Insere os nós gerados na fronteira
            if is_better: fronteira.append(child)


def inicio(ini,fim,cor):
    estacao_partida = int(ini)-1
    linha_partida = cor
    estacao_final = int(fim)-1

    node_partida = Node(estacao_partida, None, linha_partida)
    path = astar(node_partida, estacao_final)
    print('Trajeto percorrido:')
    lista = []
    for estacao, _ in path:
        lista.append(estacao)
    print(f"Tempo total {path[-1][1]} minutos")
    return [path[-1][1], lista]
