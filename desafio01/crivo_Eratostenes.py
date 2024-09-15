# Crivo de Eratóstenes

# Inicializando as listas
list_to_check = list(range(2, 100))  # Números de 2 a 99
primos_list = []  # Para armazenar os números primos
non_primos_list = [False] * len(list_to_check)  # Marca não primos como True

def CrivodeEratostenes():
    for i in range(len(list_to_check)):
        if not non_primos_list[i]:  # Se o número não foi marcado como não primo
            primos_list.append(list_to_check[i])  # Adiciona à lista de primos
            for multiple in range(list_to_check[i] * 2, 100, list_to_check[i]):
                if multiple in list_to_check:
                    non_primos_list[list_to_check.index(multiple)] = True  # Marca os múltiplos como não primos

CrivodeEratostenes()

print("Números primos:", primos_list)