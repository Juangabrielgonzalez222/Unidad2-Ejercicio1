import csv
from Email import Email

class ManejadorEmail:
    __listaEmail=[]
    def __init__(self):
        self.__listaEmail=[]
    def agregarEmail(self,email):
        if type(email)==Email:
            self.__listaEmail.append(email)
        else:
            print('Error, no se pudo agregar un email a la lista, el tipo de datos es incorrecto.')
    def cargarDesdeArchivo(self):
        archivo=open('direccionesEmail.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                partesCorreo=fila[0].split('@')
                idCuenta=partesCorreo[0]
                partesCorreo=partesCorreo[1].split('.')
                dominio=partesCorreo[0]
                tipoDominio=partesCorreo[1]
                email=Email(idCuenta,dominio,tipoDominio)
                self.agregarEmail(email)
        archivo.close()
    def verificarIdentificadorRepetido(self,identificador):
        i=0
        cantidadIdEncontrada=0
        cantidadEmails=len(self.__listaEmail)
        while cantidadIdEncontrada<2 and i<cantidadEmails:
            if self.__listaEmail[i].verificarIdentificador(identificador):
                cantidadIdEncontrada+=1
            i+=1
        if cantidadIdEncontrada==2:
            print('El identificador {} se encuentra repetido'.format(identificador))
        else:
            print('El identificador {} no se encuentra repetido'.format(identificador))

    def test(self):
        print('Comienza test ManejadorEmail')
        manejador=ManejadorEmail()
        manejador.cargarDesdeArchivo()
        manejador.agregarEmail('email')
        manejador.verificarIdentificadorRepetido('gomez123')
        manejador.verificarIdentificadorRepetido('prueba')
        manejador.verificarIdentificadorRepetido('pedro')
        manejador.verificarIdentificadorRepetido('pedro1000122')
        manejador.agregarEmail(Email('pedro1000122','outlook','com',''))
        manejador.verificarIdentificadorRepetido('pedro1000122')
        print('Fin test ManejadorEmail. \n')