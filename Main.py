import re
from Email import Email
from Menu import Menu

if __name__== '__main__':
    nombre=input('Ingrese nombre:')
    correo=input('Ingrese correo:')
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
        contraseña=input('Ingrese contraseña:\n')
        partesCorreo=correo.split('@')
        idCuenta=partesCorreo[0]
        partesCorreo=partesCorreo[1].split('.')
        dominio=partesCorreo[0]
        tipoDominio=partesCorreo[1]
        email=Email(idCuenta,dominio,tipoDominio,contraseña)
        email.crearCuenta(email.retornaEmail())
        print('Estimado {} te enviaremos tus mensajes a la direccion {}'.format(nombre,email.retornaEmail()))
        menu=Menu()
        menu.lanzarMenu(email)
    else:
        print ('El correo ingresado no tiene un formato correcto')