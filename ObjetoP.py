from ClaseP import Privados

insPrivada=Privados()
insPrivada.codigo(input("Ingrese el codigo del centro educativo que desea identificar "))
insPrivada.nombre(input("Ingrese el nombre del centro educativo que desea identificar "))
insPrivada.direccion(input("Ingrese la direccion del centro educativo que desea identificar "))
insPrivada.telefono(input("Ingrese el telefon del centro educativo que desea identificar "))
insPrivada.director(input("Ingrese el nombre del director del centro educativo que desea identificar "))
insPrivada.url(input("Ingrese la URL del centro educativo"))
insPrivada.cantH(int(input("Ingrese la cantidad de estudiantes varones: ")))
insPrivada.cantM(int(input("Ingrese la cantidad de estudiantes muejeres")))

insPrivada.mostrarDatosCE()