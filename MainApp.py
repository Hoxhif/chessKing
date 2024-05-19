from Consola import Consola
from modelo.Rey import Rey # Es importante entender esto, si yo solamente pongo from modelo import Rey, estoy importando el paquete rey pero no la clase Rey 
class MainApp:
    def __init__(self):
        self.__rey=None

    def main(self):
        valor: int = 0
        while valor != 1:
            Consola.mostrarMenu()
            valor = Consola.elegirOpcionMenu()
            self.__ejecutarOpcion(valor)

    def __ejecutarOpcion(self,opcion):
        match(opcion):
            case 1: Consola.desperdirse()
            case 2: self.__crearReyPorDefecto()
            case 3: self.__crearReyColor()
            case 4: self.__mover()

    def __crearReyPorDefecto(self):
        self.__rey = Rey()
        self.__mostrarRey()

    def __crearReyColor(self):
        self.__rey = Rey(Consola.elegirColor())
        self.__mostrarRey()

    def __mover(self):
        if self.__rey == None:
            raise TypeError("No se ha inicializado al Rey")
        Consola.mostrarMenuDirecciones()
        self.__rey.mover(Consola.elegirDireccion())
        self.__mostrarRey()

    def __mostrarRey(self):
        print(self.__rey)

if __name__ == "__main__":
    app = MainApp()
    app.main()
        

#print("Hola")