def insere_ordenada(lista: list[int], x:int) -> list:
    idx = 0

    # verifica a qual numero x eh maior para coloca-lo em sequencia
    for item in lista:
        if x > item:
            idx = lista.index(item) + 1

    nova_lista = lista[:idx] + [x] + lista[idx:]

    return nova_lista

# input de variaveis

lista_ordenada = str(input("Digite os numeros em ordem crescente, separados por espaco: ")).split()
lista_ordenada = [int(i) for i in lista_ordenada]
x = int(input("Digite o numero que quer inserir nessa lista: "))

print(insere_ordenada(lista_ordenada, x))
