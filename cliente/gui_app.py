import tkinter as tk
from PIL import ImageTk,Image
import pymysql
## TTK para widgets
from tkinter import ttk

def barra_menu(root):
    barra_menu=tk.Menu(root) #crea un objeto de barra de menu y asociar la pantalla que se va anclar
    root.config(menu = barra_menu,width=300, height =300)#configuracion para anclar la barra de menu
    menu_inicio = tk.Menu(barra_menu,tearoff=0) #creando el primer objeto para anclar dentro de barra de menu
    barra_menu.add_cascade(label= 'Inicio',menu= menu_inicio)#agregar
    menu_inicio.add_command(label="imprimir")
    menu_inicio.add_command(label="salir", command= root.destroy)

class Frame(tk.Frame):
    def __init__(self,root = None,posx=0,posy=0,width=0,height=0): #constructor que recibe la raiz por defecto none
        super().__init__(root,width=width,height=height)
        #self.root=root
        self.place(x=posx,y=posy) #empaquetar
        self.config(bg="#dcdcdc")
        #self.campos()
        #self.tabla_bomba()
        #self.tabla_ph()
        #self.my_canvas()
        """print("hola")
        conn = pymysql.connect(host='database-logo1.c2aglixw4x9k.us-east-1.rds.amazonaws.com', user='admin',
                               database='datoslogo', password='logoadmin', cursorclass=pymysql.cursors.DictCursor)
        with conn.cursor() as cur:
            cur.execute(Select * From datoslogo.clientelogo Where status = '01')
            result = cur.fetchall()
            print(result)"""
        #datos=[{'idclientelogo': 1, 'status': '01', 'date': '04/27/2022, 18:05:06'}, {'idclientelogo': 31, 'status': '01', 'date': '04/28/2022, 23:15:06'}, {'idclientelogo': 32, 'status': '01', 'date': '04/28/2022, 23:45:01'}, {'idclientelogo': 33, 'status': '01', 'date': '04/28/2022, 23:46:14'}, {'idclientelogo': 34, 'status': '01', 'date': '04/28/2022, 23:47:24'}, {'idclientelogo': 35, 'status': '01', 'date': '04/28/2022, 23:47:40'}, {'idclientelogo': 36, 'status': '01', 'date': '04/29/2022, 19:59:03'}, {'idclientelogo': 37, 'status': '01', 'date': '04/29/2022, 19:59:36'}, {'idclientelogo': 38, 'status': '01', 'date': '04/29/2022, 20:01:41'}]
    def head(self):
        font_siemens = ("Lucida Sans", 30, "bold")
        self.label_nombre1 = tk.Label(self, text='SIEMENS',fg='white', font=font_siemens, bg='#338b85')
        #self.label_nombre1.grid(column=0,row=0,columnspan=10)
        self.label_nombre1.place(x=10,y=10)
        font_titulo=("Arial", 15, "bold")
        self.labelTitulo=tk.Label(self,text='SISTEMA ANALÍTICO DE HIDROPONIA',fg='black',
                                  font=font_titulo,bg='#dcdcdc')
        self.labelTitulo.place(x=460,y=25)
        '''logosiemenspic = Image.open('img/logounam.png')
        resizesiemens = logosiemenspic.resize((100, 56), Image.ANTIALIAS)
        newSiemens = ImageTk.PhotoImage(resizesiemens)
        logounam=ImageTk.PhotoImage(Image.open('img/logounam.png'))
        self.labelLogoSiemens = tk.Label(self,image=logounam)
        self.labelLogoSiemens.grid(row=0,column=0,columnspan=3,rowspan=3)
        #labelLogoSiemens.grid(row=0, column=0, columnspan=3, rowspan=3)'''

        font_unam = ("Arial", 30, "bold")
        self.label_nombre2 = tk.Label(self, text='UNAM',fg='#D6AE09', font=font_unam)
        self.label_nombre2.place(relx=0.6, y=10)
        #self.label_nombre2.grid(column=10,row=1)
    def seleccionLogo(self):
        #labels
        self.label_nombre=tk.Label(self,text='seleccionar logo')
        #self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.place(x=320,y=12)
        self.boton_select = ttk.Combobox(self,  values=["logoCDMX01",
                                                        "logoCDMX02","logoCDMX03",
                                                        "logoCDMX04","logoMTY01",
                                                        "logoMTY02"])
        self.boton_select.place(x=450,y=12)

        self.btnAceptar=tk.Button(self,text='aceptar')
        self.btnAceptar.place(x=630,y=10)
        self.btnActualizar = tk.Button(self, text='actualizar')
        self.btnActualizar.place(x=800, y=10)

    def tablas(self):

        self.label_nombre1=tk.Label(self,text='tablas del logo')
        self.label_nombre1.place(x=2,y=2)
    def datosLogo(self):
        font_title = ("Arial", 8, "bold")
        self.label_title=tk.Label(self,text='datos del logo',font=font_title,bg='#dcdcdc')
        self.label_title.place(x=10,y=10)


        self.labelCoor=tk.Label(self,text='coordenadas:',bg='#dcdcdc')
        self.labelCoor.place(x=50,y=40)
        self.labelCoorV=tk.Label(self,text='19.3262659,-99.1842875',bg='white')
        self.labelCoorV.place(x=150,y=40)

        self.labelUbicacion = tk.Label(self, text='localidad:', bg='#dcdcdc')
        self.labelUbicacion.place(x=350,y=40)
        self.labelUbicacionV = tk.Label(self, text='Anexo de Ingeniería, UNAM', bg='white')
        self.labelUbicacionV.place(x=450, y=40)

        self.labelCul = tk.Label(self, text='cultivo:', bg='#dcdcdc')
        self.labelCul.place(x=50, y=70)
        self.labelCulV = tk.Label(self, text='lechugas', bg='white')
        self.labelCulV.place(x=120, y=70)

        self.labelCantidad = tk.Label(self, text='número de plantas:', bg='#dcdcdc')
        self.labelCantidad.place(x=350, y=70)
        self.labelCantidadV = tk.Label(self, text='20', bg='white')
        self.labelCantidadV.place(x=480, y=70)


    def kpi(self,title,posx,posy,diccionario):
        font_title = ("Arial", 8, "bold")
        self.label_title = tk.Label(self, text='indicadores clave de rendimiento (kpi)', font=font_title, bg='#dcdcdc')
        self.label_title.place(x=10, y=10)

        font_kpi = ("Arial", 8, "bold")
        self.labelFrameTitle=tk.LabelFrame(self,text=title,font=font_kpi,bd=3)
        self.labelFrameTitle.place(x=posx,y=posy)
        p=len(diccionario)
        #obteniendo las claves del diccionario
        keys=list(diccionario.keys())
        values=list(diccionario.values())
        #print(keys,values)

        for x in range(len(diccionario)):
            self.labelField1 = tk.Label(self.labelFrameTitle, text=keys[x])
            self.labelField1.grid(row=x, column=0, padx=10, pady=5)
            self.labelValues = tk.Label(self.labelFrameTitle, text=values[x],bg='white')
            self.labelValues.grid(row=x, column=1, padx=10, pady=5)
    def tablas(self):
        font_title = ("Arial", 10, "bold")
        self.labelTitleTable1=tk.Label(self,text='datos de pH',font=font_title,bg='#dcdcdc')
        self.labelTitleTable1.place(x=250, y=5)
        self.tabla_ph=ttk.Treeview(self,
                                   column=("inicio", "trabajo"))
        self.tabla_ph.place(x=80,y=30)
        self.tabla_ph.heading('#0', text='id')
        self.tabla_ph.heading('#1', text='pH')
        self.tabla_ph.heading('#2', text='fecha')
        self.tabla_ph.column('#0', width=100,anchor=tk.CENTER)
        self.tabla_ph.column('#1', width=150,anchor=tk.CENTER)
        self.tabla_ph.column('#2', width=200,anchor=tk.CENTER)
        #Datos MySQL
        datosPh = [{'idclientelogo': 1, 'status': '7.88', 'date': '04/27/2022 18:05:06'},
                   {'idclientelogo': 2, 'status': '6.89', 'date': '04/28/2022, 23:15:06'},
                   {'idclientelogo': 32, 'status': '7.2', 'date': '04/28/2022, 23:45:01'},
                   {'idclientelogo': 33, 'status': '8.4', 'date': '04/28/2022, 23:46:14'},
                   {'idclientelogo': 34, 'status': '5.9', 'date': '04/28/2022, 23:47:24'},
                   {'idclientelogo': 35, 'status': '7.9', 'date': '04/28/2022, 23:47:40'},
                   {'idclientelogo': 36, 'status': '7.2', 'date': '04/29/2022, 19:59:03'},
                   {'idclientelogo': 37, 'status': '8.1', 'date': '04/29/2022, 19:59:36'},
                   {'idclientelogo': 37, 'status': '8.1', 'date': '04/29/2022, 19:59:36'},
                   {'idclientelogo': 37, 'status': '8.1', 'date': '04/29/2022, 19:59:36'},
                   {'idclientelogo': 37, 'status': '8.1', 'date': '04/29/2022, 19:59:36'},
                   {'idclientelogo': 37, 'status': '8.1', 'date': '04/29/2022, 19:59:36'},
                   {'idclientelogo': 37, 'status': '8.1', 'date': '04/29/2022, 19:59:36'},
                   {'idclientelogo': 37, 'status': '8.1', 'date': '04/29/2022, 19:59:36'},
                   {'idclientelogo': 38, 'status': '7.0', 'date': '04/29/2022, 20:01:41'}]
        for x in range(len(datosPh)):
            lista = list(datosPh[x].values())
            index = str(x)
            print(index)
            lista = lista[1:]
            self.tabla_ph.insert('', 0, text=index, values=lista)

        self.labelTitleTable2 = tk.Label(self, text='datos de bomba', font=font_title, bg='#dcdcdc')
        self.labelTitleTable2.place(x=250, y=260)
        self.tabla_bomba = ttk.Treeview(self,
                                     column=("inicio", "trabajo"))
        self.tabla_bomba.place(x=80, y=280)
        self.tabla_bomba.heading('#0', text='id')
        self.tabla_bomba.heading('#1', text='status')
        self.tabla_bomba.heading('#2', text='fecha')
        self.tabla_bomba.column('#0', width=100, anchor=tk.CENTER)
        self.tabla_bomba.column('#1', width=150, anchor=tk.CENTER)
        self.tabla_bomba.column('#2', width=200, anchor=tk.CENTER)
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
            self.tabla_bomba.insert('', 0, text=index, values=lista)









    """"
            #DATA REPORT
        self.label_k = tk.Label(self, text='La bomba se ha prendido 10 veces durante el dia')
        self.label_k.config(font=('Arial', 12, 'bold'))
        self.label_k.grid(row=6, column=0, padx=10, pady=10)

        self.label_12 = tk.Label(self, text='Anita lava la tina')
        self.label_12.config(font=('Arial', 12, 'bold'))
        self.label_12.grid(row=1, column=5, padx=10, pady=10)

        self.label_12 = tk.Label(self, text='Anita lava la tina')
        self.label_12.config(font=('Arial', 12, 'bold'))
        self.label_12.grid(row=2, column=5, padx=10, pady=10)

        self.label_12 = tk.Label(self, text='Anita lava la tina')
        self.label_12.config(font=('Arial', 12, 'bold'))
        self.label_12.grid(row=3, column=5, padx=10, pady=10)



        self.label_k = tk.Label(self, text='El consumo de energia es de 1 kW')
        self.label_k.config(font=('Arial', 12, 'bold'))
        self.label_k.grid(row=7, column=0, padx=10, pady=10)
        #canvas


            #DATA PREDICTIONS


        self.label_k = tk.Label(self, text='Grafico a futuro')
        self.label_k.config(font=('Arial', 12, 'bold'))
        self.label_k.grid(row=6, column=3, padx=10, pady=10)


        #inputs
        self.input_kpi =  ttk.Combobox(self,values=["Ph","Bomba"])
        items=("ph","bomba")
        #self.input_kpi.


        self.input_kpi.grid(row=0,column=1)
        #self.input_kpi.config(width=50)

        #botones
        self.boton_select=tk.Button(self,text="Consultar")
        self.boton_select.config(width=20,font=('Arial',12,'bold'),fg='red')
        self.boton_select.grid(row=0,column=3,padx=10,pady=10)

    def tabla_bomba(self):
        self.tabla_bomba=ttk.Treeview(self,
                                      column=("inicio","trabajo"))
        self.tabla_bomba.grid(row=4,column=0,columnspan=4)
        self.tabla_bomba.heading('#0',text='ID')
        self.tabla_bomba.heading('#1', text='status')
        self.tabla_bomba.heading('#2', text='fecha')
        datos = [{'idclientelogo': 1, 'status': 'ON', 'date': '04/27/2022, 18:05:06'},
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
        for x in range(len(datos)):
            lista=list(datos[x].values())
            index=str(x)
            print(index)
            lista = lista[1:]
            self.tabla_bomba.insert('',0,text=index,values=lista)

    def tabla_ph(self):
        self.tabla_ph = ttk.Treeview(self,
                                        column=("inicio", "trabajo"))
        self.tabla_ph.grid(row=5, column=0, columnspan=4)
        self.tabla_ph.heading('#0', text='ID')
        self.tabla_ph.heading('#1', text='PH')
        self.tabla_ph.heading('#2', text='Fecha')
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
            self.tabla_ph.insert('', 0, text=index, values=lista)

    def my_canvas(self):
        self.canva = tk.Canvas(self, width=480 , heigh=200, bg="red")
        self.canva.grid(row=4, column=5, columnspan=5, rowspan=8 ,padx=10, pady=10)    """
