#enumerate  = ['NORTE', 'SUR', 'ESTE', 'OESTE', 'NORESTE', 'NOROESTE', 'SURESTE','SUROESTE', 'ENROQUE_CORTO', 'ENROQUE_LARGO']

from enum import Enum

class Direccion(Enum):
    NORTE = ("Norte")
    SUR = ("Sur")
    ESTE = ("Este")
    OESTE = ("Oeste")
    NOROESTE = ("Noroeste")
    NORESTE = ("Noreste")
    SURESTE = ("Sureste")
    SUROESTE = ("Suroeste")
    ENROQUE_CORTO =("Enroque Corto")
    ENROQUE_LARGO = ("Enroque Largo")

    
    def __str__(self):
        return self.value

#En Python directamente no hace falta hacer un constructor para darle valor a una variable de candena a mostrar, sino que ya le podemos asignar valores a los enumerados directamente, y luego con el metodo __str__ es como si fuera el to string daondle el valor de cada uno.

'''
cadenaAMostrar=""
def _init_direccion(self):
    self.cadenaAMostrar=cadenaAMostrar

def toString():
    return cadenaAMostrar

    def toString(self):
        return self.value

'''

'''
 NORTE, SUR, ESTE, OESTE, NOROESTE, NORESTE, SUROESTE, SURESTE, ENROQUE_CORTO, ENROQUE_LARGO;

 private String cadenaAMostrar;

 private Direccion(String cadenaAMosrar){
    this.cadenaAMostrar= cadenaAMostrar;
 }

 public String toString(){
    return cadenaAMostrar;
 }


'''