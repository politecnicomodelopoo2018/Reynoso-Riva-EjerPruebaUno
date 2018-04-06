from CLASEPERSONA import Persona
a=Persona()

class Datos(object):
    fecha=None
    fechaRegistro=None
    peso=None
    altura=None

    def setFecha(self,fecha):
        self.fecha=fecha

    def getFecha(self):
        return self.fecha

    def setPeso(self,peso):
        self.peso=peso

    def getPeso(self):
        return self.peso

    def setAltura(self,altura):
        self.altura=altura

    def getAltura(self):
        return self.altura

    def AgregarFecha(self,fecha):
        self.registro.append(fecha)

    def AgregarPeso(self,peso):
        self.registro.append(peso)

    def AgregarAltura(self,altura):
        self.registro.append(altura)

    def setfechaRegistro(self,fechaRegistro):
        self.fechaRegistro=fechaRegistro

    def getfechaRegistro(self):
        return self.fechaRegistro


    def AgregarFechaRegistro(self,fechaRegistro):
        self.registro.append(fechaRegistro)



