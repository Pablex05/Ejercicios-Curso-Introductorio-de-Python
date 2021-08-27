if __name__ == '__main__':
    palabra_adivinar = input()
    palabra_adivinar = palabra_adivinar.upper()
    lista_letras_adivinadas = []
    j=0
    while True:
        letra = input()
        letra = letra.upper()
        for i, l in enumerate(palabra_adivinar):
            if l.lower() == letra.lower():
                lista_letras_adivinadas.insert(i, letra)
        palabra_adivinar = list(palabra_adivinar)
        j = j + 1
        if lista_letras_adivinadas == palabra_adivinar:
            break
    print(j)

"""
esta es la forma alternativa para hacer el mismo ejercicio

if __name__ == '__main__':
    palabra_adivinar = input()
    palabra_adivinar = str(palabra_adivinar.upper())
    lista_letras_adivinadas = []
    j=0
    while True:
        letra = input()
        letra = str(letra.upper())
        if letra in palabra_adivinar:
            palabra_adivinar=palabra_adivinar.replace(letra,"")
            j = j + 1
        else:
            j = j + 1

        if palabra_adivinar == "":
            break
    print(j)
"""
