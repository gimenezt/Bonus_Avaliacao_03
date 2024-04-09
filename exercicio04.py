def interseccao(lista1:list[int], lista2:list[int]) -> list[int]:
    lista_intersec = []

    for i in range(0, len(lista1)):
        for j in range(0, len(lista2)):
            if lista1[i] == lista2[j]:
                lista_intersec.append(lista1[i])

    return lista_intersec

lista1 = str(input("Digite os numeros da lista/conjunto 1 separados por espaco: ")).split()
lista1 = [int(i) for i in lista1]

lista2 = str(input("Agora, digite os numeros da lista/conjunto 2 separados por espaco: ")).split()
lista2 = [int(i) for i in lista2]

lista_intersec = interseccao(lista1, lista2)

if len(lista_intersec)>0:
    print("INTERSECCAO:" + str(lista_intersec))
else:
    print("Nao ha interseccao entre as listas/conjuntos.")