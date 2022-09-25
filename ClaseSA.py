from ClaseP import Privados

class SociedadAnonima(Privados):
    # atributos
    nombresa=""
    representante=""
    correo=""

    #metodos clase

    def nombresa(self, nom):
        self.nombresa=nom
    
    def representante(self, rep):
        self.representante=rep
    
    def correo(self, co):
        self.correo=co
    
    def mostrarDatosCE(self):
        print( super().mostrarDatosCE())
        print("El nombre de la sociedad anonima del colegio es. ", self.nombresa)
        print("El representante de la SA es: ", self.representante)
        print("El correo del representante es: ", self.correo)
        print("------------------------------------------------------------------")

    