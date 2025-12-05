from core import MOVES, estado_seguro

def aplicar_movimento_validando(estado, movimento):
    """
    Aplica um movimento (dm, dc) a partir do estado atual,
    verificando se é consistente com as regras do problema.

    Retorna:
      (True, novo_estado, None) se tudo ok
      (False, estado_atual, motivo) se o movimento for inválido
    """
    Me, Ce, Md, Cd, B = estado
    dm, dc = movimento

    # 1) Movimento precisa ser um dos operadores permitidos
    if (dm, dc) not in MOVES:
        return False, estado, f"Movimento {movimento} não é permitido."

    if dm == 0 and dc == 0:
        return False, estado, "Barco não pode mover vazio."

    # 2) Aplica o movimento dependendo de onde está o barco
    if B == 'E':
        # barco sai da esquerda para a direita
        if Me < dm or Ce < dc:
            return False, estado, "Não há pessoas suficientes na margem esquerda."
        nMe = Me - dm
        nCe = Ce - dc
        nMd = Md + dm
        nCd = Cd + dc
        B2 = 'D'
    else:
        # barco sai da direita para a esquerda
        if Md < dm or Cd < dc:
            return False, estado, "Não há pessoas suficientes na margem direita."
        nMe = Me + dm
        nCe = Ce + dc
        nMd = Md - dm
        nCd = Cd - dc
        B2 = 'E'

    # 3) Checa conservação de quantidades
    if nMe < 0 or nCe < 0 or nMd < 0 or nCd < 0:
        return False, estado, "Alguma quantidade ficou negativa."
    if nMe + nMd != 3 or nCe + nCd != 3:
        return False, estado, "Conservação de missionários ou canibais violada."

    # 4) Checa regra de segurança
    if not estado_seguro(nMe, nCe, nMd, nCd):
        return False, (nMe, nCe, nMd, nCd, B2), "Regra de segurança violada."

    novo_estado = (nMe, nCe, nMd, nCd, B2)
    return True, novo_estado, None


def verificar_sequencia(movimentos, verbose=True):
    """
    Verifica se uma sequência de movimentos leva do estado inicial
    ao estado objetivo sem violar as regras do problema.

    'movimentos' deve ser uma lista de tuplas (dm, dc).
    Retorna True se a sequência for válida, False caso contrário.
    """
    estado = (3, 3, 0, 0, 'E')
    objetivo = (0, 0, 3, 3, 'D')

    if verbose:
        print("Estado inicial:", estado)

    for i, mov in enumerate(movimentos, start=1):
        ok, novo_estado, erro = aplicar_movimento_validando(estado, mov)
        if not ok:
            if verbose:
                print(f"\nPasso {i}: movimento {mov} inválido.")
                print("Motivo:", erro)
                print("Estado atual:", estado)
            return False
        if verbose:
            print(f"\nPasso {i}: movimento {mov}")
            print("  ", estado, "->", novo_estado)
        estado = novo_estado

    if estado != objetivo:
        if verbose:
            print("\nSequência terminou em", estado,
                  "mas o objetivo não foi atingido.")
        return False

    if verbose:
        print("\nSequência válida: objetivo atingido sem violações.")
    return True


def extrair_movimentos(caminho):
    """
    A partir de uma lista de estados [s0, s1, ..., sn],
    retorna a lista de movimentos (dm, dc) realizados em cada passo.
    """
    movimentos = []
    for s1, s2 in zip(caminho, caminho[1:]):
        Me1, Ce1, Md1, Cd1, B1 = s1
        Me2, Ce2, Md2, Cd2, B2 = s2

        if B1 == 'E' and B2 == 'D':
            dm = Me1 - Me2
            dc = Ce1 - Ce2
        elif B1 == 'D' and B2 == 'E':
            dm = Md1 - Md2
            dc = Cd1 - Cd2
        else:
            # transição estranha (barco não trocou de margem)
            dm = 0
            dc = 0

        movimentos.append((dm, dc))
    return movimentos

