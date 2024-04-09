def uniao(lista1:list[int], lista2:list[int]) -> list[int]:
    lista_uniao = []

    for item in lista1:
        if item not in lista_uniao:
            lista_uniao.append(item)
    
    for item in lista2:
        if item not in lista_uniao:
            lista_uniao.append(item)

    return lista_uniao

lista1 = str(input("Digite os numeros da lista/conjunto 1 separados por espaco: ")).split()
lista1 = [int(i) for i in lista1]

lista2 = str(input("Agora, digite os numeros da lista/conjunto 2 separados por espaco: ")).split()
lista2 = [int(i) for i in lista2]

lista_uniao = uniao(lista1, lista2)

print("CONJUNTO UNIAO: " + str(lista_uniao))
