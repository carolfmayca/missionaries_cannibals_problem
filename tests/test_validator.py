from canibais.validator import (
    aplicar_movimento_validando,
    verificar_sequencia,
)
from canibais.core import bfs_missionarios_canibais


def test_movimento_barco_vazio_invalido():
    estado = (3, 3, 0, 0, 'E')
    ok, _, msg = aplicar_movimento_validando(estado, (0, 0))
    assert not ok
    assert "Barco não pode mover vazio" in msg


def test_verificar_sequencia_valida_da_bfs():
    caminho = bfs_missionarios_canibais()

    # extrai movimentos como no extrair_movimentos
    movimentos = []
    for s1, s2 in zip(caminho, caminho[1:]):
        Me1, Ce1, Md1, Cd1, B1 = s1
        Me2, Ce2, Md2, Cd2, B2 = s2

        if B1 == 'E' and B2 == 'D':
            dm = Me1 - Me2
            dc = Ce1 - Ce2
        else:
            dm = Md1 - Md2
            dc = Cd1 - Cd2

        movimentos.append((dm, dc))

    assert verificar_sequencia(movimentos, verbose=False)


def test_verificar_sequencia_claramente_invalida():
    # tenta levar 3 missionários de uma vez
    movimentos = [(3, 0)]
    assert not verificar_sequencia(movimentos, verbose=False)
