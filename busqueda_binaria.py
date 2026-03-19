lista_creada = [2, 3, 5, 8, 21, 52, 63, 85]


def mostrar_encontrado(pos, valor):
    print(f"Numero encontrado en la posicion {pos} -> {valor}")


def busqueda_binaria(numero: int, lista: list[int]):
    pi = 0
    pd = len(lista) - 1
    encontrado = False
    pos = 0
    if numero == lista[pi]:
        encontrado = True
        pos = pi

    if numero == lista[pd]:
        encontrado = True
        pos = pd

    while pi <= pd and not encontrado:
        pm = (pi + pd) // 2
        if numero == lista[pm]:
            encontrado = True
            pos = pm

        elif numero > lista[pm]:
            pi = pm + 1
        else:
            pd = pm - 1

    return (encontrado, pos)


def main():
    opcion = ""
    while opcion != "salir":
        opcion = input("Deseas buscar un numero? si / salir: ").lower()
        if opcion == "si":
            numero = int(input("Ingresa el numero a buscar: "))
            encontrado, posicion = busqueda_binaria(numero, lista_creada)
            if encontrado:
                mostrar_encontrado(posicion, numero)
            else:
                print("Numero no encontrado")


main()
