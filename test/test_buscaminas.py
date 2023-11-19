from src.minas import contar_minas_adyacentes, revelar_celda, verificar_victoria

def test_contar_minas_adyacentes():
    tablero_prueba = [
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', 'X', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.']
    ]
    assert contar_minas_adyacentes(tablero_prueba, 0, 0) == 0


def test_revelar_celda():
    tablero_prueba = [
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', 'X', 'X', 'X', '.', '.'],
        ['.', '.', '.', 'X', '.', 'X', '.', '.'],
        ['.', '.', '.', 'X', 'X', 'X', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.']
    ]
    #Probamos la funcion para revelar una celda sin minas adyacentes
    assert revelar_celda(tablero_prueba, 0, 0) == True
    #Verificamos si la celda se ha revelado correctamente
    assert tablero_prueba[0][0] != '.'

def test_verificar_victoria():
    tablero_ganador = [
        ['1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1']
    ]
    tablero_incompleto = [
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.']
    ]
    #Verificamos la victoria en un tablero revelado completamente
    assert verificar_victoria(tablero_ganador) == True
    #Verificamos que la función detecte un tablero incompleto
    assert verificar_victoria(tablero_incompleto) == False
