# COMANDO: Para realizar esta tarefa, você precisa ter feito o TDE 3. Escreva para mim um programa em linguagem de programação em python, que leia um arquivo de texto. O programa deve selecionar uma das senhas como sendo a senha que desbloqueia o sistema. Após isso, o usuário deve insirir senhas aleatorias contidas no arquivo de texto para tentar entrar no sistema, e se após 3 tentativas a senha inserida não for a mesma senha que o programa escolheu,  o algoritmo deve iniciar o Brute Force solicitando as permissões do usuário e em seguida imprimir a senha que ele elegeu na tela do computador. Após isso, o usuário deve Insira a senha fornecida, e se a senha fornecida for a senha correta, o programa deve exibir a mensagem: “Acesso liberado!”. Após três tentativas erradas, o programa deve ser encerrado.

import os
import random

# Caminho do arquivo
nome_arquivo = "desafio04/senhas.txt"

# Lê as senhas do arquivo e guarda em uma lista
with open(nome_arquivo, "r") as arquivo:
    senhas = arquivo.readlines()

senhas = [senha.strip() for senha in senhas]

# Escolhe uma senha aleatória
senha_master = random.choice(senhas)

i = 0
j = 0

while i < 3:
    senha = str(input('\nDigite a senha: '))
    if senha != senha_master:
        i += 1
        print("\nSenha incorreta, tente novamente.")
    else:
        print("\nAcesso liberado!")
        break

permissao = input("\nPermitir tentativa de brute force? (s/n): ").strip().lower()
if permissao != 's':
    print("\nPermissão negada. O programa será encerrado.")
    exit()
else:
    for i, tentativa in enumerate(senhas, start=1):
        if tentativa != senha_master:
            i += 1
            print(f"tentativa {i - 1}")
        else:
            print(f"\nSenha quebrada: {tentativa}")
            while j < 3:
                senha = str(input('Digite a senha: '))
                if senha != senha_master:
                    j += 1
                    print("\nSenha incorreta, tente novamente.")
                else:
                    print("\nAcesso liberado!")
                    break
            else:
                print("\nTentativas esgotadas. O programa será encerrado.")
                break
