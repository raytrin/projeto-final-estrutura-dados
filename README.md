# Sistema de Cadastro de Reserva de Estudantes

Projeto final da disciplina de **Estrutura de Dados**.

## Sobre o projeto

O sistema simula o cadastro da lista de espera de uma escola em Guarujá, SP. Três perfis de funcionário usam o sistema, nesta ordem, dentro da mesma execução , ao final do atendimento de um perfil, o sistema passa automaticamente para o próximo:

1. **Secretário(a)** — cadastra pessoas na lista de espera (nome, idade e telefone; a cidade é sorteada automaticamente a partir do arquivo de cidades), consulta uma pessoa pelo nome e exibe quantas pessoas estão cadastradas.
2. **Diretor(a)** — edita ou descadastra uma pessoa da lista, e consulta quem é a primeira e a última pessoa em ordem alfabética.
3. **Assistente** — calcula a menor distância entre a cidade da escola e a cidade de uma pessoa cadastrada (com e sem passar por uma cidade intermediária fixa) e descobre qual é a cidade mais próxima da escola que tem moradores cadastrados.

## Estruturas de dados

Cada perfil trabalha sobre uma estrutura de dados diferente, escolhida de acordo com a operação que ele precisa fazer:

| Perfil | Estrutura | Por quê |
|---|---|---|
| Secretário(a) | Lista encadeada simples | Só precisa inserir no fim; não faz busca |
| Diretor(a) | Árvore binária de busca (gerada a partir da lista, chave = nome) | Todas as operações do(a) diretor(a) envolvem busca por nome |
| Assistente | Grafo ponderado e não-direcionado (cidades e distâncias) | Todas as operações do(a) assistente envolvem menor distância entre cidades |

## Estrutura do projeto

```
main.py                      # menus e leitura de teclado (não fala direto com as estruturas de dados)
atribuicoes_secretario.py    # interface entre main.py e a lista encadeada
atribuicoes_diretor.py       # interface entre main.py e a árvore binária de busca
atribuicoes_assistente.py    # interface entre main.py e o grafo
lista_encadeada.py           # estrutura: Elemento + ListaEncadeada
arvore_binaria.py            # estrutura: No + ArvoreBinariaBusca
grafo.py                     # estrutura: Grafo (Dijkstra)
utils/
  atribui_cidade.py          # sorteia uma cidade aleatória para cada pessoa cadastrada
dados/
  cidades_vizinhas_estrutura_dados.csv   # cidades e distâncias usadas pelo grafo
```

## Dependências

- Python 3
- pandas (usado na leitura do arquivo de cidades)

## Como executar

```bash
uv run main.py
```

Ou, com o ambiente virtual ativado:

```bash
python main.py
```