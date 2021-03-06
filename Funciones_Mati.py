def solicitar_nombre(quien=""):
    """Entradas: -- | Salidas: str"""
    if quien != "":
        quien += " "
    nombre = input(quien + "Ingrese su nombre: ")
    return nombre


def solicitar_puntaje_objetivo():
    x = 0
    while x <= 10:
        x = int(input("Ingrese la cantidad de puntos que se deben alcanzar para que finalice la partida: "))
        if x <= 10:
            print("Ingrese un valor mayor a 10")
    return x


def check_acierto(dados, apuesta):
    acierto = False
    d1, d2, d3 = dados
    paridad = (d1 + d2 + d3) % 2
    if apuesta is True and paridad == 0 or apuesta is False and paridad == 1:
        acierto = True
    return acierto


def cargar_entero_con_tope_minimo(tope_minimo, mensaje=None):
    if mensaje:
        print(mensaje)
    x = int(input("Ingrese un número mayor a " + str(tope_minimo) + ": "))
    while x <= tope_minimo:
        print("El valor ingresado no es válido")
        x = int(input("Ingrese un número mayor a " + str(tope_minimo) + ": "))
    return x


# prueba = cargar_entero_con_tope_minimo(10, "Para continuar deberá ingresar el puntaje máximo necesario para que la partida finalice.")

def solicitar_apuesta(quien=""):
    apuesta = input(quien + ": ¿Apuesta por par? (s/n): ")
    while apuesta.lower() != "s" and apuesta.lower() != "n":
        apuesta = input("Para responder solo debe ingresar s para SÍ o n para NO: ")
    if apuesta == "s":
        par = True
    else:
        par = False
    return par


def check_acierto_critico(tupla_int):
    """Entrada: (int, int, int) | Salida: bool"""
    iguales = False
    r = 0
    for d in tupla_int:
        r += d % 2
    if r == 0 or r == len(tupla_int):
        iguales = True
    return iguales

