from tkinter import *
import re, sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
from turtle import width
import mysql.connector

import formularios.formularioadmin
class VentanaEmergente:
    def __init__(self,usuario):
        self.ventana1=tk.Tk()
        self.ventana1.title("Modificar profesor")
        self.ventana1.config(bg='Light cyan')
        self.ventana1.geometry("1150x650")
        self.ventana1.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")
        self.usuarioName=usuario

        self.decoraframe=tk.Frame(self.ventana1,bg="dark blue",height=20)
        self.decoraframe.pack(fill="both",expand="no",side="top")
        
        self.lista=LabelFrame(self.ventana1,text="Lista de profesores",font=("Times New Roman",10))
        self.lista.config(bg="light cyan")
        self.lista.pack(fill="both",expand="no",padx=5,pady=5,side="top")

        self.tree = ttk.Treeview(self.lista,columns=("#1","#2","#3","#4","#5","#6","#7","#8","#9","#10","#11","#12"),height="7")
        self.tree.heading("#0",text="Cedula de identidad")
        self.tree.heading("#1",text="Nombres")
        self.tree.heading("#2",text="Apellidos")
        self.tree.heading("#3",text="Teléfono")
        self.tree.heading("#4",text="Dirección")
        self.tree.heading("#5",text="Ingreso")
        self.tree.heading("#6",text="Nacimiento")
        self.tree.heading("#7",text="Edad")
        self.tree.heading("#8",text="RIF")
        self.tree.heading("#9",text="Email")
        self.tree.heading("#10",text="Sexo")
        self.tree.heading("#11",text="Cargo")
        self.tree.heading("#12",text="Programa")

        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.tree.get_children()

        for elemento in profesor:
            self.tree.delete(elemento)
        try:
            cur.execute("SELECT a.cedula_identidad, a.nombres, a.apellidos, a.telefono, a.direccion, a.fecha_ingreso, a.fecha_nacimiento, a.edad, a.rif, a.email,a.sexo, b.nombre_cargo,d.nombre_programa FROM profesor a, cargo b, programa d WHERE a.cedula_identidad NOT IN ('111111','222222') AND b.id_cargo=a.id_cargo AND d.id_programa=a.id_programa ORDER BY a.nombres DESC")
            for row in cur:
                self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]))
        except:
            pass

        con.close()
        self.tree.column("#0",width=113)
        self.tree.column("#1",width=95)
        self.tree.column("#2",width=80)
        self.tree.column("#3",width=80)
        self.tree.column("#4",width=120)
        self.tree.column("#5",width=80)
        self.tree.column("#6",width=80)
        self.tree.column("#7",width=35)
        self.tree.column("#8",width=80)
        self.tree.column("#9",width=150)
        self.tree.column("#10",width=35)
        self.tree.column("#11",width=70)
        self.tree.column("#12",width=70)

        self.tree.bind("<1>",self.getrow)
        self.tree.pack(side="left",fill="both",padx=5,pady=5)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.lista, orient="vertical", command = self.tree.yview)
        scrolvert.pack(side="left",fill="y")
        self.tree.config(yscrollcommand=scrolvert.set)

        # SCROLL HORIZONTAL TREEVIEW
        #scrolhoriz = st.Scrollbar(self.lista, orient="horizontal", command = self.tree.xview)
        #scrolhoriz.pack(side="bottom",fill="x")
        #self.tree.config(xscrollcommand=scrolhoriz)

        #####################################
        ######### Label frame ###############

        self.buscador=tk.LabelFrame(self.ventana1,text='Buscador',font=("Times New Roman",10))
        self.buscador.config(bg="light cyan")
        self.modificar=tk.LabelFrame(self.ventana1,text="Actualizar informacion",font=("Times New Roman",10))
        self.modificar.config(bg="light cyan")

        self.buscador.pack(fill="both",expand="no",padx=5,pady=20,side="left")
        self.modificar.pack(fill="both",expand="yes",padx=20,pady=20,side="right")

        #### Frame Logo

        self.frameLogo=tk.Frame(self.buscador,bg="light blue",width=249,height=193)
        self.frameLogo.place(x=15, y= 169)

        self.imagen=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\Orquesta.png")
        fondo=tk.Label(self.frameLogo,image=self.imagen,bg="light cyan").place(x=0,y=0)

        #######################################
        ###       Para el self.buscador         ####

        label1=tk.Label(self.buscador,text="Consulta por:",bg="Light cyan",font=("Times New Roman",10))
        label1.grid(row=1,column=0,padx=5,pady=5)

        lableBucar=tk.Label(self.buscador,text="Buscar:",bg="Light cyan",font=("Times New Roman",10))
        lableBucar.grid(row=5,column=0,padx=5,pady=5)

        self.buscador1=tk.StringVar()
        self.entry1=tk.Entry(self.buscador,width=30,textvariable=self.buscador1,font=("Times New Roman",10))
        self.entry1.grid(row=5,column=1,padx=5,pady=5)


        self.opcion=tk.StringVar()
        opcionesBusqueda=("Nombres","Apellidos","Cédula","Fecha de ingreso","Cargo","Programa")
         
        self.comobox1=ttk.Combobox(self.buscador,
                                width=20,
                                textvariable=self.opcion,
                                values=opcionesBusqueda,
                                state='readonly',
                                font=("Times New Roman",10))
        self.comobox1.current(1)

       
        self.comobox1.grid(row=1,column=1)
        ################## combobox interactivo

        lableBucar=tk.Label(self.buscador,text="Programa:",bg="Light cyan",font=("Times New Roman",10))
        lableBucar.grid(row=4,column=0,padx=5,pady=5)

        self.opcionPrograma=tk.StringVar()
        self.comoboxProgramaBus=ttk.Combobox(self.buscador,
                                width=20,
                                textvariable=self.opcionPrograma,
                                state='readonly',
                                font=("Times New Roman",10))

        self.comoboxProgramaBus['value']=self.cargarComboProgramasAdmin()
        self.comoboxProgramaBus.grid(row=4,column=1,padx=5,pady=15)

        self.comoboxProgramaBus.current(0)

        btnBuscar=tk.Button(self.buscador,text="Buscar",command=self.search)
        btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",10))
        btnBuscar.grid(row=6,column=0,padx=5,pady=5)

        btnLimpiar=tk.Button(self.buscador,text="Limpiar",command=self.clear)
        btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",10))
        btnLimpiar.grid(row=6,column=1,padx=5,pady=5)

        

        ############################################
        ################### Para self.modificar #########


        label2=tk.Label(self.modificar,text="(*)Cédula de identidad:",bg="Light cyan",font=("Times New Roman",10))
        label2.grid(row=1,column=0,padx=10,pady=10)

        label3=tk.Label(self.modificar,bg="light cyan",text="Nombres:",font=("Times New Roman",10))
        label3.grid(row=2,column=0,padx=10,pady=10)

        label4=tk.Label(self.modificar,text="Apellidos:",bg="Light cyan",font=("Times New Roman",10))
        label4.grid(row=3,column=0,padx=10,pady=10)

        label5=tk.Label(self.modificar,bg="light cyan",text="Télefono:",font=("Times New Roman",10))
        label5.grid(row=4,column=0,padx=10,pady=10)

        label6=tk.Label(self.modificar,text="Dirección:",bg="Light cyan",font=("Times New Roman",10))
        label6.grid(row=5,column=0,padx=10,pady=10)

        label7=tk.Label(self.modificar,bg="light cyan",text="Fecha de ingreso:",font=("Times New Roman",10))
        label7.grid(row=6,column=0,padx=10,pady=10)

        label8=tk.Label(self.modificar,bg="light cyan",text="Fecha de nacimiento:",font=("Times New Roman",10))
        label8.grid(row=7,column=0,padx=10,pady=10)

        label9=tk.Label(self.modificar,bg="light cyan",text="Edad:",font=("Times New Roman",10))
        label9.grid(row=8,column=0,padx=10,pady=10)


        ###############################
        self.tci=tk.StringVar()
        self.tnom=tk.StringVar()
        self.tape=tk.StringVar()
        self.ttel=tk.StringVar()
        self.tdir=tk.StringVar()
        self.tingreso=tk.StringVar()
        self.tnaci=tk.StringVar()
        self.tedad=tk.StringVar()

        
        self.entryci=ttk.Entry(self.modificar,textvariable=self.tci,font=("Times New Roman",10))
        self.entryci.grid(row=1,column=1,padx=10,pady=10)

        self.entryNom=ttk.Entry(self.modificar,textvariable=self.tnom,font=("Times New Roman",10))
        self.entryNom.grid(row=2,column=1,padx=10,pady=10)

        self.entryApe=ttk.Entry(self.modificar,textvariable=self.tape,font=("Times New Roman",10))
        self.entryApe.grid(row=3,column=1,padx=10,pady=10)

        self.entryTel=ttk.Entry(self.modificar,textvariable=self.ttel,font=("Times New Roman",10))
        self.entryTel.grid(row=4,column=1,padx=10,pady=10)

        self.entryDir=ttk.Entry(self.modificar,textvariable=self.tdir,font=("Times New Roman",10))
        self.entryDir.grid(row=5,column=1,padx=10,pady=10)

        self.entryIngreso=ttk.Entry(self.modificar,textvariable=self.tingreso,font=("Times New Roman",10))
        self.entryIngreso.grid(row=6,column=1,padx=10,pady=10)

        self.entryNaci=ttk.Entry(self.modificar,textvariable=self.tnaci,font=("Times New Roman",10))
        self.entryNaci.grid(row=7,column=1,padx=10,pady=10)

        self.entryEdad=ttk.Entry(self.modificar,textvariable=self.tedad,font=("Times New Roman",10))
        self.entryEdad.grid(row=8,column=1,padx=10,pady=10)

        ####################################
        #         Otra columna


        label10=tk.Label(self.modificar,bg="light cyan",text="RIF:",font=("Times New Roman",10))
        label10.grid(row=1,column=3,padx=10,pady=10)

        label11=tk.Label(self.modificar,bg="light cyan",text="Email:",font=("Times New Roman",10))
        label11.grid(row=2,column=3,padx=10,pady=10)

        label12=tk.Label(self.modificar,bg="light cyan",text="Sexo:",font=("Times New Roman",10))
        label12.grid(row=3,column=3,padx=10,pady=10)

        label13=tk.Label(self.modificar,bg="light cyan",text="(*)Cargo:",font=("Times New Roman",10))
        label13.grid(row=4,column=3,padx=10,pady=10)

        label14=tk.Label(self.modificar,bg="light cyan",text="(*)Programa:",font=("Times New Roman",10))
        label14.grid(row=5,column=3,padx=10,pady=10)

        ##########################################
        self.trif=tk.StringVar()
        self.temail=tk.StringVar()
        self.opcionSexo=tk.StringVar()

        self.entryRIF=ttk.Entry(self.modificar,textvariable=self.trif,font=("Times New Roman",10))
        self.entryRIF.grid(row=1,column=4,padx=10,pady=10)

        self.entryEmail=ttk.Entry(self.modificar,textvariable=self.temail,font=("Times New Roman",10))
        self.entryEmail.grid(row=2,column=4,padx=10,pady=10)


        opcionesSexo=("F","M")
        self.comobox4=ttk.Combobox(self.modificar,
                                width=20,
                                textvariable=self.opcionSexo,
                                values=opcionesSexo,
                                state='readonly',
                                font=("Times New Roman",10))
        self.comobox4.current(0)
        self.comobox4.grid(row=3,column=4,padx=10,pady=10)


        self.opcionCargo=tk.StringVar()
        self.comoboxCargo=ttk.Combobox(self.modificar,
                                width=20,
                                textvariable=self.opcionCargo,
                                state='readonly',
                                font=("Times New Roman",10))
        self.comoboxCargo['value']=self.cargarComboCargoAdmin()
        
        self.comoboxCargo.grid(row=4,column=4)
        self.comoboxCargo.current(0)
        
        ############### Combobox interactivo

        self.opcionPrograma=tk.StringVar()
        self.comoboxPrograma=ttk.Combobox(self.modificar,
                                width=20,
                                textvariable=self.opcionPrograma,
                                state='readonly',
                                font=("Times New Roman",10))

        self.comoboxPrograma['value']=self.cargarComboProgramasAdmin()
        self.comoboxPrograma.grid(row=5,column=4,padx=5,pady=15)

        self.comoboxPrograma.current(0)


        ##################### BOTONES #######################

        btnAgregar=tk.Button(self.modificar,text="Agregar",command=self.add_new,font=("Times New Roman",10))
        btnAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        #btnAgregar.grid(row=1,column=6,padx=2,pady=4)
        btnAgregar.place(x=580,y=60,width=100,height=50)


        btnModificar=tk.Button(self.modificar,text="Modificar",command=self.update_profe,font=("Times New Roman",10))
        btnModificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnModificar.place(x=580,y=120,width=100,height=50)

        btnEliminar=tk.Button(self.modificar,text="Eliminar",command=self.delete_profe,font=("Times New Roman",10))
        btnEliminar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnEliminar.place(x=580,y=180,width=100,height=50)

        btnVolver=tk.Button(self.modificar,text="Volver",command=self.volver,font=("Times New Roman",10))
        btnVolver.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnVolver.place(x=580,y=240,width=100,height=50)

        ################### DECORACIONES #####################

        framedeco=tk.Frame(self.ventana1)
        framedeco.config(bg="Dark blue",bd=5,height="20",width="40")
        framedeco.pack(fill="both",expand="no",padx=5,pady=20,side="left")

        self.ventana1.resizable(False,False)
        self.ventana1.mainloop()

    ######################### COmbobox interactivo Programas
    def cargarComboProgramasAdmin(self):
        query="SELECT nombre_programa FROM programa"

        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        db_rows=cursor.fetchall()
        data=[]
        for rows in db_rows:
            data.append(rows[0])
        return data

    def cargarComboCargoAdmin(self):
        query="SELECT nombre_cargo FROM cargo"

        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        db_rows=cursor.fetchall()
        data=[]
        for rows in db_rows:
            data.append(rows[0])
        return data
    ##########################################################
    
    def search(self):
        opcioncontrol=self.comobox1.get()
        opcionPrograma=self.comoboxProgramaBus.get()
        buscarLista=self.entry1.get()
        if opcioncontrol=="Nombres":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cedula_identidad, a.nombres, a.apellidos, a.telefono, a.direccion, a.fecha_ingreso, a.fecha_nacimiento, a.edad, a.rif, a.email,a.sexo, b.nombre_cargo,d.nombre_programa FROM profesor a, cargo b, programa d WHERE a.nombres LIKE '%"+buscarLista+"%' AND d.nombre_programa='"+opcionPrograma+"' AND a.cedula_identidad NOT IN ('222222','111111') AND b.id_cargo=a.id_cargo AND d.id_programa=a.id_programa ORDER BY a.nombres DESC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateLista(respuesta)

        if opcioncontrol=="Apellidos":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cedula_identidad, a.nombres, a.apellidos, a.telefono, a.direccion, a.fecha_ingreso, a.fecha_nacimiento, a.edad, a.rif, a.email,a.sexo, b.nombre_cargo,d.nombre_programa FROM profesor a, cargo b, programa d WHERE a.apellidos LIKE '%"+buscarLista+"%' AND d.nombre_programa='"+opcionPrograma+"' AND a.cedula_identidad NOT IN ('222222','111111') AND b.id_cargo=a.id_cargo AND d.id_programa=a.id_programa ORDER BY a.nombres DESC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateLista(respuesta)

        if opcioncontrol=="Cédula":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cedula_identidad, a.nombres, a.apellidos, a.telefono, a.direccion, a.fecha_ingreso, a.fecha_nacimiento, a.edad, a.rif, a.email,a.sexo, b.nombre_cargo,d.nombre_programa FROM profesor a, cargo b, programa d WHERE a.cedula_identidad LIKE '%"+buscarLista+"%' AND d.nombre_programa='"+opcionPrograma+"' AND a.cedula_identidad NOT IN ('222222','111111') AND b.id_cargo=a.id_cargo AND d.id_programa=a.id_programa ORDER BY a.nombres DESC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateLista(respuesta)

        if opcioncontrol=="Fecha de ingreso":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cedula_identidad, a.nombres, a.apellidos, a.telefono, a.direccion, a.fecha_ingreso, a.fecha_nacimiento, a.edad, a.rif, a.email,a.sexo, b.nombre_cargo,d.nombre_programa FROM profesor a, cargo b, programa d WHERE a.fecha_ingreso LIKE '%"+buscarLista+"%' AND d.nombre_programa='"+opcionPrograma+"' AND a.cedula_identidad NOT IN ('222222','111111') AND b.id_cargo=a.id_cargo AND d.id_programa=a.id_programa ORDER BY a.nombres DESC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateLista(respuesta)

        if opcioncontrol=="Cargo":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cedula_identidad, a.nombres, a.apellidos, a.telefono, a.direccion, a.fecha_ingreso, a.fecha_nacimiento, a.edad, a.rif, a.email,a.sexo, b.nombre_cargo,d.nombre_programa FROM profesor a, cargo b, programa d WHERE b.nombre_cargo LIKE '%"+buscarLista+"%' AND d.nombre_programa='"+opcionPrograma+"' AND a.cedula_identidad NOT IN ('222222','111111') AND b.id_cargo=a.id_cargo AND d.id_programa=a.id_programa ORDER BY a.nombres DESC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateLista(respuesta)

        if opcioncontrol=="Programa":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cedula_identidad, a.nombres, a.apellidos, a.telefono, a.direccion, a.fecha_ingreso, a.fecha_nacimiento, a.edad, a.rif, a.email,a.sexo, b.nombre_cargo,d.nombre_programa FROM profesor a, cargo b, programa d WHERE d.nombre_programa='"+opcionPrograma+"' AND a.cedula_identidad NOT IN ('222222','111111') AND b.id_cargo=a.id_cargo AND d.id_programa=a.id_programa ORDER BY a.nombres DESC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateLista(respuesta)

    def clear(self):
        query="SELECT a.cedula_identidad, a.nombres, a.apellidos, a.telefono, a.direccion, a.fecha_ingreso, a.fecha_nacimiento, a.edad, a.rif, a.email,a.sexo, b.nombre_cargo,d.nombre_programa FROM profesor a, cargo b, programa d WHERE a.cedula_identidad NOT IN ('111111','222222') AND b.id_cargo=a.id_cargo AND d.id_programa=a.id_programa ORDER BY a.nombres DESC"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.buscador1.set("")
        self.updateLista(respuesta)

    def updateLista(self,respuesta):
        info=self.tree.get_children()

        for elemento in info:
            self.tree.delete(elemento)
        for row in respuesta:
            self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]))

    def getrow(self,event):
        rowid=self.tree.identify_row(event.y)
        self.tree.selection_set(rowid)
        item=self.tree.item(self.tree.focus())
        self.ci=item["text"]
        
        ############ Busca la informacion en la base de datos

        query="SELECT a.cedula_identidad, a.nombres, a.apellidos, a.telefono, a.direccion, a.fecha_ingreso, a.fecha_nacimiento, a.edad, a.rif, a.email,a.sexo, b.nombre_cargo,d.nombre_programa FROM profesor a, cargo b, programa d WHERE a.cedula_identidad='"+self.ci+"' AND a.cedula_identidad NOT IN ('111111','222222') AND b.id_cargo=a.id_cargo AND d.id_programa=a.id_programa"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        
        if len(respuesta)>0:
            self.tci.set(respuesta[0][0])
            self.tnom.set(respuesta[0][1])
            self.tape.set(respuesta[0][2])
            self.ttel.set(respuesta[0][3])
            self.tdir.set(respuesta[0][4])
            self.tingreso.set(respuesta[0][5])
            self.tnaci.set(respuesta[0][6])
            self.tedad.set(respuesta[0][7])
            self.trif.set(respuesta[0][8])
            self.temail.set(respuesta[0][9])
            self.comobox4.set(respuesta[0][10])
            self.comoboxCargo.set(respuesta[0][11])
            self.comoboxPrograma.set(respuesta[0][12])
   
    def definir_cargo(self):
        opcioncontrol=self.opcionCargo.get()
        query="SELECT id_cargo FROM cargo WHERE nombre_cargo='"+opcioncontrol+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()

        return respuesta[0][0]

    def definir_programa(self):
        opcioncontrol=self.opcionPrograma.get()
        query="SELECT id_programa FROM programa WHERE nombre_programa='"+opcioncontrol+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()

        return respuesta[0][0]

    ###### Restricciones ###########
    def validar_Cedula(self):
        cedula=self.tci.get()
        validar=re.match('[0-999999]+$',cedula,re.I)
        if cedula=="":
            #self.entryci.config(border='1 px solid yellow')
            return False
        elif not validar:
            #self.entryci.config(border='1 px solid red')
            return False
        else:
            #self.entryci.config(border='1 px solid green')
            return True
    ###############################

    def add_new(self):
        cedula_identidad=self.tci.get()
        nombres=self.tnom.get()
        apellidos=self.tape.get()
        telefono=self.ttel.get()
        direccion=self.tdir.get()
        fingreso=self.tingreso.get()
        fnacimiento=self.tnaci.get()
        edad=self.tedad.get()
        RIF=self.trif.get()
        email=self.temail.get()
        sexo=self.opcionSexo.get()
        cargo=self.definir_cargo()
        programa=self.definir_programa()

        try:
            if self.validar_Cedula():
                query="INSERT INTO profesor(cedula_identidad,nombres,apellidos,telefono,direccion,fecha_ingreso,fecha_nacimiento,edad,rif,email,sexo,id_cargo,id_programa) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(cedula_identidad,nombres,apellidos,telefono,direccion,fingreso,fnacimiento,edad,RIF,email,sexo,cargo,programa))
                
                cone.commit()
                cone.close()
                self.clear()
                mb.showinfo("Información","Se han cargado con éxito los datos.")
                self.tci.set("")
                self.tnom.set("")
                self.tape.set("")
                self.ttel.set("")
                self.tdir.set("")
                self.tingreso.set("")
                self.tnaci.set("")
                self.tedad.set("")
                self.trif.set("")
                self.temail.set("")
            else:
                mb.showwarning("Error","Debe completar los campos obligatorios")
        except:
            mb.showinfo("Información","Este dato ya existe")

    def update_profe(self):
        
        cedula_identidad=self.tci.get()
        nombres=self.tnom.get()
        apellidos=self.tape.get()
        telefono=self.ttel.get()
        direccion=self.tdir.get()
        fingreso=self.tingreso.get()
        fnacimiento=self.tnaci.get()
        edad=str(self.tedad.get())
        RIF=self.trif.get()
        email=self.temail.get()
        sexo=self.opcionSexo.get()
        cargo=str(self.definir_cargo())
        programa=str(self.definir_programa())

        

        if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea actualizar estos datos? "):
            if self.validar_Cedula():
            
                query="UPDATE profesor p JOIN cargo c ON p.id_cargo=c.id_cargo JOIN programa r ON p.id_programa=r.id_programa SET p.cedula_identidad=%s,p.nombres=%s,p.apellidos=%s,p.telefono=%s,p.direccion=%s,p.fecha_ingreso=%s,p.fecha_nacimiento=%s,p.edad=%s,p.rif=%s,p.email=%s,p.sexo=%s,p.id_cargo=%s,p.id_programa=%s WHERE p.cedula_identidad='"+self.ci+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(cedula_identidad,nombres,apellidos,telefono,direccion,fingreso,fnacimiento,edad,RIF,email,sexo,cargo,programa))
                

                cone.commit()
                cone.close()

                self.clear()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han cargado con éxito los datos.")
                    self.tci.set("")
                    self.tnom.set("")
                    self.tape.set("")
                    self.ttel.set("")
                    self.tdir.set("")
                    self.tingreso.set("")
                    self.tnaci.set("")
                    self.tedad.set("")
                    self.trif.set("")
                    self.temail.set("")
                else:
                    mb.showinfo("Informacion", "No existe un profesor con dicha informacion")
                
            else:
                mb.showwarning("Error","Debe seleccionar los campos a self.modificar")
        else:
            return True

    def delete_profe(self):
        cedula_identidad=self.tci.get()
        try:
            if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea borrar estos datos? "):
                query="DELETE FROM profesor WHERE cedula_identidad='"+cedula_identidad+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query)
            
                cone.commit()
                cone.close()
                self.clear()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han borrado los datos con éxito.")
                    self.tci.set("")
                    self.tnom.set("")
                    self.tape.set("")
                    self.ttel.set("")
                    self.tdir.set("")
                    self.tingreso.set("")
                    self.tnaci.set("")
                    self.tedad.set("")
                    self.trif.set("")
                    self.temail.set("")
                else:
                    mb.showinfo("Informacion", "No existe un profesor con dicha informacion")
                

            else:
                return True
        except:
            mb.showwarning("Error","Introduzca la informacion que desee borrar o selecione en la tabla.")

    def abrir(self):

            conexion=mysql.connector.connect(host="localhost",
                                            user="root",
                                            passwd="", 
                                            database="bdnucleolecheria")
            return conexion
    
    def volver(self):
        self.ventana1.destroy()
        app=formularios.formularioadmin.Administrador(self.usuarioName)

