class Datos(object):
    fecha=None
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
        self.fecha.append(fecha)

    def AgregarPeso(self,peso):
        self.peso.append(peso)

    def AgregarAltura(self,altura):
        self.altura.append(altura)

    def SaberPeso(self,peso):


