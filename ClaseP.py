from ClassCE import CentrosEducativos

class Privados(CentrosEducativos):
    #atributos de clase Privados
    cantH=0
    cantM=0

    def cantH(self,cantidadH):
        self.cantH=cantidadH

    def cantM(self, cantidadM):
        self.cantM=cantidadM
    
    def mostrarDatosCE(self):
        print( super().mostrarDatosCE())
        print("La cantidad de estudiantes varones es: ", self.cantH)
        print("La cantidad de estudiantes mujees es: ", self.cantM)
