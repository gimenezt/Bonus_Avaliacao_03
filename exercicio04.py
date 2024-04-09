def interseccao(lista1:list[int], lista2:list[int]) -> list[int]:
    lista_intersec = []

    for num in lista1: 
        if num in lista2: # se o numero existir na outra lista, adiciona
            lista_intersec.append(num)

    return lista_intersec

lista1 = str(input("Digite os numeros da lista/conjunto 1 separados por espaco: ")).split()
lista1 = [int(i) for i in lista1] # transformando itens em int

lista2 = str(input("Agora, digite os numeros da lista/conjunto 2 separados por espaco: ")).split()
lista2 = [int(i) for i in lista2] # transformando itens em int

lista_intersec = interseccao(lista1, lista2)

if len(lista_intersec)>0:
    print("INTERSECCAO:" + str(lista_intersec))
else: # tratatia para lista vazia
    print("Nao ha interseccao entre as listas/conjuntos.")
