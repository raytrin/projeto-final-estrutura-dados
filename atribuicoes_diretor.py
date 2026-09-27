from arvore_binaria import ArvoreBinariaBusca


def construir_arvore_a_partir_da_lista(lista):

    arvore = ArvoreBinariaBusca()

    atual = lista.primeiro
    while atual is not None:
        arvore.insere(atual)
        atual = atual.proximo

    return arvore


def editar_pessoa(arvore, nome):
    pessoa = arvore.pesquisa(nome)

    if pessoa is None:
        print(f"\nNão encontramos {nome} na lista de espera.")
        return

    print("\nDados atuais:")
    pessoa.mostra_elemento()

    print("\nO que deseja alterar?")
    print("(1) Nome")
    print("(2) Idade")
    print("(3) Telefone")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        novo_nome = input("Novo nome: ")
        arvore.remover(pessoa.nome)
        pessoa.nome = novo_nome
        arvore.insere(pessoa)

    elif opcao == "2":
        pessoa.idade = int(input("Nova idade: "))

    elif opcao == "3":
        pessoa.telefone = input("Novo telefone: ")

    else:
        print("Opção inválida. Nada foi alterado.")
        return

    print("\nAlteração feita com sucesso!")


def descadastrar_pessoa(arvore, nome):
    pessoa = arvore.pesquisa(nome)

    if pessoa is None:
        print(f"\nNão encontramos {nome} na lista de espera.")
        return

    print("\nPessoa encontrada:")
    pessoa.mostra_elemento()

    confirmacao = input("Confirma o descadastramento? (S/N): ").strip().upper()

    if confirmacao == "S":
        arvore.remover(nome)
        print(f"\n{nome} foi descadastrado(a) com sucesso.")
    else:
        print("\nOperação cancelada.")


def exibir_primeiro_alfabetico(arvore):
    pessoa = arvore.minimo()

    if pessoa is None:
        print("\nNão há ninguém cadastrado.")
        return

    print("\nPrimeira pessoa em ordem alfabética:")
    pessoa.mostra_elemento()


def exibir_ultimo_alfabetico(arvore):
    pessoa = arvore.maximo()

    if pessoa is None:
        print("\nNão há ninguém cadastrado.")
        return

    print("\nÚltima pessoa em ordem alfabética:")
    pessoa.mostra_elemento()