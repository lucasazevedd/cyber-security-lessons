# Simulado I: Trabalhando com números primos
# aluno: Lucas Israel de Azevedo

# Primeiro Passo: Escreva um programa em linguagem de programação em Python que mostre todos os número primos de 0 à 99.

chave_publica = 6319
num_primos = []

def verificadorPrimos(num):
    if num < 2:
        return False #Números menores que 2 não podem ser primos.
    i = 2 
    while i * i <= num: #Verifica os números com base na Raiz do número (√num)
        if num % i == 0:
            return False #Se encontrarmos uma divisão que resulte em um número inteiro (resto da divisão = 0) esse número não é primo.
        i += 1 #Continua a verificação até encontrar um divisor
    return True

def descobridorPrimos(a, b):
    for numero in range(a, b): #Verifica todos os números entre 2 e 99
        if verificadorPrimos(numero):
            num_primos.append(numero)

#Segundo Passo: Em seguida, descubra quais número P e Q (estes números funcionam como chave privada), que multiplicados resultem em 6319 (Este número funciona como chave pública)

def decriptador(list):
    for p in range(len(list)): #Loop para testar as combinações dos números primos encontrados entre 1 e 100
        for q in range(p, len(list)):
            if list[p] * list[q] == chave_publica:
                print(f"{list[p]} * {list[q]} = {chave_publica}")

descobridorPrimos(1,100)
decriptador(num_primos)