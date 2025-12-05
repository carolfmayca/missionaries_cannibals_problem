from canibais.core import estado_seguro, bfs_missionarios_canibais, sucessores


def test_estado_seguro_basico():
    # estados clássicos
    assert estado_seguro(3, 3, 0, 0)
    assert estado_seguro(0, 0, 3, 3)

    # missionários em minoria na esquerda
    assert not estado_seguro(1, 2, 2, 1)
    # missionários em minoria na direita
    assert not estado_seguro(2, 1, 1, 2)


def test_bfs_encontra_objetivo():
    caminho = bfs_missionarios_canibais()
    assert caminho is not None
    assert caminho[0] == (3, 3, 0, 0, 'E')
    assert caminho[-1] == (0, 0, 3, 3, 'D')


def test_sucessores_do_estado_inicial():
    estado_inicial = (3, 3, 0, 0, 'E')
    succ = sucessores(estado_inicial)

    # todos os sucessores precisam ser seguros
    assert all(estado_seguro(*s[:4]) for s in succ)

    # do estado inicial, existem três sucessores válidos
    assert set(succ) == {
        (3, 1, 0, 2, 'D'),  # 2 canibais
        (3, 2, 0, 1, 'D'),  # 1 canibal  
        (2, 2, 1, 1, 'D'),  # 1 missionário e 1 canibal
    }
