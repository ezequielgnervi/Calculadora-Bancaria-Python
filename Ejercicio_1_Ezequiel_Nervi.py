import time


# =========================================
# CONSTANTES
# =========================================

PIN_CORRECTO = "1234"
INTENTOS_MAXIMOS = 3
SALDO_INICIAL = 50000

OPCION_DEPOSITAR = 1
OPCION_EXTRAER = 2
OPCION_SALIR = 3

INTENTOS_CONEXION = 3
PAUSA_CONEXION = 1


# =========================================
# FUNCIONES
# =========================================

def simular_conexion():
    """Muestra los intentos de conexión al servidor."""
    # escribir el código de la función
    for i in range(1,INTENTOS_CONEXION +1):
        print(f"Conectando al servidor... intento {i}")
        time.sleep(1.0)
    

def validar_acceso(pin_correcto):
    """Pide el PIN y devuelve True si es correcto dentro de los intentos permitidos."""
    # escribir el código de la función
    intentos:int = INTENTOS_CONEXION
    while intentos >0:
        ing = input("Ingrese el pin: ")
        if ing == pin_correcto:
            return True
        else:
            intentos -=1
            print(f"Vuelva a intentar, te quedan {intentos} intentos")
    print("Intentos agotados")
    return False


def mostrar_menu():
    """Muestra el menú y devuelve una opción válida."""
    # escribir el código de la función
    while True:
        print("1. Depositar \n2. Extraer\n3. Salir")
        opc = input()
        if opc in["1","2","3"]:
            return int(opc)
        else:
            print("Opcion invalida")




def pedir_monto():
    """Pide un monto mayor a cero y lo devuelve."""
    # escribir el código de la función
    while True:
        monto = float(input("Ingrese el monto: "))
        if monto >0:
            return monto
        else:
            print("monto invalido, debe ser mayor a 0")



def depositar(saldo, monto):
    """Devuelve el saldo luego de depositar."""
    # escribir el código de la función
   
    print("Saldo: ",saldo)
    print("Monto: ",monto)
    saldo = saldo + monto
    return saldo


def extraer(saldo, monto):
    """Intenta extraer dinero. Si no alcanza, mantiene el saldo."""
    # escribir el código de la función
    if saldo <monto:
        print("Fondos insuficientes")
        print("se mantiene el saldo")
        return saldo
    else:
        saldo = saldo - monto
        return saldo
    


# =========================================
# PROGRAMA PRINCIPAL
# =========================================

def main():
    """Ejecuta el cajero automático."""
    simular_conexion()

    if not validar_acceso(PIN_CORRECTO):
        print("Acceso denegado.")
        return

    saldo = SALDO_INICIAL
    print("Acceso concedido.")
    print("Saldo actual:", saldo)

    while True:
        opcion = mostrar_menu()

        if opcion == OPCION_DEPOSITAR:
            monto = pedir_monto()
            saldo = depositar(saldo, monto)
            print("Depósito realizado.")
            print("Saldo actual:", saldo)

        elif opcion == OPCION_EXTRAER:
            monto = pedir_monto()
            saldo = extraer(saldo, monto)
            print("Saldo actual:", saldo)

        else:
            print("Gracias por usar el cajero.")
            break


main()