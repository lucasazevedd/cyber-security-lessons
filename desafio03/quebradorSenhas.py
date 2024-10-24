# COMANDO: Crie em linguagem de programação python um programa. Esse algoritmo deve gerar, aleatoriamente um arquivo de texto contendo 200 senhas aleatórias. As senhas devem conter: Letras Maiúsculas, minúsculas, números, e caracteres especiais. Cada senha deve ter 12 caracteres. O algoritmo deve solicitar permissões para criar o arquivo e salvar o mesmo na pasta dowloads do computador. O arquivo criado deve se chamar "senhas.txt".

# Requisitos:
    # 12 caracteres;
    # Letras maiúsculas;
    # Letras minúsculas;
    # Números;
    # Caracteres especiais.

import random
import os

# organizando os caracteres por tipo
maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
caracteres_especiais = '!@#$%^&*()-_=+[]{}|;:,.<>?/'

todos_caracteres = maiusculas + minusculas + numeros + caracteres_especiais # junta todos os tipos de caracteres

def geradorSenhas():
    # gera uma senha utilizando todos_caracteres
    senha = ''.join(random.choice(todos_caracteres) for n in range(12))
    return senha    

def verificadorSenhas(senha):
    # condição que valida que a senha tenha todos os requisitos propostos
    if (any(c in maiusculas for c in senha) and 
        any(c in minusculas for c in senha) and 
        any(c in numeros for c in senha) and 
        any(c in caracteres_especiais for c in senha)):
        return True # se a senha atender aos requisitos
    else:
        return False # se a senha não atender aos requisitos

# Permissão para salvar as senhas no computador do usuário
permissao = input("Deseja criar o arquivo de senhas na pasta Downloads? (s/n): ")

if permissao.lower() in ['s', 'sim']:
    pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    caminho_arquivo = os.path.join(pasta_downloads, "senhas.txt")
    with open(caminho_arquivo, 'w') as arquivo:
        # loop para gerar 200 senhas
        i = 0
        while i < 200:
            senha = geradorSenhas() # gera as senhas
            while not verificadorSenhas(senha):  # gera uma nova senha até atender aos critérios
                senha = geradorSenhas()

            # Escreve a senha no arquivo
            arquivo.write(senha + '\n')
            i += 1

    print(f"Arquivo 'senhas.txt' criado com sucesso na pasta Downloads.")
else:
    print("Criação de arquivo cancelada.")