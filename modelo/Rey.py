from modelo.Color import Color
from modelo.Posicion import Posicion
from modelo.Direccion import Direccion
class Rey:

    __color: Color
    __posicion: Posicion

    # En python no hay sobrecarga de métodos
    # Por lo que solo podemos hacer un tipo de constructor, el init, y acaso el copy, pero no podemos crear diferentes constructores. 

    # Parece que en el init si pones los parametros con none, puedes invocarlo sin el parametro y funciona también. 
    def __init__(self, color=None):
        if color == None:
            self.__setColor(Color.BLANCO)
            self.__setPosicion(Posicion(1, 'e'))
        else: 
            self.__setColor(color)
            if color == Color.BLANCO:
                self.__setPosicion(Posicion(1, 'e'))
            elif color == Color.NEGRO:
                self.__setPosicion(Posicion(8, 'e'))
    
    def getColor(self):
        return self.__color
    
    def getPosicion(self):
        return self.__posicion
    
    def __setColor(self, color):
        if color == None:
            raise TypeError("El color no puede ser nulo.") #Puede ser tambien un NoneError
        self.__color=color
    
    def __setPosicion(self, posicion):
        if posicion == None:
            raise TypeError("La posición no puede ser nula.")
        self.__posicion=posicion
    

    def mover(self, direccion):
        if direccion == None:
            raise TypeError("La direccion no puede ser nula.")
        if self.getPosicion().getFila() > 8 or self.getPosicion().getFila() < 1:
            raise TypeError("El rey se sale del tablero si se intenta hacer este movimiento.")
        if self.getPosicion().getColumna() < 'b' or self.getPosicion().getColumna() > 'g':
            raise TypeError("El rey se sale del tablero si se intenta hacer este movimiento.")
        match(direccion):
            case Direccion.NORTE: self.__setPosicion(Posicion(self.getPosicion().getFila()+1, self.getPosicion().getColumna()))
            case Direccion.SUR: self.__setPosicion(Posicion(self.getPosicion().getFila() -1, self.getPosicion().getColumna()))
            case Direccion.OESTE: self.__setPosicion(Posicion(self.getPosicion().getFila(), chr(ord(self.getPosicion().getColumna())-1))) #Esto se usa poder hacer suma aritmetica con caracteres, lo que hace es convertirlo en ASCII para poder sumar el caracter de ASCII y luego lo vuelve a convertir a ordinal.
            case Direccion.ESTE: self.__setPosicion(Posicion(self.getPosicion().getFila(),chr(ord(self.getPosicion().getColumna() )+1)))
            case Direccion.NORESTE: self.__setPosicion(Posicion(self.getPosicion().getFila()+1, chr(ord(self.getPosicion().getColumna())+1)))
            case Direccion.NOROESTE: self.__setPosicion(Posicion(self.getPosicion().getFila()+1, chr(ord(self.getPosicion().getColumna())-1)))
            case Direccion.SURESTE: self.__setPosicion(Posicion(self.getPosicion().getFila()-1, chr(ord(self.getPosicion().getColumna())+1)))
            case Direccion.SUROESTE: self.__setPosicion(Posicion(self.getPosicion().getFila()-1, chr(ord(self.getPosicion().getColumna())-1)))
            case Direccion.ENROQUE_CORTO:
                self.__comprobarEnroque()
                if self.getColor() == Color.BLANCO:
                    self.__setPosicion(Posicion(1, 'g'))
                elif self.getColor() == Color.NEGRO:
                        self.__setPosicion(Posicion(8,'g'))
            case Direccion.ENROQUE_LARGO:
                self.__comprobarEnroque()
                if self.getColor() == Color.BLANCO:
                    self.__setPosicion(Posicion(1, 'c'))
                elif self.getColor() == Color.NEGRO:
                    self.__setPosicion(Posicion(8,'c'))

    def __comprobarEnroque(self):
        if self.getColor() == Color.BLANCO:
            if self.getPosicion().getFila() != 1 or self.getPosicion().getColumna() != 'e':
                raise TypeError("No se puede realizar el enroque")
        elif self.getColor() == Color.NEGRO:
            if self.getPosicion().getFila() != 8 or self.getPosicion().getColumna() != 'e':
                raise TypeError("No se puede realizar el enroque")
    
    def __str__(self):
        return f"El rey de color {self.getColor()} está en la posición: Fila: {self.getPosicion().getFila()} Columna: {self.getPosicion().getColumna()}"
'''
def toString(self):
        return "El rey de color {self.getColor.toString()} está en la posición: Fila: {self.getPosicion.getFila()} Columna: {self.getPosicion.getColumna()} "
'''
    

