class Persona (object):
    nombre=None
    apellido=None
    fecha_nac=None
    peso=None
    altura=None

    def __init__(self):
        self.registro=[]

    def setNombre(self,nombre):
        self.nombre=nombre.title()

    def getNombre(self):
        return self.nombre

    def setApellido(self,apellido):
        self.apellido=apellido.title()

    def getApellido(self):
        return self.apellido

    def setFecha_nac(self, fecha_nac):
        self.fecha_nac = fecha_nac

    def getFecha_nac(self):
        return self.fecha_nac



