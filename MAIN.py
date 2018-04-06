from CLASEPERSONA import Persona
from CLASEDATOS import Datos
import datetime

a=Persona()
b=Datos()



variable1='S'

while variable1 == 'S':

    nombre=input("INGRESE UN NOMBRE: ")
    a.setNombre(nombre)


    apellido=input("INGRESE UN APELLIDO: ")
    a.setApellido(apellido)


    fecha_nac=input("INGRESE UNA FECHA DE NACIMIENTO: ")
    a.setFecha_nac(fecha_nac)

    altura=input("INGRESE UNA ALTURA: ")
    b.setAltura(altura)

    peso=input("INGRESE UN PESO: ")
    b.setPeso(peso)

    fechaRegistro=input("INGRESE LA FECHA DE HOY: ")
    b.setfechaRegistro(fechaRegistro)


    variable = input ("quiere agregar otro registro?")

    if variable=='N':
        break




fecha = input("INGRESE UNA FECHA QUE QUIERA SABER EL PESO: ")
b.setFecha(fecha)


for i in a.registro:
    if fecha == a.registro[i]:
        print (i)
