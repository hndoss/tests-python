import json
import re
import os

from HitosIV import hitos

class HitosIV:
    """Una clase para los hitos del proyecto de Infraestructura Virtual"""

    def todos_hitos(self):
        return hitos

    def cuantos(self):
        return len(hitos['hitos'])

    def uno(self,hito_id):
        if hito_id > len(hitos['hitos']) or hito_id < 0:
            raise IndexError("Índice fuera de rango")
        return hitos['hitos'][hito_id]

    def nuevo( self, filename, title, fecha ):
        if ( not type(filename) is str):
            raise TypeError( "El nombre del fichero debe ser una cadena" )
        if ( not type(title) is str):
            raise TypeError( "El título del hito debe ser una cadena" )
        if not re.match("\d+/\d+\d+", fecha) :
            raise ValueError( "El formato de la fecha es incorrecto" )
        existe = list(filter( lambda hito: hito['file'] == filename, hitos['hitos'] ))
        if len(existe) > 0:
            raise ValueError( "Ese fichero ya existe")
        
        hitos['hitos'].append( {'file': filename,
                                'title': title,
                                'fecha': fecha } )
