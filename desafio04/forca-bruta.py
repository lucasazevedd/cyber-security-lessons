# COMANDO: Para realizar esta tarefa, você precisa ter feito o TDE 3. Escreva para mim um programa em linguagem de programação em python, que leia um arquivo de texto. O programa deve selecionar uma das senhas como sendo a senha que desbloqueia o sistema. Após isso, o usuário deve insirir senhas aleatorias contidas no arquivo de texto para tentar entrar no sistema, e se após 3 tentativas a senha inserida não for a mesma senha que o programa escolheu,  o algoritmo deve iniciar o Brute Force solicitando as permissões do usuário e em seguida imprimir a senha que ele elegeu na tela do computador. Após isso, o usuário deve Insira a senha fornecida, e se a senha fornecida for a senha correta, o programa deve exibir a mensagem: “Acesso liberado!”. Após três tentativas erradas, o programa deve ser encerrado.

# Certifique-se de que o arquivo 'senhas.txt' está na mesma pasta deste programa.
# O arquivo deve conter uma senha por linha.

import os
import random
import sys

# Obter o diretório do script atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Caminho do arquivo
nome_arquivo = os.path.join(diretorio_atual, "senhas.txt")

# Verifica se o arquivo existe;
if not os.path.exists(nome_arquivo):
    print("\nArquivo 'senhas.txt' não encontrado.")
    sys.exit(1)

# Lê as senhas do arquivo e guarda em uma lista
with open(nome_arquivo, "r") as arquivo:
    senhas = [senha.strip() for senha in arquivo.readlines()]

# Escolhe uma senha aleatória
senha_master = random.choice(senhas)

# Número máximo de tentativas
tentativas_permitidas = 3

# Fase 1: Tentativas do usuário
for tentativa in range(1, tentativas_permitidas + 1):
    senha = input("\nDigite a senha: ")
    if senha == senha_master:
        print("\nAcesso liberado!")
        exit()
    else:
        print(f"\nSenha incorreta. Tentativa {tentativa} de {tentativas_permitidas}.")

# Permissão para brute force
permissao = input("\nPermitir tentativa de brute force? (s/n): ").strip().lower()
if permissao != 's':
    print("\nPermissão negada. O programa será encerrado.")
    exit()

# Fase 2: Brute force
print("\nIniciando brute force...")
for tentativa in senhas:
    print(f"Tentando: {tentativa}")
    if tentativa == senha_master:
        print(f"\nSenha quebrada: {tentativa}")
        break

# Fase 3: Última tentativa com a senha quebrada
for tentativa in range(1, tentativas_permitidas + 1):
    senha = input("\nDigite a senha fornecida: ")
    if senha == senha_master:
        print("\nAcesso liberado!")
        exit()
    else:
        print(f"\nSenha incorreta. Tentativa {tentativa} de {tentativas_permitidas}.")

print("\nTentativas esgotadas. O programa será encerrado.")
