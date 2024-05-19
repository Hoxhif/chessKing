from enum import Enum

class Color(Enum):
    BLANCO = ("Blanco")
    NEGRO = ("Negro")

    def __str__(self):
        return self.value
'''
def toString(self):
        return self.values
'''
    