""" las elecciones """


def funcion(lista):
    return {i: lista.count(i) for i in lista_candidatos}


if __name__ == '__main__':
    lista_candidatos = []
    cantidad_de_votos = int(input("ingrese la cantidad votos totales: "))

    for i in range(cantidad_de_votos):
        lista_candidatos.append(input("ingrese el nombre del candidato seleccionado: "))

    resultado = funcion(lista_candidatos)
    maximo = max(resultado, key=resultado.get)
    print(maximo)
