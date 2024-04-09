lista = []
existe_soma = "N"

n = int(input("Digite um número inteiro e positivo para o tamanho da lista: "))
while n <= 0:  # verifica se n eh positivo
    n = int(input("[ERRO] Digite um número POSITIVO: "))

k = int(input("Digite a soma: "))

for i in range(0, n):
    num = int(input(f"Digite o numero {i+1} da sequencia: "))

    lista.append(num)

for i in range(0, len(lista)):
    for j in range(0, len(lista)):
        if lista[i] + lista[j] == k and i != j:  # evita contar o mesmo numero duas vezes
            existe_soma = "S"

print(existe_soma)
