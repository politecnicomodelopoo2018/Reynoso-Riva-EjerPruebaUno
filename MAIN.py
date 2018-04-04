from CLASEPERSONA import Persona
from CLASEDATOS import Datos
import datetime

a=Persona()
b=Datos()

nombre=input("INGRESE UN NOMBRE: ")
a.setNombre(nombre)


apellido=input("INGRESE UN APELLIDO: ")
a.setApellido(apellido)


fecha_nac=input("INGRESE UNA FECHA: ")
a.setFecha_nac(fecha_nac)



fecha=input("INGRESE UNA FECHA DE PESO: ")
b.setFecha(fecha)


altura=input("INGRESE UNA ALTURA: ")
b.setAltura(altura)

peso=input("INGRESE UN PESO: ")
b.setPeso(peso)



print(a.nombre)
print(a.apellido)
print(a.fecha_nac)
print(b.fecha)
print(b.altura)
print(b.peso)
