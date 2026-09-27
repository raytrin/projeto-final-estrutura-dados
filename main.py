from lista_encadeada import ListaEncadeada
from grafo import Grafo
import atribuicoes_secretario as secretario
import atribuicoes_diretor as diretor
import atribuicoes_assistente as assistente


def menu_secretario(lista):
    print("---------- Olá, Secretário(a)! ----------")
    while True:
        print("\n Você deseja:")
        print("(1) Cadastrar pessoa na lista de espera.")
        print("(2) Consultar pessoa cadastrada.")
        print("(3) Exibir quantidade de pessoas cadastradas.")
        print("(4) Finalizar a execução.")

        opcao = input("Digite sua opção: ")

        if opcao == "1":
            nome = input("Digite o nome da pessoa: ")
            idade = int(input("Digite a idade: "))
            telefone = input("Digite o telefone: ")
            secretario.cadastrar_pessoa(lista, nome, idade, telefone)

        elif opcao == "2":
            nome = input("Nome da pessoa a consultar: ")
            secretario.consultar_pessoa(lista, nome)

        elif opcao == "3":
            secretario.exibir_quantidade(lista)

        elif opcao == "4":
            print("\nEncerrando o atendimento do(a) secretário(a)...")
            return

        else:
            print("Opção inválida. Tente novamente.")


def menu_diretor(lista):
    print("\n---------- Olá, Diretor(a)! ----------")
    arvore = diretor.construir_arvore_a_partir_da_lista(lista)

    while True:
        print("\nVocê deseja:")
        print("(1) Alterar nome, idade ou telefone da pessoa cadastrada.")
        print("(2) Descadastrar pessoa")
        print("(3) Obter informações da primeira pessoa em ordem alfabética de nome.")
        print("(4) Obter informações da última pessoa em ordem alfabética de nome.")
        print("(5) Confirmar validade da lista de espera e finalizar execução.")

        opcao = input("Digite sua opção: ")

        if opcao == "1":
            nome = input("Nome da pessoa a editar: ")
            diretor.editar_pessoa(arvore, nome)

        elif opcao == "2":
            nome = input("Nome da pessoa a descadastrar: ")
            diretor.descadastrar_pessoa(arvore, nome)

        elif opcao == "3":
            diretor.exibir_primeiro_alfabetico(arvore)

        elif opcao == "4":
            diretor.exibir_ultimo_alfabetico(arvore)

        elif opcao == "5":
            print("\nEncerrando o atendimento do(a) diretor(a)...")
            return arvore

        else:
            print("Opção inválida. Tente novamente.")


def menu_assistente(arvore, grafo):
    print("\n---------- Olá, Assistente! ----------")

    while True:
        print("\nVocê deseja:")
        print("(1) Menor distância até a cidade de uma pessoa cadastrada")
        print("(2) Menor distância até a cidade de uma pessoa, passando por Indaiatuba")
        print("(3) Cidade mais próxima da escola com moradores cadastrados")
        print("(4) Encerrar o programa")

        opcao = input("Digite sua opção: ")

        if opcao == "1":
            nome = input("Nome da pessoa: ")
            assistente.menor_distancia_ate_pessoa(arvore, grafo, nome)

        elif opcao == "2":
            nome = input("Nome da pessoa: ")
            assistente.menor_distancia_passando_por_indaiatuba(arvore, grafo, nome)

        elif opcao == "3":
            assistente.cidade_mais_proxima_com_moradores(arvore, grafo)

        elif opcao == "4":
            print("\nEncerrando o programa. Até mais!")
            return

        else:
            print("Opção inválida. Tente novamente.")


def main():
    lista = ListaEncadeada()

    menu_secretario(lista)

    arvore = menu_diretor(lista)

    grafo = Grafo()
    menu_assistente(arvore, grafo)


if __name__ == "__main__":
    main()