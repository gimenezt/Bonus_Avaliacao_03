def insere_ordenada(lista: list[int], x:int) -> list:
    idx = 0

    # encontra o idx correto para inserção
    while idx < len(lista) and x > lista[idx]:
        idx += 1

    nova_lista = lista[:idx] + [x] + lista[idx:]

    return nova_lista

# input de variaveis

lista_ordenada = str(input("Digite os numeros em ordem crescente, separados por espaco: ")).split()
lista_ordenada = [int(i) for i in lista_ordenada]
x = int(input("Digite o numero que quer inserir nessa lista: "))

print(insere_ordenada(lista_ordenada, x))
