n = input("Digite um numero inteiro e positivo para o tamanho da sequencia: ")
lista = []

while not isinstance(n, int): # verifica se n eh int
    n = input("[ERRO] Digite um numero INTEIRO: ")

while n <= 0: # verifica se n eh positivo
    n = input("[ERRO] Digite um numero POSITIVO: ")

for i in range(0, n):
    num = input("Digite o numero {} da sequencia: ".format(i+1))

    while not isinstance(n, int): # verifica o num eh int
        num = input("[ERRO] Digite um numero INTEIRO: ")

    lista.append(num)

# logica para tirar numeros repetidos
i = 0
while i < len(lista):
    j = i + 1 
    while j < len(lista):
        if lista[i] == lista[j]: # verificando se ha algum elemento repetido posteriormente
            lista.pop(j) 
        else:
            j += 1
    i += 1

lista.sort()

for each_num in lista:
    print(each_num)
