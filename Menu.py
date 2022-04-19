from ManejadorEmail import ManejadorEmail
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.test,
            '4':self.salir
        }
    def lanzarMenu(self,email):
        #Menu opciones
        i=str(len(self.__opciones))
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1 para modificar contraseña.')
            print('-Ingrese 2 para leer un archivo y buscar un identificador.')
            print('-Ingrese 3 para ejecutar un test.')
            print('-Ingrese 4 para salir.')
            opcion=input('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion=='1' or opcion=='3':
                ejecutar(email)
            else:
                ejecutar()
    def opcion1(self,email):
        #Cambiar contraseña
        contraseñaActual=input('Ingrese la contraseña actual:\n')
        if email.verificarContraseña(contraseñaActual):
            contraseñaNueva=input('Ingrese la contraseña nueva:\n')
            email.modificarContraseña(contraseñaNueva)
            print('Se modifico la contraseña.')
        else:
            print('La contraseña no coincide.')
    def opcion2(self):
        #Leer archivo y buscar identificador
        manejadorEmail=ManejadorEmail()
        manejadorEmail.cargarDesdeArchivo()
        identificador=input('Ingrese identificador: \n')
        manejadorEmail.verificarIdentificadorRepetido(identificador)
    def test(self,email):
        #Realizar test
        email.test()
        manejador=ManejadorEmail()
        manejador.test()
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')