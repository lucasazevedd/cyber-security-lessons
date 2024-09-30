#Mecanismos de Cadastro e Autenticação de Senhas – Entendimento Básico dos Princípios de Segurança

#COMANDO: Crie um programa em python que seja capaz de realizar o cadastramento de uma senha. A senha deve conter letras maisculas e minusculas, números e caracteres especiais. Caso a senha informada pelo usuário não atenda a esses requisitos, o usuário deve ser notificado. Em seguida, o código deve solicitar que o usuário insira sua senha novamente para validação. Caso a senha seja informada de forma errada por três tentativas, a senha deve ser bloqueada e em seguida deve encerrar o algoritmo.

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

criarSenha()