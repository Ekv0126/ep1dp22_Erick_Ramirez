from cgitb import text
from distutils.cmd import Command
#from locale import MON_1
import tkinter

ventana1=tkinter.Tk()

l1=0
l2=0
l3=0
l4=0
res1=0
m=""
caso1=0
caso2=0
m1=""

ventana1.geometry("500x500")
label_titulo=tkinter.Label(ventana1,text="Actividad 1")

def largo():
    l1=int(len(txt1.get()))
    #print(l1)
    l2=int(len(txt2.get()))
    l3=int(len(txt3.get()))
    l4=int(len(txt4.get()))
    res1=l1+l2+l3+l4
    if((l1>l2)and(l1>l3) and(l1>l4)):
        m="La palabra más larga es: ", txt1.get()
    elif ((l2>l1)and(l2>l3) and(l2>l4)):
        m="La palabra más larga es: ", txt2.get()
    elif ((l2>l1)and(l2>l3) and(l2>l4)):
        m="La palabra más larga es: ", txt3.get()
    elif((l4>l1)and(l4>l3) and(l4>l2)):
        m="La palabra más larga es: ", txt4.get()
    else:
        m="Todas las palabras tienen el mismo largo"

    caso1=res1/4
    caso2=(l2+l3)
    if caso1==caso2:
        m1="La suma de las longitudes SI es igual al promedio de la suma del largo del texto2 y texto3"
    elif caso1>caso2:
        m1="La suma de las longitudes es MAYOR que el promedio de la suam del texto2 y texto 3"
    else:
        m1="La suma de las longitudes es MENOR que la del promedio de la suma del texto 2 y texto3"

    label_r1["text"]="El resutaldo de la suma de las longirudes es> ", res1
    label_r2["text"]= m
    label_r3["text"]=m1


label_txt1=tkinter.Label(ventana1,text="Ingrese el primer texto a evaluar")
txt1=tkinter.Entry(ventana1)
txt2=tkinter.Entry(ventana1)
txt3=tkinter.Entry(ventana1)
txt4=tkinter.Entry(ventana1)
label_txt2=tkinter.Label(ventana1,text="Ingrese el segundo texto")
label_txt3=tkinter.Label(ventana1,text="Ingrese el tercer texto")
label_txt4=tkinter.Label(ventana1,text="Ingrese el cuarto texto")

btn_accion=tkinter.Button(ventana1, text="Ejecutar acción", command=largo)

label_r1=tkinter.Label(ventana1, text="Rsultado de actividad 1.1")
label_r2=tkinter.Label(ventana1, text="Resultado actividad 1.2")
label_r3=tkinter.Label(ventana1, text="Resultado actividad 1.3")

label_titulo.pack()
label_txt1.pack()
txt1.pack()
label_txt2.pack()
txt2.pack()
label_txt3.pack()
txt3.pack()
label_txt4.pack()
txt4.pack()
btn_accion.pack()
label_r1.pack()
label_r2.pack()
label_r3.pack()

ventana1.mainloop()

