# Problema dos Missionários e Canibais

Este projeto implementa uma solução para o clássico problema dos Missionários e Canibais usando algoritmos de busca em grafos.

## Descrição do Problema

Três missionários e três canibais precisam atravessar um rio usando um barco que comporta no máximo 2 pessoas. A regra de segurança é que em nenhuma margem os canibais podem ser maioria em relação aos missionários (senão eles os devorariam).

### Regras

- 3 missionários e 3 canibais inicialmente na margem esquerda
- Barco comporta 1 ou 2 pessoas
- Em qualquer margem: se há missionários, eles devem ser >= canibais
- Objetivo: levar todos para a margem direita

## Estrutura do Projeto

```
missionaries_cannibals_problem/
├── canibais/
│   ├── __init__.py
│   ├── core.py          # Algoritmo BFS e lógica principal
│   ├── main.py          # Script principal de execução
│   └── validator.py     # Validação de movimentos e caminhos
├── tests/
│   ├── test_core.py     # Testes do algoritmo principal
│   ├── test_validator.py # Testes de validação
│   ├── test_caminhos_arquivo.py # Testes de leitura de arquivos
│   └── exemplos/        # Arquivos de exemplo para testes
├── pytest.ini          # Configuração do pytest
└── README.md           # Este arquivo
```

## Representação do Estado

Cada estado é representado como uma tupla `(Me, Ce, Md, Cd, B)`:

- `Me`: Missionários na margem esquerda
- `Ce`: Canibais na margem esquerda  
- `Md`: Missionários na margem direita
- `Cd`: Canibais na margem direita
- `B`: Posição do barco ('E' = esquerda, 'D' = direita)

### Exemplo

- Estado inicial: `(3, 3, 0, 0, 'E')`
- Estado objetivo: `(0, 0, 3, 3, 'D')`

## Como Usar

### 1. Encontrar Solução Automaticamente

```bash
python3 -c "from canibais.core import bfs_missionarios_canibais; print(bfs_missionarios_canibais())"
```

### 2. Validar Caminho de Arquivo

```bash
python3 canibais/main.py caminho_para_arquivo.txt
```

O arquivo deve conter um estado por linha no formato: `Me,Ce,Md,Cd,B`

Exemplo de arquivo:

```
3,3,0,0,E
3,1,0,2,D
3,2,0,1,E
3,0,0,3,D
1,0,2,3,E
0,0,3,3,D
```

## Movimentos Permitidos

O barco pode transportar:

- `(1, 0)`: 1 missionário
- `(0, 1)`: 1 canibal  
- `(2, 0)`: 2 missionários
- `(0, 2)`: 2 canibais
- `(1, 1)`: 1 missionário e 1 canibal

## Algoritmo

A solução usa **Busca em Largura (BFS)** para encontrar o caminho mais curto:

1. Inicia do estado `(3, 3, 0, 0, 'E')`
2. Gera todos os sucessores válidos (movimentos que mantêm segurança)
3. Continua até encontrar o estado objetivo `(0, 0, 3, 3, 'D')`
4. Reconstrói o caminho usando o mapeamento de estados pais

## Executar Testes

```bash
# Instalar pytest se necessário
pip install pytest

# Executar todos os testes
pytest

# Executar testes com verbosidade
pytest -v

# Executar teste específico
pytest tests/test_core.py::test_bfs_encontra_solucao
```

### Exemplos de Teste Disponíveis

- `caminho_valido.txt`: Caminho completo e válido
- `caminho_parcial_sem_objetivo.txt`: Caminho que não atinge o objetivo
- `caminho_invalido_seguranca.txt`: Caminho que viola regras de segurança

## Funcionalidades

### Módulo `core.py`

- `bfs_missionarios_canibais()`: Encontra solução usando BFS
- `sucessores(estado)`: Gera estados sucessores válidos
- `estado_seguro()`: Verifica se um estado respeita as regras

### Módulo `validator.py`

- `aplicar_movimento_validando()`: Aplica movimento com validação
- `extrair_movimentos()`: Extrai movimentos de uma sequência de estados
- `verificar_sequencia()`: Valida uma sequência completa

### Módulo `main.py`

- `carregar_caminho_de_arquivo()`: Lê estados de arquivo
- Script principal para validar caminhos externos
