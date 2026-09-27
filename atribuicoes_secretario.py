def cadastrar_pessoa(lista, nome, idade, telefone):
    lista.inserir_fim(nome, idade, telefone)
    print(f"\n{nome} cadastrado(a) com sucesso! Lista atual:")
    lista.mostrar_lista()


def consultar_pessoa(lista, nome):
    pessoa = lista.busca_por_nome(nome)

    if pessoa is None:
        print(f"\nNão encontramos {nome} na lista de espera.")
        return

    print("\nPessoa encontrada:")
    pessoa.mostra_elemento()


def exibir_quantidade(lista):
    print(f"\nTemos {lista.tamanho_lista()} pessoa(s) cadastrada(s) na lista de espera.")