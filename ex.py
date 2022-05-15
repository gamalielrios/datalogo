from tkinter import *
from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('300x200')

frame = Frame(ws,frame3=Frame(root=root,posx=10,posy=150,width=600,height=490))
frame.pack()

food = LabelFrame(frame, text='Food', bd=5)
food.grid(row=0, column=0, padx=20, pady=20)

#Checkbutton(food, text='Pizza').pack(anchor=W)


drinks = LabelFrame(frame, text='Drinks', bd=5, relief=RIDGE)
drinks.grid(row=0, column=1, sticky=E, padx=20, pady=20)

Checkbutton(drinks, text='Water').pack(anchor=W)
Checkbutton(drinks, text='Coffee').pack(anchor=W)
Checkbutton(drinks, text='Fanta').pack(anchor=W)
Checkbutton(drinks, text='Bear').pack(anchor=W)

ws.mainloop()

##########copia
#endregion

    #region Frame Seleccionar logo


    #endregion
    #region FrameSeleccionar
    #endregion
"""
#region combobox
    labelSelect=Label(root,text='Seleccionar logo',fg='white', font=(16), bg='black')
    labelSelect.grid(row=0,column=0,columnspan=2)
    cmbSelect = ttk.Combobox(root, values=["logoCDMX01", "logoCDMX02","logoCDMX02","logoCDMX02","logoMTY01","logoMTY02"])
    cmbSelect.grid(row=0, column=2)


    btnSelect = Button(root, text="Aceptar", fg='black', font=(16))
    btnSelect.grid(row=0, column=3)

#endregion

#region Frame 1
    frame1=Frame(root, width=500,height=100)
    frame1.config(bg="black")
    frame1.grid(row=1,column=0,columnspan=4,rowspan=2,padx=5,pady=5,ipadx=30,ipady=50)
    tabla_ph = ttk.Treeview(frame1,
                                 column=("inicio", "trabajo"))

    tabla_ph.place(x=0,y=0)
    tabla_ph.heading('#0', text='ID')
    tabla_ph.heading('#1', text='PH')
    tabla_ph.heading('#2', text='Fecha')
    datosPh = [{'idclientelogo': 1, 'status': '7.88', 'date': '04/27/2022, 18:05:06'},
               {'idclientelogo': 2, 'status': '6.89', 'date': '04/28/2022, 23:15:06'},
               {'idclientelogo': 32, 'status': '7.2', 'date': '04/28/2022, 23:45:01'},
               {'idclientelogo': 33, 'status': '8.4', 'date': '04/28/2022, 23:46:14'},
               {'idclientelogo': 34, 'status': '5.9', 'date': '04/28/2022, 23:47:24'},
               {'idclientelogo': 35, 'status': '7.9', 'date': '04/28/2022, 23:47:40'},
               {'idclientelogo': 36, 'status': '7.2', 'date': '04/29/2022, 19:59:03'},
               {'idclientelogo': 37, 'status': '8.1', 'date': '04/29/2022, 19:59:36'},
               {'idclientelogo': 38, 'status': '7.0', 'date': '04/29/2022, 20:01:41'}]
    for x in range(len(datosPh)):
        lista = list(datosPh[x].values())
        index = str(x)
        print(index)
        lista = lista[1:]
        tabla_ph.insert('', 0, text=index, values=lista)
#endregion

#region NumMensajes
    frame9 = Frame(root, width=600, height=100, highlightbackground='green', highlightthicknes=2)
    frame9.config(bg="#00FF99")
    frame9.grid(row=4, column=4, columnspan=10, padx=10)

   # labelCostos = Label(frame9, text="Costos", fg='blue', font=(16), bg='black')
    #labelCostos.grid(row=0, column=0,columnspan=10)
#endregion

#region Frame2
#configuracion del frame 2
    frame2=Frame(root, width=600,height=610,highlightbackground='green', highlightthicknes=2)
    frame2.config(bg="#00FF99")
    frame2.grid(row=0,column=4,columnspan=9,rowspan=4,padx=10)

    logosiemenspic=Image.open('img/logosiemens.png')
    resizesiemens=logosiemenspic.resize((100,56),Image.ANTIALIAS)
    newSiemens=ImageTk.PhotoImage(resizesiemens)
    labelLogoSiemens=Label(frame2,image=newSiemens)
    labelLogoSiemens.grid(row=0,column=0,columnspan=3,rowspan=3)


    logounam= Image.open('img/logounam.png')
    resizeunam = logounam.resize((100, 100), Image.ANTIALIAS)
    newUnam = ImageTk.PhotoImage(resizeunam)
    labelLogoUnam = Label(frame2, image=newUnam)
    labelLogoUnam.grid(row=0, column=7,columnspan=3,rowspan=3)


    labelhead = Label(frame2, text="Proyecto logo 8.4!", fg='white', font=(20), bg='red')
    labelhead.grid(row=0, column=3,rowspan=3,columnspan=4)

    labelhead2 = Label(frame2, text="Ubicacion",fg='white', font=(6), bg='red')
    labelhead2.grid(row=4, column=2,columnspan=5)

    labelUbicacion = Label(frame2, text="Coordenadas", fg='white', font=(6), bg='red')
    labelUbicacion.grid(row=5, column=0,columnspan=2)

    labelCoordenadas = Label(frame2, text="19.3262659,-99.1842875", fg='white', font=(6), bg='red')
    labelCoordenadas.grid(row=5, column=3,columnspan=2)

    labelLocalidad = Label(frame2, text="Anexo de Ingenieria, UNAM", fg='white', font=(6), bg='red')
    labelLocalidad.grid(row=5, column=6,columnspan=2)


    labelheadRegistro = Label(frame2, text="Registro", fg='white', font=(6), bg='red')
    labelheadRegistro.grid(row=7, column=2, columnspan=5)

    labelSiembra = Label(frame2, text="Siembra", fg='white', font=(6), bg='red')
    labelSiembra.grid(row=8, column=0)

    labelSiembraValue = Label(frame2, text="04/27/2022", fg='white', font=(6), bg='red')
    labelSiembraValue.grid(row=8, column=2, columnspan=2)

    labelCosecha = Label(frame2, text="Cosecha", fg='white', font=(6), bg='red')
    labelCosecha.grid(row=8, column=6)
    labelCosechaValue = Label(frame2, text="07/27/2022", fg='white', font=(6), bg='red')
    labelCosechaValue.grid(row=8, column=7)


    labelCultivo = Label(frame2, text="Cultivo", fg='white', font=(6), bg='red')
    labelCultivo.grid(row=9, column=0)

    labelCultivoValue = Label(frame2, text="Lechugas", fg='white', font=(6), bg='red')
    labelCultivoValue.grid(row=9, column=2, columnspan=2)

    labelNumPlantas = Label(frame2, text="Numero de plantas", fg='white', font=(6), bg='red')
    labelNumPlantas.grid(row=9, column=6)
    labelNumPlantasValue = Label(frame2, text="20", fg='white', font=(6), bg='red')
    labelNumPlantasValue.grid(row=9, column=7)
#endregion

#region Frame 3
    frame3 = Frame(root, width=500, height=100)
    frame3.config(bg="black")
    frame3.grid(row=3, column=0, columnspan=4, rowspan=2, padx=5, pady=5, ipadx=30, ipady=50)

    #labbelmap.grid(row=0,column=0,rowspan=8)

    tabla_bomba = ttk.Treeview(frame3,
                               column=("inicio", "trabajo"))
    #tabla_bomba.grid(row=4, column=0, columnspan=4)
    tabla_bomba.place(x=0,y=0)
    tabla_bomba.heading('#0', text='ID')
    tabla_bomba.heading('#1', text='status')
    tabla_bomba.heading('#2', text='fecha')
    datosbomba = [{'idclientelogo': 1, 'status': 'ON', 'date': '04/27/2022, 18:05:06'},
             {'idclientelogo': 31, 'status': 'OFF', 'date': '04/28/2022, 23:15:06'},
             {'idclientelogo': 32, 'status': 'ON', 'date': '04/28/2022, 23:45:01'},
             {'idclientelogo': 33, 'status': 'OFF', 'date': '04/28/2022, 23:46:14'},
             {'idclientelogo': 34, 'status': 'ON', 'date': '04/28/2022, 23:47:24'},
             {'idclientelogo': 35, 'status': 'OFF', 'date': '04/28/2022, 23:47:40'},
             {'idclientelogo': 36, 'status': 'ON', 'date': '04/29/2022, 19:59:03'},
             {'idclientelogo': 37, 'status': 'OFF', 'date': '04/29/2022, 19:59:36'},
             {'idclientelogo': 32, 'status': 'ON', 'date': '04/28/2022, 23:45:01'},
             {'idclientelogo': 33, 'status': 'OFF', 'date': '04/28/2022, 23:46:14'},
             {'idclientelogo': 34, 'status': 'ON', 'date': '04/28/2022, 23:47:24'},
             {'idclientelogo': 35, 'status': 'OFF', 'date': '04/28/2022, 23:47:40'},
             {'idclientelogo': 36, 'status': 'ON', 'date': '04/29/2022, 19:59:03'},
             {'idclientelogo': 37, 'status': 'OFF', 'date': '04/29/2022, 19:59:36'},
             {'idclientelogo': 38, 'status': 'ON', 'date': '04/29/2022, 20:01:41'}]
    for x in range(len(datosbomba)):
        lista = list(datosbomba[x].values())
        index = str(x)
        print(index)
        lista = lista[1:]
        tabla_bomba.insert('', 0, text=index, values=lista)

#endregion

#region Frame 4
    frame4=Frame(root, width=20,height=100,highlightbackground='green', highlightthicknes=2)
    frame4.config(bg="black")
    frame4.grid(row=5,column=0,columnspan=3,rowspan=2,padx=10)

    #labeles

    labeltitlePH = Label(frame4, text="Estadistica descriptiva de los valores de PH ", fg='white', font=('Arial',10), bg='black')
    labeltitlePH.grid(row=0, column=0,columnspan=2,rowspan=2)

    labelPromedio=Label(frame4,text="Promeido (Ph): ",fg='blue',font=('Arial',10),bg='black')
    labelPromedio.grid(row=2,column=0)

    valuePromedio=Label(frame4,text="7.8: ",fg='blue',font=('Arial',10),bg='black')
    valuePromedio.grid(row=2,column=1)

    labelDSPh = Label(frame4, text="Desviacion estandar (Ph): ", fg='blue', font=('Arial',10), bg='black')
    labelDSPh.grid(row=3, column=0)

    valueDSPh = Label(frame4, text="0.002 ", fg='blue', font=('Arial',10), bg='black')
    valueDSPh.grid(row=3, column=1)

    labelMediana = Label(frame4, text="Mediana (Ph): ", fg='blue',font=('Arial',10), bg='black')
    labelMediana.grid(row=4, column=0)

    valueMediana = Label(frame4, text="7.8", fg='blue', font=('Arial',10), bg='black')
    valueMediana.grid(row=4, column=1)


    labelModaPh = Label(frame4, text="Moda (Ph): ", fg='blue', font=('Arial',10), bg='black')
    labelModaPh.grid(row=5, column=0)
    valueModaPh = Label(frame4, text="7.1", fg='blue', font=('Arial',10), bg='black')
    valueModaPh.grid(row=5, column=1)


    labelModelPh = Label(frame4, text="Modelo matematico (Ph): ", fg='blue', font=('Arial',10), bg='black')
    labelModelPh.grid(row=6, column=0)


    valueModelPh = Label(frame4, text="x=24.634y+232.3", fg='blue', font=('Arial',10), bg='black')
    valueModelPh.grid(row=6, column=1)






#endregion

#region Frame 5
    frame5=Frame(root, width=20,height=100,highlightbackground='green', highlightthicknes=2)
    frame5.config(bg="black")
    frame5.grid(row=5,column=3,columnspan=3,rowspan=2,padx=10)


    # labeles


    labeltitleB1 = Label(frame5, text="Informacion de la bomba ", fg='white', font=('Arial',10),bg='black')
    labeltitleB1.grid(row=0, column=0, columnspan=2, rowspan=2)

    labelSB1 = Label(frame5, text="Status: ", fg='blue', font=('Arial',10), bg='black')
    labelSB1.grid(row=2, column=0)

    valueSB1 = Label(frame5, text="OFF: ", fg='blue', font=('Arial',10), bg='black')
    valueSB1.grid(row=2, column=1)

    labelTimeOnB1 = Label(frame5, text="Tiempo de encendido: ", fg='blue', font=('Arial',10), bg='black')
    labelTimeOnB1.grid(row=3, column=0)

    valueTimeOnB1 = Label(frame5, text="00:10:43", fg='blue', font=('Arial',10), bg='black')
    valueTimeOnB1.grid(row=3, column=1)

    labelFrecuenciaOnB1 = Label(frame5, text="Frecuencia de encendido [p/dia]: ", fg='blue', font=('Arial',10), bg='black')
    labelFrecuenciaOnB1.grid(row=4, column=0)

    valueFrecuenciaOnB1 = Label(frame5, text="13", fg='blue', font=('Arial',10), bg='black')
    valueFrecuenciaOnB1.grid(row=4, column=1)

    labelEnergyB1 = Label(frame5, text="Consumo de energia: ", fg='blue', font=('Arial',10), bg='black')
    labelEnergyB1.grid(row=5, column=0)
    valueEnergyB1 = Label(frame5, text="7.1 [Watts]", fg='blue', font=('Arial',10), bg='black')
    valueEnergyB1.grid(row=5, column=1)

    labelTimeDrainB1 = Label(frame5, text="Tiempo de vaciado promedio: ", fg='blue', font=('Arial',10), bg='black')
    labelTimeDrainB1.grid(row=6, column=0)

    valueTimeDrainB1= Label(frame5, text="00:10:43", fg='blue', font=('Arial',10), bg='black')
    valueTimeDrainB1.grid(row=6, column=1)
#endregion

#region Frame 6
    frame6=Frame(root, width=20,height=100,highlightbackground='green', highlightthicknes=2)
    frame6.config(bg="black")
    frame6.grid(row=5,column=6,columnspan=3,rowspan=2,padx=10)

    #labels
    labeltitleInterpretacion = Label(frame6, text="Interpretacion de los datos ", fg='white', font=('Arial',10), bg='black')
    labeltitleInterpretacion.grid(row=0, column=0, columnspan=2, rowspan=2)

    labelHPH = Label(frame6, text="Nivel historico de PH: ", fg='blue', font=('Arial',10), bg='black')
    labelHPH.grid(row=2, column=0)

    valueHPH = Label(frame6, text="Bueno: ", fg='blue', font=('Arial',10), bg='black')
    valueHPH.grid(row=2, column=1)

    labelVPH = Label(frame6, text="Variacion de PH: ", fg='blue', font=('Arial',10), bg='black')
    labelVPH.grid(row=3, column=0)

    valueVPH = Label(frame6, text="Regular", fg='blue', font=('Arial',10), bg='black')
    valueVPH.grid(row=3, column=1)

    labelPHF = Label(frame6, text="PH estimado: ", fg='blue', font=('Arial',10), bg='black')
    labelPHF.grid(row=4, column=0)

    valuePHF = Label(frame6, text="7.3", fg='blue', font=('Arial',10), bg='black')
    valuePHF.grid(row=4, column=1)

    labelCH2O = Label(frame6, text="Consumo de energia: ", fg='blue', font=('Arial',10), bg='black')
    labelCH2O.grid(row=5, column=0)
    valueCH2O = Label(frame6, text="Moderado", fg='blue', font=('Arial',10), bg='black')
    valueCH2O.grid(row=5, column=1)

    labelCW = Label(frame6, text="Consumo de agua: ", fg='blue', font=('Arial',10), bg='black')
    labelCW.grid(row=6, column=0)

    valueCW = Label(frame6, text="Moderado", fg='blue', font=('Arial',10), bg='black')
    valueCW.grid(row=6, column=1)
#endregion

#region Buton Update




    buttonUpdate=Button(root,text="Actualizar",fg = 'black', font=(16))
    buttonUpdate.grid(row=6,column=10)
#endregion

        """



