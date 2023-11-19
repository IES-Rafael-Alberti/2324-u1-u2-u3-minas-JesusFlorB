import random

#Tamaño del tablero
filas = 8
columnas = 8

#Inicializamos el tablero con celdas vacias '.'
tablero = [['.' for _ in range(columnas)] for _ in range(filas)]

#Colocacion aleatoria de las minas
num_minas = 5
minas = set()

#Generacion de minas aleatorias y ocultamiento
while len(minas) < num_minas:
    fila = random.randint(0, filas - 1)
    columna = random.randint(0, columnas - 1)
    minas.add((fila, columna))

def contar_minas_adyacentes(tablero, fila, columna):
    """
    Cuenta el numero de minas adyacentes a una celda.

    Args:
        tablero (list): El tablero del juego representado como una lista de listas.
        fila (int): Indice de la fila de la celda.
        columna (int): Indice de la columna de la celda.

    Returns:
        int: Numero de minas adyacentes.
    """
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            #Verifica las celdas alrededor de la celda actual
            if 0 <= fila + i < filas and 0 <= columna + j < columnas:
                if (fila + i, columna + j) in minas:
                    count += 1
    return count

def revelar_celda(tablero, fila, columna):
    """
    Revela una celda y sus minas adyacentes si no es una mina.

    Args:
        tablero (list): El tablero del juego representado como una lista de listas.
        fila (int): Indice de la fila de la celda.
        columna (int): Indice de la columna de la celda.

    Returns:
        bool: False si la celda revelada es una mina, de lo contrario devuelve True.
    """
    if (fila, columna) in minas:
        return False  #El juego termina si el jugador ha toca una mina
    else:
        #Si no hay minas adyacentes, revela celdas vacias de forma recursiva
        minas_adyacentes = contar_minas_adyacentes(tablero, fila, columna)
        if minas_adyacentes > 0:
            tablero[fila][columna] = str(minas_adyacentes)
        else:
            tablero[fila][columna] = ' '  #Mostrar celda vacia
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= fila + i < filas and 0 <= columna + j < columnas:
                        if tablero[fila + i][columna + j] == '.':
                            revelar_celda(tablero, fila + i, columna + j)
        return True

celdas_reveladas = set()

def marcar_celda(tablero, fila, columna):
    """
    Marca una celda con una marca 'F'.

    Args:
        tablero (list): El tablero del juego representado como una lista de listas.
        fila (int): Indice de la fila de la celda.
        columna (int): Indice de la columna de la celda.
    """
    if (fila, columna) not in celdas_reveladas:
        tablero[fila][columna] = 'F'  #'F' representa una marca
        celdas_reveladas.add((fila, columna))
    else:
        print("¡La celda ya ha sido revelada!")

def verificar_victoria(tablero):
    """
    Verifica si todas las celdas sin minas han sido reveladas.

    Args:
        tablero (list): El tablero del juego representado como una lista de listas.

    Returns:
        bool: True si todas las celdas sin minas han sido reveladas, devuelve False en otro caso.
    """
    for fila in tablero:
        for celda in fila:
            if celda == '.':
                return False  #Todavia hay celdas sin revelar
    return True  #Todas las celdas sin minas han sido reveladas

def imprimir_tablero(tablero):
    """
    Imprime el tablero de juego.

    Args:
        tablero (list): El tablero del juego representado como una lista de listas.
    """
    for fila in tablero:
        print(' '.join(fila))

def jugar():
    """
    Funcion principal para jugar.
    """
    juego_terminado = False

    while not juego_terminado:
        imprimir_tablero(tablero)
        print("\nAcciones disponibles:")
        print("1. Revelar celda")
        print("2. Marcar celda")
        print("3. Salir")

        eleccion = input("Selecciona una opcion: ")

        if eleccion in ("1", "2"):
            fila = int(input("Ingresa la fila: "))
            columna = int(input("Ingresa la columna: "))
            
            if 0 <= fila < filas and 0 <= columna < columnas:
                if eleccion == "1":
                    if not revelar_celda(tablero, fila, columna):
                        print("¡Has tocado una mina! Has perdido.")
                        juego_terminado = True
                    elif verificar_victoria(tablero):
                        print("¡Felicidades! Has despejado todas las celdas sin tocar las minas.")
                        juego_terminado = True
                else:
                    marcar_celda(tablero, fila, columna)
            else:
                print("Coordenadas fuera del rango.")

        elif eleccion == "3":
            print("Saliendo del juego...")
            juego_terminado = True

        else:
            print("Seleccion invalida. Por favor, elige una opcion valida.")

if __name__ == "__main__":

    jugar()