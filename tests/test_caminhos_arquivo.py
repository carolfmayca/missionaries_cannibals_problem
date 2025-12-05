from pathlib import Path

from canibais.main import carregar_caminho_de_arquivo
from canibais.validator import extrair_movimentos, verificar_sequencia

BASE_DIR = Path(__file__).parent
EXEMPLOS_DIR = BASE_DIR / "exemplos"


def test_caminho_valido_txt():
    caminho_arquivo = EXEMPLOS_DIR / "caminho_valido.txt"
    caminho = carregar_caminho_de_arquivo(str(caminho_arquivo))

    assert caminho is not None
    movimentos = extrair_movimentos(caminho)
    assert verificar_sequencia(movimentos, verbose=False)


def test_caminho_parcial_nao_atinge_objetivo():
    caminho_arquivo = EXEMPLOS_DIR / "caminho_parcial_sem_objetivo.txt"
    caminho = carregar_caminho_de_arquivo(str(caminho_arquivo))

    assert caminho is not None
    movimentos = extrair_movimentos(caminho)
    assert not verificar_sequencia(movimentos, verbose=False)


def test_caminho_invalido_seguranca():
    caminho_arquivo = EXEMPLOS_DIR / "caminho_invalido_seguranca.txt"
    caminho = carregar_caminho_de_arquivo(str(caminho_arquivo))

    # se o arquivo estiver bem formado, o loader devolve algo
    assert caminho is not None

    movimentos = extrair_movimentos(caminho)
    # deve falhar em algum ponto (regra de segurança, etc.)
    assert not verificar_sequencia(movimentos, verbose=False)
