from collections import deque

# Estado: (Me, Ce, Md, Cd, B)
# Me = missionarios na esquerda
# Ce = canibais na esquerda
# Md = missionarios na direita
# Cd = canibais na direita
# B  = 'E' (barco na esquerda) ou 'D' (barco na direita)

MOVES = [
    (1, 0),  # 1 missionario
    (0, 1),  # 1 canibal
    (2, 0),  # 2 missionarios
    (0, 2),  # 2 canibais
    (1, 1),  # 1 missionario e 1 canibal
]


def estado_seguro(Me, Ce, Md, Cd):
    """Verifica se o estado respeita a regra de segurança em ambas as margens."""
    cond_esq = (Me == 0) or (Me >= Ce)
    cond_dir = (Md == 0) or (Md >= Cd)
    return cond_esq and cond_dir


def sucessores(estado):
    """
    Gera todos os estados sucessores seguros a partir de um estado dado.
    """
    Me, Ce, Md, Cd, B = estado
    prox_estados = []

    if B == 'E':
        # barco sai da esquerda para a direita
        for dm, dc in MOVES:
            if Me >= dm and Ce >= dc:
                nMe = Me - dm
                nCe = Ce - dc
                nMd = Md + dm
                nCd = Cd + dc
                if estado_seguro(nMe, nCe, nMd, nCd):
                    prox_estados.append((nMe, nCe, nMd, nCd, 'D'))
    else:
        # barco sai da direita para a esquerda
        for dm, dc in MOVES:
            if Md >= dm and Cd >= dc:
                nMe = Me + dm
                nCe = Ce + dc
                nMd = Md - dm
                nCd = Cd - dc
                if estado_seguro(nMe, nCe, nMd, nCd):
                    prox_estados.append((nMe, nCe, nMd, nCd, 'E'))

    return prox_estados


def bfs_missionarios_canibais():
    """
    Executa uma busca em largura (BFS) para encontrar
    um caminho do estado inicial ao estado objetivo.
    Retorna a lista de estados da solução (incluindo início e fim),
    ou None se não houver solução.
    """
    inicio = (3, 3, 0, 0, 'E')
    objetivo = (0, 0, 3, 3, 'D')

    fila = deque([inicio])
    pai = {inicio: None}  # mapeia estado -> antecessor

    while fila:
        atual = fila.popleft()

        if atual == objetivo:
            # reconstrói o caminho a partir do dicionario de pais
            caminho = []
            s = atual
            while s is not None:
                caminho.append(s)
                s = pai[s]
            caminho.reverse()
            return caminho

        for prox in sucessores(atual):
            if prox not in pai:  # ainda não visitado
                pai[prox] = atual
                fila.append(prox)

    return None