posicion_x = 0

def adelante(cantX):
    global posicion_x
    linea = " " * posicion_x
    posicion_x += cantX
    for i in range(cantX):
        if i == cantX-1:
            linea= linea + "→"
        else:
            linea= linea + "-"
        i=i+1
    print(linea)

def abajo(cantY):
    lineaBajada = " " * posicion_x
    for i in range(cantY):
        if i == cantY-1:
            print(lineaBajada + "↓")
        else:
            print(lineaBajada + "|")
            i=i+1

def reiniciar():
    global posicion_x
    posicion_x = 0
    print("Posición reiniciada.")
