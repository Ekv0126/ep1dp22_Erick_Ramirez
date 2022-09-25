from ClaseSA import SociedadAnonima

entidad = SociedadAnonima()

entidad.codigo(input("Ingrese el codigo del centro educativo que desea identificar "))
entidad.nombre(input("Ingrese el nombre del centro educativo que desea identificar "))
entidad.direccion(input("Ingrese la direccion del centro educativo que desea identificar "))
entidad.telefono(input("Ingrese el telefon del centro educativo que desea identificar "))
entidad.director(input("Ingrese el nombre del director del centro educativo que desea identificar "))
entidad.url(input("Ingrese la URL del centro educativo"))
entidad.cantH(int(input("Ingrese la cantidad de estudiantes varones: ")))
entidad.cantM(int(input("Ingrese la cantidad de estudiantes muejeres")))

entidad.nombresa(input("Ingrese el nombre de la sociedad Anonima: "))
entidad.representante(input("ingrese el nombre del representante: "))
entidad.correo(input("Ingrese el corre del representante: "))

entidad.mostrarDatosCE()


