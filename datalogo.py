import tkinter as tk
#from tkinter import *
#from tkinter import ttk
from PIL import ImageTk,Image
import statistics as st
#from tkinter import ttk
from cliente.gui_app import Frame, barra_menu
def main():

#region Frame Padre
    #configuracion del padre
    root = tk.Tk()  # para crear una ventana
    root.title("DataLogo")
    root.iconbitmap('img/planta.ico')
    root.state("zoomed")
    root.config(bg="#a7a7a7")
    frame1=Frame(root=root,width=1900,height=80,)
    frame1.head()
    frame2=Frame(root=root,posx=10,posy=90,width=1260,height=50)
    frame2.seleccionLogo()

    frame3=Frame(root=root,posx=10,posy=150,width=600,height=490)
    frame3.tablas()
    frame4=Frame(root=root,posx=620,posy=150,width=650,height=100)
    frame4.datosLogo()

    frame5=Frame(root=root,posx=620,posy=260,width=650,height=380)

    kpi_ph_diccionario={'promedio':7.22,'desviación estandar':0.23,'mediana':7.20, 'moda':7.8,'modelo matematico': 'x=13.23y +21'}
    frame5.kpi(title='ph',posx=40,posy=35,diccionario=kpi_ph_diccionario)

    kpi_bomba_diccionario={'status':'OFF','tiempo de encendido [minutos]':22.3,'frecuencia de encendido [p/dia]':11,
                           'Consumo de energia [w]':22.2,'tiempo de vaciado promedio [minutos]':60,}

    frame5.kpi(title='información de la bomba',posx=320,posy=35,diccionario=kpi_bomba_diccionario)

    kpi_interpretacion_diccionario={'nivel historico de pH':'bueno','variación de pH':'regular','pH estimado':7.8,'Consumo de agua':'moderado'}
    frame5.kpi(title='interpretación de los datos',posx=40,posy=230,diccionario=kpi_interpretacion_diccionario)


    kpi_costos_diccionario = {'cloud storage': 10.23, 'IoT core': 2.23, 'DBRS': 7.8,
                                  'S3': 2.34}
    frame5.kpi(title='costos aws', posx=320, posy=230, diccionario=kpi_costos_diccionario)


    root.mainloop()
if __name__== "__main__":
    main()

def calculosPh():
    print()

