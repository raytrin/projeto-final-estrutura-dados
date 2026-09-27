CIDADE_ESCOLA = "Guarujá"
CIDADE_INTERMEDIARIA = "Indaiatuba"


def _mostra_caminho(caminho, distancia):
    print("Caminho: " + " -> ".join(caminho))
    print(f"Distância total: {distancia} km")


def menor_distancia_ate_pessoa(arvore, grafo, nome):
    pessoa = arvore.pesquisa(nome)

    if pessoa is None:
        print(f"\nNão encontramos {nome} na lista de espera.")
        return

    caminho, distancia = grafo.caminho_minimo(CIDADE_ESCOLA, pessoa.cidade)

    if caminho is None:
        print(f"\nNão existe caminho até {pessoa.cidade} no grafo de cidades.")
        return

    print("\nPessoa encontrada:")
    pessoa.mostra_elemento()
    _mostra_caminho(caminho, distancia)


def menor_distancia_passando_por_indaiatuba(arvore, grafo, nome):
    pessoa = arvore.pesquisa(nome)

    if pessoa is None:
        print(f"\nNão encontramos {nome} na lista de espera.")
        return

    caminho, distancia = grafo.caminho_minimo_passando_por(
        CIDADE_ESCOLA, CIDADE_INTERMEDIARIA, pessoa.cidade
    )

    if caminho is None:
        print(f"\nNão existe caminho até {pessoa.cidade} passando por {CIDADE_INTERMEDIARIA}.")
        return

    print("\nPessoa encontrada:")
    pessoa.mostra_elemento()
    _mostra_caminho(caminho, distancia)


def cidade_mais_proxima_com_moradores(arvore, grafo):
    pessoas = arvore.lista_em_ordem()

    if not pessoas:
        print("\nNão há ninguém cadastrado.")
        return

    distancias = grafo.todas_as_distancias(CIDADE_ESCOLA)
    cidades_com_moradores = {pessoa.cidade for pessoa in pessoas}
    cidade_mais_proxima = min(
        cidades_com_moradores,
        key=lambda cidade: distancias.get(cidade, float("inf")),
    )
    distancia = distancias[cidade_mais_proxima]

    print(f"\nCidade mais próxima com moradores cadastrados: {cidade_mais_proxima}")
    print(f"Distância até a escola: {distancia} km")

    print("\nMoradores nessa cidade:")
    for pessoa in pessoas:
        if pessoa.cidade == cidade_mais_proxima:
            pessoa.mostra_elemento()