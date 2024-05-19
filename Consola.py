from modelo.Color import Color
from modelo.Direccion import Direccion

class Consola:

    def mostrarMenu():
        print("1. Salir")
        print("2. Crear Rey por Defecto")
        print("3. Crear Rey Personalizado")
        print("4. Mover")

    def elegirOpcionMenu():
        while True:
            try:
                opcion = int(input("Elije la opción que desea (1-4): "))
                if opcion < 1 or opcion > 4:
                    print("La opción elegida no es válida")
                else:
                    return opcion
            except ValueError:
                print("Por favor, introduce un número válido.")

    def elegirColor():
        color: Color
        opcion: int
        while True:
            opcion = int(input("Elije el Color: 1 para Blanco y 2 para Negro: "))
            if opcion<1 or opcion >2:
                print("No es una opción válida")
            else:
                match(opcion):
                    case 1:
                        color = Color.BLANCO
                        return color
                    case 2:
                        color = Color.NEGRO
                        return color

    def mostrarMenuDirecciones():
        print("Elija la dirección deseada: ")
        incremental: int
        incremental= 1
        for nombres in Direccion:
            print(f"{incremental}.- {nombres.value}")
            incremental+=1


    def elegirDireccion():
        while True:
                opcion = int(input("Elije la opción que desea (1-10): "))
                if (opcion < 1 or opcion > 10):
                    print("No es una opción válida")
                else:
                    match(opcion):
                        case 1: return Direccion.NORTE
                        case 2: return Direccion.SUR
                        case 3: return Direccion.ESTE
                        case 4: return Direccion.OESTE
                        case 5: return Direccion.NOROESTE
                        case 6: return Direccion.NORESTE
                        case 7: return Direccion.SURESTE
                        case 8: return Direccion.SUROESTE
                        case 9: return Direccion.ENROQUE_CORTO
                        case 10: return Direccion.ENROQUE_LARGO

    def desperdirse():
        print("Fin del programa, pase buena tarde")
        SystemExit