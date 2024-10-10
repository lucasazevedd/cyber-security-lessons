# Requisitos: Após o cadastramento bem-sucedido da senha no TDE 1, o sistema deverá solicitar que o usuário altere sua senha. O sistema deve pedir que o usuário informe a senha atual antes de permitir a alteração. Caso a senha atual seja inserida corretamente, o sistema deverá liberar a alteração da senha. O novo processo de autenticação deverá seguir as mesmas regras de validação estabelecidas no TDE 1 (letras maiúsculas, minúsculas, números e caracteres especiais). Se o usuário informar a senha incorreta por três tentativas consecutivas, o sistema deverá bloquear o processo e encerrar, como no TDE 1. Assim como na etapa anterior, é fundamental garantir a proteção dos dados de autenticação durante todo o processo, impedindo a exposição das senhas e assegurando a integridade do sistema.

# COMANDO: Aproveitando o código do TDE 1, implemente a próxima etapa. Após a senha ser cadastrada com sucesso, o algoritmo deve solicitar que o usúario altere a sua senha para fazer login. Se a senha informada for a senha correta, ele deve liberar o acesso, caso contrário deve bloquear as tentativas, conforme feito anteriormente no TDE1.

import re

def criarSenha(): #Cria a senha e chama as outras funções para validar e autenticar
    print('\nVamos definir sua senha agora.')
    print('Sua senha deve conter:\n - Letras Maiúsculas e Minúsculas; \n - Números; \n - Caracteres Especias(!@#$%&*()_\-+=\[\]{}|\\:;\'",.<>?/)')
    while True:
        senha = input('Insira sua Senha: \n')
        mensagem_erro = validarSenha(senha)
        
        if mensagem_erro:
            print(mensagem_erro)
        else:
            print('Senha cadastrada com sucesso!')
            autenticarSenha(senha)
            alterarSenha(senha)
            break

def validarSenha(senha): #valida se a Senha possui todos os requisitos necessários
    if not re.search(r'[A-Z]', senha):
        return "\nA senha precisa conter pelo menos uma letra maiúscula."
    if not re.search(r'[a-z]', senha):
        return "\nA senha precisa conter pelo menos uma letra minúscula."
    if not re.search(r'[0-9]', senha):
        return "\nA senha precisa conter pelo menos um número."
    if not re.search(r'[!@#$%^&*()_\-+=\[\]{}|\\:;\'",.<>?/]', senha):
        return "\nA senha precisa conter pelo menos um caractere especial."
    return None

def autenticarSenha(senha): #verifica se o usuário vai escrever corretamente a senha em no máximo de 3 tentativas
    print('\nVamos validar sua senha... ')
    tentativas = 0

    while tentativas < 3:
        senha_login = input('Digite sua senha: ')
        
        if senha_login != senha:
            tentativas += 1
            print(f'\nSenha incorreta. Você tem mais {3 - tentativas} tentativas.')
        else:
            print('\nSenha correta! Usuário logado com sucesso!')
            return
        
    print('\nNúmero de tentativas excedido. Senha bloqueada.')

def alterarSenha(senha): # Solicita alteração da senha após validação da senha atual
    print('\nVamos alterar sua senha agora.')
    tentativas = 0

    while tentativas < 3:
        senha_atual = input('Digite sua senha atual: ')

        if senha_atual != senha:
            tentativas += 1
            print(f'\nSenha incorreta. Você tem mais {3 - tentativas} tentativas.')
        else:
            while True:
                nova_senha = input('Digite sua nova senha: ')
                mensagem_erro = validarSenha(nova_senha)

                if mensagem_erro:
                    print(mensagem_erro)
                else:
                    print('Nova senha cadastrada com sucesso!')
                    autenticarSenha(nova_senha)
                    return
            
    print('\nNúmero de tentativas excedido. O processo de alteração de senha foi bloqueado.')
            


criarSenha()