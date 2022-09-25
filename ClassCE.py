import telnetlib


print("Evaluación Parcial No. 1")
print("Erick Ramírez Villafuerte")
print("Carné 200915472")
print("Docente: Lic Mynor Flores")

class CentrosEducativos:
    #atributos de clase
    codigo=""
    nombre=""
    direccion=""
    telefono=""
    director=""
    url=""

    #metodos de clase.
    def codigo(self, cod):
        self.codigo=cod
    
    def nombre(self, nom):
        self.nombre=nom

    def direccion(self, dir):
        self.direccion=dir
    
    def telefono(self, tel):
        self.telefono=tel
    
    def director(self, direc):
        self.director=direc
    
    def url(self,url):
        self.url=url

    def mostrarDatosCE(self):
        print("--------------------------------------------")
        print("El código del centro educativo es: ", self.codigo)
        print("El nombre del centro educativoes: ", self.nombre)
        print("La dirección del centro educatov es: ", self.direccion)
        print("El telefono del cenrto educativo es: ", self.telefono)
        print("El director del centro educativo es: ", self.director)
        print("La url del colegio es: ", self.url)

        



