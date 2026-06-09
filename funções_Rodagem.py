# importa a conexão com o banco
from chamar_banco import *

# importa as funções do sistema
from funções_ação import *


# pergunta se o usuário deseja continuar no sistema
def continuar_a_repetir_menu():

    escolha = input("\nDeseja continuar? (s/n): ").lower()

    # continua no menu
    if escolha == "s":

        return True

    # encerra o sistema
    elif escolha == "n":

        print("Sistema encerrado.")
        return False

    # impede respostas inválidas
    else:

        print("Escolha sim ou não!")
        return continuar_a_repetir_menu()


# função principal do sistema
def menu():

    continuar = True

    # mantém o menu funcionando
    while continuar:

        # exibe as opções disponíveis
        print("\n=== SISTEMA SCPTI ===")
        print("1 - Cadastrar usuário")
        print("2 - Registrar solicitação")
        print("3 - Encaminhar solicitação")
        print("4 - Concluir solicitação")
        print("5 - Ver histórico")
        print("6 - Ver estatísticas")
        print("0 - Sair")

        # recebe a opção escolhida
        op = input("\nEscolha: ")

        # cadastra novo usuário
        if op == "1":

            cadastrar_usuario()
            continuar = continuar_a_repetir_menu()

        # registra nova solicitação
        elif op == "2":

            registrar_solicitacao()
            continuar = continuar_a_repetir_menu()

        # encaminha solicitação para técnico
        elif op == "3":

            encaminhar_solicitacao()
            continuar = continuar_a_repetir_menu()

        # conclui atendimento
        elif op == "4":

            concluir_solicitacao()
            continuar = continuar_a_repetir_menu()

        # mostra histórico de solicitações
        elif op == "5":

            ver_historico()
            continuar = continuar_a_repetir_menu()

        # exibe estatísticas do sistema
        elif op == "6":

            estatisticas()
            continuar = continuar_a_repetir_menu()

        # encerra o sistema
        elif op == "0":

            print("Sistema encerrado.")
            break

        # impede opções inválidas
        else:

            print("Opção inválida!")


# inicia o sistema
menu()
