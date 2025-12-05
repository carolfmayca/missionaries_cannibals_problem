# canibais/cli.py
import sys
from core import bfs_missionarios_canibais
from validator import extrair_movimentos, verificar_sequencia


def carregar_caminho_de_arquivo(caminho_arquivo):
    """
    Lê um caminho (lista de estados) de um arquivo.
    Cada linha deve ter: Me,Ce,Md,Cd,B
    Exemplo: 3,3,0,0,E
    """
    caminho = []

    try:
        with open(caminho_arquivo, 'r') as f:
            for i, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue

                parts = line.split(',')
                if len(parts) != 5:
                    print(f"[Linha {i}] Formato inválido: {line}")
                    continue

                Me, Ce, Md, Cd, B = parts

                try:
                    estado = (int(Me), int(Ce), int(Md), int(Cd), B)
                    caminho.append(estado)
                except ValueError:
                    print(f"[Linha {i}] Valores inválidos: {line}")

        if not caminho:
            print("Nenhum estado válido encontrado no arquivo.")
            return None

        return caminho

    except FileNotFoundError:
        print(f"Arquivo '{caminho_arquivo}' não encontrado.")
        return None


def main():
    if len(sys.argv) == 1:
        print("Nenhum arquivo fornecido. Executando BFS para encontrar solução...\n")
        caminho = bfs_missionarios_canibais()
    else:
        arquivo = sys.argv[1]
        print(f"Lendo caminho do arquivo: {arquivo}\n")
        caminho = carregar_caminho_de_arquivo(arquivo)

    if caminho is None:
        print("Não foi possível obter um caminho válido.")
        return

    print("Caminho de estados:")
    print("  (Me, Ce, Md, Cd, B)")
    for s in caminho:
        print(" ", s)

    movimentos = extrair_movimentos(caminho)

    print("\nMovimentos extraídos (Missionários,Canibais):")
    print(movimentos)

    print("\nVerificando sequência de movimentos...")
    ok = verificar_sequencia(movimentos, verbose=True)

    print("\nResultado da verificação:", ok)


if __name__ == "__main__":
    main()
