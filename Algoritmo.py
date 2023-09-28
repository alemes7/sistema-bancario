from Classes import *

import os
import time

def menu_inicial():
    print('Bem-vindo ao Sistema Bancário')
    print("1. Fazer login")
    print("2. Adicionar cliente")
    print("3. Sair")

def menu_principal(cliente_logado):
    print(f"Menu Principal - Cliente: {cliente_logado.nome}")
    print("1. Remover conta")
    print("2. Atualizar cadastro")
    print("3. Transferência entre clientes")
    print("4. Saque")
    print("5. Depósito")
    print("6. Logout")

def main():
    sistema = SistemaBancario()

    while True:
        limpar_terminal()
        menu_inicial()
        op_inicial = input('Escolha uma opção: ')
        
        if op_inicial == '1':
            limpar_terminal()
            cpf = input("Digite o CPF do cliente: ")
            
            if cpf in sistema.clientes:
                cliente_logado = sistema.clientes[cpf]
                cliente_logado.logar()
                
                while cliente_logado.logado:
                    limpar_terminal()
                    menu_principal(cliente_logado.cliente)
                    op_principal = input('Escolha uma opção: ')
                    
                    if op_principal == '1':
                        limpar_terminal()
                        limpar_terminal()
                        cliente_logado.cliente.excluir_cliente(sistema)
                        cliente_logado.logout()
                        parar()
                    elif op_principal == '2':
                        limpar_terminal()
                        novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
                        novo_cpf = input("Digite o novo CPF (ou pressione Enter para manter o atual): ")
                        cliente_logado.cliente.atualizar_cadastro(novo_nome, novo_cpf)
                        parar()
                    elif op_principal == '3':
                        limpar_terminal()
                        cpf_destino = input("Digite o CPF do cliente de destino: ")
                        cliente_destino = sistema.buscar_cliente(cpf_destino)
                        
                        if cliente_destino:
                            valor = float(input("Digite o valor da transferência: "))
                            cliente_logado.cliente.transferencia(cliente_destino, valor)
                        parar()
                    elif op_principal == '4':
                        limpar_terminal()
                        valor = float(input("Digite o valor do saque: "))
                        cliente_logado.cliente.saque(valor)
                        parar()
                    elif op_principal == '5':
                        limpar_terminal()
                        valor = float(input("Digite o valor do depósito: "))
                        cliente_logado.cliente.deposito(valor)
                        parar()
                    elif op_principal == '6':
                        cliente_logado.logout()
                    else:
                        print('Opção inválida\nEscolha uma opção válida.')
                        parar()
            else:
                print('Login falhou.\nCliente não encontrado.')
        elif op_inicial == '2':
            limpar_terminal()
            nome = input('Digite o nome do cliente: ')
            cpf = input('Digite o CPF do cliente: ')
            cliente = Cliente(nome, cpf)
            sistema.add_cliente(cliente)
            parar()
        elif op_inicial == '3':
            print('Saindo do sistema.\nAté logo')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')
            parar()