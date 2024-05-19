class Posicion:


    __fila: int
    __columna: chr


# https://www.datacamp.com/tutorial/property-getters-setters?utm_source=google&utm_medium=paid_search&utm_campaignid=21057859163&utm_adgroupid=157296744137&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=695611216499&utm_targetid=dsa-2218886984580&utm_loc_interest_ms=&utm_loc_physical_ms=9047035&utm_content=&utm_campaign=230119_1-sea~dsa~tofu_2-b2c_3-es-lang-en_4-prc_5-na_6-na_7-le_8-pdsh-go_9-na_10-na_11-na-apr24&gad_source=1&gclid=CjwKCAjw5v2wBhBrEiwAXDDoJd_iA2fxdLgYIAU71MP0WEPhUxNVEsUm1cSBbdVdgETX64-cNjFaiRoC2H8QAvD_BwE


    def __init__(self, fila, columna):
        self.__setFila(fila)
        self.__setColumna(columna)

    def __copy__(self):
        return Posicion(self.getFila(), self.getColumna())

    def __setFila(self, fila):
        fila = int(fila)
        if fila < 1 or fila > 8:
            raise ValueError("El valor de la fila no es correcto")
        self.__fila= fila
    
    def __setColumna(self, columna):
        if columna < 'a' or columna > 'h':
            raise ValueError("El valor de la columna no es correcto")
        self.__columna=columna

    def getFila(self):
        return self.__fila
    
    def getColumna(self):
        return self.__columna
    

    
    #Equivalente a el método equals de java (creo)
    def __eq__(self, other):
        if isinstance(other, Posicion):
            return self.__fila == other.__fila and self.__columna == other.__columna
        else: return False

    #Equivalente a el método hash de java (creo)
    def __hash__(self):
        return hash((self.__fila, self.__columna))
    
    def __str__(self):
        return f"El valor de la Columna es: {self.getColumna()}, El valor de la Fila es: {self.getFila()}"
    
    '''
    def toString(self):
        return "El valor de la Columna es: {self.getColumna()}, El valor de la Fila es: {self.getFila()} "
    '''