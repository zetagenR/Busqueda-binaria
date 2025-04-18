def busqueda_binaria_iterativa(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1


def busqueda_binaria_recursiva(lista, objetivo, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1

    if inicio > fin:
        return -1

    medio = (inicio + fin) // 2
    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria_recursiva(lista, objetivo, medio + 1, fin)
    else:
        return busqueda_binaria_recursiva(lista, objetivo, inicio, medio - 1)


entrada = input("Ingresa una lista de números separados por comas: ")
lista_ordenada = list(map(int, entrada.replace(" ", "").split(",")))
lista_ordenada.sort()

print("Lista ordenada:", lista_ordenada)

while True:

    objetivo = int(input("¿Qué número deseas buscar? "))

    pos_iterativa = busqueda_binaria_iterativa(lista_ordenada, objetivo)
    pos_recursiva = busqueda_binaria_recursiva(lista_ordenada, objetivo)

    if pos_iterativa != -1:
        print(f"[Iterativa] El número {objetivo} está en la posición {pos_iterativa + 1}.")  # Mostramos la posición 1-based
    else:
        print(f"[Iterativa] El número {objetivo} no está en la lista.")

    if pos_recursiva != -1:
        print(f"[Recursiva] El número {objetivo} está en la posición {pos_recursiva + 1}.")  # Mostramos la posición 1-based
    else:
        print(f"[Recursiva] El número {objetivo} no está en la lista.")
    
    continuar = input("¿Quieres buscar otro número? (s/n): ").lower()
    if continuar != 's':
        print("Gracias por usar la búsqueda binaria.")
        break
