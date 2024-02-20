def imprimir_sudoku(sudoku): # Funcion para imprimir lineas al sudoku
    for i in range(9): # Hace el recorrido de manera horizontal
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(9): # Hace el recorrido de manera vertical
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            print(sudoku[i][j], end=" ") # Imprime las lines de manera vertical y horizontal
        print()


def espacios_vacios_sudoku(sudoku): # Funcion para determinar los espacios vacios, en este caso el 0
    for i in range(9):  # Hace el recorrido de manera horizontal
        for j in range(9): # Hace el recorrido de manera vertical
            if sudoku[i][j] == 0:
                return i, j # Retorna ambas variables
    return None, None


def validacion_sudoku(sudoku, fila, columna, num): # Funcion para verificar si el número ya está en la fila
    if num in sudoku[fila]:
        return False

    if num in [sudoku[i][columna] for i in range(9)]: # Verifica si el número ya está en la columna
        return False

    inicio_fila, inicio_columna = 3 * (fila // 3), 3 * (columna // 3) # Verificar si el número ya está en el bloque
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_columna, inicio_columna + 3):
            if sudoku[i][j] == num: # Retorna False si el numero se encuentra en el bloque
                return False

    return True # Retorna True si el numero no se encuentra en el bloque


def resolver_sudoku(sudoku): # Funcion para empezar a llenar el sudoku
    fila, columna = espacios_vacios_sudoku(sudoku) # carga las filas y columnas para ver cuales estan vacios

    if fila is None and columna is None: # Valida si no hay espacios vacíos
        return True # Retorna un True si el sudoku está resuelto

    for num in range(1, 10):
        if validacion_sudoku(sudoku, fila, columna, num): # Coloca el número
            sudoku[fila][columna] = num

            if resolver_sudoku(sudoku): # Llamada recursiva para el siguiente espacio vacío
                return True

            sudoku[fila][columna] = 0 # Si la llamada recursiva no encuentra una solución, retrocede

    return False # Si no hay solución para este estado, Retorna un False


# Sudoku
sudoku_1 = [
    [5, 0, 0, 9, 1, 3, 7, 2, 0],
    [3, 0, 0, 0, 8, 0, 5, 0, 9],
    [0, 9, 0, 2, 5, 0, 0, 8, 0],
    [6, 8, 0, 4, 7, 0, 2, 3, 0],
    [0, 0, 9, 5, 0, 0, 4, 6, 0],
    [7, 0, 4, 0, 0, 0, 0, 0, 5],
    [0, 2, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 8, 9, 1, 6, 0, 0],
    [8, 5, 0, 7, 2, 0, 0, 0, 3]
]

if resolver_sudoku(sudoku_1):
    print("Sudoku resuelto:")
    imprimir_sudoku(sudoku_1) # Imprime el sudoku en un arreglo, dividido por bloques de 3x3
else:
    print("No hay solución para el Sudoku")
