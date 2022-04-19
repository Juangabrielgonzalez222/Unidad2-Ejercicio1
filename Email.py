class Email:
    __idCuenta=''
    __dominio=''
    __tipoDominio=''
    __contraseña=''
    def __init__(self,idCuenta='',dominio='',tipo='',contraseña=''):
        self.__idCuenta=idCuenta
        self.__dominio=dominio
        self.__tipoDominio=tipo
        self.__contraseña=contraseña
    def retornaEmail(self):
        return '{}@{}.{}'.format(self.__idCuenta,self.__dominio,self.__tipoDominio)
    def getDominio(self):
        return self.__dominio
    def verificarContraseña(self,contraseña):
        return self.__contraseña==contraseña
    def verificarIdentificador(self,id):
        return self.__idCuenta==id
    def crearCuenta(self,correo):
            print('Se creo la cuenta con la direccion',correo)
    def modificarContraseña(self,nuevaContraseña):
        self.__contraseña=nuevaContraseña
    def mostrarDatos(self):
        print('IdCuenta:{}, Dominio:{},TipoDominio:{} Contraseña:{}'.format(self.__idCuenta,self.__dominio,self.__tipoDominio,self.__contraseña))
    def test(self):
        print('Comienza test Email')
        emailTest1=Email('prueba','gmail','com','1234')
        emailTest2=Email('prueba2','gmail','com','555552')
        print('Metodo retornaEmail():')
        print(emailTest1.retornaEmail())
        print(emailTest2.retornaEmail())
        print('Metodo getDominio():')
        print(emailTest1.getDominio())
        print(emailTest2.getDominio())
        print('Metodo verificarContraseña():')
        print(emailTest1.verificarContraseña('1234'))
        print(emailTest2.verificarContraseña('1234'))
        print('Metodo verificarIdentificador():')
        print(emailTest1.verificarIdentificador('prueba'))
        print(emailTest2.verificarIdentificador('prueba3'))
        print('Metodo crearCuenta():')
        emailTest1.crearCuenta(emailTest1.retornaEmail())
        emailTest2.crearCuenta(emailTest2.retornaEmail())
        print('Metodo modificarContraseña():')
        emailTest1.modificarContraseña('12345')
        emailTest2.modificarContraseña('12222')
        print('mostrarDatos():')
        emailTest1.mostrarDatos()
        emailTest2.mostrarDatos()
        print('Fin test Email. \n')