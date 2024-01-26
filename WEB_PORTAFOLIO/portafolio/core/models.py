from django.db import models

class Proyecto:
    def __init__(self,nombre,descripcion,imagen,costo):
        self.nombre=nombre
        self.descripcion=descripcion
        self.imagen=imagen
        self.costo=costo

