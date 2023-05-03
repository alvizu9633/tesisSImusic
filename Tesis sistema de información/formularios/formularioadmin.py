from cProfile import label
from cgitb import text
from distutils import command
from sqlite3 import Cursor
from textwrap import fill
import tkinter as tk
import re,sys
from tkinter import LEFT, W, PhotoImage, messagebox as mb
from tkinter import scrolledtext as st
from tkinter import ttk
from tokenize import String
from turtle import heading, left, width
from urllib import response
from tkinter import ttk
from pygame import mixer

import mysql.connector

import formularios.formulariousuario

import formularios.detalleProfesor.formularioModificar

class Administrador:

    def __init__(self,usuario):
        
        ###Programa estandar para las ventanas ---------------------
        self.ventana1=tk.Tk()
        self.ventana1.title("Administrador")
        self.ventana1.geometry("1050x650")
        self.ventana1.config(bg='light cyan',bd=15)
        self.ventana1.resizable(0,0)
        self.ventana1.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")
        #-------------------------------------------------------

        #Frame admin decorativo
        self.frame1=tk.Frame(self.ventana1)

        #Frame admin informacion tentativa
        self.frame2=tk.Frame(self.ventana1)

        #Frame informacion de los usuarios
        self.frame3=tk.Frame(self.ventana1)
        self.frame3.config(bg="dark blue",bd=11)
        self.frame3.place(x=-15,y=-15,width=1050,height=70)

        # Información usuario

        self.UsuarioName=usuario
        self.id_usuario=tk.StringVar()
        self.id_usuario.set(self.UsuarioName)
    
        labelUsuario=tk.Label(self.frame3,text="Usuario: "+self.id_usuario.get(),bg="dark blue",font=("Times New Roman",15), fg="white")
        labelUsuario.place(x=830,y=7)

        #label informacion de profesores
        self.label1=tk.Label(self.frame3,text="Administrador",bg="dark blue",font=("Times New Roman",20), fg="white")
        self.label1.place(x=110,y=10)

        ##-------------------Botones predeterminados --------------------------

            #Boton menu
        self.hidemenu=0
        self.botonmenu=tk.Button(self.frame3,text="Menu", command=self.ocultarmostrarMenu,bg="blueviolet", bd= 5,font=("Times New Roman",15), fg="white",activebackground="light blue",activeforeground="Black")
        self.photo=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\home.png")
        self.botonmenu.config( image=self.photo, compound=LEFT)
        self.botonmenu.place(x=10,y=5)
        

        self.profesores()
        mixer.init()
        mixer.music.load("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\Sonido\\Inicio.mp3")
        mixer.music.play()

        #Mainloop----------------------------------------------
        self.ventana1.mainloop()

    def ocultarmostrarMenu(self):
        
        if self.hidemenu==0:
            self.frame1.place_forget()#place(x=-70,y=0,width=350,height=800)
            self.frame2.place_forget()#place(x=-100,y=0,width=400,height=800)
            self.hidemenu=1
        else:
             #Frame admin decorativo
            self.frame1=tk.Frame(self.ventana1)
            self.frame1.config(bg="dark blue")
            self.frame1.place(x=55,y=55,width=250,height=800)

             #### Frame Logo

            self.frameLogo=tk.Frame(self.frame1,bg="light blue",width=250,height=800)
            self.frameLogo.place(x=0, y= 0)

            self.imagen1=tk.PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\borde_menu.png")
            fondo2=tk.Label(self.frameLogo,image=self.imagen1,bg="light cyan").place(x=0,y=0)
        

            #Frame admin informacion tentativa
            self.frame2=tk.Frame(self.ventana1)
            self.frame2.config(bg="light blue")
            self.frame2.place(x=-15,y=55,width=300,height=800)

            ##-------------------Botones predeterminados --------------------------

            #Boton menu
            self.hidemenu=0
        
            #Boton gestion profesores
            self.boton1=tk.Button(self.frame2,text="Gestionar profesores",command=self.profesores,bg="blueviolet", bd= 5,font=("Times New Roman",15), fg="white")
            self.boton1.place(x=40,y=20,width=200,height=50)

            #Boton gestion usuarios
            self.boton2=tk.Button(self.frame2,text="Gestionar usuarios",command=self.usuarios,bg="blueviolet", bd= 5,font=("Times New Roman",15), fg="white")
            self.boton2.place(x=40,y=100,width=200,height=50)

            #Boton gestion instrumentos
            self.boton3=tk.Button(self.frame2,text="Gestionar instrumentos",command=self.instrumentos,bg="blueviolet", bd= 5,font=("Times New Roman",15), fg="white")
            self.boton3.place(x=40,y=180,width=200,height=50)

            #Boton gestion clases
            self.boton4=tk.Button(self.frame2,text="Gestionar clases",command=self.clases,bg="blueviolet", bd= 5,font=("Times New Roman",15), fg="white")
            self.boton4.place(x=40,y=260,width=200,height=50)

            #Boton gestion alumnos
            self.boton5=tk.Button(self.frame2,text="Gestionar alumnos",command=self.alumnos,bg="blueviolet", bd= 5,font=("Times New Roman",15), fg="white")
            self.boton5.place(x=40,y=340,width=200,height=50)

            #Boton cerrar sesion
            self.boton6=tk.Button(self.frame2,text="Cerrar sesion",command=self.logout,bg="blueviolet", bd= 5,font=("Times New Roman",15), fg="white")
            self.boton6.place(x=40,y=420,width=200,height=50)
        
    def profesores(self):
        self.ocultarmostrarMenu()
        
        ########################################
        ##        Frame interactivo           ##
        ########################################

        self.frame4Interactivo=tk.Frame(self.ventana1)
        self.frame4Interactivo.config(bg='light cyan',bd=11)
        self.frame4Interactivo.place(x=-15,y=55,width=1050,height=580)
        
        #Label titulo
        self.labeltitulo=tk.Label(self.frame4Interactivo,text="Gestión de profesores",bg="light cyan",font=("Times New Roman",20), fg="Black")
        self.labeltitulo.place(x=20,y=30)

        #Label total
        self.label2=tk.Label(self.frame4Interactivo,text="Total profesores:",bg="light cyan",font=("Times New Roman",16), fg="Black")
        self.label2.place(x=40,y=70)

        #####################################################
        #######     Respuesta total profesores        #######
        #####################################################

        self.labelrespuesta=tk.Label(self.frame4Interactivo,text=" ",bg="light cyan",font=("Times New Roman",16), fg="Black")
        self.labelrespuesta.place(x=180,y=70)
        
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select COUNT(cedula_identidad)  from profesor WHERE cedula_identidad!='111111' AND cedula_identidad!='222222'"
        cursor.execute(sql)
        respuesta=cursor.fetchall() 
        self.cuenta=respuesta[0][0]
        cone.close()

        self.labelrespuesta.config(text=self.cuenta)

        #Ventanas creados al utilizar el boton

            ###Ventana para modificar/eliminar un profesor
        self.boton3=tk.Button(self.frame4Interactivo,text="Modificar",command=self.modificarProfesor,bg="blueviolet", bd= 5,font=("Times New Roman",16), fg="white",activebackground="light blue",activeforeground="Black")
        self.boton3.place(x=40,y=130,width=200,height=50)



        ############################################################################
        #########   Frame y labelframe listado de profesores por programa ##########
        ############################################################################

        ##Frame decorativo o marco

        self.framedecorativo=tk.Frame(self.frame4Interactivo)
        self.framedecorativo.config(bg="dark blue")
        self.framedecorativo.place(x=-15,y=240,width=1070,height=470)

        ##LabelFrame para el listado

        self.labelframe1=tk.LabelFrame(self.framedecorativo,text="Ordenados por programa",font=("Times New Roman",16),fg="white")
        self.labelframe1.config(bg="dark blue")
        self.labelframe1.place(x=10,y=13,height=80)

        ############### Combobox interactivo

        self.opcionPrograma=tk.StringVar()
        self.comobox2=ttk.Combobox(self.labelframe1,
                                width=20,
                                textvariable=self.opcionPrograma,
                                state='readonly',
                                font=("Times New Roman",14))

        self.comobox2['value']=self.cargarComboProgramasAdmin()
        self.comobox2.grid(row=2,column=2,padx=5,pady=15)

        self.comobox2.current(0)
        #################################################################

        btnBuscar=tk.Button(self.labelframe1,text="Buscar",command=self.searchProfesor,font=("Times New Roman",14),width=8)
        btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnBuscar.grid(row=2,column=4,padx=5,pady=5)

        btnLimpiar=tk.Button(self.labelframe1,text="Limpiar",command=self.clearProfesor,font=("Times New Roman",14),width=8)
        btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnLimpiar.grid(row=2,column=5,padx=5,pady=5)
    
            ##Frame para las busquedas

        self.framebusquedas=tk.Frame(self.framedecorativo,bg="light blue")
        self.framebusquedas.place(x=0,y=100,width=1050,height=210)

            #### Label frame agregar nuevo programa
        
        self.labelframeProgramas=tk.LabelFrame(self.framedecorativo,text="Agregar programa",font=("Times New Roman",16),fg="white")
        self.labelframeProgramas.config(bg="dark blue")
        self.labelframeProgramas.place(x=450,y=13,height=80)

        self.labelPrograma2=tk.Label(self.labelframeProgramas,text='Nombre del programa:',font=("Times New Roman",14),bg="dark blue",fg="white")
        self.labelPrograma2.grid(column=0,row=2,padx=5,pady=5)

        self.programaTxt=tk.StringVar()
        self.entryAggPrograma=tk.Entry(self.labelframeProgramas,font=("Times New Roman",14),width=15,textvariable=self.programaTxt)
        self.entryAggPrograma.grid(column=1,row=2,padx=5, pady=5)

        btnagregarPrograma=tk.Button(self.labelframeProgramas,text="Agregar",command=self.add_newProgram,font=("Times New Roman",14),width=10)
        btnagregarPrograma.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnagregarPrograma.grid(row=2,column=2,padx=5,pady=5)

        btnagregarModificar=tk.Button(self.labelframeProgramas,text="Modificar",command=self.modificarPrograma,font=("Times New Roman",14),width=10)
        btnagregarModificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnagregarModificar.grid(row=2,column=3,padx=5,pady=5)

        ###########################################################
        ################    botones de las pag    #################
        ###########################################################

            ##Tree para mostrar columnas
        self.tree = ttk.Treeview(self.framebusquedas,columns=("#1","#2","#3","#4","#5","#6","#7","#8","#9","#10","#11"),height="9")
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
        
            ##Tamano de columnas

        self.tree.column("#0",width=113)
        self.tree.column("#1",width=95)
        self.tree.column("#2",width=80)
        self.tree.column("#3",width=80)
        self.tree.column("#4",width=90)
        self.tree.column("#5",width=80)
        self.tree.column("#6",width=80)
        self.tree.column("#7",width=35)
        self.tree.column("#8",width=80)
        self.tree.column("#9",width=150)
        self.tree.column("#10",width=35)
        self.tree.column("#11",width=70)


        self.tree.pack(side="left",padx=10,pady=5)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.framebusquedas, orient="vertical", command = self.tree.yview)
        scrolvert.pack(side="left",fill="y")
        self.tree.config(yscrollcommand=scrolvert.set)

        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.tree.get_children()

        for elemento in profesor:
            self.tree.delete(elemento)
        try:
            cur.execute("SELECT a.cedula_identidad, a.nombres, a.apellidos, a.telefono, a.direccion, a.fecha_ingreso, a.fecha_nacimiento, a.edad, a.rif, a.email,a.sexo, b.nombre_cargo FROM profesor a, cargo b, programa d WHERE a.cedula_identidad NOT IN ('111111','222222') AND b.id_cargo=a.id_cargo AND d.id_programa=a.id_programa ORDER BY a.nombres DESC")
            for row in cur:
                self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
        except:
            pass

        self.frameLogo=tk.Frame(self.ventana1,bg="light blue",width=684,height=204)
        self.frameLogo.place(x=350, y= 60)

        self.imagen2=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\AN-N-LECHERÍAHorizontal684x204.png")
        fondo=tk.Label(self.frameLogo,image=self.imagen2,bg="light cyan").place(x=0,y=0)
    
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
    ##########################################################
    ############################## Agregar nuevo programa y modificarlo

    def add_newProgram(self):
        nombre_programa=self.programaTxt.get()

        try:
            if self.validar_contrasena(nombre_programa):
                query="INSERT INTO programa(id_programa,nombre_programa) VALUES(null,'"+nombre_programa+"')"

                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query)
                
                cone.commit()
                cone.close()
                self.comobox2['value']=self.cargarComboProgramasAdmin()
                mb.showinfo("Información","Se han cargado con éxito los datos.")
                self.programaTxt.set("")
            else:
                mb.showwarning("Error","Debe completar los campos obligatorios")
        except:
            mb.showinfo("Información","Este dato no cumple con los requisitos")

    def modificarPrograma(self):
        try:
            self.ventana1.destroy()
            self.ventana2=tk.Tk()
            self.ventana2.title("Modificar programa")
            self.ventana2.config(bg='dark blue')
            self.ventana2.geometry("625x450")
            self.ventana2.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")

                ###########------------------- Formulario label frame

            self.labelframe1=tk.LabelFrame(self.ventana2,text="Programas creados",fg="white",font=("Times New Roman",20))
            self.labelframe1.config(bg="dark blue")
            self.labelframe1.place(x=10,y=100,width=500,height=300)
            self.labelframe1.pack(pady=1)
                
                ###########################Label

            self.labelcedula=tk.Label(self.labelframe1,text="Identificacion del programa:",bg="dark blue",fg="white",font=("Times New Roman",12))
            self.labelcedula.grid(row=0,column=0,padx=10,pady=10)

            self.labelusuario=tk.Label(self.labelframe1,text="Nombre del programa:",bg="dark blue",fg="white",font=("Times New Roman",12))
            self.labelusuario.grid(row=1,column=0,padx=10,pady=10)


                ########################### Entry

            self.nombre_programaNuevo=tk.StringVar()
            self.IdPrograma=tk.StringVar()

                
            self.entryIdPrograma=ttk.Entry(self.labelframe1,textvariable=self.IdPrograma,font=("Times New Roman",12),state="readonly")
            self.entryIdPrograma.grid(row=0,column=1,padx=10,pady=10)

            self.entryProgramaNuevo=ttk.Entry(self.labelframe1,textvariable=self.nombre_programaNuevo,font=("Times New Roman",12))
            self.entryProgramaNuevo.grid(row=1,column=1,padx=10,pady=10)

            
                #################### Boton modificar, eliminar y volver

            btnmodificarPrograma=tk.Button(self.labelframe1,text="Modificar",command=self.update_programa)
            btnmodificarPrograma.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,width=15,font=("Times New Roman",12))
            btnmodificarPrograma.grid(row=6,column=0,padx=4,pady=4)

            btneliminarPrograma=tk.Button(self.labelframe1,text="Eliminar",command=self.delete_programa)
            btneliminarPrograma.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,width=15,font=("Times New Roman",12))
            btneliminarPrograma.grid(row=6,column=2,padx=4,pady=4)

            btnvolver=tk.Button(self.labelframe1,text="volver",command=self.volverAdminProfesor)
            btnvolver.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,width=15,font=("Times New Roman",12))
            btnvolver.grid(row=7,column=1,padx=4,pady=4)

            ############ Label frame treeview
            labelframeTreeProgram=tk.LabelFrame(self.ventana2,text="Lista de programas",fg="white",font=("Times New Roman",20))
            labelframeTreeProgram.config(bg="dark blue")
            labelframeTreeProgram.place(x=100,y=225,width=380,height=195)
            

            framebusquedas=tk.Frame(labelframeTreeProgram,bg="light blue")
            framebusquedas.grid(column=6,row=1,padx=20,pady=5,ipadx=10,ipady=10)
            ################### Treeview

             ##Tree para mostrar columnas
            self.tree = ttk.Treeview(framebusquedas,columns=("#1"),height="4")
            self.tree.heading("#0",text="Nombre programa")
            self.tree.heading("#1",text="Id Programa")

                ##Tamano de columnas

            self.tree.column("#0",width=200)
            self.tree.column("#1",width=110)

            self.tree.bind("<1>",self.getrow_programa)
            self.tree.pack(padx=10,pady=1,side="left")


            # SCROLL VERTICAL TREEVIEW
            scrolvert = st.Scrollbar(framebusquedas, orient="vertical", command = self.tree.yview)
            scrolvert.pack(side="left",fill="y")
            self.tree.config(yscrollcommand=scrolvert.set)

            con=mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="", 
                                        database="bdnucleolecheria")

            cur=con.cursor()
            programa=self.tree.get_children()

            for elemento in programa:
                self.tree.delete(elemento)
            try:
                cur.execute("SELECT id_programa, nombre_programa FROM programa ORDER BY nombre_programa DESC")
                rows=cur.fetchall()
                for row in rows:
                    self.tree.insert('',0,text=row[1],values=(row[0]))
            except:
                pass     
        except:
            pass


        self.ventana2.mainloop()

    def update_programa(self):
            
        programa=self.nombre_programaNuevo.get()
        id_programa=self.IdPrograma.get()

        if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea actualizar estos datos? "):
            if self.validar_contrasena(programa):
            
                query="UPDATE programa SET nombre_programa=%s WHERE id_programa=%s"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(programa,id_programa))
                

                cone.commit()
                cone.close()

                self.clearPrograma()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han cargado con éxito los datos.")
                    self.IdPrograma.set("")
                    self.nombre_programaNuevo.set("")

                else:
                    mb.showinfo("Informacion", "No existe un profesor con dicha informacion")
                
            else:
                mb.showwarning("Error","Debe seleccionar los campos a self.modificar")
        else:
            return True

    def volverAdminProfesor(self):
        self.ventana2.destroy()
        app=formularios.formularioadmin.Administrador(self.UsuarioName)

    def getrow_programa(self,event):
        rowid=self.tree.identify_row(event.y)
        self.tree.selection_set(rowid)
        item=self.tree.item(self.tree.focus())
        self.programa=item["text"]
        self.id_programa=item["values"]
        
        ############ Busca la informacion en la base de datos

        query="SELECT id_programa, nombre_programa FROM programa WHERE nombre_programa='"+self.programa+"'"
        
  
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall()
        cone.close()
        
        if len(respuesta)>0:
            self.IdPrograma.set(respuesta[0][0])
            self.nombre_programaNuevo.set(respuesta[0][1])
          
    def delete_programa(self):
        id_programa=self.IdPrograma.get()
        try:
            if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea borrar estos datos? "):
                query="DELETE FROM programa WHERE id_programa='"+id_programa+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query)
            
                cone.commit()
                cone.close()
                self.clearPrograma()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han borrado los datos con éxito.")
                    self.IdPrograma.set("")
                    self.nombre_programaNuevo.set("")

                else:
                    mb.showinfo("Informacion", "No existe un profesor con dicha informacion")
                

            else:
                return True
        except:
            mb.showwarning("Error","Introduzca la informacion que desee borrar o selecione en la tablaRepresentante.")

    def clearPrograma(self):
        query="SELECT id_programa, nombre_programa FROM programa ORDER BY nombre_programa DESC"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.updateListaPrograma(respuesta)

    def updateListaPrograma(self,respuesta):
        info=self.tree.get_children()

        for elemento in info:
            self.tree.delete(elemento)
        for row in respuesta:
            self.tree.insert("",0,text=row[1],values=(row[0]))
    ######### Metodos para gestion de profesores

    def searchProfesor(self):
        opcionPrograma=self.comobox2.get()
        con=mysql.connector.connect(host="localhost",
                            user="root",
                            passwd="", 
                            database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.tree.get_children()

        for elemento in profesor:
            self.tree.delete(elemento)
        try:
            cur.execute("SELECT a.cedula_identidad, a.nombres, a.apellidos, a.telefono, a.direccion, a.fecha_ingreso, a.fecha_nacimiento, a.edad, a.rif, a.email,a.sexo, b.nombre_cargo FROM profesor a, cargo b, programa d WHERE a.id_programa=d.id_programa AND b.id_cargo=a.id_cargo AND d.nombre_programa='"+opcionPrograma+"' AND a.cedula_identidad!='111111' AND a.cedula_identidad!='222222' ORDER BY a.nombres DESC")
            for row in cur:
                self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
        except:
            mb.showinfo("Información", "No se encontraron archivos.")

    def clearProfesor(self):
        query="SELECT a.cedula_identidad, a.nombres, a.apellidos, a.telefono, a.direccion, a.fecha_ingreso, a.fecha_nacimiento, a.edad, a.rif, a.email,a.sexo, b.nombre_cargo,d.nombre_programa FROM profesor a, cargo b, programa d WHERE a.cedula_identidad NOT IN ('111111','222222') AND b.id_cargo=a.id_cargo AND d.id_programa=a.id_programa ORDER BY a.nombres DESC"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.updateListaProfesor(respuesta)

    def updateListaProfesor(self,respuesta):
        info=self.tree.get_children()

        for elemento in info:
            self.tree.delete(elemento)
        for row in respuesta:
            self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]))

    def administracion(self):
        con=mysql.connector.connect(host="localhost",
                            user="root",
                            passwd="", 
                            database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.tree.get_children()

        for elemento in profesor:
            self.tree.delete(elemento)
        try:
            cur.execute("SELECT a.cedula_identidad, a.nombres, a.apellidos, a.telefono, a.direccion, a.fecha_ingreso, a.fecha_nacimiento, a.edad, a.rif, a.email,a.sexo, b.nombre_cargo FROM profesor a, cargo b, programa d WHERE a.id_programa=d.id_programa AND b.id_cargo=a.id_cargo AND d.nombre_programa='Administración' AND a.cedula_identidad!='111111' AND a.cedula_identidad!='222222' ORDER BY a.nombres DESC")
            for row in cur:
                self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
        except:
            mb.showinfo("Información", "No se encontraron archivos.")
    
    def modificarProfesor(self):
        self.ventana1.destroy()
        app= formularios.detalleProfesor.formularioModificar.VentanaEmergente(self.UsuarioName)
        
    #################### Fin de metodos de gestion de profesores

    ################ Metodo para gestion de usuarios

    def usuarios(self):
        self.ocultarmostrarMenu()

        self.frame4Interactivo.place_forget()

        ########################################
        ##        Frame interactivo           ##
        ########################################

        self.frame4Interactivo=tk.Frame(self.ventana1)
        self.frame4Interactivo.config(bg='light cyan',bd=11)
        self.frame4Interactivo.place(x=-15,y=55,width=1050,height=580)

        #### Frame Logo

        self.frameLogo=tk.Frame(self.frame4Interactivo,bg="light cyan",width=444,height=243)
        self.frameLogo.place(x=0, y=390)

        self.imagen=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\mimimalista.png")
        fondo=tk.Label(self.frameLogo,image=self.imagen,bg="light cyan").place(x=0,y=0)

         #Label titulo frame
        self.labeltitulo=tk.Label(self.frame4Interactivo,text="Gestión de usuarios",bg="light cyan",font=("Times New Roman",20), fg="Black")
        self.labeltitulo.place(x=20,y=30)

        self.framedecorativo=tk.Frame(self.frame4Interactivo)
        self.framedecorativo.config(bg="dark blue")
        self.framedecorativo.place(x=445,y=-10,width=600,height=900)

        self.labelinfo=tk.Label(self.framedecorativo,text="Usuarios disponibles",bg="dark blue",font=("Times New Roman",20), fg="white")
        self.labelinfo.place(x=0,y=10)
        self.labelinfo.pack(padx=1)

        self.framebusquedas=tk.Frame(self.framedecorativo,bg="White")
        self.framebusquedas.place(x=0,y=40,width=1050,height=210)
        self.framebusquedas.pack(padx=3,pady=20)

      
         ##Tree para mostrar columnas
        self.tree = ttk.Treeview(self.framebusquedas,columns=("#1","#2","#3","#4"),height="9")
        self.tree.heading("#0",text="Usuario")
        self.tree.heading("#1",text="Cedula de identidad")
        self.tree.heading("#2",text="Nombres")
        self.tree.heading("#3",text="Apellidos")
        self.tree.heading("#4",text="Privilegio")
            ##Tamano de columnas

        self.tree.column("#0",width=113)
        self.tree.column("#1",width=100)
        self.tree.column("#2",width=90)
        self.tree.column("#3",width=90)
        self.tree.column("#4",width=80)

        self.tree.bind("<1>",self.getrow_usuario)
        
        self.tree.pack(side="left",padx=2)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.framebusquedas, orient="vertical", command = self.tree.yview)
        scrolvert.pack(side="left",fill="y")
        self.tree.config(yscrollcommand=scrolvert.set)

        #Muestra de todos los usuarios en el treeview

        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.tree.get_children()

        for elemento in profesor:
            self.tree.delete(elemento)
        try:
            cur.execute("SELECT  a.nombre_usuario, a.cedula_identidad, a.nombres, a.apellidos, b.funcion FROM usuario a, tipo_usuario b WHERE a.cedula_identidad NOT IN ('111111','222222') AND b.privilegio=a.privilegio ORDER BY a.nombres ASC")
            for row in cur:
                self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4]))
        except:
            pass

        ################Frame Entry y labels

        self.labelframe1=tk.LabelFrame(self.framedecorativo,text="Seleccion usuario",fg="white",font=("Times New Roman",20))
        self.labelframe1.config(bg="dark blue")
        self.labelframe1.place(x=10,y=13,width=500,height=300)
        self.labelframe1.pack(pady=1)
        
        ###########################Label

        self.labelcedula=tk.Label(self.labelframe1,text="Cédula de identidad:",bg="dark blue",fg="white",font=("Times New Roman",12))
        self.labelcedula.grid(row=0,column=0,padx=10,pady=10)

        self.labelusuario=tk.Label(self.labelframe1,text="Usuario:",bg="dark blue",fg="white",font=("Times New Roman",12))
        self.labelusuario.grid(row=1,column=0,padx=10,pady=10)

        self.labelnombre=tk.Label(self.labelframe1,text="Nombres:",bg="dark blue",fg="white",font=("Times New Roman",12))
        self.labelnombre.grid(row=2,column=0,padx=10,pady=10)

        self.labelapellido=tk.Label(self.labelframe1,text="Apellidos:",bg="dark blue",fg="white",font=("Times New Roman",12))
        self.labelapellido.grid(row=3,column=0,padx=10,pady=10)

        self.labelfuncion=tk.Label(self.labelframe1,text="Privilegio:",bg="dark blue",fg="white",font=("Times New Roman",12))
        self.labelfuncion.grid(row=4,column=0,padx=10,pady=10)

        ########################### Entry

        self.tciUs=tk.StringVar()
        self.tusuario=tk.StringVar()
        self.tnom=tk.StringVar()
        self.tape=tk.StringVar()
        self.tfuncion=tk.StringVar()
        
        self.entryci=ttk.Entry(self.labelframe1,textvariable=self.tciUs,state="readonly",font=("Times New Roman",12))
        self.entryci.grid(row=0,column=1,padx=10,pady=10)

        self.entryUsuario=ttk.Entry(self.labelframe1,textvariable=self.tusuario,state="readonly",font=("Times New Roman",12))
        self.entryUsuario.grid(row=1,column=1,padx=10,pady=10)

        self.entryNom=ttk.Entry(self.labelframe1,textvariable=self.tnom,state="readonly",font=("Times New Roman",12))
        self.entryNom.grid(row=2,column=1,padx=10,pady=10)

        self.entryApe=ttk.Entry(self.labelframe1,textvariable=self.tape,state="readonly",font=("Times New Roman",12))
        self.entryApe.grid(row=3,column=1,padx=10,pady=10)
        
        self.entryFun=ttk.Entry(self.labelframe1,textvariable=self.tfuncion,state="readonly",font=("Times New Roman",12))
        self.entryFun.grid(row=4,column=1,padx=10,pady=10)

        ########################### Botones (Modificar, eliminar)

        self.btneliminar=tk.Button(self.labelframe1,text="Eliminar",command=self.delete_usuario)
        self.btneliminar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,width=20,font=("Times New Roman",12))
        self.btneliminar.grid(row=1,column=5,padx=4,pady=4)

        self.btnModificar=tk.Button(self.labelframe1,text="Cambiar Contraseña",command=self.update_usuario)
        self.btnModificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,width=20,font=("Times New Roman",12))
        self.btnModificar.grid(row=3,column=5,padx=4,pady=4)
        

        ############################### Label frame modificar en el frame interactivo 

        self.labelframeAgregar=tk.LabelFrame(self.frame4Interactivo,text="Agregar nuevo usuario",fg="Black",bg="light cyan",font=("Times New Roman",14))
        self.labelframeAgregar.place(x=20,y=70)

        ############ Entry y label

        self.labelcedula=tk.Label(self.labelframeAgregar,text="Cédula de identidad",bg="light cyan",font=("Times New Roman",12))
        self.labelcedula.grid(row=0,column=0,padx=10,pady=4)

        self.labelusuario=tk.Label(self.labelframeAgregar,text="Usuario",bg="light cyan",font=("Times New Roman",12))
        self.labelusuario.grid(row=0,column=1,padx=10,pady=4)

        self.labelnombre=tk.Label(self.labelframeAgregar,text="Nombres",bg="light cyan",font=("Times New Roman",12))
        self.labelnombre.grid(row=2,column=0,padx=10,pady=4)

        self.labelapellido=tk.Label(self.labelframeAgregar,text="Apellidos",bg="light cyan",font=("Times New Roman",12))
        self.labelapellido.grid(row=2,column=1,padx=10,pady=4)

        self.labelfuncion=tk.Label(self.labelframeAgregar,text="Privilegio",bg="light cyan",font=("Times New Roman",12))
        self.labelfuncion.grid(row=4,column=0,padx=10,pady=4)

        self.labelfuncion=tk.Label(self.labelframeAgregar,text="Contraseña",bg="light cyan",font=("Times New Roman",12))
        self.labelfuncion.grid(row=4,column=1,padx=10,pady=4)

        ###### Entry agregar usuario

        self.tciUsAg=tk.StringVar()
        self.tusuarioAg=tk.StringVar()
        self.tnomAg=tk.StringVar()
        self.tapeAg=tk.StringVar()
        self.tfuncionAg=tk.StringVar()
        self.tpasswdAg=tk.StringVar()
        
        query="SELECT cedula_identidad FROM profesor WHERE cedula_identidad NOT IN ('111111','222222') ORDER BY cedula_identidad ASC"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        self.respuesta=cursor.fetchall() 
        cone.close()
        
        opcionesCedula=self.respuesta
        self.comobox4=ttk.Combobox(self.labelframeAgregar,
                                width=20,
                                textvariable=self.tciUsAg,
                                values=opcionesCedula,
                                font=("Times New Roman",12))
        self.comobox4.current(0)
        self.comobox4.grid(row=1,column=0,padx=10,pady=10)
        self.comobox4.bind('<KeyRelease>',self.searchProfe)

        self.entryUsu=ttk.Entry(self.labelframeAgregar,textvariable=self.tusuarioAg,font=("Times New Roman",12))
        self.entryUsu.grid(row=1,column=1,padx=10,pady=10)

        self.entryNombre=ttk.Entry(self.labelframeAgregar,textvariable=self.tnomAg,font=("Times New Roman",12))
        self.entryNombre.grid(row=3,column=0,padx=10,pady=10)

        self.entryApellido=ttk.Entry(self.labelframeAgregar,textvariable=self.tapeAg,font=("Times New Roman",12))
        self.entryApellido.grid(row=3,column=1,padx=10,pady=10)
        
        self.opcionFuncion=tk.StringVar()
        opcionesFuncion=("Administrador","Profesor")
        self.comobox3=ttk.Combobox(self.labelframeAgregar,
                                width=20,
                                textvariable=self.opcionFuncion,
                                values=opcionesFuncion,
                                state='readonly',
                                font=("Times New Roman",12))
        self.comobox3.current(0)
        self.comobox3.grid(row=5,column=0,padx=10,pady=10)

        self.entrypassword=ttk.Entry(self.labelframeAgregar,textvariable=self.tpasswdAg,show="*",font=("Times New Roman",12))
        self.entrypassword.grid(row=5,column=1,padx=10,pady=10)
        

        ################################# Boton Agregar

        self.btneAgregar=tk.Button(self.labelframeAgregar,text="Agregar",command=self.add_new)
        self.btneAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        self.btneAgregar.config(width=10,height=2,font=("Times New Roman",12))
        self.btneAgregar.grid(row=6,column=0,padx=4,pady=4)

    ################################ ------------------ Agregar nuevo usuario

    def searchProfe(self,event):
        value=event.widget.get()
        if value == '':
            self.comobox4['values']= self.respuesta

        else:
            data=[]
            for item  in self.respuesta:
                if value in item:
                    data=value
            self.comobox4['values']=data

    ###### Restricciones ###########
    def validar_Cedula(self,ci):
        cedula=ci
        validar=re.match('[0-999999]+$',cedula,re.I)
        if cedula=="":
            return False
        elif not validar:
            return False
        else:
            return True

    def validar_contrasena(self,passwordR):
        password=passwordR
        validar=re.match('^[a-z\áéíóúñàèìòù0-999999 ]+$',password,re.I)
        if password=="":
            return False
        elif not validar:
            return False
        else:
            return True

    ###############################

    def definir_privilegio(self):

        opcioncontrol=self.opcionFuncion.get()
        if opcioncontrol == "Administrador":
            respuesta="1_admin"
            return respuesta

        if opcioncontrol == "Profesor":
            respuesta="2_profe"
            return respuesta

    def clearUsuario(self):
        query="SELECT a.nombre_usuario, a.cedula_identidad, a.nombres, a.apellidos, b.funcion FROM usuario a, tipo_usuario b WHERE a.cedula_identidad NOT IN ('111111','222222') AND b.privilegio=a.privilegio ORDER BY a.nombres ASC"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.updateListaUsuario(respuesta)

    def updateListaUsuario(self,respuesta):
        info=self.tree.get_children()

        for elemento in info:
            self.tree.delete(elemento)
        for row in respuesta:
            self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4]))

    def add_new(self):
        cedula_identidad=self.tciUsAg.get()
        Nomusuario=self.tusuarioAg.get()
        nombres=self.tnomAg.get()
        apellidos=self.tapeAg.get()
        funcion=self.definir_privilegio()
        contrasena=self.tpasswdAg.get()
        try:
            if self.validar_Cedula(cedula_identidad) & self.validar_contrasena(contrasena):
                query="INSERT INTO usuario(nombres,apellidos,contraseña,privilegio,cedula_identidad,nombre_usuario) VALUES(%s,%s,%s,%s,%s,%s)"

                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(nombres,apellidos,contrasena,funcion,cedula_identidad,Nomusuario))
                
                cone.commit()
                cone.close()
                self.clearUsuario()
                mb.showinfo("Información","Se han cargado con éxito los datos.")
                self.tciUsAg.set("")
                self.tusuarioAg.set("")
                self.tnomAg.set("")
                self.tapeAg.set("")
                self.tpasswdAg.set("")
        
            else:
                mb.showwarning("Error","Debe completar los campos obligatorios")
        except:
            mb.showerror("Error", "No se encuentra la información")

    def getrow_usuario(self,event):
        rowid=self.tree.identify_row(event.y)
        self.tree.selection_set(rowid)
        item=self.tree.item(self.tree.focus())
        self.usuario=item["text"]
        
        ############ Busca la informacion en la base de datos

        query="SELECT a.cedula_identidad, a.nombre_usuario, a.nombres, a.apellidos, b.funcion FROM usuario a, tipo_usuario b WHERE a.nombre_usuario='"+self.usuario+"' AND a.cedula_identidad NOT IN ('111111','222222') AND b.privilegio=a.privilegio"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        
        if len(respuesta)>0:
            self.tciUs.set(respuesta[0][0])
            self.tusuario.set(respuesta[0][1])
            self.tnom.set(respuesta[0][2])
            self.tape.set(respuesta[0][3])
            self.tfuncion.set(respuesta[0][4])

    def delete_usuario(self):
        cedula_identidad=self.tciUs.get()
        nom_usuario=self.tusuario.get()
        try:
            if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea borrar estos datos? "):
                query="DELETE FROM usuario WHERE cedula_identidad='"+cedula_identidad+"'AND nombre_usuario ='"+nom_usuario+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query)
            
                cone.commit()
                cone.close()
                self.clearUsuario()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han borrado los datos con éxito.")
                    self.tciUs.set("")
                    self.tusuario.set("")
                    self.tnom.set("")
                    self.tape.set("")
                    self.tfuncion.set("")
                else:
                    mb.showinfo("Informacion", "No existe un profesor con dicha informacion")
                

            else:
                return True
        except:
            mb.showwarning("Error","Introduzca la informacion que desee borrar o selecione en la tablaRepresentante.")

    def update_usuario(self):
        
        
        ci=self.tciUs.get()
        uss=self.tusuario.get()
        nom=self.tnom.get()
        ape=self.tape.get()
        funcion=self.tfuncion.get()

        try:
            if self.validar_Cedula(ci) :
                self.ventana1.destroy()
                self.ventana2=tk.Tk()
                self.ventana2.title("Modificar usuario")
                self.ventana2.config(bg='dark blue')
                self.ventana2.geometry("625x450")
                self.ventana2.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")

                ###########------------------- Formulario label frame

                self.labelframe1=tk.LabelFrame(self.ventana2,text="Seleccion usuario",fg="white",font=("Times New Roman",20))
                self.labelframe1.config(bg="dark blue")
                self.labelframe1.place(x=10,y=100,width=500,height=300)
                self.labelframe1.pack(pady=1)
                
                ###########################Label

                self.labelcedula=tk.Label(self.labelframe1,text="Cédula de identidad:",bg="dark blue",fg="white",font=("Times New Roman",12))
                self.labelcedula.grid(row=0,column=0,padx=10,pady=10)

                self.labelusuario=tk.Label(self.labelframe1,text="Usuario:",bg="dark blue",fg="white",font=("Times New Roman",12))
                self.labelusuario.grid(row=1,column=0,padx=10,pady=10)

                self.labelnombre=tk.Label(self.labelframe1,text="Nombres:",bg="dark blue",fg="white",font=("Times New Roman",12))
                self.labelnombre.grid(row=2,column=0,padx=10,pady=10)

                self.labelapellido=tk.Label(self.labelframe1,text="Apellidos:",bg="dark blue",fg="white",font=("Times New Roman",12))
                self.labelapellido.grid(row=3,column=0,padx=10,pady=10)

                self.labelfuncion=tk.Label(self.labelframe1,text="Privilegio:",bg="dark blue",fg="white",font=("Times New Roman",12))
                self.labelfuncion.grid(row=4,column=0,padx=10,pady=10)

                self.labelfuncion=tk.Label(self.labelframe1,text="Contraseña:",bg="dark blue",fg="white",font=("Times New Roman",12))
                self.labelfuncion.grid(row=5,column=0,padx=10,pady=10)

                ########################### Entry

                self.tciUs=tk.StringVar()
                self.tusuario=tk.StringVar()
                self.tnom=tk.StringVar()
                self.tape=tk.StringVar()
                self.tpassword=tk.StringVar()
                
                self.entryci=ttk.Entry(self.labelframe1,textvariable=self.tciUs,font=("Times New Roman",12))
                self.entryci.grid(row=0,column=1,padx=10,pady=10)

                self.entryUsuario=ttk.Entry(self.labelframe1,textvariable=self.tusuario,font=("Times New Roman",12))
                self.entryUsuario.grid(row=1,column=1,padx=10,pady=10)

                self.entryNom=ttk.Entry(self.labelframe1,textvariable=self.tnom,font=("Times New Roman",12))
                self.entryNom.grid(row=2,column=1,padx=10,pady=10)

                self.entryApe=ttk.Entry(self.labelframe1,textvariable=self.tape,font=("Times New Roman",12))
                self.entryApe.grid(row=3,column=1,padx=10,pady=10)
                
                self.opcionFuncion=tk.StringVar()
                opcionesFuncion=("Administrador","Profesor")
                self.comobox3=ttk.Combobox(self.labelframe1,
                                        width=20,
                                        textvariable=self.opcionFuncion,
                                        values=opcionesFuncion,
                                        state='readonly',
                                        font=("Times New Roman",12))
                self.comobox3.current(0)
                self.comobox3.grid(row=4,column=1,padx=10,pady=10)

                self.entryContrasena=ttk.Entry(self.labelframe1,textvariable=self.tpassword,show="*",font=("Times New Roman",12))
                self.entryContrasena.grid(row=5,column=1,padx=10,pady=10)

                #################### Boton aceptar y volver

                self.btnaceptar=tk.Button(self.labelframe1,text="Aceptar",command=self.aceptar)
                self.btnaceptar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,width=20,font=("Times New Roman",12))
                self.btnaceptar.grid(row=6,column=0,padx=4,pady=4)

                self.btnvolver=tk.Button(self.labelframe1,text="volver",command=self.volver)
                self.btnvolver.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,width=20,font=("Times New Roman",12))
                self.btnvolver.grid(row=6,column=1,padx=4,pady=4)

                self.tciUs.set(ci)
                self.tusuario.set(uss)
                self.tnom.set(nom)
                self.tape.set(ape)
                self.opcionFuncion.set(funcion)
                self.tpassword.set("")

                self.ventana2.mainloop()
            else:
                mb.showerror("Informacion","Debe seleccionar un usuario")
        except:
            pass

    def volverAdminUsuario (self):
        ###Programa estandar para las ventanas ---------------------
        self.ventana1=tk.Tk()
        self.ventana1.title("Administrador")
        self.ventana1.geometry("1050x650")
        self.ventana1.config(bg='light cyan',bd=15)
        self.ventana1.resizable(0,0)
        self.ventana1.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")
        #-------------------------------------------------------

        #Frame admin decorativo
        self.frame1=tk.Frame(self.ventana1)

        #Frame admin informacion tentativa
        self.frame2=tk.Frame(self.ventana1)

        #Frame informacion de los usuarios
        self.frame3=tk.Frame(self.ventana1)
        self.frame3.config(bg="dark blue",bd=11)
        self.frame3.place(x=-15,y=-15,width=1050,height=70)

        #label informacion de profesores
        self.label1=tk.Label(self.frame3,text="Administrador",bg="dark blue",font=("Times New Roman",20), fg="white",)
        self.label1.place(x=110,y=10)

        # Información usuario
        self.id_usuario=tk.StringVar()
        self.id_usuario.set(self.UsuarioName)
        
        labelUsuario=tk.Label(self.frame3,text="Usuario: "+self.id_usuario.get(),bg="dark blue",font=("Times New Roman",15), fg="white")
        labelUsuario.place(x=830,y=7)


        ##-------------------Botones predeterminados --------------------------

        self.hidemenu=1
        self.botonmenu=tk.Button(self.frame3,text="Menu", command=self.ocultarmostrarMenu,bg="blueviolet", bd= 5,font=("Times New Roman",15), fg="white",activebackground="light blue",activeforeground="Black")
        self.photo=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\home.png")
        self.botonmenu.config( image=self.photo, compound=LEFT)
        self.botonmenu.place(x=10,y=5)

        ########################################
        ##        Frame interactivo           ##
        ########################################

        self.frame4Interactivo=tk.Frame(self.ventana1)
        self.frame4Interactivo.config(bg='light cyan',bd=11)
        self.frame4Interactivo.place(x=-15,y=55,width=1050,height=580)

        #### Frame Logo

        self.frameLogo=tk.Frame(self.frame4Interactivo,bg="light cyan",width=444,height=243)
        self.frameLogo.place(x=0, y=390)

        self.imagen=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\mimimalista.png")
        fondo=tk.Label(self.frameLogo,image=self.imagen,bg="light cyan").place(x=0,y=0)

         #Label titulo frame
        self.labeltitulo=tk.Label(self.frame4Interactivo,text="Gestión de usuarios",bg="light cyan",font=("Times New Roman",20), fg="Black")
        self.labeltitulo.place(x=20,y=30)

        self.framedecorativo=tk.Frame(self.frame4Interactivo)
        self.framedecorativo.config(bg="dark blue")
        self.framedecorativo.place(x=445,y=-10,width=600,height=900)

        self.labelinfo=tk.Label(self.framedecorativo,text="Usuarios disponibles",bg="dark blue",font=("Times New Roman",20), fg="white")
        self.labelinfo.place(x=0,y=10)
        self.labelinfo.pack(padx=1)

        self.framebusquedas=tk.Frame(self.framedecorativo,bg="White")
        self.framebusquedas.place(x=0,y=40,width=1050,height=210)
        self.framebusquedas.pack(padx=3,pady=20)

      
         ##Tree para mostrar columnas
        self.tree = ttk.Treeview(self.framebusquedas,columns=("#1","#2","#3","#4"),height="9")
        self.tree.heading("#0",text="Usuario")
        self.tree.heading("#1",text="Cedula de identidad")
        self.tree.heading("#2",text="Nombres")
        self.tree.heading("#3",text="Apellidos")
        self.tree.heading("#4",text="Privilegio")
            ##Tamano de columnas

        self.tree.column("#0",width=113)
        self.tree.column("#1",width=100)
        self.tree.column("#2",width=90)
        self.tree.column("#3",width=90)
        self.tree.column("#4",width=80)

        self.tree.bind("<1>",self.getrow_usuario)
        
        self.tree.pack(side="left",padx=2)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.framebusquedas, orient="vertical", command = self.tree.yview)
        scrolvert.pack(side="left",fill="y")
        self.tree.config(yscrollcommand=scrolvert.set)

        #Muestra de todos los usuarios en el treeview

        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.tree.get_children()

        for elemento in profesor:
            self.tree.delete(elemento)
        try:
            cur.execute("SELECT a.nombre_usuario, a.cedula_identidad, a.nombres, a.apellidos, b.funcion FROM usuario a, tipo_usuario b WHERE a.cedula_identidad NOT IN ('111111','222222') AND b.privilegio=a.privilegio ORDER BY a.nombres ASC")
            for row in cur:
                self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4]))
        except:
            pass

        ################Frame Entry y labels

        self.labelframe1=tk.LabelFrame(self.framedecorativo,text="Seleccion usuario",fg="white",font=("Times New Roman",20))
        self.labelframe1.config(bg="dark blue")
        self.labelframe1.place(x=10,y=13,width=500,height=300)
        self.labelframe1.pack(pady=1)
        
        ###########################Label

        self.labelcedula=tk.Label(self.labelframe1,text="Cédula de identidad:",bg="dark blue",fg="white",font=("Times New Roman",12))
        self.labelcedula.grid(row=0,column=0,padx=10,pady=10)

        self.labelusuario=tk.Label(self.labelframe1,text="Usuario:",bg="dark blue",fg="white",font=("Times New Roman",12))
        self.labelusuario.grid(row=1,column=0,padx=10,pady=10)

        self.labelnombre=tk.Label(self.labelframe1,text="Nombres:",bg="dark blue",fg="white",font=("Times New Roman",12))
        self.labelnombre.grid(row=2,column=0,padx=10,pady=10)

        self.labelapellido=tk.Label(self.labelframe1,text="Apellidos:",bg="dark blue",fg="white",font=("Times New Roman",12))
        self.labelapellido.grid(row=3,column=0,padx=10,pady=10)

        self.labelfuncion=tk.Label(self.labelframe1,text="Privilegio:",bg="dark blue",fg="white",font=("Times New Roman",12))
        self.labelfuncion.grid(row=4,column=0,padx=10,pady=10)

        ########################### Entry

        self.tciUs=tk.StringVar()
        self.tusuario=tk.StringVar()
        self.tnom=tk.StringVar()
        self.tape=tk.StringVar()
        self.tfuncion=tk.StringVar()
        
        self.entryci=ttk.Entry(self.labelframe1,textvariable=self.tciUs,state="readonly",font=("Times New Roman",12))
        self.entryci.grid(row=0,column=1,padx=10,pady=10)

        self.entryUsuario=ttk.Entry(self.labelframe1,textvariable=self.tusuario,state="readonly",font=("Times New Roman",12))
        self.entryUsuario.grid(row=1,column=1,padx=10,pady=10)

        self.entryNom=ttk.Entry(self.labelframe1,textvariable=self.tnom,state="readonly",font=("Times New Roman",12))
        self.entryNom.grid(row=2,column=1,padx=10,pady=10)

        self.entryApe=ttk.Entry(self.labelframe1,textvariable=self.tape,state="readonly",font=("Times New Roman",12))
        self.entryApe.grid(row=3,column=1,padx=10,pady=10)
        
        self.entryFun=ttk.Entry(self.labelframe1,textvariable=self.tfuncion,state="readonly",font=("Times New Roman",12))
        self.entryFun.grid(row=4,column=1,padx=10,pady=10)

        ########################### Botones (Modificar, eliminar)

        self.btneliminar=tk.Button(self.labelframe1,text="Eliminar",command=self.delete_usuario)
        self.btneliminar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,width=20,font=("Times New Roman",12))
        self.btneliminar.grid(row=1,column=5,padx=4,pady=4)

        self.btnModificar=tk.Button(self.labelframe1,text="Cambiar Contraseña",command=self.update_usuario)
        self.btnModificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,width=20,font=("Times New Roman",12))
        self.btnModificar.grid(row=3,column=5,padx=4,pady=4)
        

        ############################### Label frame modificar en el frame interactivo 

        self.labelframeAgregar=tk.LabelFrame(self.frame4Interactivo,text="Agregar nuevo usuario",fg="Black",bg="light cyan",font=("Times New Roman",14))
        self.labelframeAgregar.place(x=20,y=70)

        ############ Entry y label

        self.labelcedula=tk.Label(self.labelframeAgregar,text="Cédula de identidad",bg="light cyan",font=("Times New Roman",12))
        self.labelcedula.grid(row=0,column=0,padx=10,pady=4)

        self.labelusuario=tk.Label(self.labelframeAgregar,text="Usuario",bg="light cyan",font=("Times New Roman",12))
        self.labelusuario.grid(row=0,column=1,padx=10,pady=4)

        self.labelnombre=tk.Label(self.labelframeAgregar,text="Nombres",bg="light cyan",font=("Times New Roman",12))
        self.labelnombre.grid(row=2,column=0,padx=10,pady=4)

        self.labelapellido=tk.Label(self.labelframeAgregar,text="Apellidos",bg="light cyan",font=("Times New Roman",12))
        self.labelapellido.grid(row=2,column=1,padx=10,pady=4)

        self.labelfuncion=tk.Label(self.labelframeAgregar,text="Privilegio",bg="light cyan",font=("Times New Roman",12))
        self.labelfuncion.grid(row=4,column=0,padx=10,pady=4)

        self.labelfuncion=tk.Label(self.labelframeAgregar,text="Contraseña",bg="light cyan",font=("Times New Roman",12))
        self.labelfuncion.grid(row=4,column=1,padx=10,pady=4)

        ###### Entry agregar usuario

        self.tciUsAg=tk.StringVar()
        self.tusuarioAg=tk.StringVar()
        self.tnomAg=tk.StringVar()
        self.tapeAg=tk.StringVar()
        self.tfuncionAg=tk.StringVar()
        self.tpasswdAg=tk.StringVar()
        
        query="SELECT cedula_identidad FROM profesor WHERE cedula_identidad NOT IN ('111111','222222') ORDER BY cedula_identidad ASC"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        self.respuesta=cursor.fetchall() 
        cone.close()
        
        opcionesCedula=self.respuesta
        self.comobox4=ttk.Combobox(self.labelframeAgregar,
                                width=20,
                                textvariable=self.tciUsAg,
                                values=opcionesCedula,
                                font=("Times New Roman",12))
        self.comobox4.current(0)
        self.comobox4.grid(row=1,column=0,padx=10,pady=10)
        self.comobox4.bind('<KeyRelease>',self.search)

        self.entryUsu=ttk.Entry(self.labelframeAgregar,textvariable=self.tusuarioAg,font=("Times New Roman",12))
        self.entryUsu.grid(row=1,column=1,padx=10,pady=10)

        self.entryNombre=ttk.Entry(self.labelframeAgregar,textvariable=self.tnomAg,font=("Times New Roman",12))
        self.entryNombre.grid(row=3,column=0,padx=10,pady=10)

        self.entryApellido=ttk.Entry(self.labelframeAgregar,textvariable=self.tapeAg,font=("Times New Roman",12))
        self.entryApellido.grid(row=3,column=1,padx=10,pady=10)
        
        self.opcionFuncion=tk.StringVar()
        opcionesFuncion=("Administrador","Profesor")
        self.comobox3=ttk.Combobox(self.labelframeAgregar,
                                width=20,
                                textvariable=self.opcionFuncion,
                                values=opcionesFuncion,
                                state='readonly',
                                font=("Times New Roman",12))
        self.comobox3.current(0)
        self.comobox3.grid(row=5,column=0,padx=10,pady=10)

        self.entrypassword=ttk.Entry(self.labelframeAgregar,textvariable=self.tpasswdAg,show="*",font=("Times New Roman",12))
        self.entrypassword.grid(row=5,column=1,padx=10,pady=10)
        

        ################################# Boton Agregar

        self.btneAgregar=tk.Button(self.labelframeAgregar,text="Agregar",command=self.add_new)
        self.btneAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12))
        self.btneAgregar.config(width=10,height=2)
        self.btneAgregar.grid(row=6,column=0,padx=4,pady=4)

        #Mainloop----------------------------------------------
        self.ventana1.mainloop()
    
    def aceptar(self):
        
        self.ci=self.tciUs.get()
        self.uss=self.tusuario.get()
        self.nombre=self.tnom.get()
        self.apellido=self.tape.get()
        self.privilegio=self.definir_privilegio()
        self.password=self.tpassword.get()
        

        if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea actualizar estos datos? "):
            if self.validar_Cedula(self.ci) & self.validar_contrasena(self.password):
            
                query="UPDATE usuario p JOIN tipo_usuario c ON p.privilegio=c.privilegio SET p.nombres='"+self.nombre+"',p.apellidos='"+self.apellido+"',p.contraseña='"+self.password+"',p.privilegio='"+self.privilegio+"',p.cedula_identidad='"+self.ci+"',p.nombre_usuario='"+self.uss+"'WHERE p.nombre_usuario='"+self.usuario+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query)
                cone.commit()
                cone.close()

                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han cargado con éxito los datos.")
                    self.ventana2.destroy()
                    self.volverAdminUsuario()

                else:
                    mb.showinfo("Informacion", "No existe un profesor con dicha informacion")
                
            else:
                mb.showwarning("Error","Debe seleccionar los campos a self.modificar")
        else:
            return True

    def volver(self):
        self.ventana2.destroy()
        self.volverAdminUsuario()

    ###################### --------------------- Fin de las modificaciones usuario

    ######################### MODULO INSTRUMENTOS #############################

    def instrumentos(self):

        self.ocultarmostrarMenu()
        
        ########################################
        ##        Frame interactivo           ##
        ########################################

        self.frame4Interactivo=tk.Frame(self.ventana1)
        self.frame4Interactivo.config(bg='light cyan',bd=11)
        self.frame4Interactivo.place(x=-15,y=55,width=1050,height=580)
        
        #Label titulo
        self.labeltitulo=tk.Label(self.frame4Interactivo,text="Gestión de instrumentos",bg="light cyan",font=("Times New Roman",20), fg="Black")
        self.labeltitulo.place(x=20,y=30)

        ########## Frame Logo fundamusical

        self.frameLogo2=tk.Frame(self.frame4Interactivo,bg="light blue",width=623,height=306)
        self.frameLogo2.place(x=-50, y=340)

        self.imagen3=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\Pentagrama-removebg-preview.png")
        fondo2=tk.Label(self.frameLogo2,image=self.imagen3,bg="light cyan").place(x=0,y=0)

        #Label frame para cada una de las funciones

        #--------------- Label frame opciones

        self.frameOpcioneslabel=tk.LabelFrame(self.frame4Interactivo,text='Opciones',font=("Times New Roman",20))
        self.frameOpcioneslabel.config(bg="light cyan")
        self.frameOpcioneslabel.place(x=20,y=100)


        ####------------------- Botones en label frame opciones

        btnAgregar=tk.Button(self.frameOpcioneslabel,text="Agregar nuevo",font=("Times New Roman",14),command=self.agregar_instrumento)
        btnAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnAgregar.grid(row=1,column=2,ipady=10,ipadx=10,padx=10,pady=20)

        btnModificar=tk.Button(self.frameOpcioneslabel,text="Modificar",font=("Times New Roman",14), command=self.modificarInstrumento)
        btnModificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnModificar.grid(row=1,column=3,ipady=10,ipadx=30,padx=10,pady=20)


        #---------------------- labelframe lista de alumnos 

        self.framedecorativo=tk.Frame(self.frame4Interactivo)
        self.framedecorativo.config(bg="dark blue")
        self.framedecorativo.place(x=400,y=-10,width=650,height=900)

        ########## Frame Logo fundamusical

        self.frameLogo2=tk.Frame(self.framedecorativo,bg="light blue",width=624,height=257)
        self.frameLogo2.place(x=0, y=320)

        self.imagen2=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\pentagramaColor.png")
        fondo2=tk.Label(self.frameLogo2,image=self.imagen2,bg="dark blue").place(x=0,y=0)

        self.labelinfo=tk.Label(self.framedecorativo,text="Situación actual",bg="dark blue",font=("Times New Roman",20), fg="white")
        self.labelinfo.place(x=0,y=10)
        self.labelinfo.pack(padx=1)

        self.framebusquedas=tk.Frame(self.framedecorativo,bg="White")
        self.framebusquedas.place(x=-10,y=40,width=600,height=210)
        self.framebusquedas.pack(pady=20,side="top")

      
         ##Tree para mostrar columnas
        self.tree = ttk.Treeview(self.framebusquedas,columns=("#1","#2","#3","#4","#5","#6","#7"),height="9")
        self.tree.heading("#0",text="Serial")
        self.tree.heading("#1",text="Nro inventario")
        self.tree.heading("#2",text="Descripción")
        self.tree.heading("#3",text="Marca")
        self.tree.heading("#4",text="Condición")
        self.tree.heading("#5",text="Ubicación")
        self.tree.heading("#6",text="Procedencia")
        self.tree.heading("#7",text="Vigente")
        
            ##Tamano de columnas

        self.tree.column("#0",width=90)
        self.tree.column("#1",width=90)
        self.tree.column("#2",width=70)
        self.tree.column("#3",width=50)
        self.tree.column("#4",width=80)
        self.tree.column("#5",width=75)
        self.tree.column("#6",width=80)
        self.tree.column("#7",width=40)

        self.tree.bind("<1>",self.getrow_instrumentos)
        
        self.tree.pack(side="left")


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.framebusquedas, orient="vertical", command = self.tree.yview)
        scrolvert.pack(side="left",fill="y")
        self.tree.config(yscrollcommand=scrolvert.set)

        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        alumno=self.tree.get_children()

        for elemento in alumno:
            self.tree.delete(elemento)
        try:
            cur.execute("SELECT num_serial,cod_inventario,descripcion,marca,condicion,ubicacion,procedencia,comodato_vigente FROM instrumento")
            for row in cur:
                self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
        except:
            pass

        
         ##Tamano de columnas

        ########## Botón más información

        self.frameinfo=tk.LabelFrame(self.framedecorativo,text='',font=("Times New Roman",20))
        self.frameinfo.config(bg="dark blue")
        self.frameinfo.place(x=20,y=290)
        self.hide=1
        self.btnInfo=tk.Button(self.frameinfo,text="Más información",font=("Times New Roman",11),command=self.ocultarMostrarDetalles)
        self.btnInfo.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        self.btnInfo.grid(row=0,column=0,ipady=5,ipadx=5,padx=10,pady=10)

        self.labelDetalle=tk.Label(self.framedecorativo,text="Detalles generales",bg="dark blue",font=("Times New Roman",20), fg="white")
        self.labelDetalle.place(x=180,y=300)

    ########### Ocultar y mostrar detalles instrumentos

    def ocultarMostrarDetalles(self):
         
        if self.hide==0:
            self.frameDetalles.place_forget()#place(x=-70,y=0,width=350,height=800)
            self.hide=1
        else:
             #################Información que aparece y desaparece
            
            self.frameDetalles=tk.Frame(self.framedecorativo,bg="light cyan")
            self.frameDetalles.place(x=180,y=370,height=150,width=400)

            self.textTotaldisp=tk.StringVar()
            query="SELECT COUNT(comodato_vigente) From instrumento WHERE comodato_vigente='NO' AND condicion='OPERATIVO'"
            cone=self.abrir()
            cursor=cone.cursor()
            cursor.execute(query)

            self.totalDisponible=cursor.fetchall() 
            cone.close()

            self.labelDisponible=tk.Label(self.frameDetalles,text="Instrumentos disponibles=",font=("Times New Roman",15), fg="black")
            self.labelDisponible.config(bg="light cyan")
            self.labelDisponible.place(x=10,y=20)

            self.entryDisponible=tk.Entry(self.frameDetalles,textvariable=self.textTotaldisp,state="readonly",font=("Times New Roman",12))
            self.entryDisponible.config(width=5)
            self.entryDisponible.place(x=230,y=20)

            self.textTotaldisp.set(self.totalDisponible[0][0])

            ###----------------------------
            self.ttotalAsignados=tk.StringVar()
            query="SELECT COUNT(en_posesion) FROM instrumento_alumno WHERE en_posesion='SI'"
            cone=self.abrir()
            cursor=cone.cursor()
            cursor.execute(query)

            self.totalAsignados=cursor.fetchall() 
            cone.close()

            self.labelAsignados=tk.Label(self.frameDetalles,text="Instrumentos asignados=",font=("Times New Roman",15), fg="black")
            self.labelAsignados.config(bg="light cyan")
            self.labelAsignados.place(x=10,y=60)

            self.entryAsignados=tk.Entry(self.frameDetalles,textvariable=self.ttotalAsignados,state="readonly",font=("Times New Roman",12))
            self.entryAsignados.config(width=5)
            self.entryAsignados.place(x=230,y=60)

            self.ttotalAsignados.set(self.totalAsignados[0][0])
            
            ###----------------------------
            self.ttotalinoperativos=tk.StringVar()
            query="SELECT COUNT(condicion) FROM instrumento WHERE condicion='DAÑADO' OR condicion='INOPERATIVO'"
            cone=self.abrir()
            cursor=cone.cursor()
            cursor.execute(query)

            self.totalinoperativos=cursor.fetchall() 
            cone.close()

            self.labelInoperativo=tk.Label(self.frameDetalles,text="Instrumentos inoperativos=",font=("Times New Roman",15), fg="black")
            self.labelInoperativo.config(bg="light cyan")
            self.labelInoperativo.place(x=10,y=100)

            self.entryInoperativo=tk.Entry(self.frameDetalles,textvariable=self.ttotalinoperativos,state="readonly",font=("Times New Roman",12))
            self.entryInoperativo.config(width=5)
            self.entryInoperativo.place(x=230,y=100)

            self.ttotalinoperativos.set(self.totalinoperativos[0][0])

            self.hide=0

    def agregar_instrumento(self):
            
        try:
            
            self.ventana1.destroy()
            self.ventana2=tk.Tk()
            self.ventana2.title("Agregar Instrumento")
            self.ventana2.config(bg='dark blue')
            self.ventana2.geometry("860x450")
            self.ventana2.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")

                ###########------------------- Formulario label frame

            self.labelframe1=tk.LabelFrame(self.ventana2,text="Agregar Instrumento",fg="white",font=("Times New Roman",20))
            self.labelframe1.config(bg="dark blue")
            self.labelframe1.place(x=10,y=100,width=500,height=300)
            self.labelframe1.pack(pady=1)
                
                ###########################Label

            self.labelserial=tk.Label(self.labelframe1,text="Serial:",bg="dark blue",fg="white",font=("Times New Roman",12))
            self.labelserial.grid(row=0,column=0,padx=4,pady=10)

            self.labelinventario=tk.Label(self.labelframe1,text="Número de inventario:",bg="dark blue",fg="white",font=("Times New Roman",12))
            self.labelinventario.grid(row=1,column=0,padx=4,pady=10)

            self.labeldescripcion=tk.Label(self.labelframe1,text="Descripción:",bg="dark blue",fg="white",font=("Times New Roman",12))
            self.labeldescripcion.grid(row=2,column=0,padx=4,pady=10)

            self.labelmarca=tk.Label(self.labelframe1,text="Marca:",bg="dark blue",fg="white",font=("Times New Roman",12))
            self.labelmarca.grid(row=3,column=0,padx=4,pady=10)

            self.labelmedida=tk.Label(self.labelframe1,text="Medida:",bg="dark blue",fg="white",font=("Times New Roman",12))
            self.labelmedida.grid(row=4,column=0,padx=4,pady=10)

            self.labelaccesorio=tk.Label(self.labelframe1,text="Accesorios:",bg="dark blue",fg="white",font=("Times New Roman",12))
            self.labelaccesorio.grid(row=5,column=0,padx=4,pady=10)

            self.labelubicacion=tk.Label(self.labelframe1,text="Ubicación:",bg="dark blue",fg="white",font=("Times New Roman",12))
            self.labelubicacion.grid(row=0,column=2,padx=4,pady=10)

            self.labelcondicion=tk.Label(self.labelframe1,text="Condición:",bg="dark blue",fg="white",font=("Times New Roman",12))
            self.labelcondicion.grid(row=1,column=2,padx=4,pady=10)

            self.labelprocedencia=tk.Label(self.labelframe1,text="Procedencia:",bg="dark blue",fg="white",font=("Times New Roman",12))
            self.labelprocedencia.grid(row=2,column=2,padx=4,pady=10)

            self.labelvigente=tk.Label(self.labelframe1,text="Comodato vigente:",bg="dark blue",fg="white",font=("Times New Roman",12))
            self.labelvigente.grid(row=3,column=2,padx=4,pady=10)

                ########################### Entry

            self.tserial=tk.StringVar()
            self.tinventario=tk.StringVar()
            self.tDescripcion=tk.StringVar()
            self.tmarca=tk.StringVar()
            self.tmedida=tk.StringVar()
            self.taccesorio=tk.StringVar()
            self.tubicacion=tk.StringVar()
                
            self.entryserial=ttk.Entry(self.labelframe1,textvariable=self.tserial,font=("Times New Roman",12))
            self.entryserial.grid(row=0,column=1,padx=4,pady=10)

            self.entryInventario=ttk.Entry(self.labelframe1,textvariable=self.tinventario,font=("Times New Roman",12))
            self.entryInventario.grid(row=1,column=1,padx=4,pady=10)

            self.entryDescripcion=ttk.Entry(self.labelframe1,textvariable=self.tDescripcion,font=("Times New Roman",12))
            self.entryDescripcion.grid(row=2,column=1,padx=4,pady=10)

            self.entryMarca=ttk.Entry(self.labelframe1,textvariable=self.tmarca,font=("Times New Roman",12))
            self.entryMarca.grid(row=3,column=1,padx=4,pady=10)

            self.entryMedida=ttk.Entry(self.labelframe1,textvariable=self.tmedida,font=("Times New Roman",12))
            self.entryMedida.grid(row=4,column=1,padx=4,pady=10)

            self.entryAccesorio=ttk.Entry(self.labelframe1,textvariable=self.taccesorio,font=("Times New Roman",12))
            self.entryAccesorio.grid(row=5,column=1,padx=4,pady=10)

            self.entryUbicacion=ttk.Entry(self.labelframe1,textvariable=self.tubicacion,font=("Times New Roman",12))
            self.entryUbicacion.grid(row=0,column=4,padx=4,pady=10)
                
            self.opcionCondicion=tk.StringVar()
            opcionesCondicion=("OPERATIVO","DAÑADO","HURTO","INOPERATIVO")
            self.comoboxCondicion=ttk.Combobox(self.labelframe1,
                                        width=20,
                                        textvariable=self.opcionCondicion,
                                        values=opcionesCondicion,
                                        state='readonly',
                                        font=("Times New Roman",12))
            self.comoboxCondicion.current(0)
            self.comoboxCondicion.grid(row=1,column=4,padx=4,pady=10)

            self.opcionProcedencia=tk.StringVar()
            opcionesProcedencia=("FMSB","DSR","COMODATO","OTRO")
            self.comoboxProcedencia=ttk.Combobox(self.labelframe1,
                                        width=20,
                                        textvariable=self.opcionProcedencia,
                                        values=opcionesProcedencia,
                                        state='readonly',
                                        font=("Times New Roman",12))
            self.comoboxProcedencia.current(0)
            self.comoboxProcedencia.grid(row=2,column=4,padx=4,pady=10)

            self.opcionVigencia=tk.StringVar()
            opcionesVigencia=("SI","NO")
            self.comoboxVigencia=ttk.Combobox(self.labelframe1,
                                        width=20,
                                        textvariable=self.opcionVigencia,
                                        values=opcionesVigencia,
                                        state='readonly',
                                        font=("Times New Roman",12))
            self.comoboxVigencia.current(0)
            self.comoboxVigencia.grid(row=3,column=4,padx=4,pady=10)

                #################### Boton aceptar y volver

            self.btnaceptar=tk.Button(self.labelframe1,text="Aceptar",command=self.insertar_instrumento)
            self.btnaceptar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,width=20,font=("Times New Roman",12))
            self.btnaceptar.grid(row=7,column=1,padx=4,pady=4)

            self.btnvolver=tk.Button(self.labelframe1,text="volver",command=self.volver_instrumento)
            self.btnvolver.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,width=20,font=("Times New Roman",12))
            self.btnvolver.grid(row=7,column=2,padx=4,pady=4)

           
            self.ventana2.mainloop()
        except:
            pass

    def insertar_instrumento (self):

        serial=self.tserial.get()
        inventario=self.tinventario.get()
        descripcion=self.tDescripcion.get()
        marca=self.tmarca.get()
        medida=self.tmedida.get()
        accesorio=self.taccesorio.get()
        ubicacion=self.tubicacion.get()
        condicion=self.opcionCondicion.get()
        procedencia=self.opcionProcedencia.get()
        vigente= self.opcionVigencia.get()
        
        
        if self.validar_contrasena(serial):
            query="INSERT INTO instrumento(num_serial,descripcion,marca,medida,accesorio,condicion,ubicacion,procedencia,comodato_vigente,cod_inventario) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            cone=self.abrir()
            cursor=cone.cursor()
            cursor.execute(query,(serial,descripcion,marca,medida,accesorio,condicion,ubicacion,procedencia,vigente,inventario))
            
            cone.commit()
            cone.close()
            mb.showinfo("Información","Se han cargado con éxito los datos.")
            self.tserial.set("")
            self.tinventario.set("")
            self.tDescripcion.set("")
            self.tmarca.set("")
            self.tmedida.set("")
            self.taccesorio.set("")
            self.tubicacion.set("")
            
    
        else:
            mb.showwarning("Error","Debe completar los campos obligatorios")

    def volver_instrumento(self):
        self.ventana2.destroy()

        ###Programa estandar para las ventanas ---------------------
        self.ventana1=tk.Tk()
        self.ventana1.title("Administrador")
        self.ventana1.geometry("1050x650")
        self.ventana1.config(bg='light cyan',bd=15)
        self.ventana1.resizable(0,0)
        self.ventana1.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")
        #-------------------------------------------------------

        #Frame admin decorativo
        self.frame1=tk.Frame(self.ventana1)

        #Frame admin informacion tentativa
        self.frame2=tk.Frame(self.ventana1)

        #Frame informacion de los usuarios
        self.frame3=tk.Frame(self.ventana1)
        self.frame3.config(bg="dark blue",bd=11)
        self.frame3.place(x=-15,y=-15,width=1050,height=70)

        #label informacion de profesores
        self.label1=tk.Label(self.frame3,text="Administrador",bg="dark blue",font=("Times New Roman",20), fg="white")
        self.label1.place(x=110,y=10)

        # Información usuario
        self.id_usuario=tk.StringVar()
        self.id_usuario.set(self.UsuarioName)
        
        labelUsuario=tk.Label(self.frame3,text="Usuario: "+self.id_usuario.get(),bg="dark blue",font=("Times New Roman",15), fg="white")
        labelUsuario.place(x=830,y=7)

        ##-------------------Botones predeterminados --------------------------

            #Boton menu
        self.hidemenu=1
        self.botonmenu=tk.Button(self.frame3,text="Menu", command=self.ocultarmostrarMenu,bg="blueviolet", bd= 5,font=("Times New Roman",15), fg="white",activebackground="light blue",activeforeground="Black")
        self.photo=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\home.png")
        self.botonmenu.config( image=self.photo, compound=LEFT)
        self.botonmenu.place(x=10,y=5)
        

        ########################################
        ##        Frame interactivo           ##
        ########################################
        
        self.frame4Interactivo=tk.Frame(self.ventana1)
        self.frame4Interactivo.config(bg='light cyan',bd=11)
        self.frame4Interactivo.place(x=-15,y=55,width=1050,height=580)

        ########## Frame Logo fundamusical

        self.frameLogo2=tk.Frame(self.frame4Interactivo,bg="light blue",width=623,height=306)
        self.frameLogo2.place(x=-50, y=340)

        self.imagen3=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\Pentagrama-removebg-preview.png")
        fondo2=tk.Label(self.frameLogo2,image=self.imagen3,bg="light cyan").place(x=0,y=0)
        
        #Label titulo
        self.labeltitulo=tk.Label(self.frame4Interactivo,text="Gestión de instrumentos",bg="light cyan",font=("Times New Roman",20), fg="Black")
        self.labeltitulo.place(x=20,y=30)

        #Label frame para cada una de las funciones

        #--------------- Label frame opciones

        self.frameOpcioneslabel=tk.LabelFrame(self.frame4Interactivo,text='Opciones',font=("Times New Roman",20))
        self.frameOpcioneslabel.config(bg="light cyan")
        self.frameOpcioneslabel.place(x=20,y=100)


        ####------------------- Botones en label frame opciones

        btnAgregar=tk.Button(self.frameOpcioneslabel,text="Agregar nuevo",font=("Times New Roman",14),command=self.agregar_instrumento)
        btnAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnAgregar.grid(row=1,column=2,ipady=10,ipadx=10,padx=10,pady=20)

        btnModificar=tk.Button(self.frameOpcioneslabel,text="Modificar",font=("Times New Roman",14), command=self.modificarInstrumento)
        btnModificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnModificar.grid(row=1,column=3,ipady=10,ipadx=30,padx=10,pady=20)


        #---------------------- labelframe lista de alumnos 

        self.framedecorativo=tk.Frame(self.frame4Interactivo)
        self.framedecorativo.config(bg="dark blue")
        self.framedecorativo.place(x=400,y=-10,width=650,height=900)

        ########## Frame Logo fundamusical

        self.frameLogo2=tk.Frame(self.framedecorativo,bg="light blue",width=624,height=257)
        self.frameLogo2.place(x=0, y=320)

        self.imagen2=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\pentagramaColor.png")
        fondo2=tk.Label(self.frameLogo2,image=self.imagen2,bg="dark blue").place(x=0,y=0)

        self.labelinfo=tk.Label(self.framedecorativo,text="Situación actual",bg="dark blue",font=("Times New Roman",20), fg="white")
        self.labelinfo.place(x=0,y=10)
        self.labelinfo.pack(padx=1)

        self.framebusquedas=tk.Frame(self.framedecorativo,bg="White")
        self.framebusquedas.place(x=-10,y=40,width=600,height=210)
        self.framebusquedas.pack(pady=20,side="top")

      
         ##Tree para mostrar columnas
        self.tree = ttk.Treeview(self.framebusquedas,columns=("#1","#2","#3","#4","#5","#6","#7"),height="9")
        self.tree.heading("#0",text="Serial")
        self.tree.heading("#1",text="Nro inventario")
        self.tree.heading("#2",text="Descripción")
        self.tree.heading("#3",text="Marca")
        self.tree.heading("#4",text="Condición")
        self.tree.heading("#5",text="Ubicación")
        self.tree.heading("#6",text="Procedencia")
        self.tree.heading("#7",text="Vigente")
        
            ##Tamano de columnas

        self.tree.column("#0",width=90)
        self.tree.column("#1",width=90)
        self.tree.column("#2",width=70)
        self.tree.column("#3",width=50)
        self.tree.column("#4",width=80)
        self.tree.column("#5",width=75)
        self.tree.column("#6",width=80)
        self.tree.column("#7",width=40)

        self.tree.bind("<1>",self.getrow_instrumentos)
        
        self.tree.pack(side="left")


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.framebusquedas, orient="vertical", command = self.tree.yview)
        scrolvert.pack(side="left",fill="y")
        self.tree.config(yscrollcommand=scrolvert.set)

        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        alumno=self.tree.get_children()

        for elemento in alumno:
            self.tree.delete(elemento)
        try:
            cur.execute("SELECT num_serial,cod_inventario,descripcion,marca,condicion,ubicacion,procedencia,comodato_vigente FROM instrumento")
            for row in cur:
                self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
        except:
            pass

        
         ##Tamano de columnas

        ########## Botón más información

        self.frameinfo=tk.LabelFrame(self.framedecorativo,text='',font=("Times New Roman",20))
        self.frameinfo.config(bg="dark blue")
        self.frameinfo.place(x=20,y=290)

        self.hide=1
        self.btnInfo=tk.Button(self.frameinfo,text="Más información",font=("Times New Roman",11),command=self.ocultarMostrarDetalles)
        self.btnInfo.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        self.btnInfo.grid(row=0,column=0,ipady=5,ipadx=5,padx=10,pady=10)

        self.labelDetalle=tk.Label(self.framedecorativo,text="Detalles generales",bg="dark blue",font=("Times New Roman",20), fg="white")
        self.labelDetalle.place(x=180,y=300)
        #Mainloop----------------------------------------------
        self.ventana1.mainloop()

    def modificarInstrumento(self):
        self.ventana1.destroy()
        self.ventana2=tk.Tk()
        self.ventana2.title("Modificar Instrumento")
        self.ventana2.config(bg='Light cyan')
        self.ventana2.geometry("1150x650")
        self.ventana2.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")

        #### Frame Logo

        self.frameLogo=tk.Frame(self.ventana2,bg="light blue",width=190,height=202)
        self.frameLogo.place(x=22, y= 45)

        self.imagen2=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\ClaveSolSPequena.png")
        fondo=tk.Label(self.frameLogo,image=self.imagen2,bg="light cyan").place(x=0,y=0)

        #### Frame Logo

        self.frameLogo2=tk.Frame(self.ventana2,bg="light blue",width=190,height=202)
        self.frameLogo2.place(x=923, y= 45)

        self.imagen3=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\ClaveSolSPequena.png")
        fondo=tk.Label(self.frameLogo2,image=self.imagen3,bg="light cyan").place(x=0,y=0)

        self.decoraframe=tk.Frame(self.ventana2,bg="dark blue",height=20)
        self.decoraframe.pack(fill="both",expand="no",side="top")

        self.lista=tk.LabelFrame(self.ventana2,text="Instrumentos disponibles",font=("Times New Roman",10))
        self.lista.config(bg="light cyan")
        self.lista.pack(expand="no",padx=5,pady=5,ipady=10,side="top")

        self.tree = ttk.Treeview(self.lista,columns=("#1","#2","#3","#4","#5","#6","#7","#8","#9"),height="7")
        self.tree.heading("#0",text="Serial")
        self.tree.heading("#1",text="Nro inventario")
        self.tree.heading("#2",text="Descripcion")
        self.tree.heading("#3",text="Marca")
        self.tree.heading("#4",text="Medida")
        self.tree.heading("#5",text="Condición")
        self.tree.heading("#6",text="Ubicación")
        self.tree.heading("#7",text="Procedencia")
        self.tree.heading("#8",text="Vigente")
        self.tree.heading("#9",text="Accesorio")

        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.tree.get_children()

        for elemento in profesor:
            self.tree.delete(elemento)
        try:
            cur.execute("SELECT num_serial,cod_inventario,descripcion,marca,medida,condicion,ubicacion,procedencia,comodato_vigente,accesorio FROM instrumento")
            for row in cur:
                self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
        except:
            pass

        con.close()
        self.tree.column("#0",width=90)
        self.tree.column("#1",width=95)
        self.tree.column("#2",width=70)
        self.tree.column("#3",width=50)
        self.tree.column("#4",width=80)
        self.tree.column("#5",width=80)
        self.tree.column("#6",width=75)
        self.tree.column("#7",width=100)
        self.tree.column("#8",width=50)
        self.tree.column("#9",width=50)
        
        self.tree.bind("<1>",self.getrow_instrumentos)
        self.tree.pack(side="left",fill="both",padx=5,pady=5)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.lista, orient="vertical", command = self.tree.yview)
        scrolvert.pack(side="left",fill="y")
        self.tree.config(yscrollcommand=scrolvert.set)

        #####################################
        ######### Label frame ###############

        self.buscador=tk.LabelFrame(self.ventana2,text='Buscador',font=("Times New Roman",10))
        self.buscador.config(bg="light cyan")
        self.modificar=tk.LabelFrame(self.ventana2,text="Actualizar informacion",font=("Times New Roman",10))
        self.modificar.config(bg="light cyan")

        self.buscador.pack(fill="both",expand="no",padx=5,pady=20,side="left")
        self.modificar.pack(fill="both",expand="yes",padx=20,pady=20,side="right")

        #### Frame Logo

        self.frameLogo=tk.Frame(self.buscador,bg="light blue",width=249,height=249)
        self.frameLogo.place(x=15, y= 95)

        self.imagen=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\saxo.png")
        fondo=tk.Label(self.frameLogo,image=self.imagen,bg="light cyan").place(x=0,y=0)

        #######################################
        ###       Para el self.buscador         ####

        label1=tk.Label(self.buscador,text="Consulta por:",bg="Light cyan",font=("Times New Roman",10))
        label1.grid(row=1,column=0,padx=5,pady=5)

        self.buscador1=tk.StringVar()
        self.entry1=tk.Entry(self.buscador,width=30,textvariable=self.buscador1,font=("Times New Roman",10))
        self.entry1.grid(row=4,column=1,padx=5,pady=5)

        lableBucar=tk.Label(self.buscador,text="Buscar:",bg="Light cyan",font=("Times New Roman",10))
        lableBucar.grid(row=4,column=0,padx=5,pady=5)

        self.opcion=tk.StringVar()
        opcionesBusqueda=("Serial","Nro inventario","Descripción","Marca","Procedencia","Vigencia","Condición","Ubicación")
         
        self.comobox1=ttk.Combobox(self.buscador,
                                width=20,
                                textvariable=self.opcion,
                                values=opcionesBusqueda,
                                state='readonly',
                                font=("Times New Roman",10))
        self.comobox1.current(0)

       
        self.comobox1.grid(row=1,column=1)

        btnBuscar=tk.Button(self.buscador,text="Buscar",command=self.search,font=("Times New Roman",10))
        btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnBuscar.grid(row=6,column=0,padx=5,pady=5)

        btnLimpiar=tk.Button(self.buscador,text="Limpiar",command=self.clear,font=("Times New Roman",10))
        btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnLimpiar.grid(row=6,column=1,padx=5,pady=5)

        

        ############################################
        ################### Para self.modificar #########


        label2=tk.Label(self.modificar,text="(*)Serial:",bg="Light cyan",font=("Times New Roman",10))
        label2.grid(row=1,column=0,padx=10,pady=10)

        label3=tk.Label(self.modificar,bg="light cyan",text="Nro Inventario:",font=("Times New Roman",10))
        label3.grid(row=2,column=0,padx=10,pady=10)

        label4=tk.Label(self.modificar,text="Descripción:",bg="Light cyan",font=("Times New Roman",10))
        label4.grid(row=3,column=0,padx=10,pady=10)

        label5=tk.Label(self.modificar,bg="light cyan",text="Marca:",font=("Times New Roman",10))
        label5.grid(row=4,column=0,padx=10,pady=10)

        label6=tk.Label(self.modificar,text="Medida:",bg="Light cyan",font=("Times New Roman",10))
        label6.grid(row=5,column=0,padx=10,pady=10)

        label7=tk.Label(self.modificar,bg="light cyan",text="Condición:",font=("Times New Roman",10))
        label7.grid(row=6,column=0,padx=10,pady=10)

        label8=tk.Label(self.modificar,bg="light cyan",text="Ubicación:",font=("Times New Roman",10))
        label8.grid(row=7,column=0,padx=10,pady=10)

        label9=tk.Label(self.modificar,bg="light cyan",text="Procedencia:",font=("Times New Roman",10))
        label9.grid(row=8,column=0,padx=10,pady=10)
    
        ###############################
        self.tserial=tk.StringVar()
        self.tinv=tk.StringVar()
        self.tdescripcion=tk.StringVar()
        self.tmarca=tk.StringVar()
        self.tmedida=tk.StringVar()
        self.tubicacion=tk.StringVar()
        self.taccesorio=tk.StringVar()
        

        
        self.entryserial=ttk.Entry(self.modificar,textvariable=self.tserial,font=("Times New Roman",10))
        self.entryserial.grid(row=1,column=1,padx=10,pady=10)

        self.entryInventario=ttk.Entry(self.modificar,textvariable=self.tinv,font=("Times New Roman",10))
        self.entryInventario.grid(row=2,column=1,padx=10,pady=10)

        self.entrydescripcion=ttk.Entry(self.modificar,textvariable=self.tdescripcion,font=("Times New Roman",10))
        self.entrydescripcion.grid(row=3,column=1,padx=10,pady=10)

        self.entryMarca=ttk.Entry(self.modificar,textvariable=self.tmarca,font=("Times New Roman",10))
        self.entryMarca.grid(row=4,column=1,padx=10,pady=10)

        self.entryMedida=ttk.Entry(self.modificar,textvariable=self.tmedida,font=("Times New Roman",10))
        self.entryMedida.grid(row=5,column=1,padx=10,pady=10)

        self.opcionCondicion=tk.StringVar()
        opcionesCondicion=("OPERATIVO","DAÑADO","HURTO","INOPERATIVO")
        self.comoboxCondicion=ttk.Combobox(self.modificar,
                                        width=20,
                                        textvariable=self.opcionCondicion,
                                        values=opcionesCondicion,
                                        state='readonly',
                                        font=("Times New Roman",12))
        self.comoboxCondicion.current(0)
        self.comoboxCondicion.grid(row=6,column=1,padx=10,pady=10)

        self.entryUbicacion=ttk.Entry(self.modificar,textvariable=self.tubicacion,font=("Times New Roman",10))
        self.entryUbicacion.grid(row=7,column=1,padx=10,pady=10)

        self.opcionProcedencia=tk.StringVar()
        opcionesProcedencia=("FMSB","DSR","COMODATO","OTRO")
        self.comoboxProcedencia=ttk.Combobox(self.modificar,
                                        width=20,
                                        textvariable=self.opcionProcedencia,
                                        values=opcionesProcedencia,
                                        state='readonly',
                                        font=("Times New Roman",12))
        self.comoboxProcedencia.current(0)
        self.comoboxProcedencia.grid(row=8,column=1,padx=10,pady=10)

        ####################################
        #         Otra columna


        label10=tk.Label(self.modificar,bg="light cyan",text="Vigencia:",font=("Times New Roman",10))
        label10.grid(row=1,column=3,padx=10,pady=10)

        label11=tk.Label(self.modificar,bg="light cyan",text="Accesorio:",font=("Times New Roman",10))
        label11.grid(row=2,column=3,padx=10,pady=10)

        ##########################################
      

        self.opcionVigencia=tk.StringVar()
        opcionesVigencia=("SI","NO")
        self.comoboxVigencia=ttk.Combobox(self.modificar,
                                        width=20,
                                        textvariable=self.opcionVigencia,
                                        values=opcionesVigencia,
                                        state='readonly',
                                        font=("Times New Roman",12))
        self.comoboxVigencia.current(0)
        self.comoboxVigencia.grid(row=1,column=4,padx=10,pady=10)

       
        self.entryAccesorio=ttk.Entry(self.modificar,textvariable=self.taccesorio,font=("Times New Roman",10))
        self.entryAccesorio.grid(row=2,column=4,padx=10,pady=10)

        ##################### BOTONES #######################

        btnAgregar=tk.Button(self.modificar,text="Agregar",command=self.add_new_instrumento,font=("Times New Roman",10))
        btnAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        #btnAgregar.grid(row=1,column=6,padx=2,pady=4)
        btnAgregar.place(x=580,y=60,width=100,height=50)


        btnModificar=tk.Button(self.modificar,text="Modificar",command=self.update_instrumento,font=("Times New Roman",10))
        btnModificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnModificar.place(x=580,y=120,width=100,height=50)

        btnEliminar=tk.Button(self.modificar,text="Eliminar",command=self.delete_instrumento,font=("Times New Roman",10))
        btnEliminar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnEliminar.place(x=580,y=180,width=100,height=50)

        btnVolver=tk.Button(self.modificar,text="Volver",command=self.volver_instrumento,font=("Times New Roman",10))
        btnVolver.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnVolver.place(x=580,y=240,width=100,height=50)

        ################### DECORACIONES #####################

        framedeco=tk.Frame(self.ventana2)
        framedeco.config(bg="Dark blue",bd=5,height="20",width="40")
        framedeco.pack(fill="both",expand="no",padx=5,pady=20,side="left")

        self.ventana2.resizable(False,False)
        self.ventana2.mainloop()

    def search(self):
        opcioncontrol=self.comobox1.get()
        buscarLista=self.entry1.get()
        if opcioncontrol=="Serial":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT num_serial,cod_inventario,descripcion,marca, medida,condicion,ubicacion,procedencia,comodato_vigente,accesorio FROM instrumento WHERE num_serial LIKE '%"+buscarLista+"%' ORDER BY descripcion DESC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateLista(respuesta)

        if opcioncontrol=="Nro inventario":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT num_serial,cod_inventario,descripcion,marca, medida,condicion,ubicacion,procedencia,comodato_vigente,accesorio FROM instrumento WHERE cod_inventario LIKE '%"+buscarLista+"%' ORDER BY descripcion DESC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateLista(respuesta)

        if opcioncontrol=="Descripción":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT num_serial,cod_inventario,descripcion,marca, medida,condicion,ubicacion,procedencia,comodato_vigente,accesorio FROM instrumento WHERE descripcion LIKE '%"+buscarLista+"%' ORDER BY descripcion DESC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateLista(respuesta)

        if opcioncontrol=="Marca":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT num_serial,cod_inventario,descripcion,marca, medida,condicion,ubicacion,procedencia,comodato_vigente,accesorio FROM instrumento WHERE marca LIKE '%"+buscarLista+"%' ORDER BY descripcion DESC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateLista(respuesta)

        if opcioncontrol=="Procedencia":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT num_serial,cod_inventario,descripcion,marca, medida,condicion,ubicacion,procedencia,comodato_vigente,accesorio FROM instrumento WHERE procedencia LIKE '%"+buscarLista+"%' ORDER BY descripcion DESC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateLista(respuesta)

        if opcioncontrol=="Vigencia":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT num_serial,cod_inventario,descripcion,marca, medida,condicion,ubicacion,procedencia,comodato_vigente,accesorio FROM instrumento WHERE comodato_vigente LIKE '%"+buscarLista+"%' ORDER BY descripcion DESC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateLista(respuesta)

        if opcioncontrol=="Condición":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT num_serial,cod_inventario,descripcion,marca, medida,condicion,ubicacion,procedencia,comodato_vigente,accesorio FROM instrumento WHERE condicion LIKE '%"+buscarLista+"%' ORDER BY descripcion DESC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateLista(respuesta)

        if opcioncontrol=="Ubicación":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT num_serial,cod_inventario,descripcion,marca, medida,condicion,ubicacion,procedencia,comodato_vigente,accesorio FROM instrumento WHERE ubicacion LIKE '%"+buscarLista+"%' ORDER BY descripcion DESC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateLista(respuesta)

    def clear(self):
        query="SELECT num_serial,cod_inventario,descripcion,marca, medida,condicion,ubicacion,procedencia,comodato_vigente,accesorio FROM instrumento"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.updateLista(respuesta)

    def updateLista(self,respuesta):
        info=self.tree.get_children()

        for elemento in info:
            self.tree.delete(elemento)
        for row in respuesta:
            self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))

    def getrow_instrumentos(self,event):
        rowid=self.tree.identify_row(event.y)
        self.tree.selection_set(rowid)
        item=self.tree.item(self.tree.focus())
        self.serial_num=item["text"]
        
        ############ Busca la informacion en la base de datos

        query="SELECT num_serial,cod_inventario,descripcion,marca, medida,condicion,ubicacion,procedencia,comodato_vigente,accesorio FROM instrumento WHERE num_serial='"+self.serial_num+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        
        if len(respuesta)>0:
            self.tserial.set(respuesta[0][0])
            self.tinv.set(respuesta[0][1])
            self.tdescripcion.set(respuesta[0][2])
            self.tmarca.set(respuesta[0][3])
            self.tmedida.set(respuesta[0][4])
            self.opcionCondicion.set(respuesta[0][5])
            self.tubicacion.set(respuesta[0][6])
            self.opcionProcedencia.set(respuesta[0][7])
            self.opcionVigencia.set(respuesta[0][8])
            self.taccesorio.set(respuesta[0][9])
             
    ###### Restricciones ###########
    def validar_Serial(self):
        cedula=self.tserial.get()
        validar=re.match('[a-z/0-999999]+$',cedula,re.I)
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

    def add_new_instrumento(self):
        serial=self.tserial.get()
        inventario=self.tinv.get()
        descripcion=self.tdescripcion.get()
        marca=self.tmarca.get()
        medida=self.tmedida.get()
        condicion=self.opcionCondicion.get()
        ubicacion=self.tubicacion.get()
        procedencia=self.opcionProcedencia.get()
        vigencia=self.opcionVigencia.get()
        accesorio=self.taccesorio.get()
        

        try:
            if self.validar_Serial():
                query="INSERT INTO instrumento(num_serial,descripcion,marca,medida,accesorio,condicion,ubicacion,procedencia,comodato_vigente,cod_inventario) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(serial,descripcion,marca,medida,accesorio,condicion,ubicacion,procedencia,vigencia,inventario))
                
                cone.commit()
                cone.close()
                self.clear()
                mb.showinfo("Información","Se han cargado con éxito los datos.")
                self.tserial.set("")
                self.tinv.set("")
                self.tdescripcion.set("")
                self.tmarca.set("")
                self.tmedida.set("")
                self.taccesorio.set("")
                self.tubicacion.set("")
                self.tinv.set("")
            else:
                mb.showwarning("Error","Debe completar los campos obligatorios")
        except:
            mb.showinfo("Información","Este dato ya existe")

    def update_instrumento(self):
        serial=self.tserial.get()
        inventario=self.tinv.get()
        descripcion=self.tdescripcion.get()
        marca=self.tmarca.get()
        medida=self.tmedida.get()
        condicion=self.opcionCondicion.get()
        ubicacion=self.tubicacion.get()
        procedencia=self.opcionProcedencia.get()
        vigencia=self.opcionVigencia.get()
        accesorio=self.taccesorio.get()
        
        

        if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea actualizar estos datos? "):
            if self.validar_Serial():
            
                query="UPDATE instrumento SET num_serial=%s,descripcion=%s,marca=%s,medida=%s,accesorio=%s,condicion=%s,ubicacion=%s,procedencia=%s,comodato_vigente=%s,cod_inventario=%s WHERE num_serial=%s"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(serial,descripcion,marca,medida,accesorio,condicion,ubicacion,procedencia,vigencia,inventario,serial))
                

                cone.commit()
                cone.close()

                self.clear()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han cargado con éxito los datos.")
                    self.tserial.set("")
                    self.tinv.set("")
                    self.tdescripcion.set("")
                    self.tmarca.set("")
                    self.tmedida.set("")
                    self.taccesorio.set("")
                    self.tubicacion.set("")
                    self.tinv.set("")

                else:
                    mb.showinfo("Informacion", "No existe un instrumento con dicha informacion")
                
            else:
                mb.showwarning("Error","Debe seleccionar los campos a modificar")
        else:
            return True

    def delete_instrumento(self):
        serial=self.tserial.get()
        try:
            if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea borrar estos datos? "):
                query="DELETE FROM instrumento WHERE num_serial='"+serial+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query)
            
                cone.commit()
                cone.close()
                self.clear()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han borrado los datos con éxito.")
                    self.tserial.set("")
                    self.tinv.set("")
                    self.tdescripcion.set("")
                    self.tmarca.set("")
                    self.tmedida.set("")
                    self.taccesorio.set("")
                    self.tubicacion.set("")
                    self.tinv.set("")

                else:
                    mb.showinfo("Informacion", "No existe un instrumento con dicha informacion")
                

            else:
                return True
        except:
            mb.showwarning("Error","Introduzca la informacion que desee borrar o selecione en la tablaRepresentante.")
    
    ################################ MODULO ALUMNOS ##################################

    def alumnos(self):
        self.ocultarmostrarMenu()

        self.frame4Interactivo.place_forget()

        ########################################
        ##        Frame interactivo           ##
        ########################################

        self.frame4Interactivo=tk.Frame(self.ventana1)
        self.frame4Interactivo.config(bg='light cyan',bd=11)
        self.frame4Interactivo.place(x=-15,y=55,width=1050,height=580)


        #### Frame Logo

        self.frameLogo=tk.Frame(self.frame4Interactivo,bg="light cyan",width=343,height=223)
        self.frameLogo.place(x=285, y= 1)

        self.imagen=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\music.png")
        fondo=tk.Label(self.frameLogo,image=self.imagen,bg="light cyan").place(x=0,y=0)

         #Label titulo frame
        self.labeltitulo=tk.Label(self.frame4Interactivo,text="Gestión de alumnos",bg="light cyan",font=("Times New Roman",20), fg="Black")
        self.labeltitulo.place(x=20,y=30)

         #Label total
        self.label2=tk.Label(self.frame4Interactivo,text="Total alumnos:",bg="light cyan",font=("Times New Roman",16), fg="Black")
        self.label2.place(x=40,y=70)

        #####################################################
        #######     Respuesta total profesores        #######
        #####################################################

        self.labelrespuesta=tk.Label(self.frame4Interactivo,text=" ",bg="light cyan",font=("Times New Roman",16), fg="Black")
        self.labelrespuesta.place(x=180,y=70)
        
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select COUNT(cod_alumno)  from alumno"
        cursor.execute(sql)
        respuesta=cursor.fetchall() 
        self.cuenta=respuesta[0][0]
        cone.close()

        self.labelrespuesta.config(text=self.cuenta)

        #############################################
        self.frameDeco=tk.Frame(self.frame4Interactivo,bg="dark blue")
        self.frameDeco.place(x=-11,y=290,width=1051,height=300)

        self.labelframetree=tk.LabelFrame(self.frame4Interactivo,text="Inscritos",bg="light cyan",font=("Times New Roman",15))
        self.labelframetree.place(x=50,y=150)

      
         ##Tree para mostrar columnas
        self.tree = ttk.Treeview(self.labelframetree,columns=("#1","#2","#3","#4","#5","#6","#7","#8","#9"),height="9")
        self.tree.heading("#0",text="Cédula")
        self.tree.heading("#1",text="Nombres")
        self.tree.heading("#2",text="Apellidos")
        self.tree.heading("#3",text="Edad")
        self.tree.heading("#4",text="Programa")
        self.tree.heading("#5",text="Nivel")
        self.tree.heading("#6",text="Sexo")
        self.tree.heading("#7",text="Fecha nacimiento")
        self.tree.heading("#8",text="Dirección")
        self.tree.heading("#9",text="Instrumento principal")
        
            ##Tamano de columnas
        self.tree.column("#0",width=90)
        self.tree.column("#1",width=90)
        self.tree.column("#2",width=70)
        self.tree.column("#3",width=40)
        self.tree.column("#4",width=100)
        self.tree.column("#5",width=90)
        self.tree.column("#6",width=40)
        self.tree.column("#7",width=120)
        self.tree.column("#8",width=120)
        self.tree.column("#9",width=120)

        self.tree.bind("<1>",self.getrow_instrumentos)
        
        self.tree.pack(side="top",padx=20,pady=20)


        # SCROLL VERTICAL TREEVIEW
        #scrolvert = st.Scrollbar(self.framebusquedas, orient="vertical", command = self.tree.yview)
        #scrolvert.pack(side="left",fill="y")
        #self.tree.config(yscrollcommand=scrolvert.set)

        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        alumno=self.tree.get_children()

        for elemento in alumno:
            self.tree.delete(elemento)
        try:
            cur.execute("SELECT a.ci_alumno,a.nombres,a.apellidos,a.edad,b.nombre_programa,a.nivel,a.sexo,a.fecha_nacimiento,a.direccion,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa ORDER BY a.apellidos ASC")
            for row in cur:
                self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
        except:
            pass

        
         ##Tamano de columnas

        
        #################### BUSCADOR 

        self.buscador=tk.LabelFrame(self.frame4Interactivo,text='Buscador',font=("Times New Roman",10))
        self.buscador.config(bg="light cyan")
        self.buscador.place(x= 600, y= 1)

        label1=tk.Label(self.buscador,text="Consulta por:",bg="Light cyan",font=("Times New Roman",10))
        label1.grid(row=1,column=0,padx=5,pady=5)

        self.buscador1=tk.StringVar()
        self.entry1=tk.Entry(self.buscador,width=30,textvariable=self.buscador1,font=("Times New Roman",10))
        self.entry1.grid(row=4,column=1,padx=5,pady=5)

        self.labelprograma=tk.Label(self.buscador,text="Programa:",bg="Light cyan",font=("Times New Roman",10))
        self.labelprograma.grid(row=2,column=0,padx=5,pady=5)

        ############### Combobox interactivo

        self.opcionPrograma=tk.StringVar()
        self.comobox2=ttk.Combobox(self.buscador,
                                width=20,
                                textvariable=self.opcionPrograma,
                                state='readonly',
                                font=("Times New Roman",10))

        self.comobox2['value']=self.cargarComboProgramas()
        self.comobox2.current(0)
        self.comobox2.grid(row=2,column=1,padx=5,pady=1)

        #################################################################

        lableBucar=tk.Label(self.buscador,text="Buscar:",bg="Light cyan",font=("Times New Roman",10))
        lableBucar.grid(row=4,column=0,padx=5,pady=5)

        self.opcion=tk.StringVar()
        opcionesBusqueda=("Nombres","Apellidos","Cédula","Nivel")
         
        self.comobox1=ttk.Combobox(self.buscador,
                                width=20,
                                textvariable=self.opcion,
                                values=opcionesBusqueda,
                                state='readonly',
                                font=("Times New Roman",10))
        self.comobox1.current(1)

       
        self.comobox1.grid(row=1,column=1)

        btnBuscar=tk.Button(self.buscador,text="Buscar",command=self.searchAlumno,font=("Times New Roman",10),width=9)
        btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnBuscar.grid(row=6,column=0,padx=5,pady=5)

        btnLimpiar=tk.Button(self.buscador,text="Limpiar",command=self.clearAlumno,font=("Times New Roman",10),width=9)
        btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnLimpiar.grid(row=6,column=2,padx=5,pady=5)


        ##################################### Pequeño menú de tres opciones Modificar, asignar instrumento y Gestionar Representantes

       
        self.labelframeMenu=tk.LabelFrame(self.frame4Interactivo,text="Gestión de alumnos",bg="dark blue",font=("Times New Roman",20),fg="white")
        self.labelframeMenu.place(x=50,y=420)

        self.btnModificarAlumno=tk.Button(self.labelframeMenu,text="Modificar",command=self.modificarAlumno,bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,width=22,font=("Times New Roman",16))
        self.btnModificarAlumno.grid(column=2,row=0,padx=20)

        self.btnRepresentante=tk.Button(self.labelframeMenu,text=" Gestión Representantes",command=self.representante,bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,width=22,font=("Times New Roman",16))
        self.btnRepresentante.grid(column=4,row=0,pady=20)

        self.btnModificarAlumno=tk.Button(self.labelframeMenu,text="Asignar instrumento",command=self.asignarInstrumento,bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,width=22,font=("Times New Roman",16))
        self.btnModificarAlumno.grid(column=6,row=0,padx=20)

    ######################### COmbobox interactivo Programas
    def cargarComboProgramas(self):
        query="SELECT nombre_programa FROM programa WHERE nombre_programa NOT IN ('Administración')"

        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        db_rows=cursor.fetchall()
        data=[]
        for rows in db_rows:
            data.append(rows[0])
        return data
    ##########################################################
        
    def searchAlumno(self):
        opcioncontrol=self.comobox1.get()
        buscarLista=self.buscador1.get()
        opcionPrograma=self.comobox2.get()
        if opcioncontrol=="Nombres":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.ci_alumno,a.nombres,a.apellidos,a.edad,b.nombre_programa,a.nivel,a.sexo,a.fecha_nacimiento,a.direccion,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa AND a.nombres LIKE '%"+buscarLista+"%' AND b.nombre_programa='"+opcionPrograma+"'  ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAlumno(respuesta)


        if opcioncontrol=="Apellidos":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.ci_alumno,a.nombres,a.apellidos,a.edad,b.nombre_programa,a.nivel,a.sexo,a.fecha_nacimiento,a.direccion,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa AND a.apellidos LIKE '%"+buscarLista+"%' AND b.nombre_programa='"+opcionPrograma+"'  ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAlumno(respuesta)

        if opcioncontrol=="Cédula":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.ci_alumno,a.nombres,a.apellidos,a.edad,b.nombre_programa,a.nivel,a.sexo,a.fecha_nacimiento,a.direccion,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa AND a.ci_alumno LIKE '%"+buscarLista+"%' AND b.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAlumno(respuesta)

        if opcioncontrol=="Nivel":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.ci_alumno,a.nombres,a.apellidos,a.edad,b.nombre_programa,a.nivel,a.sexo,a.fecha_nacimiento,a.direccion,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa AND a.nivel LIKE '%"+buscarLista+"%' AND b.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAlumno(respuesta)

    def clearAlumno(self):
        query="SELECT a.ci_alumno,a.nombres,a.apellidos,a.edad,b.nombre_programa,a.nivel,a.sexo,a.fecha_nacimiento,a.direccion,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa ORDER BY a.apellidos ASC"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.buscador1.set("")
        self.updateListaAlumno(respuesta)

    def updateListaAlumno(self,respuesta):
        info=self.tree.get_children()

        for elemento in info:
            self.tree.delete(elemento)
        for row in respuesta:
            self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
    ########################## Modificar Alumno, gestion representantes y asignar instrumento

    def modificarAlumno(self):
        self.ventana1.destroy()
        self.ventana2=tk.Tk()
        self.ventana2.title("Modificar Alumno")
        self.ventana2.config(bg='Light cyan')
        self.ventana2.geometry("1150x650")
        self.ventana2.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")

        #### Frame Logo

        self.frameLogo=tk.Frame(self.ventana2,bg="light blue",width=190,height=202)
        self.frameLogo.place(x=22, y= 45)

        self.imagen2=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\ClaveSolSPequena.png")
        fondo=tk.Label(self.frameLogo,image=self.imagen2,bg="light cyan").place(x=0,y=0)

        #### Frame Logo

        self.frameLogo2=tk.Frame(self.ventana2,bg="light blue",width=190,height=202)
        self.frameLogo2.place(x=903, y= 45)

        self.imagen3=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\ClaveSolSPequena.png")
        fondo=tk.Label(self.frameLogo2,image=self.imagen3,bg="light cyan").place(x=0,y=0)


        self.decoraframe=tk.Frame(self.ventana2,bg="dark blue",height=20)
        self.decoraframe.pack(fill="both",expand="no",side="top")

        self.lista=tk.LabelFrame(self.ventana2,text="Instrumentos disponibles",font=("Times New Roman",10))
        self.lista.config(bg="light cyan")
        self.lista.pack(expand="no",padx=5,pady=5,ipady=10,side="top")

        self.tree = ttk.Treeview(self.lista,columns=("#1","#2","#3","#4","#5","#6","#7","#8","#9","#10"),height="7")
        self.tree.heading("#0",text="Código")
        self.tree.heading("#1",text="Cédula")
        self.tree.heading("#2",text="Nombres")
        self.tree.heading("#3",text="Apellidos")
        self.tree.heading("#4",text="edad")
        self.tree.heading("#5",text="Programa")
        self.tree.heading("#6",text="Nivel")
        self.tree.heading("#7",text="Sexo")
        self.tree.heading("#8",text="Fecha de nacimiento")
        self.tree.heading("#9",text="Dirección")
        self.tree.heading("#10",text="Instrumento principal")

        self.tree.column("#0",width=80)
        self.tree.column("#1",width=45)
        self.tree.column("#2",width=70)
        self.tree.column("#3",width=70)
        self.tree.column("#4",width=29)
        self.tree.column("#5",width=50)
        self.tree.column("#6",width=50)
        self.tree.column("#7",width=25)
        self.tree.column("#8",width=70)
        self.tree.column("#9",width=70)
        self.tree.column("#10",width=50)
        
        self.tree.bind("<1>",self.getrow_Modificar_Alumnos)
        self.tree.pack(side="left",fill="both",padx=5,pady=5)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.lista, orient="vertical", command = self.tree.yview)
        scrolvert.pack(side="left",fill="y")
        self.tree.config(yscrollcommand=scrolvert.set)
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.tree.get_children()

        for elemento in profesor:
            self.tree.delete(elemento)
        try:
            cur.execute("SELECT  a.cod_alumno,a.ci_alumno,a.nombres,a.apellidos,a.edad,b.nombre_programa,a.nivel,a.sexo,a.fecha_nacimiento,a.direccion,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa")
            rows=cur.fetchall()
            for row in rows:
                self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
        except:
            pass

        con.close()
        

        #####################################
        ######### Label frame ###############

        self.buscador=tk.LabelFrame(self.ventana2,text='Buscador',font=("Times New Roman",10))
        self.buscador.config(bg="light cyan")
        self.modificar=tk.LabelFrame(self.ventana2,text="Actualizar informacion",font=("Times New Roman",10))
        self.modificar.config(bg="light cyan")

        self.buscador.pack(fill="both",expand="no",padx=5,pady=20,side="left")
        self.modificar.pack(fill="both",expand="yes",padx=20,pady=20,side="right")

        #### Frame Logo

        self.frameLogo=tk.Frame(self.buscador,bg="light blue",width=268,height=185)
        self.frameLogo.place(x=7, y= 159)

        self.imagen=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\alumno.png")
        fondo=tk.Label(self.frameLogo,image=self.imagen,bg="light cyan").place(x=0,y=0)

        #######################################
        ###       Para el self.buscador         ####

        label1=tk.Label(self.buscador,text="Consulta por:",bg="Light cyan",font=("Times New Roman",10))
        label1.grid(row=1,column=0,padx=5,pady=5)

        self.opcion=tk.StringVar()
        opcionesBusqueda=("Cédula","Código alumno","Nombres","Apellidos","Nivel","Instrumento principal")
         
        self.comobox1=ttk.Combobox(self.buscador,
                                width=20,
                                textvariable=self.opcion,
                                values=opcionesBusqueda,
                                state='readonly')
        

       
        self.comobox1.grid(row=1,column=1)
        self.comobox1.current(0)

        ################## combobox interactivo

        lableBucar=tk.Label(self.buscador,text="Programa:",bg="Light cyan",font=("Times New Roman",10))
        lableBucar.grid(row=4,column=0,padx=5,pady=5)

        self.opcionPrograma=tk.StringVar()
        self.comoboxProgramaBus=ttk.Combobox(self.buscador,
                                width=20,
                                textvariable=self.opcionPrograma,
                                state='readonly',
                                font=("Times New Roman",10))
        
        self.comoboxProgramaBus['value']=self.cargarComboProgramas()
        self.comoboxProgramaBus.current(1)

        self.comoboxProgramaBus.grid(row=4,column=1,padx=5,pady=15)
        

        

        self.buscador1=tk.StringVar()
        self.entry1=tk.Entry(self.buscador,width=30,textvariable=self.buscador1,font=("Times New Roman",10))
        self.entry1.grid(row=5,column=1,padx=5,pady=5)

        lableBucar=tk.Label(self.buscador,text="Buscar:",bg="Light cyan",font=("Times New Roman",10))
        lableBucar.grid(row=5,column=0,padx=5,pady=5)

        btnBuscar=tk.Button(self.buscador,text="Buscar",command=self.searchAlumnosModificar,font=("Times New Roman",10))
        btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnBuscar.grid(row=6,column=0,padx=5,pady=5)

        btnLimpiar=tk.Button(self.buscador,text="Limpiar",command=self.clearAlumnosModificar,font=("Times New Roman",10))
        btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnLimpiar.grid(row=6,column=1,padx=5,pady=5)

        

        ############################################
        ################### Para self.modificar #########


        label2=tk.Label(self.modificar,text="Cédula de identidad:",bg="Light cyan",font=("Times New Roman",10))
        label2.grid(row=1,column=0,padx=10,pady=10)

        label3=tk.Label(self.modificar,bg="light cyan",text="(*)Código alumno:",font=("Times New Roman",10))
        label3.grid(row=2,column=0,padx=10,pady=10)

        label4=tk.Label(self.modificar,text="Nombres:",bg="Light cyan",font=("Times New Roman",10))
        label4.grid(row=3,column=0,padx=10,pady=10)

        label5=tk.Label(self.modificar,bg="light cyan",text="Apellidos:",font=("Times New Roman",10))
        label5.grid(row=4,column=0,padx=10,pady=10)

        label6=tk.Label(self.modificar,text="Edad:",bg="Light cyan",font=("Times New Roman",10))
        label6.grid(row=5,column=0,padx=10,pady=10)

        label7=tk.Label(self.modificar,bg="light cyan",text="Programa:",font=("Times New Roman",10))
        label7.grid(row=6,column=0,padx=10,pady=10)

        label8=tk.Label(self.modificar,bg="light cyan",text="Nivel:",font=("Times New Roman",10))
        label8.grid(row=7,column=0,padx=10,pady=10)

        label9=tk.Label(self.modificar,bg="light cyan",text="Sexo:",font=("Times New Roman",10))
        label9.grid(row=8,column=0,padx=10,pady=10)
        
        
        ###############################
        self.tcialumno=tk.StringVar()
        self.tcodalumno=tk.StringVar()
        self.tnombre=tk.StringVar()
        self.tapellido=tk.StringVar()
        self.tedad=tk.StringVar()
        self.opcionNivel=tk.StringVar()
        self.opcionSexo=tk.StringVar()
        
        self.entryserial=ttk.Entry(self.modificar,textvariable=self.tcialumno,font=("Times New Roman",10))
        self.entryserial.grid(row=1,column=1,padx=10,pady=10)

        self.entryInventario=ttk.Entry(self.modificar,textvariable=self.tcodalumno,font=("Times New Roman",10))
        self.entryInventario.grid(row=2,column=1,padx=10,pady=10)

        self.entrydescripcion=ttk.Entry(self.modificar,textvariable=self.tnombre,font=("Times New Roman",10))
        self.entrydescripcion.grid(row=3,column=1,padx=10,pady=10)

        self.entryMarca=ttk.Entry(self.modificar,textvariable=self.tapellido,font=("Times New Roman",10))
        self.entryMarca.grid(row=4,column=1,padx=10,pady=10)

        self.entryMedida=ttk.Entry(self.modificar,textvariable=self.tedad,font=("Times New Roman",10))
        self.entryMedida.grid(row=5,column=1,padx=10,pady=10)

        ################## combobox interactivo

        self.opcionPrograma=tk.StringVar()
        self.comoboxProgramaModificar=ttk.Combobox(self.modificar,
                                width=20,
                                textvariable=self.opcionPrograma,
                                state='readonly',
                                font=("Times New Roman",10))

        self.comoboxProgramaModificar['value']=self.cargarComboProgramas()
        self.comoboxProgramaModificar.grid(row=6,column=1,padx=5,pady=15)

        self.comoboxProgramaModificar.current(0)

        opcionesNivel=("Inicial","Infantil","Juvenil")
        self.comoboxNivel=ttk.Combobox(self.modificar,
                                width=20,
                                textvariable=self.opcionNivel,
                                values=opcionesNivel,
                                state='readonly',
                                font=("Times New Roman",10))
        self.comoboxNivel.current(0)
        self.comoboxNivel.grid(row=7,column=1,padx=10,pady=10)

        opcionesSexo=("F","M")
        self.comobox4=ttk.Combobox(self.modificar,
                                width=20,
                                textvariable=self.opcionSexo,
                                values=opcionesSexo,
                                state='readonly',
                                font=("Times New Roman",10))
        self.comobox4.current(0)
        self.comobox4.grid(row=8,column=1,padx=10,pady=10)

        ####################################
        #         Otra columna


        label10=tk.Label(self.modificar,bg="light cyan",text="Fecha de nacimiento:",font=("Times New Roman",10))
        label10.grid(row=1,column=3,padx=10,pady=10)

        label11=tk.Label(self.modificar,bg="light cyan",text="Dirección:",font=("Times New Roman",10))
        label11.grid(row=2,column=3,padx=10,pady=10)

        label12=tk.Label(self.modificar,bg="light cyan",text="Instrumento principal:",font=("Times New Roman",10))
        label12.grid(row=3,column=3,padx=10,pady=10)

        ##########################################
      

        self.tFnacimiento=tk.StringVar()
        self.tdireccion=tk.StringVar()
        self.tinstrumentoPr1ncipal=tk.StringVar()
       
        self.entryFechaNacimiento=ttk.Entry(self.modificar,textvariable=self.tFnacimiento,font=("Times New Roman",10))
        self.entryFechaNacimiento.grid(row=1,column=4,padx=10,pady=10)

        self.entryDireccion=ttk.Entry(self.modificar,textvariable=self.tdireccion,font=("Times New Roman",10))
        self.entryDireccion.grid(row=2,column=4,padx=10,pady=10)

        self.entryInstrumentoPrin=ttk.Entry(self.modificar,textvariable=self.tinstrumentoPr1ncipal,font=("Times New Roman",10))
        self.entryInstrumentoPrin.grid(row=3,column=4,padx=10,pady=10)

        ##################### BOTONES #######################

        btnAgregar=tk.Button(self.modificar,text="Agregar",command=self.add_new_Alumno)
        btnAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",10))
        btnAgregar.place(x=635,y=60,width=100,height=50)

        btnModificar=tk.Button(self.modificar,text="Modificar",command=self.update_Alumno)
        btnModificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",10))
        btnModificar.place(x=635,y=120,width=100,height=50)

        btnEliminar=tk.Button(self.modificar,text="Eliminar",command=self.delete_Alumno)
        btnEliminar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",10))
        btnEliminar.place(x=635,y=180,width=100,height=50)

        btnVolver=tk.Button(self.modificar,text="Volver",command=self.volver_Alumno)
        btnVolver.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",10))
        btnVolver.place(x=635,y=240,width=100,height=50)

        ################### DECORACIONES #####################

        framedeco=tk.Frame(self.ventana2)
        framedeco.config(bg="Dark blue",bd=5,height="20",width="40")
        framedeco.pack(fill="both",expand="no",padx=5,pady=20,side="left")

        self.ventana2.resizable(False,False)
        self.ventana2.mainloop()

    ################# Comandos botones para buscar
    def searchAlumnosModificar(self):
        opcioncontrol=self.comobox1.get()
        buscarLista=self.buscador1.get()
        opcionPrograma=self.comoboxProgramaBus.get()
        if opcioncontrol=="Nombres":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, a.ci_alumno, a.nombres,a.apellidos,a.edad,b.nombre_programa,a.nivel,a.sexo,a.fecha_nacimiento,a.direccion,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa AND a.nombres LIKE '%"+buscarLista+"%' AND b.nombre_programa='"+opcionPrograma+"'  ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAlumnoModificar(respuesta)

        if opcioncontrol=="Apellidos":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, a.ci_alumno, a.nombres,a.apellidos,a.edad,b.nombre_programa,a.nivel,a.sexo,a.fecha_nacimiento,a.direccion,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa AND a.apellidos LIKE '%"+buscarLista+"%' AND b.nombre_programa='"+opcionPrograma+"'  ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAlumnoModificar(respuesta)

        if opcioncontrol=="Cédula":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, a.ci_alumno, a.nombres,a.apellidos,a.edad,b.nombre_programa,a.nivel,a.sexo,a.fecha_nacimiento,a.direccion,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa AND a.ci_alumno LIKE '%"+buscarLista+"%' AND b.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAlumnoModificar(respuesta)

        if opcioncontrol=="Nivel":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, a.ci_alumno, a.nombres,a.apellidos,a.edad,b.nombre_programa,a.nivel,a.sexo,a.fecha_nacimiento,a.direccion,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa AND a.nivel LIKE '%"+buscarLista+"%' AND b.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAlumnoModificar(respuesta)

        if opcioncontrol=="Código de alumno":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, a.ci_alumno,, a.nombres,a.apellidos,a.edad,b.nombre_programa,a.nivel,a.sexo,a.fecha_nacimiento,a.direccion,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa AND a.cod_alumno LIKE '%"+buscarLista+"%' AND b.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAlumnoModificar(respuesta)

        if opcioncontrol=="Instrumento principal":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, a.ci_alumno, a.nombres,a.apellidos,a.edad,b.nombre_programa,a.nivel,a.sexo,a.fecha_nacimiento,a.direccion,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa AND a.instrumento_principal LIKE '%"+buscarLista+"%' AND b.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAlumnoModificar(respuesta)

    def clearAlumnosModificar(self):
        query="SELECT  a.cod_alumno, a.ci_alumno, a.nombres,a.apellidos,a.edad,b.nombre_programa,a.nivel,a.sexo,a.fecha_nacimiento,a.direccion,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa ORDER BY a.apellidos ASC"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.buscador1.set("")
        self.updateListaAlumnoModificar(respuesta)

    #################### Comandos botones para modificar
    def add_new_Alumno(self):
        ci_alumno=self.tcialumno.get()
        codigo_alumno=self.tcodalumno.get()
        nombresAlumno=self.tnombre.get()
        apellidosAlumno=self.tapellido.get()
        edad=str(self.tedad.get())
        programa=str(self.definir_programa())
        nivel=self.opcionNivel.get()
        sexo=self.opcionSexo.get()
        nacimiento=self.tFnacimiento.get()
        direccion=self.tdireccion.get()
        instrumento_principal=self.tinstrumentoPr1ncipal.get()
        

        try:
            if self.validar_contrasena(codigo_alumno):
                query="INSERT INTO alumno(cod_alumno,ci_alumno,nombres,apellidos,edad,id_programa,nivel,sexo,fecha_nacimiento,direccion,instrumento_principal) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(codigo_alumno,ci_alumno,nombresAlumno,apellidosAlumno,edad,programa,nivel,sexo,nacimiento,direccion,instrumento_principal))
                
                cone.commit()
                cone.close()
                self.clearAlumnosModificar()
                mb.showinfo("Información","Se han cargado con éxito los datos.")
                self.tcialumno.set("")
                self.tcodalumno.set("")
                self.tnombre.set("")
                self.tapellido.set("")
                self.tedad.set("")
                self.tFnacimiento.set("")
                self.tdireccion.set("")
                self.tinstrumentoPr1ncipal.set("")
            else:
                mb.showwarning("Error","Debe completar los campos obligatorios")
        except:
            mb.showinfo("Información","Este dato ya existe")

    def definir_programa(self):
        opcioncontrol=self.opcionPrograma.get()
        query="SELECT id_programa FROM programa WHERE nombre_programa='"+opcioncontrol+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()

        return respuesta[0][0]
    
    def update_Alumno(self):
        ci_alumno=self.tcialumno.get()
        codigo_alumno=self.tcodalumno.get()
        nombresAlumno=self.tnombre.get()
        apellidosAlumno=self.tapellido.get()
        edad=str(self.tedad.get())
        programa=str(self.definir_programa())
        nivel=self.opcionNivel.get()
        sexo=self.opcionSexo.get()
        nacimiento=self.tFnacimiento.get()
        direccion=self.tdireccion.get()
        instrumento_principal=self.tinstrumentoPr1ncipal.get()
        
        

        if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea actualizar estos datos? "):
            if self.validar_contrasena(codigo_alumno):
            
                query="UPDATE alumno SET cod_alumno=%s,ci_alumno=%s,nombres=%s,apellidos=%s,edad=%s,id_programa=%s,nivel=%s,sexo=%s,fecha_nacimiento=%s,direccion=%s,instrumento_principal=%s WHERE cod_alumno='"+self.cod_alumno+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(codigo_alumno,ci_alumno,nombresAlumno,apellidosAlumno,edad,programa,nivel,sexo,nacimiento,direccion,instrumento_principal))
                

                cone.commit()
                cone.close()

                self.clearAlumnosModificar()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han cargado con éxito los datos.")
                    self.tcialumno.set("")
                    self.tcodalumno.set("")
                    self.tnombre.set("")
                    self.tapellido.set("")
                    self.tedad.set("")
                    self.tFnacimiento.set("")
                    self.tdireccion.set("")
                    self.tinstrumentoPr1ncipal.set("")
                else:
                    mb.showinfo("Informacion", "No existe un alumno con dicha informacion")
                
            else:
                mb.showwarning("Error","Debe seleccionar los campos a modificar")
        else:
            return True

    def delete_Alumno(self):
        cod_alumno=self.tcodalumno.get()
        try:
            if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea borrar estos datos? "):
                query="DELETE FROM alumno WHERE cod_alumno='"+cod_alumno+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query)
            
                cone.commit()
                cone.close()
                self.clearAlumnosModificar()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han borrado los datos con éxito.")
                    self.tcialumno.set("")
                    self.tcodalumno.set("")
                    self.tnombre.set("")
                    self.tapellido.set("")
                    self.tedad.set("")
                    self.tFnacimiento.set("")
                    self.tdireccion.set("")
                    self.tinstrumentoPr1ncipal.set("")
                else:
                    mb.showinfo("Informacion", "No existe un alumno con dicha informacion")
            else:
                return True
        except:
            mb.showwarning("Error","Introduzca la informacion que desee borrar o selecione en la tablaRepresentante.")

    def getrow_Modificar_Alumnos(self,event):
        rowid=self.tree.identify_row(event.y)
        self.tree.selection_set(rowid)
        item=self.tree.item(self.tree.focus())
        self.cod_alumno=item["text"]
        
        ############ Busca la informacion en la base de datos

        query="SELECT a.ci_alumno, a.cod_alumno,a.nombres,a.apellidos,a.edad,b.nombre_programa,a.nivel,a.sexo,a.fecha_nacimiento,a.direccion,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa AND cod_alumno='"+self.cod_alumno+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        
        if len(respuesta)>0:
            self.tcialumno.set(respuesta[0][0])
            self.tcodalumno.set(respuesta[0][1])
            self.tnombre.set(respuesta[0][2])
            self.tapellido.set(respuesta[0][3])
            self.tedad.set(respuesta[0][4])
            self.opcionPrograma.set(respuesta[0][5])
            self.opcionNivel.set(respuesta[0][6])
            self.opcionSexo.set(respuesta[0][7])
            self.tFnacimiento.set(respuesta[0][8])
            self.tdireccion.set(respuesta[0][9])
            self.tinstrumentoPr1ncipal.set(respuesta[0][10])

    def volverModificarRepresentante(self):
        self.representante()

    def volver_Alumno(self):
        self.ventana2.destroy()

        ###Programa estandar para las ventanas ---------------------
        self.ventana1=tk.Tk()
        self.ventana1.title("Administrador")
        self.ventana1.geometry("1050x650")
        self.ventana1.config(bg='light cyan',bd=15)
        self.ventana1.resizable(0,0)
        self.ventana1.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")

        #-------------------------------------------------------

        #Frame admin decorativo
        self.frame1=tk.Frame(self.ventana1)

        #Frame admin informacion tentativa
        self.frame2=tk.Frame(self.ventana1)

        #Frame informacion de los usuarios
        self.frame3=tk.Frame(self.ventana1)
        self.frame3.config(bg="dark blue",bd=11)
        self.frame3.place(x=-15,y=-15,width=1050,height=70)

        #label informacion de profesores
        self.label1=tk.Label(self.frame3,text="Administrador",bg="dark blue",font=("Times New Roman",20), fg="white")
        self.label1.place(x=110,y=10)

        # Información usuario
        self.id_usuario=tk.StringVar()
        self.id_usuario.set(self.UsuarioName)
        
        labelUsuario=tk.Label(self.frame3,text="Usuario: "+self.id_usuario.get(),bg="dark blue",font=("Times New Roman",15), fg="white")
        labelUsuario.place(x=830,y=7)

        ##-------------------Botones predeterminados --------------------------

        self.hidemenu=1
        self.botonmenu=tk.Button(self.frame3,text="Menu", command=self.ocultarmostrarMenu,bg="blueviolet", bd= 5,font=("Times New Roman",15), fg="white",activebackground="light blue",activeforeground="Black")
        self.photo=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\home.png")
        self.botonmenu.config( image=self.photo, compound=LEFT)
        self.botonmenu.place(x=10,y=5)

        ########################################
        ##        Frame interactivo           ##
        ########################################

        self.frame4Interactivo=tk.Frame(self.ventana1)
        self.frame4Interactivo.config(bg='light cyan',bd=11)
        self.frame4Interactivo.place(x=-15,y=55,width=1050,height=580)

        #### Frame Logo

        self.frameLogo=tk.Frame(self.frame4Interactivo,bg="light cyan",width=343,height=223)
        self.frameLogo.place(x=285, y= 1)

        self.imagen=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\music.png")
        fondo=tk.Label(self.frameLogo,image=self.imagen,bg="light cyan").place(x=0,y=0)

         #Label titulo frame
        self.labeltitulo=tk.Label(self.frame4Interactivo,text="Gestión de alumnos",bg="light cyan",font=("Times New Roman",20), fg="Black")
        self.labeltitulo.place(x=20,y=30)

         #Label total
        self.label2=tk.Label(self.frame4Interactivo,text="Total alumnos:",bg="light cyan",font=("Times New Roman",16), fg="Black")
        self.label2.place(x=40,y=70)

        #####################################################
        #######     Respuesta total profesores        #######
        #####################################################

        self.labelrespuesta=tk.Label(self.frame4Interactivo,text=" ",bg="light cyan",font=("Times New Roman",16), fg="Black")
        self.labelrespuesta.place(x=180,y=70)
        
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select COUNT(cod_alumno)  from alumno"
        cursor.execute(sql)
        respuesta=cursor.fetchall() 
        self.cuenta=respuesta[0][0]
        cone.close()

        self.labelrespuesta.config(text=self.cuenta)

        #############################################
        self.frameDeco=tk.Frame(self.frame4Interactivo,bg="dark blue")
        self.frameDeco.place(x=-11,y=290,width=1051,height=300)

        self.labelframetree=tk.LabelFrame(self.frame4Interactivo,text="Inscritos",bg="light cyan",font=("Times New Roman",15))
        self.labelframetree.place(x=50,y=150)

      
         ##Tree para mostrar columnas
        self.tree = ttk.Treeview(self.labelframetree,columns=("#1","#2","#3","#4","#5","#6","#7","#8","#9"),height="9")
        self.tree.heading("#0",text="Cédula")
        self.tree.heading("#1",text="Nombres")
        self.tree.heading("#2",text="Apellidos")
        self.tree.heading("#3",text="Edad")
        self.tree.heading("#4",text="Programa")
        self.tree.heading("#5",text="Nivel")
        self.tree.heading("#6",text="Sexo")
        self.tree.heading("#7",text="Fecha nacimiento")
        self.tree.heading("#8",text="Dirección")
        self.tree.heading("#9",text="Instrumento principal")
        
            ##Tamano de columnas
        self.tree.column("#0",width=90)
        self.tree.column("#1",width=90)
        self.tree.column("#2",width=70)
        self.tree.column("#3",width=40)
        self.tree.column("#4",width=100)
        self.tree.column("#5",width=90)
        self.tree.column("#6",width=40)
        self.tree.column("#7",width=120)
        self.tree.column("#8",width=120)
        self.tree.column("#9",width=120)

        self.tree.bind("<1>",self.getrow_instrumentos)
        
        self.tree.pack(side="top",padx=20,pady=20)


        # SCROLL VERTICAL TREEVIEW
        #scrolvert = st.Scrollbar(self.framebusquedas, orient="vertical", command = self.tree.yview)
        #scrolvert.pack(side="left",fill="y")
        #self.tree.config(yscrollcommand=scrolvert.set)

        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        alumno=self.tree.get_children()

        for elemento in alumno:
            self.tree.delete(elemento)
        try:
            cur.execute("SELECT a.ci_alumno,a.nombres,a.apellidos,a.edad,b.nombre_programa,a.nivel,a.sexo,a.fecha_nacimiento,a.direccion,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa ORDER BY a.apellidos ASC")
            for row in cur:
                self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
        except:
            pass

        
         ##Tamano de columnas

        
        #################### BUSCADOR 

        self.buscador=tk.LabelFrame(self.frame4Interactivo,text='Buscador',font=("Times New Roman",10))
        self.buscador.config(bg="light cyan")
        self.buscador.place(x= 600, y= 1)

        label1=tk.Label(self.buscador,text="Consulta por:",bg="Light cyan",font=("Times New Roman",10))
        label1.grid(row=1,column=0,padx=5,pady=5)

        self.buscador1=tk.StringVar()
        self.entry1=tk.Entry(self.buscador,width=30,textvariable=self.buscador1,font=("Times New Roman",10))
        self.entry1.grid(row=4,column=1,padx=5,pady=5)

        self.labelprograma=tk.Label(self.buscador,text="Programa:",bg="Light cyan",font=("Times New Roman",10))
        self.labelprograma.grid(row=2,column=0,padx=5,pady=5)

        ############### Combobox interactivo

        self.opcionPrograma=tk.StringVar()
        self.comobox2=ttk.Combobox(self.buscador,
                                width=20,
                                textvariable=self.opcionPrograma,
                                state='readonly',
                                font=("Times New Roman",10))

        self.comobox2['value']=self.cargarComboProgramas()
        self.comobox2.current(0)
        self.comobox2.grid(row=2,column=1,padx=5,pady=1)

        #################################################################

        lableBucar=tk.Label(self.buscador,text="Buscar:",bg="Light cyan",font=("Times New Roman",10))
        lableBucar.grid(row=4,column=0,padx=5,pady=5)

        self.opcion=tk.StringVar()
        opcionesBusqueda=("Nombres","Apellidos","Cédula","Nivel")
         
        self.comobox1=ttk.Combobox(self.buscador,
                                width=20,
                                textvariable=self.opcion,
                                values=opcionesBusqueda,
                                state='readonly',
                                font=("Times New Roman",10))
        self.comobox1.current(1)

       
        self.comobox1.grid(row=1,column=1)

        btnBuscar=tk.Button(self.buscador,text="Buscar",command=self.searchAlumno,font=("Times New Roman",10),width=9)
        btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnBuscar.grid(row=6,column=0,padx=5,pady=5)

        btnLimpiar=tk.Button(self.buscador,text="Limpiar",command=self.clearAlumno,font=("Times New Roman",10),width=9)
        btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnLimpiar.grid(row=6,column=2,padx=5,pady=5)


        ##################################### Pequeño menú de tres opciones Modificar, asignar instrumento y Gestionar Representantes

       
        self.labelframeMenu=tk.LabelFrame(self.frame4Interactivo,text="Gestión de alumnos",bg="dark blue",font=("Times New Roman",20),fg="white")
        self.labelframeMenu.place(x=50,y=420)

        self.btnModificarAlumno=tk.Button(self.labelframeMenu,text="Modificar",command=self.modificarAlumno,bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,width=22,font=("Times New Roman",16))
        self.btnModificarAlumno.grid(column=2,row=0,padx=20)

        self.btnRepresentante=tk.Button(self.labelframeMenu,text=" Gestión Representantes",command=self.representante,bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,width=22,font=("Times New Roman",16))
        self.btnRepresentante.grid(column=4,row=0,pady=20)

        self.btnModificarAlumno=tk.Button(self.labelframeMenu,text="Asignar instrumento",command=self.asignarInstrumento,bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,width=22,font=("Times New Roman",16))
        self.btnModificarAlumno.grid(column=6,row=0,padx=20)

    def updateListaAlumnoModificar(self,respuesta):
        info=self.tree.get_children()

        for elemento in info:
            self.tree.delete(elemento)
        for row in respuesta:
            self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))

########################## gestion representantes 

    def representante(self):
        self.ventana1.destroy()
        self.ventana2=tk.Tk()
        self.ventana2.title("Representantes")
        self.ventana2.config(bg='Light cyan')
        self.ventana2.geometry("1150x650")
        self.ventana2.resizable(0,0)
        self.ventana2.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")

        self.decoraframe=tk.Frame(self.ventana2,bg="dark blue",height=20)
        self.decoraframe.pack(fill="both",expand="no",side="top")

        frameoscuro=tk.Frame(self.ventana2,bg="dark blue",height=330)
        frameoscuro.pack(fill="both",expand="no",side="bottom")

        self.lista=tk.LabelFrame(self.ventana2,text="Agregar nuevo",font=("Times New Roman",10))
        self.lista.config(bg="light cyan")
        self.lista.place(x=10,y=20)

        self.tablaRepresentante=tk.LabelFrame(self.ventana2,text="Lista representantes",font=("Times New Roman",10))
        self.tablaRepresentante.config(bg="light cyan")
        self.tablaRepresentante.place(x=150,y=20)

        self.tablaAlumnos=tk.LabelFrame(self.ventana2,text="Lista Alumnos",font=("Times New Roman",10))
        self.tablaAlumnos.config(bg="light cyan")
        self.tablaAlumnos.place(x=300,y=176)

        self.labelframeRepresentantesSeleccion=tk.LabelFrame(self.ventana2,text="Selección Representante",font=("Times New Roman",15),fg="white")
        self.labelframeRepresentantesSeleccion.config(bg="dark blue")
        self.labelframeRepresentantesSeleccion.place(x=1,y=325)

        self.labelframeAlumnosSeleccion=tk.LabelFrame(self.ventana2,text="Selección Alumno",font=("Times New Roman",15),fg="white")
        self.labelframeAlumnosSeleccion.config(bg="dark blue")
        self.labelframeAlumnosSeleccion.place(x=280,y=325)

        self.labelframeTablaAlumnosRepresentantes=tk.LabelFrame(self.ventana2,text="Alumnos con su representante",font=("Times New Roman",15),fg="white")
        self.labelframeTablaAlumnosRepresentantes.config(bg="dark blue")
        self.labelframeTablaAlumnosRepresentantes.place(x=530,y=325)

        self.labelframeopcionesAR=tk.LabelFrame(self.ventana2,text="Alumnos con su representante",font=("Times New Roman",15),fg="white")
        self.labelframeopcionesAR.config(bg="dark blue")
        self.labelframeopcionesAR.place(x=10,y=530)

        self.buscador=tk.LabelFrame(self.ventana2,text='Buscador',font=("Times New Roman",10))
        self.buscador.config(bg="light cyan")
        self.buscador.place(x= 555, y= 530)

        ###################### Ventana agregar nuevo

        btnAgregarNuevo=tk.Button(self.lista,text="Agregar nuevo",command=self.agregarNuevoRepresentante)
        btnAgregarNuevo.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12),width=12)
        btnAgregarNuevo.grid(row=0,column=4,padx=2,pady=10)

        btnVolver=tk.Button(self.lista,text="Volver",command=self.volver_Alumno)
        btnVolver.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12),width=12)
        btnVolver.grid(row=1,column=4,padx=2,pady=10)

        ########################## TREEVIEW REPRESENTANTES

        self.tree = ttk.Treeview(self.tablaRepresentante,columns=("#1","#2","#3","#4","#5","#6","#7","#8","#9"),height="5")
        self.tree.heading("#0",text="Cédula")
        self.tree.heading("#1",text="Nombres")
        self.tree.heading("#2",text="Apellidos")
        self.tree.heading("#3",text="Teléfono celular")
        self.tree.heading("#4",text="Teléfono Fijo")
        self.tree.heading("#5",text="Profesión")
        self.tree.heading("#6",text="Ocupación")
        self.tree.heading("#7",text="Vive con alumno")
        self.tree.heading("#8",text="Filiación")
        self.tree.heading("#9",text="Dirección")

        self.tree.column("#0",width=70)
        self.tree.column("#1",width=100)
        self.tree.column("#2",width=100)
        self.tree.column("#3",width=100)
        self.tree.column("#4",width=100)
        self.tree.column("#5",width=120)
        self.tree.column("#6",width=120)
        self.tree.column("#7",width=25)
        self.tree.column("#8",width=75)
        self.tree.column("#9",width=70)
        
        self.tree.bind("<1>",self.getrow_seleccion_representante)
        self.tree.pack(side="left",fill="both",padx=5,pady=5)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.tablaRepresentante, orient="vertical", command = self.tree.yview)
        scrolvert.pack(side="left",fill="y")
        self.tree.config(yscrollcommand=scrolvert.set)
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.tree.get_children()

        for elemento in profesor:
            self.tree.delete(elemento)
        try:
            cur.execute("SELECT ci_representante,nombres,apellidos,telefono_celular,telefono_fijo,profesion,ocupacion,vive_con_alumno,filiacion_representado,direccion FROM representante")
            rows=cur.fetchall()
            for row in rows:
                self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
        except:
            pass

        con.close()
        #################### Treeview Alumnos

        self.treeAlumno = ttk.Treeview(self.tablaAlumnos,columns=("#1","#2","#3","#4"),height="4")
        self.treeAlumno.heading("#0",text="Código")
        self.treeAlumno.heading("#1",text="Cédula")
        self.treeAlumno.heading("#2",text="Nombres")
        self.treeAlumno.heading("#3",text="Apellidos")
        self.treeAlumno.heading("#4",text="Programa")

        self.treeAlumno.column("#0",width=100)
        self.treeAlumno.column("#1",width=70)
        self.treeAlumno.column("#2",width=130)
        self.treeAlumno.column("#3",width=130)
        self.treeAlumno.column("#4",width=160)
        
        self.treeAlumno.bind("<1>",self.getrow_seleccion_alumnos)
        self.treeAlumno.pack(side="right",fill="both",padx=5,pady=5)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.tablaAlumnos, orient="vertical", command = self.tree.yview)
        scrolvert.pack(side="left",fill="y")
        self.treeAlumno.config(yscrollcommand=scrolvert.set)
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.treeAlumno.get_children()

        for elemento in profesor:
            self.treeAlumno.delete(elemento)
        try:
            cur.execute("SELECT  a.cod_alumno,a.ci_alumno,a.nombres,a.apellidos,b.nombre_programa FROM alumno a, programa b WHERE a.id_programa=b.id_programa")
            rows=cur.fetchall()
            for row in rows:
                self.treeAlumno.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4]))
        except:
            pass

        con.close()

        #################### Labelframe seleccion representantes Label

        labelCiRepresentanteSel=tk.Label(self.labelframeRepresentantesSeleccion,bg="dark blue",text="(*)Cédula de identidad:",font=("Times New Roman",10),fg="white")
        labelCiRepresentanteSel.grid(row=0,column=1,padx=1,pady=10)

        labelnombres=tk.Label(self.labelframeRepresentantesSeleccion,bg="dark blue",text="Nombres:",font=("Times New Roman",10),fg="white")
        labelnombres.grid(row=1,column=1,padx=1,pady=10)

        labelapellidos=tk.Label(self.labelframeRepresentantesSeleccion,bg="dark blue",text="Apellidos:",font=("Times New Roman",10),fg="white")
        labelapellidos.grid(row=2,column=1,padx=1,pady=10)

        labelfiliacion=tk.Label(self.labelframeRepresentantesSeleccion,bg="dark blue",text="Filiacion:",font=("Times New Roman",10),fg="white")
        labelfiliacion.grid(row=3,column=1,padx=1,pady=10)

        ####################### Entrys
        self.Tci_representante=tk.StringVar()
        self.Tnombres=tk.StringVar()
        self.Tapellidos=tk.StringVar()
        self.tfiliacion=tk.StringVar()

        self.entryCedulaRepresentante=ttk.Entry(self.labelframeRepresentantesSeleccion,textvariable=self.Tci_representante,font=("Times New Roman",10),state="readonly")
        self.entryCedulaRepresentante.grid(row=0,column=2,padx=1,pady=10)

        self.entrynombres=ttk.Entry(self.labelframeRepresentantesSeleccion,textvariable=self.Tnombres,font=("Times New Roman",10),state="readonly")
        self.entrynombres.grid(row=1,column=2,padx=1,pady=10)

        self.entryApellidos=ttk.Entry(self.labelframeRepresentantesSeleccion,textvariable=self.Tapellidos,font=("Times New Roman",10),state="readonly")
        self.entryApellidos.grid(row=2,column=2,padx=1,pady=10)

        self.entryfiliacion=ttk.Entry(self.labelframeRepresentantesSeleccion,textvariable=self.tfiliacion,font=("Times New Roman",10),state="readonly")
        self.entryfiliacion.grid(row=3,column=2,padx=1,pady=10)

        #################### Labelframe seleccion representantes Label

        self.codigoAlumno=tk.StringVar()
        self.nombresAlumno=tk.StringVar()
        self.apellidosAlumno=tk.StringVar()
        self.programaAlumno=tk.StringVar()

        labelcod_alumno=tk.Label(self.labelframeAlumnosSeleccion,bg="dark blue",text="(*)Código alumno:",font=("Times New Roman",10),fg="white")
        labelcod_alumno.grid(row=0,column=1,padx=1,pady=10)

        labelnombres=tk.Label(self.labelframeAlumnosSeleccion,bg="dark blue",text="Nombres:",font=("Times New Roman",10),fg="white")
        labelnombres.grid(row=1,column=1,padx=1,pady=10)

        labelapellidos=tk.Label(self.labelframeAlumnosSeleccion,bg="dark blue",text="Apellidos:",font=("Times New Roman",10),fg="white")
        labelapellidos.grid(row=2,column=1,padx=1,pady=10)

        labelprograma=tk.Label(self.labelframeAlumnosSeleccion,bg="dark blue",text="Programa:",font=("Times New Roman",10),fg="white")
        labelprograma.grid(row=3,column=1,padx=1,pady=10)

        ####################### Entrys

        self.entryCod_alumno=ttk.Entry(self.labelframeAlumnosSeleccion,textvariable=self.codigoAlumno,font=("Times New Roman",10),state="readonly")
        self.entryCod_alumno.grid(row=0,column=2,padx=1,pady=10)

        self.entrynombres=ttk.Entry(self.labelframeAlumnosSeleccion,textvariable=self.nombresAlumno,font=("Times New Roman",10),state="readonly")
        self.entrynombres.grid(row=1,column=2,padx=1,pady=10)

        self.entryApellidos=ttk.Entry(self.labelframeAlumnosSeleccion,textvariable=self.apellidosAlumno,font=("Times New Roman",10),state="readonly")
        self.entryApellidos.grid(row=2,column=2,padx=1,pady=10)

        self.entryprogramaSeleccion=ttk.Entry(self.labelframeAlumnosSeleccion,textvariable=self.programaAlumno,font=("Times New Roman",10),state="readonly")
        self.entryprogramaSeleccion.grid(row=3,column=2,padx=1,pady=10)

        ########################## TREEVIEW ALUMNOS Y REPRESENTANTES

        self.treeAlumnosRepresentantes = ttk.Treeview(self.labelframeTablaAlumnosRepresentantes,columns=("#1","#2","#3","#4","#5","#6","#7"),height="6")
        self.treeAlumnosRepresentantes.heading("#0",text="Código alumno")
        self.treeAlumnosRepresentantes.heading("#1",text="Nombres alumno")
        self.treeAlumnosRepresentantes.heading("#2",text="Apellidos alumno")
        self.treeAlumnosRepresentantes.heading("#3",text="Programa")
        self.treeAlumnosRepresentantes.heading("#4",text="Cédula representante")
        self.treeAlumnosRepresentantes.heading("#5",text="Nombres representante")
        self.treeAlumnosRepresentantes.heading("#6",text="Apellidos representante")
        self.treeAlumnosRepresentantes.heading("#7",text="Filiación")

        self.treeAlumnosRepresentantes.column("#0",width=70)
        self.treeAlumnosRepresentantes.column("#1",width=80)
        self.treeAlumnosRepresentantes.column("#2",width=80)
        self.treeAlumnosRepresentantes.column("#3",width=70)
        self.treeAlumnosRepresentantes.column("#4",width=70)
        self.treeAlumnosRepresentantes.column("#5",width=80)
        self.treeAlumnosRepresentantes.column("#6",width=80)
        self.treeAlumnosRepresentantes.column("#7",width=50)

        
        self.treeAlumnosRepresentantes.bind("<1>",self.getrow_Representante_alumno)
        self.treeAlumnosRepresentantes.pack(side="left",fill="both",padx=5,pady=5)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.labelframeTablaAlumnosRepresentantes, orient="vertical", command = self.tree.yview)
        scrolvert.pack(side="left",fill="y")
        self.treeAlumnosRepresentantes.config(yscrollcommand=scrolvert.set)
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.treeAlumnosRepresentantes.get_children()

        for elemento in profesor:
            self.treeAlumnosRepresentantes.delete(elemento)
        try:
            cur.execute("SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.ci_representante,b.nombres,b.apellidos,b.filiacion_representado FROM alumno a, representante b, representante_alumno c, programa d WHERE c.ci_representante=b.ci_representante AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno")
            rows=cur.fetchall()
            for row in rows:
                self.treeAlumnosRepresentantes.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
        except:
            pass

        con.close()

        ###################### Agregar, modificar y eliminar 

        btnAgregar=tk.Button(self.labelframeopcionesAR,text="Agregar",command=self.add_new_representante_alumno)
        btnAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12),width=16)
        btnAgregar.grid(row=0,column=1,padx=2,pady=10)

        btnmodificar=tk.Button(self.labelframeopcionesAR,text="Modificar",command=self.update_AlumnoRepresentante)
        btnmodificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12),width=16)
        btnmodificar.grid(row=0,column=2,padx=2,pady=10)

        btneliminar=tk.Button(self.labelframeopcionesAR,text="Eliminar",command=self.delete_representante_alumno)
        btneliminar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12),width=16)
        btneliminar.grid(row=0,column=3,padx=2,pady=10)

        #################### BUSCADOR 

        

        label1=tk.Label(self.buscador,text="Consulta por:",bg="Light cyan",font=("Times New Roman",10))
        label1.grid(row=0,column=0,padx=5,pady=5)

        self.buscador1=tk.StringVar()
        self.entry1=tk.Entry(self.buscador,width=30,textvariable=self.buscador1,font=("Times New Roman",10))
        self.entry1.grid(row=0,column=3,padx=5,pady=5)

        self.labelprograma=tk.Label(self.buscador,text="Programa:",bg="Light cyan",font=("Times New Roman",10))
        self.labelprograma.grid(row=1,column=0,padx=5,pady=5)

        ############### Combobox interactivo

        self.opcionPrograma=tk.StringVar()
        self.comobox2=ttk.Combobox(self.buscador,
                                width=20,
                                textvariable=self.opcionPrograma,
                                state='readonly',
                                font=("Times New Roman",10))

        self.comobox2['value']=self.cargarComboProgramas()
        self.comobox2.current(0)
        self.comobox2.grid(row=1,column=1,padx=5,pady=1)

        #################################################################

        lableBucar=tk.Label(self.buscador,text="Buscar:",bg="Light cyan",font=("Times New Roman",10))
        lableBucar.grid(row=0,column=2,padx=5,pady=5)

        self.opcion=tk.StringVar()
        opcionesBusqueda=("Nombres Alumno","Apellidos Alumno","Cédula Representante")
         
        self.comobox1=ttk.Combobox(self.buscador,
                                width=20,
                                textvariable=self.opcion,
                                values=opcionesBusqueda,
                                state='readonly',
                                font=("Times New Roman",10))
        self.comobox1.current(0)

       
        self.comobox1.grid(row=0,column=1)

        btnBuscar=tk.Button(self.buscador,text="Buscar",command=self.searchAlumnoRepresentante,font=("Times New Roman",10),width=9)
        btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnBuscar.grid(row=1,column=2,padx=5,pady=5)

        btnLimpiar=tk.Button(self.buscador,text="Limpiar",command=self.clearRepresentanteAlumno,font=("Times New Roman",10),width=9)
        btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnLimpiar.grid(row=1,column=3,padx=5,pady=5)

########################## Funciones

    def agregarNuevoRepresentante(self):
        try:
            self.ventana2.destroy()
            self.ventana1=tk.Tk()
            self.ventana1.title("Agregar Representante")
            self.ventana1.config(bg='light cyan')
            self.ventana1.geometry("625x450")
            self.ventana1.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")

                ###########------------------- Formulario label frame

            self.lista=tk.LabelFrame(self.ventana1,text="Agregar nuevo",font=("Times New Roman",10))
            self.lista.config(bg="light cyan")
            self.lista.pack(side="top",expand="no")

            self.tablaRepresentante=tk.LabelFrame(self.ventana1,text="Lista representantes",font=("Times New Roman",10))
            self.tablaRepresentante.config(bg="light cyan")
            self.tablaRepresentante.pack(side="bottom",expand="no")

            ####################### ENTRY Y LABELS REPRESENTANTES
            ################################## LABEL COLUMNA 1

            labelCiRepresentante=tk.Label(self.lista,bg="light cyan",text="(*)Cédula de identidad:",font=("Times New Roman",10))
            labelCiRepresentante.grid(row=0,column=1,padx=2,pady=10)

            labelnombres=tk.Label(self.lista,bg="light cyan",text="Nombres:",font=("Times New Roman",10))
            labelnombres.grid(row=1,column=1,padx=2,pady=10)

            labelapellidos=tk.Label(self.lista,bg="light cyan",text="Apellidos:",font=("Times New Roman",10))
            labelapellidos.grid(row=2,column=1,padx=2,pady=10)

            labeltelefonoCelular=tk.Label(self.lista,bg="light cyan",text="Teléfono celular:",font=("Times New Roman",10))
            labeltelefonoCelular.grid(row=3,column=1,padx=2,pady=10)

            labeltelefonoFijo=tk.Label(self.lista,bg="light cyan",text="Teléfono Fijo:",font=("Times New Roman",10))
            labeltelefonoFijo.grid(row=4,column=1,padx=2,pady=10)

            labelprofesion=tk.Label(self.lista,bg="light cyan",text="Profesión:",font=("Times New Roman",10))
            labelprofesion.grid(row=5,column=1,padx=2,pady=10)


            ######################## ENTRY COLUMNA 2

            self.Tci_representante=tk.StringVar()
            self.Tnombres=tk.StringVar()
            self.Tapellidos=tk.StringVar()
            self.Ttelcel=tk.StringVar()
            self.Ttelfijo=tk.StringVar()
            self.Tprofesion=tk.StringVar()

            self.entryCedulaRepresentante=ttk.Entry(self.lista,textvariable=self.Tci_representante,font=("Times New Roman",10))
            self.entryCedulaRepresentante.grid(row=0,column=2,padx=1,pady=10)

            self.entrynombres=ttk.Entry(self.lista,textvariable=self.Tnombres,font=("Times New Roman",10))
            self.entrynombres.grid(row=1,column=2,padx=1,pady=10)

            self.entryApellidos=ttk.Entry(self.lista,textvariable=self.Tapellidos,font=("Times New Roman",10))
            self.entryApellidos.grid(row=2,column=2,padx=1,pady=10)

            self.entrytelefonocelular=ttk.Entry(self.lista,textvariable=self.Ttelcel,font=("Times New Roman",10))
            self.entrytelefonocelular.grid(row=3,column=2,padx=1,pady=10)

            self.entryTelefonofijo=ttk.Entry(self.lista,textvariable=self.Ttelfijo,font=("Times New Roman",10))
            self.entryTelefonofijo.grid(row=4,column=2,padx=1,pady=10)

            self.entryProfesion=ttk.Entry(self.lista,textvariable=self.Tprofesion,font=("Times New Roman",10))
            self.entryProfesion.grid(row=5,column=2,padx=1,pady=10)

            ################################## LABEL COLUMNA 3

            labelocupacion=tk.Label(self.lista,bg="light cyan",text="Ocupación:",font=("Times New Roman",10))
            labelocupacion.grid(row=0,column=3,padx=2,pady=10)

            labelvive=tk.Label(self.lista,bg="light cyan",text="Vive con el alumno:",font=("Times New Roman",10))
            labelvive.grid(row=1,column=3,padx=2,pady=10) ### Combobox SI y NO

            labelfiliacion=tk.Label(self.lista,bg="light cyan",text="Filiacion:",font=("Times New Roman",10))
            labelfiliacion.grid(row=2,column=3,padx=2,pady=10)

            labeldireccion=tk.Label(self.lista,bg="light cyan",text="Dirección:",font=("Times New Roman",10))
            labeldireccion.grid(row=3,column=3,padx=2,pady=10)

            ######################## ENTRY COLUMNA 4

            self.tocupacion=tk.StringVar()
            self.tvive=tk.StringVar()
            self.tfiliacion=tk.StringVar()
            self.ttdireccion=tk.StringVar()

            self.entryocupacion=ttk.Entry(self.lista,textvariable=self.tocupacion,font=("Times New Roman",10))
            self.entryocupacion.grid(row=0,column=4,padx=1,pady=10)

            opcionesVive=("SI","NO")
            self.comoboxNivel=ttk.Combobox(self.lista,
                                    width=20,
                                    textvariable=self.tvive,
                                    values=opcionesVive,
                                    state='readonly',
                                    font=("Times New Roman",10))
            self.comoboxNivel.current(0)
            self.comoboxNivel.grid(row=1,column=4,padx=1,pady=10)

            self.entryfiliacion=ttk.Entry(self.lista,textvariable=self.tfiliacion,font=("Times New Roman",10))
            self.entryfiliacion.grid(row=2,column=4,padx=1,pady=10)

            self.entrydir=ttk.Entry(self.lista,textvariable=self.ttdireccion,font=("Times New Roman",10))
            self.entrydir.grid(row=3,column=4,padx=1,pady=10)

            ######################## Botones en las columnas 3 y 4

            btnAgregar=tk.Button(self.lista,text="Agregar",command=self.add_new_representante)
            btnAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",10),width=8)
            btnAgregar.grid(row=4,column=3,padx=2,pady=10)

            btnModificar=tk.Button(self.lista,text="Modificar",command=self.update_representante)
            btnModificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",10),width=8)
            btnModificar.grid(row=4,column=4,padx=2,pady=10)

            btnEliminar=tk.Button(self.lista,text="Eliminar",command=self.delete_representante)
            btnEliminar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",10),width=8)
            btnEliminar.grid(row=5,column=3,padx=2,pady=10)

            btnVolver=tk.Button(self.lista,text="Volver",command=self.volverModificarRepresentante)
            btnVolver.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",10),width=8)
            btnVolver.grid(row=5,column=4,padx=2,pady=10)

            self.tree = ttk.Treeview(self.tablaRepresentante,columns=("#1","#2","#3","#4","#5","#6","#7","#8","#9"),height="5")
            self.tree.heading("#0",text="Cédula")
            self.tree.heading("#1",text="Nombres")
            self.tree.heading("#2",text="Apellidos")
            self.tree.heading("#3",text="Teléfono celular")
            self.tree.heading("#4",text="Teléfono Fijo")
            self.tree.heading("#5",text="Profesión")
            self.tree.heading("#6",text="Ocupación")
            self.tree.heading("#7",text="Vive con alumno")
            self.tree.heading("#8",text="Filiación")
            self.tree.heading("#9",text="Dirección")

            self.tree.column("#0",width=70)
            self.tree.column("#1",width=70)
            self.tree.column("#2",width=70)
            self.tree.column("#3",width=70)
            self.tree.column("#4",width=70)
            self.tree.column("#5",width=50)
            self.tree.column("#6",width=50)
            self.tree.column("#7",width=25)
            self.tree.column("#8",width=45)
            self.tree.column("#9",width=70)
            
            self.tree.bind("<1>",self.getrow_Modificar_Representante)
            self.tree.pack(side="left",fill="both",padx=5,pady=5)


            # SCROLL VERTICAL TREEVIEW
            scrolvert = st.Scrollbar(self.tablaRepresentante, orient="vertical", command = self.tree.yview)
            scrolvert.pack(side="left",fill="y")
            self.tree.config(yscrollcommand=scrolvert.set)
            con=mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="", 
                                        database="bdnucleolecheria")

            cur=con.cursor()
            profesor=self.tree.get_children()

            for elemento in profesor:
                self.tree.delete(elemento)
            try:
                cur.execute("SELECT ci_representante,nombres,apellidos,telefono_celular,telefono_fijo,profesion,ocupacion,vive_con_alumno,filiacion_representado,direccion FROM representante")
                rows=cur.fetchall()
                for row in rows:
                    self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
            except:
                pass

            con.close()
        except:
            pass


        self.ventana1.mainloop()

    def getrow_seleccion_representante(self,event):
        rowid=self.tree.identify_row(event.y)
        self.tree.selection_set(rowid)
        item=self.tree.item(self.tree.focus())
        self.ci_representante=item["text"]
        
        ############ Busca la informacion en la base de datos

        query="SELECT ci_representante,nombres,apellidos,telefono_celular,telefono_fijo,profesion,ocupacion,vive_con_alumno,filiacion_representado,direccion FROM representante WHERE ci_representante='"+self.ci_representante+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        
        if len(respuesta)>0:
            self.Tci_representante.set(respuesta[0][0])
            self.Tnombres.set(respuesta[0][1])
            self.Tapellidos.set(respuesta[0][2])
            self.tfiliacion.set(respuesta[0][8])

    def getrow_seleccion_alumnos(self,event):
        rowid=self.treeAlumno.identify_row(event.y)
        self.treeAlumno.selection_set(rowid)
        item=self.treeAlumno.item(self.treeAlumno.focus())
        self.cod_alumno=item["text"]
        
        ############ Busca la informacion en la base de datos

        query="SELECT a.cod_alumno,a.nombres,a.apellidos,b.nombre_programa FROM alumno a, programa b WHERE a.id_programa=b.id_programa AND cod_alumno='"+self.cod_alumno+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        
        if len(respuesta)>0:
            self.codigoAlumno.set(respuesta[0][0])
            self.nombresAlumno.set(respuesta[0][1])
            self.apellidosAlumno.set(respuesta[0][2])
            self.programaAlumno.set(respuesta[0][3])

    def getrow_Modificar_Representante(self,event):
        rowid=self.tree.identify_row(event.y)
        self.tree.selection_set(rowid)
        item=self.tree.item(self.tree.focus())
        self.ci_representante=item["text"]
        
        ############ Busca la informacion en la base de datos

        query="SELECT ci_representante,nombres,apellidos,telefono_celular,telefono_fijo,profesion,ocupacion,vive_con_alumno,filiacion_representado,direccion FROM representante WHERE ci_representante='"+self.ci_representante+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        
        if len(respuesta)>0:
            self.Tci_representante.set(respuesta[0][0])
            self.Tnombres.set(respuesta[0][1])
            self.Tapellidos.set(respuesta[0][2])
            self.Ttelcel.set(respuesta[0][3])
            self.Ttelfijo.set(respuesta[0][4])
            self.Tprofesion.set(respuesta[0][5])
            self.tocupacion.set(respuesta[0][6])
            self.tvive.set(respuesta[0][7])
            self.tfiliacion.set(respuesta[0][8])
            self.ttdireccion.set(respuesta[0][9])

    def updateListaRepresentante(self,respuesta):
        info=self.tree.get_children()

        for elemento in info:
            self.tree.delete(elemento)
        for row in respuesta:
            self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
    
    def clearRepresentante(self):
        query="SELECT ci_representante,nombres,apellidos,telefono_celular,telefono_fijo,profesion,ocupacion,vive_con_alumno,filiacion_representado,direccion FROM representante ORDER BY apellidos ASC"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.buscador1.set("")
        self.updateListaRepresentante(respuesta)

    def add_new_representante(self):
        ci_representante=self.Tci_representante.get()
        nombres=self.Tnombres.get()
        apellidos=self.Tapellidos.get()
        telcelular=self.Ttelcel.get()
        telfijo=self.Ttelfijo.get()
        profesion=self.Tprofesion.get()
        ocupacion=self.tocupacion.get()
        vive=self.tvive.get()
        filiacion=self.tfiliacion.get()
        direccion=self.ttdireccion.get()
        
        try:
            if self.validar_Cedula(ci_representante):
                query="INSERT INTO representante(ci_representante,nombres,apellidos,telefono_celular,telefono_fijo,profesion,ocupacion,vive_con_alumno,filiacion_representado,direccion) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(ci_representante,nombres,apellidos,telcelular,telfijo,profesion,ocupacion,vive,filiacion,direccion))
                
                cone.commit()
                cone.close()
                self.clearRepresentante()
                mb.showinfo("Información","Se han cargado con éxito los datos.")
                self.Tci_representante.set("")
                self.Tnombres.set("")
                self.Tapellidos.set("")
                self.Ttelcel.set("")
                self.Ttelfijo.set("")
                self.Tprofesion.set("")
                self.tocupacion.set("")
                self.tfiliacion.set("")
                self.ttdireccion.set("")
            else:
                mb.showwarning("Error","Debe completar los campos obligatorios (*)")
        except:
            mb.showinfo("Información","Este dato ya existe")

    def update_representante(self):

        ci_representante=self.Tci_representante.get()
        nombres=self.Tnombres.get()
        apellidos=self.Tapellidos.get()
        telcelular=self.Ttelcel.get()
        telfijo=self.Ttelfijo.get()
        profesion=self.Tprofesion.get()
        ocupacion=self.tocupacion.get()
        vive=self.tvive.get()
        filiacion=self.tfiliacion.get()
        direccion=self.ttdireccion.get()

        if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea actualizar estos datos? "):
            if self.validar_Cedula(ci_representante):
            
                query="UPDATE representante SET ci_representante=%s,nombres=%s,apellidos=%s,telefono_celular=%s,telefono_fijo=%s,profesion=%s,ocupacion=%s,vive_con_alumno=%s,filiacion_representado=%s,direccion=%s WHERE ci_representante='"+self.ci_representante+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(ci_representante,nombres,apellidos,telcelular,telfijo,profesion,ocupacion,vive,filiacion,direccion))
                

                cone.commit()
                cone.close()

                self.clearRepresentante()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han cargado con éxito los datos.")
                    self.Tci_representante.set("")
                    self.Tnombres.set("")
                    self.Tapellidos.set("")
                    self.Ttelcel.set("")
                    self.Ttelfijo.set("")
                    self.Tprofesion.set("")
                    self.tocupacion.set("")
                    self.tfiliacion.set("")
                    self.ttdireccion.set("")
                else:
                    mb.showinfo("Informacion", "No existe un alumno con dicha informacion")
                
            else:
                mb.showwarning("Error","Debe seleccionar los campos a modificar")
        else:
            return True

    def delete_representante(self):
        ci_representante=self.Tci_representante.get()
        try:
            if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea borrar estos datos? "):
                query="DELETE FROM representante WHERE ci_representante='"+ci_representante+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query)
            
                cone.commit()
                cone.close()
                self.clearRepresentante()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han borrado los datos con éxito.")
                    self.Tci_representante.set("")
                    self.Tnombres.set("")
                    self.Tapellidos.set("")
                    self.Ttelcel.set("")
                    self.Ttelfijo.set("")
                    self.Tprofesion.set("")
                    self.tocupacion.set("")
                    self.tfiliacion.set("")
                    self.ttdireccion.set("")
                else:
                    mb.showinfo("Informacion", "No existe un alumno con dicha informacion")
            else:
                return True
        except:
            mb.showwarning("Error","Introduzca la informacion que desee borrar o selecione en la tablaRepresentante.")

############################## Buscador representante alumno

    def searchAlumnoRepresentante(self):
        opcioncontrol=self.comobox1.get()
        buscarLista=self.buscador1.get()
        opcionPrograma=self.comobox2.get()
        if opcioncontrol=="Apellidos Alumno":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.ci_representante,b.nombres,b.apellidos,b.filiacion_representado FROM alumno a, representante b, representante_alumno c, programa d WHERE c.ci_representante=b.ci_representante AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno AND a.apellidos LIKE '%"+buscarLista+"%' AND d.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaRepresentanteAlumno(respuesta)

        if opcioncontrol=="Cédula Representante":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.ci_representante,b.nombres,b.apellidos,b.filiacion_representado FROM alumno a, representante b, representante_alumno c, programa d WHERE c.ci_representante=b.ci_representante AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno AND b.ci_representante LIKE '%"+buscarLista+"%' AND d.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaRepresentanteAlumno(respuesta)

        if opcioncontrol=="Nombres Alumno":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.ci_representante,b.nombres,b.apellidos,b.filiacion_representado FROM alumno a, representante b, representante_alumno c, programa d WHERE c.ci_representante=b.ci_representante AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno AND a.nombres LIKE '%"+buscarLista+"%' AND d.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaRepresentanteAlumno(respuesta)
############## Funciones representante_alumno

    def updateListaRepresentanteAlumno(self,respuesta):
        info=self.treeAlumnosRepresentantes.get_children()

        for elemento in info:
            self.treeAlumnosRepresentantes.delete(elemento)
        for row in respuesta:
            self.treeAlumnosRepresentantes.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))

    def clearRepresentanteAlumno(self):
        query="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.ci_representante,b.nombres,b.apellidos,b.filiacion_representado FROM alumno a, representante b, representante_alumno c, programa d WHERE c.ci_representante=b.ci_representante AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.buscador1.set("")
        self.updateListaRepresentanteAlumno(respuesta)

    def add_new_representante_alumno(self):
        ci_representante=self.Tci_representante.get()
        cod_alumno=self.codigoAlumno.get()
        try:
            if self.validar_Cedula(ci_representante):
                query="INSERT INTO representante_alumno(ci_representante,cod_alumno) VALUES(%s,%s)"

                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(ci_representante,cod_alumno))
                
                cone.commit()
                cone.close()
                self.clearRepresentanteAlumno()
                mb.showinfo("Información","Se han cargado con éxito los datos.")
                self.Tci_representante.set("")
                self.Tnombres.set("")
                self.Tapellidos.set("")
                self.tfiliacion.set("")
                self.codigoAlumno.set("")
                self.nombresAlumno.set("")
                self.apellidosAlumno.set("")
                self.programaAlumno.set("")
                
            else:
                mb.showwarning("Error","Debe completar los campos obligatorios (*)")
        except:
            mb.showinfo("Información","Este dato ya existe")

    def getrow_Representante_alumno(self,event):
        rowid=self.treeAlumnosRepresentantes.identify_row(event.y)
        self.treeAlumnosRepresentantes.selection_set(rowid)
        item=self.treeAlumnosRepresentantes.item(self.treeAlumnosRepresentantes.focus())
        self.cod_alumnoID=item["text"]
        
        ############ Busca la informacion en la base de datos

        query="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.ci_representante,b.nombres,b.apellidos,b.filiacion_representado FROM alumno a, representante b, representante_alumno c, programa d WHERE c.ci_representante=b.ci_representante AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno AND a.cod_alumno='"+self.cod_alumnoID+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        query2="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.ci_representante,b.nombres,b.apellidos,b.filiacion_representado FROM alumno a, representante b, representante_alumno c, programa d WHERE c.ci_representante=b.ci_representante AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno AND a.cod_alumno='"+self.cod_alumnoID+"'"

        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query2)
        respuestaCI=cursor.fetchall() 
        self.cirepresentanteMod=tk.StringVar()
        self.cirepresentanteMod.set(respuestaCI[0][4])
        cone.close()
        if len(respuesta)>0:
            self.codigoAlumno.set(respuesta[0][0])
            self.nombresAlumno.set(respuesta[0][1])
            self.apellidosAlumno.set(respuesta[0][2])
            self.programaAlumno.set(respuesta[0][3])
            self.Tci_representante.set(respuesta[0][4])
            self.Tnombres.set(respuesta[0][5])
            self.Tapellidos.set(respuesta[0][6])
            self.tfiliacion.set(respuesta[0][7])

    def update_AlumnoRepresentante(self):
        cod_alumno=self.codigoAlumno.get()
        if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea actualizar estos datos? "):
            if self.validar_contrasena(cod_alumno):
                ci_representante=self.Tci_representante.get()
                Ci_ClaveMod=self.cirepresentanteMod.get()

                query="UPDATE representante_alumno SET cod_alumno=%s, ci_representante=%s WHERE ci_representante = '"+Ci_ClaveMod+"' AND cod_alumno='"+self.cod_alumnoID+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(cod_alumno,ci_representante))
                

                cone.commit()
                cone.close()

                self.clearRepresentanteAlumno()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han cargado con éxito los datos.")
                    self.Tci_representante.set("")
                    self.Tnombres.set("")
                    self.Tapellidos.set("")
                    self.tfiliacion.set("")
                    self.codigoAlumno.set("")
                    self.nombresAlumno.set("")
                    self.apellidosAlumno.set("")
                    self.programaAlumno.set("")
                else:
                    mb.showinfo("Informacion", "No existe un alumno con dicha informacion")
                
            else:
                mb.showwarning("Error","Debe seleccionar los campos a modificar")
        else:
            return True

    def delete_representante_alumno(self):

        cod_alumno=self.codigoAlumno.get()
        ci_representante=self.Tci_representante.get()
        try:
            if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea borrar estos datos? "):
                query="DELETE FROM representante_alumno WHERE ci_representante='"+ci_representante+"' AND cod_alumno='"+cod_alumno+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query)
                
                cone.commit()
                cone.close()
                self.clearRepresentanteAlumno()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han borrado los datos con éxito.")
                    self.Tci_representante.set("")
                    self.Tnombres.set("")
                    self.Tapellidos.set("")
                    self.tfiliacion.set("")
                    self.codigoAlumno.set("")
                    self.nombresAlumno.set("")
                    self.apellidosAlumno.set("")
                    self.programaAlumno.set("")
                else:
                    mb.showinfo("Informacion", "No existe un alumno con dicha informacion")
            else:
                return True
        except:
                mb.showwarning("Error","Introduzca la informacion que desee borrar o selecione en la tablaRepresentante.")
########################## asignar instrumento

    def asignarInstrumento(self):
        self.ventana1.destroy()
        self.ventana2=tk.Tk()
        self.ventana2.title("Asignar instrumentos")
        self.ventana2.config(bg='Light cyan')
        self.ventana2.geometry("1150x650")
        self.ventana2.resizable(0,0)
        self.ventana2.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")

        self.decoraframe=tk.Frame(self.ventana2,bg="dark blue",height=20)
        self.decoraframe.pack(fill="both",expand="no",side="top")

        frameoscuro=tk.Frame(self.ventana2,bg="dark blue",height=330)
        frameoscuro.pack(fill="both",expand="no",side="bottom")

        self.lista=tk.LabelFrame(self.ventana2,text="Opciones",font=("Times New Roman",10))
        self.lista.config(bg="light cyan")
        self.lista.place(x=15,y=20)

        self.tablaRepresentante=tk.LabelFrame(self.ventana2,text="Lista Instrumentos",font=("Times New Roman",10))
        self.tablaRepresentante.config(bg="light cyan")
        self.tablaRepresentante.place(x=230,y=20)

        self.tablaAlumnos=tk.LabelFrame(self.ventana2,text="Lista Alumnos",font=("Times New Roman",10))
        self.tablaAlumnos.config(bg="light cyan")
        self.tablaAlumnos.place(x=355,y=176)

        self.labelframeRepresentantesSeleccion=tk.LabelFrame(self.ventana2,text="Selección Instrumento",font=("Times New Roman",15),fg="white")
        self.labelframeRepresentantesSeleccion.config(bg="dark blue")
        self.labelframeRepresentantesSeleccion.place(x=1,y=325)

        self.labelframeAlumnosSeleccion=tk.LabelFrame(self.ventana2,text="Selección Alumno",font=("Times New Roman",15),fg="white",height=100)
        self.labelframeAlumnosSeleccion.config(bg="dark blue")
        self.labelframeAlumnosSeleccion.place(x=245,y=325)

        self.labelframeTablaAlumnosRepresentantes=tk.LabelFrame(self.ventana2,text="Alumnos con su Instrumento asignado",font=("Times New Roman",15),fg="white")
        self.labelframeTablaAlumnosRepresentantes.config(bg="dark blue")
        self.labelframeTablaAlumnosRepresentantes.place(x=490,y=325)

        self.frameEspacio=tk.Frame(self.labelframeAlumnosSeleccion,bg="dark blue",width=40,height=40)
        self.frameEspacio.grid(row=5,column=1)

        self.labelframeopcionesAR=tk.LabelFrame(self.ventana2,text="Asignar instrumento",font=("Times New Roman",15),fg="white")
        self.labelframeopcionesAR.config(bg="dark blue")
        self.labelframeopcionesAR.place(x=2,y=560)

        self.buscador=tk.LabelFrame(self.ventana2,text='Buscador',font=("Times New Roman",10))
        self.buscador.config(bg="light cyan")
        self.buscador.place(x= 520, y= 530)

        ###################### Ventana opciones

        btnVolver=tk.Button(self.lista,text="Volver",command=self.volver_Alumno)
        btnVolver.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12),width=19)
        btnVolver.grid(row=0,column=1,padx=2,pady=2)

        self.hideInstrumentoAlumno=1
        btnBuscador=tk.Button(self.lista,text="Buscar Instrumento",command=self.ocultarMostrarDetallesBuscadorInstrumento)
        btnBuscador.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12),width=19)
        btnBuscador.grid(row=1,column=1,padx=2,pady=2)

        btnBuscador=tk.Button(self.lista,text="Buscar Alumno",command=self.ocultarMostrarDetallesBuscadorAlumno)
        btnBuscador.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12),width=19)
        btnBuscador.grid(row=2,column=1,padx=2,pady=2)

        ########################## TREEVIEW INSTRUMENTOS

        self.tree = ttk.Treeview(self.tablaRepresentante,columns=("#1","#2","#3","#4","#5","#6","#7"),height="5")
        self.tree.heading("#0",text="Serial")
        self.tree.heading("#1",text="Descripción")
        self.tree.heading("#2",text="Marca")
        self.tree.heading("#3",text="Medida")
        self.tree.heading("#4",text="Condición")
        self.tree.heading("#5",text="Ubicación")
        self.tree.heading("#6",text="Comodato vigente")
        self.tree.heading("#7",text="Cod Inventario")

        self.tree.column("#0",width=100)
        self.tree.column("#1",width=100)
        self.tree.column("#2",width=100)
        self.tree.column("#3",width=100)
        self.tree.column("#4",width=100)
        self.tree.column("#5",width=120)
        self.tree.column("#6",width=120)
        self.tree.column("#7",width=130)

        self.tree.bind("<1>",self.getrow_seleccion_instrumento)
        self.tree.pack(side="left",fill="both",padx=5,pady=5)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.tablaRepresentante, orient="vertical", command = self.tree.yview)
        scrolvert.pack(side="left",fill="y")
        self.tree.config(yscrollcommand=scrolvert.set)
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.tree.get_children()

        for elemento in profesor:
            self.tree.delete(elemento)
        try:
            cur.execute("SELECT num_serial,descripcion,marca,medida,condicion,ubicacion,comodato_vigente,cod_inventario FROM instrumento")
            rows=cur.fetchall()
            for row in rows:
                self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
        except:
            pass

        con.close()
        #################### Treeview Alumnos

        self.treeAlumno = ttk.Treeview(self.tablaAlumnos,columns=("#1","#2","#3","#4","#5"),height="4")
        self.treeAlumno.heading("#0",text="Código")
        self.treeAlumno.heading("#1",text="Cédula")
        self.treeAlumno.heading("#2",text="Nombres")
        self.treeAlumno.heading("#3",text="Apellidos")
        self.treeAlumno.heading("#4",text="Programa")
        self.treeAlumno.heading("#5",text="Instrumento principal")

        self.treeAlumno.column("#0",width=100)
        self.treeAlumno.column("#1",width=70)
        self.treeAlumno.column("#2",width=130)
        self.treeAlumno.column("#3",width=130)
        self.treeAlumno.column("#4",width=160)
        self.treeAlumno.column("#5",width=160)
        
        self.treeAlumno.bind("<1>",self.getrow_seleccion_alumnos)
        self.treeAlumno.pack(side="right",fill="both",padx=5,pady=5)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.tablaAlumnos, orient="vertical", command = self.tree.yview)
        scrolvert.pack(side="left",fill="y")
        self.treeAlumno.config(yscrollcommand=scrolvert.set)
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.treeAlumno.get_children()

        for elemento in profesor:
            self.treeAlumno.delete(elemento)
        try:
            cur.execute("SELECT  a.cod_alumno,a.ci_alumno,a.nombres,a.apellidos,b.nombre_programa,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa")
            rows=cur.fetchall()
            for row in rows:
                self.treeAlumno.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))
        except:
            pass

        con.close()

        #################### Labelframe seleccion Instrumentos Label

        labelCiRepresentanteSel=tk.Label(self.labelframeRepresentantesSeleccion,bg="dark blue",text="(*)Número serial:",font=("Times New Roman",10),fg="white")
        labelCiRepresentanteSel.grid(row=0,column=1,padx=1,pady=10)

        labelnombres=tk.Label(self.labelframeRepresentantesSeleccion,bg="dark blue",text="Descripción:",font=("Times New Roman",10),fg="white")
        labelnombres.grid(row=1,column=1,padx=1,pady=10)

        labelapellidos=tk.Label(self.labelframeRepresentantesSeleccion,bg="dark blue",text="Medida:",font=("Times New Roman",10),fg="white")
        labelapellidos.grid(row=2,column=1,padx=1,pady=10)

        labelfiliacion=tk.Label(self.labelframeRepresentantesSeleccion,bg="dark blue",text="En posesión:",font=("Times New Roman",10),fg="white")
        labelfiliacion.grid(row=3,column=1,padx=1,pady=10)

        labelComodato=tk.Label(self.labelframeRepresentantesSeleccion,bg="dark blue",text="Comodato vigente:",font=("Times New Roman",10),fg="white")
        labelComodato.grid(row=4,column=1,padx=1,pady=10)


        ####################### Entrys
        self.TSerialInstrumento=tk.StringVar()
        self.TDescripcion=tk.StringVar()
        self.Tmedida=tk.StringVar()
        self.Tcondicion=tk.StringVar()
        self.Tcomodatito=tk.StringVar()

        self.entryCedulaRepresentante=ttk.Entry(self.labelframeRepresentantesSeleccion,textvariable=self.TSerialInstrumento,font=("Times New Roman",10),state="readonly")
        self.entryCedulaRepresentante.grid(row=0,column=2,padx=1,pady=10)

        self.entrynombres=ttk.Entry(self.labelframeRepresentantesSeleccion,textvariable=self.TDescripcion,font=("Times New Roman",10),state="readonly")
        self.entrynombres.grid(row=1,column=2,padx=1,pady=10)

        self.entryApellidos=ttk.Entry(self.labelframeRepresentantesSeleccion,textvariable=self.Tmedida,font=("Times New Roman",10),state="readonly")
        self.entryApellidos.grid(row=2,column=2,padx=1,pady=10)

        self.opcionCondicion=tk.StringVar()
        opcionesCondicion=("SI","NO")
        self.comoboxCondicion=ttk.Combobox(self.labelframeRepresentantesSeleccion,
                                        width=16,
                                        textvariable=self.opcionCondicion,
                                        values=opcionesCondicion,
                                        state='readonly',
                                        font=("Times New Roman",10))
        self.comoboxCondicion.current(0)
        self.comoboxCondicion.grid(row=3,column=2,padx=1,pady=10)

        self.comoboxComodatito=ttk.Combobox(self.labelframeRepresentantesSeleccion,
                                        width=16,
                                        textvariable=self.Tcomodatito,
                                        values=opcionesCondicion,
                                        state='readonly',
                                        font=("Times New Roman",10))
        self.comoboxComodatito.current(0)
        self.comoboxComodatito.grid(row=4,column=2,padx=1,pady=10)

        #################### Labelframe seleccion representantes Label

        self.codigoAlumno=tk.StringVar()
        self.nombresAlumno=tk.StringVar()
        self.apellidosAlumno=tk.StringVar()
        self.programaAlumno=tk.StringVar()

        labelcod_alumno=tk.Label(self.labelframeAlumnosSeleccion,bg="dark blue",text="(*)Código alumno:",font=("Times New Roman",10),fg="white")
        labelcod_alumno.grid(row=0,column=1,padx=1,pady=10)

        labelnombres=tk.Label(self.labelframeAlumnosSeleccion,bg="dark blue",text="Nombres:",font=("Times New Roman",10),fg="white")
        labelnombres.grid(row=1,column=1,padx=1,pady=10)

        labelapellidos=tk.Label(self.labelframeAlumnosSeleccion,bg="dark blue",text="Apellidos:",font=("Times New Roman",10),fg="white")
        labelapellidos.grid(row=2,column=1,padx=1,pady=10)

        labelprograma=tk.Label(self.labelframeAlumnosSeleccion,bg="dark blue",text="Programa:",font=("Times New Roman",10),fg="white")
        labelprograma.grid(row=3,column=1,padx=1,pady=10)

        ####################### Entrys

        self.entryCod_alumno=ttk.Entry(self.labelframeAlumnosSeleccion,textvariable=self.codigoAlumno,font=("Times New Roman",10),state="readonly")
        self.entryCod_alumno.grid(row=0,column=2,padx=1,pady=10)

        self.entrynombres=ttk.Entry(self.labelframeAlumnosSeleccion,textvariable=self.nombresAlumno,font=("Times New Roman",10),state="readonly")
        self.entrynombres.grid(row=1,column=2,padx=1,pady=10)

        self.entryApellidos=ttk.Entry(self.labelframeAlumnosSeleccion,textvariable=self.apellidosAlumno,font=("Times New Roman",10),state="readonly")
        self.entryApellidos.grid(row=2,column=2,padx=1,pady=10)

        self.entryprogramaSeleccion=ttk.Entry(self.labelframeAlumnosSeleccion,textvariable=self.programaAlumno,font=("Times New Roman",10),state="readonly")
        self.entryprogramaSeleccion.grid(row=3,column=2,padx=1,pady=10)

        ########################## TREEVIEW ALUMNOS Y REPRESENTANTES

        self.treeAlumnosInstrumentos = ttk.Treeview(self.labelframeTablaAlumnosRepresentantes,columns=("#1","#2","#3","#4","#5","#6","#7"),height="6")
        self.treeAlumnosInstrumentos.heading("#0",text="Código alumno")
        self.treeAlumnosInstrumentos.heading("#1",text="Nombres alumno")
        self.treeAlumnosInstrumentos.heading("#2",text="Apellidos alumno")
        self.treeAlumnosInstrumentos.heading("#3",text="Programa")
        self.treeAlumnosInstrumentos.heading("#4",text="Serial")
        self.treeAlumnosInstrumentos.heading("#5",text="Descripción")
        self.treeAlumnosInstrumentos.heading("#6",text="Medida")
        self.treeAlumnosInstrumentos.heading("#7",text="En posesión")

        self.treeAlumnosInstrumentos.column("#0",width=70)
        self.treeAlumnosInstrumentos.column("#1",width=80)
        self.treeAlumnosInstrumentos.column("#2",width=85)
        self.treeAlumnosInstrumentos.column("#3",width=95)
        self.treeAlumnosInstrumentos.column("#4",width=70)
        self.treeAlumnosInstrumentos.column("#5",width=80)
        self.treeAlumnosInstrumentos.column("#6",width=80)
        self.treeAlumnosInstrumentos.column("#7",width=50)

        
        self.treeAlumnosInstrumentos.bind("<1>",self.getrow_Instrumento_alumno)
        self.treeAlumnosInstrumentos.pack(side="left",fill="both",padx=5,pady=5)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.labelframeTablaAlumnosRepresentantes, orient="vertical", command = self.tree.yview)
        scrolvert.pack(side="left",fill="y")
        self.treeAlumnosInstrumentos.config(yscrollcommand=scrolvert.set)
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.treeAlumnosInstrumentos.get_children()

        for elemento in profesor:
            self.treeAlumnosInstrumentos.delete(elemento)
        try:
            cur.execute("SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.num_serial,b.descripcion,b.medida,c.en_posesion FROM alumno a, instrumento b, instrumento_alumno c, programa d WHERE c.num_serial=b.num_serial AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno")
            rows=cur.fetchall()
            for row in rows:
                self.treeAlumnosInstrumentos.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
        except:
            pass

        con.close()

        ###################### Agregar, modificar y eliminar 

        btnAgregar=tk.Button(self.labelframeopcionesAR,text="Agregar",command=self.add_new_instrumento_alumno,width=15)
        btnAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12))
        btnAgregar.grid(row=0,column=1,padx=2,pady=10)

        btnmodificar=tk.Button(self.labelframeopcionesAR,text="Modificar",command=self.update_AlumnoInstrumento,width=15)
        btnmodificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12))
        btnmodificar.grid(row=0,column=2,padx=2,pady=10)

        btneliminar=tk.Button(self.labelframeopcionesAR,text="Eliminar",command=self.delete_instrumento_alumno,width=15)
        btneliminar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12))
        btneliminar.grid(row=0,column=3,padx=2,pady=10)

        #################### BUSCADOR 

        label1=tk.Label(self.buscador,text="Consulta por:",bg="Light cyan",font=("Times New Roman",10))
        label1.grid(row=0,column=0,padx=5,pady=5)

        self.buscador1=tk.StringVar()
        self.entry1=tk.Entry(self.buscador,width=30,textvariable=self.buscador1,font=("Times New Roman",10))
        self.entry1.grid(row=0,column=3,padx=5,pady=5)

        self.labelprograma=tk.Label(self.buscador,text="Programa:",bg="Light cyan",font=("Times New Roman",10))
        self.labelprograma.grid(row=1,column=0,padx=5,pady=5)

        ############### Combobox interactivo

        self.opcionPrograma=tk.StringVar()
        self.comobox2=ttk.Combobox(self.buscador,
                                width=20,
                                textvariable=self.opcionPrograma,
                                state='readonly',
                                font=("Times New Roman",10))

        self.comobox2['value']=self.cargarComboProgramas()
        self.comobox2.current(0)
        self.comobox2.grid(row=1,column=1,padx=5,pady=1)

        #################################################################

        lableBucar=tk.Label(self.buscador,text="Buscar:",bg="Light cyan",font=("Times New Roman",10))
        lableBucar.grid(row=0,column=2,padx=5,pady=5)

        self.opcion=tk.StringVar()
        opcionesBusqueda=("Nombres Alumno","Apellidos Alumno","Número serial","Descripción")
         
        self.comobox1=ttk.Combobox(self.buscador,
                                width=20,
                                textvariable=self.opcion,
                                values=opcionesBusqueda,
                                state='readonly',
                                font=("Times New Roman",10))
        self.comobox1.current(1)

        self.comobox1.grid(row=0,column=1)

        btnBuscar=tk.Button(self.buscador,text="Buscar",command=self.searchAlumnoInstrumento,font=("Times New Roman",10),width=9)
        btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnBuscar.grid(row=1,column=2,padx=5,pady=5)

        btnLimpiar=tk.Button(self.buscador,text="Limpiar",command=self.clearInstrumentoAlumno,font=("Times New Roman",10),width=9)
        btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnLimpiar.grid(row=1,column=3,padx=5,pady=5)

########################## Buscador de instrumentos y alumnos

    def ocultarMostrarDetallesBuscadorInstrumento(self):
         

        if self.hideInstrumentoAlumno==0:
            self.frameDetalles.place_forget()
            self.hideInstrumentoAlumno=1
        else:
             #################Información que aparece y desaparece
            
            self.frameDetalles=tk.LabelFrame(self.ventana2,bg="light cyan",text="Instrumentos")
            self.frameDetalles.place(x=0,y=175,height=144,width=350)

            #################### BUSCADOR 

        

            label1=tk.Label(self.frameDetalles,text="Consulta por:",bg="Light cyan",font=("Times New Roman",10))
            label1.grid(row=0,column=0,padx=5,pady=5)

            self.buscadorInstrumento=tk.StringVar()
            self.entry1=tk.Entry(self.frameDetalles,width=30,textvariable=self.buscadorInstrumento,font=("Times New Roman",10))
            self.entry1.grid(row=2,column=1,padx=5,pady=5)

            self.labelprograma=tk.Label(self.frameDetalles,text="Comodato Vigente:",bg="Light cyan",font=("Times New Roman",10))
            self.labelprograma.grid(row=1,column=0,padx=5,pady=5)

            ############### Combobox interactivo

            self.opcionYN=tk.StringVar()
            opcionesBusquedaYN=("SI","NO")
            
            self.comoboxInstrumento=ttk.Combobox(self.frameDetalles,
                                    width=20,
                                    textvariable=self.opcionYN,
                                    values=opcionesBusquedaYN,
                                    state='readonly',
                                    font=("Times New Roman",10))
            self.comoboxInstrumento.current(0)           
            self.comoboxInstrumento.grid(row=1,column=1,padx=5,pady=1)

            #################################################################

            lableBucar=tk.Label(self.frameDetalles,text="Buscar:",bg="Light cyan",font=("Times New Roman",10))
            lableBucar.grid(row=2,column=0,padx=5,pady=5)

            self.opcionInstrumento=tk.StringVar()
            opcionesBusquedaInstrumento=("Descripción","Serial","Ubicacion","Condición")
            
            self.comoboxInstrumentoConsulta=ttk.Combobox(self.frameDetalles,
                                    width=20,
                                    textvariable=self.opcionInstrumento,
                                    values=opcionesBusquedaInstrumento,
                                    state='readonly',
                                    font=("Times New Roman",10))
            self.comoboxInstrumentoConsulta.current(1)

        
            self.comoboxInstrumentoConsulta.grid(row=0,column=1)

            btnBuscar=tk.Button(self.frameDetalles,text="Buscar",command=self.searchtablaInstrumento,font=("Times New Roman",10),width=9)
            btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnBuscar.grid(row=3,column=0,padx=5,pady=5)

            btnLimpiar=tk.Button(self.frameDetalles,text="Limpiar",command=self.clearTreeInstrumento,font=("Times New Roman",10),width=9)
            btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnLimpiar.grid(row=3,column=1,padx=5,pady=5)

            self.hideInstrumentoAlumno=0
    ########################## Funciones buscadores Instrumento

    def searchtablaInstrumento(self):
        opcioncontrol=self.comoboxInstrumentoConsulta.get()
        buscarLista=self.buscadorInstrumento.get()
        opcionPrograma=self.comoboxInstrumento.get()
        if opcioncontrol=="Ubicación":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT num_serial,descripcion,marca,medida,condicion,ubicacion,comodato_vigente,cod_inventario FROM instrumento WHERE ubicacion LIKE '%"+buscarLista+"%' AND comodato_vigente='"+opcionPrograma+"'"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaInstrumentoSup(respuesta)

        if opcioncontrol=="Serial":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT num_serial,descripcion,marca,medida,condicion,ubicacion,comodato_vigente,cod_inventario FROM instrumento WHERE num_serial LIKE '%"+buscarLista+"%' AND comodato_vigente='"+opcionPrograma+"'"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaInstrumentoSup(respuesta)

        if opcioncontrol=="Descripción":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT num_serial,descripcion,marca,medida,condicion,ubicacion,comodato_vigente,cod_inventario FROM instrumento WHERE descripcion LIKE '%"+buscarLista+"%' AND comodato_vigente='"+opcionPrograma+"'"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaInstrumentoSup(respuesta)
        
        if opcioncontrol=="Condición":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT num_serial,descripcion,marca,medida,condicion,ubicacion,comodato_vigente,cod_inventario FROM instrumento WHERE condicion LIKE '%"+buscarLista+"%' AND comodato_vigente='"+opcionPrograma+"'"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaInstrumentoSup(respuesta)

    ###### updateListaAlumno y clear alumno

    def updateListaInstrumentoSup(self,respuesta):
        info=self.tree.get_children()

        for elemento in info:
            self.tree.delete(elemento)
        for row in respuesta:
            self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))

    def clearTreeInstrumento(self):
        query="SELECT num_serial,descripcion,marca,medida,condicion,ubicacion,comodato_vigente,cod_inventario FROM instrumento"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.updateListaInstrumentoSup(respuesta)

    ############################################
    def ocultarMostrarDetallesBuscadorAlumno(self):
         

        if self.hideInstrumentoAlumno==0:
            self.frameDetalles.place_forget()#place(x=-70,y=0,width=350,height=800)
            self.hideInstrumentoAlumno=1
        else:
                #################Información que aparece y desaparece
                
            self.frameDetalles=tk.LabelFrame(self.ventana2,bg="light cyan",text="Alumnos")
            self.frameDetalles.place(x=0,y=175,height=144,width=350)

                #################### BUSCADOR 

            

            label1=tk.Label(self.frameDetalles,text="Consulta por:",bg="Light cyan",font=("Times New Roman",10))
            label1.grid(row=0,column=0,padx=5,pady=5)

            self.buscadorAlumno=tk.StringVar()
            self.entry1=tk.Entry(self.frameDetalles,width=30,textvariable=self.buscadorAlumno,font=("Times New Roman",10))
            self.entry1.grid(row=2,column=1,padx=5,pady=5)

            self.labelprograma=tk.Label(self.frameDetalles,text="Programa:",bg="Light cyan",font=("Times New Roman",10))
            self.labelprograma.grid(row=1,column=0,padx=5,pady=5)

                ############### Combobox interactivo

            self.opcionProgramaAlumno=tk.StringVar()
            self.comoboxAlumnos=ttk.Combobox(self.frameDetalles,
                                        width=20,
                                        textvariable=self.opcionProgramaAlumno,
                                        state='readonly',
                                        font=("Times New Roman",10))

            self.comoboxAlumnos['value']=self.cargarComboProgramas()
            self.comoboxAlumnos.current(0)
            self.comoboxAlumnos.grid(row=1,column=1,padx=5,pady=1)

                #################################################################

            lableBucar=tk.Label(self.frameDetalles,text="Buscar:",bg="Light cyan",font=("Times New Roman",10))
            lableBucar.grid(row=2,column=0,padx=5,pady=5)

            self.opcionAlumno=tk.StringVar()
            opcionesBusquedaAlumno=("Nombres Alumno","Apellidos Alumno","Cédula","Instrumento Principal")
                
            self.comoboxAlumnosConsulta=ttk.Combobox(self.frameDetalles,
                                        width=20,
                                        textvariable=self.opcionAlumno,
                                        values=opcionesBusquedaAlumno,
                                        state='readonly',
                                        font=("Times New Roman",10))
            self.comoboxAlumnosConsulta.current(1)

            
            self.comoboxAlumnosConsulta.grid(row=0,column=1)

            btnBuscar=tk.Button(self.frameDetalles,text="Buscar",command=self.searchtablaAlumno,font=("Times New Roman",10),width=9)
            btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnBuscar.grid(row=3,column=0,padx=5,pady=5)

            btnLimpiar=tk.Button(self.frameDetalles,text="Limpiar",command=self.clearTreeAlumno,font=("Times New Roman",10),width=9)
            btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnLimpiar.grid(row=3,column=1,padx=5,pady=5)

            self.hideInstrumentoAlumno=0

    ########################## Funciones buscadores Instrumento y alumno

    def searchtablaAlumno(self):
        opcioncontrol=self.comoboxAlumnosConsulta.get()
        buscarLista=self.buscadorAlumno.get()
        opcionPrograma=self.comoboxAlumnos.get()
        if opcioncontrol=="Apellidos Alumno":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT  a.cod_alumno,a.ci_alumno,a.nombres,a.apellidos,b.nombre_programa,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa AND a.apellidos LIKE '%"+buscarLista+"%' AND b.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAlumnoSup(respuesta)

        if opcioncontrol=="Cédula":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT  a.cod_alumno,a.ci_alumno,a.nombres,a.apellidos,b.nombre_programa,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa AND a.ci_alumno LIKE '%"+buscarLista+"%' AND b.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAlumnoSup(respuesta)

        if opcioncontrol=="Nombres Alumno":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT  a.cod_alumno,a.ci_alumno,a.nombres,a.apellidos,b.nombre_programa,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa AND a.nombres LIKE '%"+buscarLista+"%' AND b.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAlumnoSup(respuesta)
        
        if opcioncontrol=="Instrumento Principal":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT  a.cod_alumno,a.ci_alumno,a.nombres,a.apellidos,b.nombre_programa,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa AND a.instrumento_principal LIKE '%"+buscarLista+"%' AND b.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAlumnoSup(respuesta)

    ###### updateListaAlumno y clear alumno

    def updateListaAlumnoSup(self,respuesta):
        info=self.treeAlumno.get_children()

        for elemento in info:
            self.treeAlumno.delete(elemento)
        for row in respuesta:
            self.treeAlumno.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))

    def clearTreeAlumno(self):
        query="SELECT  a.cod_alumno,a.ci_alumno,a.nombres,a.apellidos,b.nombre_programa,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa "
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.buscadorAlumno.set("")
        self.updateListaAlumnoSup(respuesta)
     
####################################### Funciones

    def add_new_instrumento_alumno(self):
        num_serial=self.TSerialInstrumento.get()
        cod_alumno=self.codigoAlumno.get()
        en_posesion=self.comoboxCondicion.get()
        comodato_vigente=self.Tcomodatito.get()
        try:
            if self.validar_contrasena(num_serial):

                queryVerificar="SELECT num_serial FROM instrumento_alumno WHERE num_serial='"+num_serial+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(queryVerificar)
                info=cursor.fetchall()
                cone.close()

                if len(info)==1:
                    mb.showinfo("Información","No puede existir mas de dos alumnos con un instrumento")
                if len(info) == 0:
                
                    query="INSERT INTO instrumento_alumno(num_serial,en_posesion,cod_alumno) VALUES(%s,%s,%s)"

                    cone=self.abrir()
                    cursor=cone.cursor()
                    cursor.execute(query,(num_serial,en_posesion,cod_alumno))
                
                    cone.commit()
                    cone.close()
                    self.clearInstrumentoAlumno()

                    query2="UPDATE instrumento SET comodato_vigente='"+comodato_vigente+"' WHERE num_serial='"+num_serial+"'"
                    cone=self.abrir()
                    cursor=cone.cursor()
                    cursor.execute(query2)
                    cone.commit()
                    cone.close()
                    self.clearTreeInstrumento()
                
                    mb.showinfo("Información","Se han cargado con éxito los datos.")
                    self.TSerialInstrumento.set("")
                    self.TDescripcion.set("")
                    self.Tmedida.set("")
                    self.codigoAlumno.set("")
                    self.nombresAlumno.set("")
                    self.apellidosAlumno.set("")
                    self.programaAlumno.set("") 
            else:
                mb.showwarning("Error","Debe completar los campos obligatorios (*)")
        except:
            mb.showinfo("Información","Este dato ya existe")

    def updateListaInstrumentoAlumno(self,respuesta):
        info=self.treeAlumnosInstrumentos.get_children()

        for elemento in info:
            self.treeAlumnosInstrumentos.delete(elemento)
        for row in respuesta:
            self.treeAlumnosInstrumentos.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7]))

    def clearInstrumentoAlumno(self):
        query="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.num_serial,b.descripcion,b.medida,c.en_posesion FROM alumno a, instrumento b, instrumento_alumno c, programa d WHERE c.num_serial=b.num_serial AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.buscador1.set("")
        self.updateListaInstrumentoAlumno(respuesta)

    def getrow_seleccion_instrumento(self,event):
        rowid=self.tree.identify_row(event.y)
        self.tree.selection_set(rowid)
        item=self.tree.item(self.tree.focus())
        self.Serial=item["text"]
        
        ############ Busca la informacion en la base de datos

        query="SELECT num_serial,descripcion,medida,comodato_vigente FROM instrumento WHERE  num_serial='"+self.Serial+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        
        if len(respuesta)>0:
            self.TSerialInstrumento.set(respuesta[0][0])
            self.TDescripcion.set(respuesta[0][1])
            self.Tmedida.set(respuesta[0][2])
            self.Tcomodatito.set(respuesta[0][3])

    def searchAlumnoInstrumento(self):
        opcioncontrol=self.comobox1.get()
        buscarLista=self.buscador1.get()
        opcionPrograma=self.comobox2.get()
        if opcioncontrol=="Apellidos Alumno":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.num_serial,b.descripcion,b.medida,c.en_posesion FROM alumno a, instrumento b, instrumento_alumno c, programa d WHERE c.num_serial=b.num_serial AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno AND a.apellidos LIKE '%"+buscarLista+"%' AND d.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaInstrumentoAlumno(respuesta)

        if opcioncontrol=="Número serial":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.num_serial,b.descripcion,b.medida,c.en_posesion FROM alumno a, instrumento b, instrumento_alumno c, programa d WHERE c.num_serial=b.num_serial AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno AND b.num_serial LIKE '%"+buscarLista+"%' AND d.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaInstrumentoAlumno(respuesta)

        if opcioncontrol=="Nombres Alumno":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.num_serial,b.descripcion,b.medida,c.en_posesion FROM alumno a, instrumento b, instrumento_alumno c, programa d WHERE c.num_serial=b.num_serial AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno AND a.nombres LIKE '%"+buscarLista+"%' AND d.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaInstrumentoAlumno(respuesta)

        if opcioncontrol=="Descripción":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.num_serial,b.descripcion,b.medida,c.en_posesion FROM alumno a, instrumento b, instrumento_alumno c, programa d WHERE c.num_serial=b.num_serial AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno AND b.descripcion LIKE '%"+buscarLista+"%' AND d.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaInstrumentoAlumno(respuesta)

    def getrow_Instrumento_alumno(self,event):
        rowid=self.treeAlumnosInstrumentos.identify_row(event.y)
        self.treeAlumnosInstrumentos.selection_set(rowid)
        item=self.treeAlumnosInstrumentos.item(self.treeAlumnosInstrumentos.focus())
        self.cod_alumnoID=item["text"]
        
        ############ Busca la informacion en la base de datos

        query="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.num_serial,b.descripcion,b.medida,c.en_posesion,b.comodato_vigente FROM alumno a, instrumento b, instrumento_alumno c, programa d WHERE c.num_serial=b.num_serial AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno AND a.cod_alumno='"+self.cod_alumnoID+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()

        query2="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.num_serial,b.descripcion,b.medida,c.en_posesion FROM alumno a, instrumento b, instrumento_alumno c, programa d WHERE c.num_serial=b.num_serial AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno AND a.cod_alumno='"+self.cod_alumnoID+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query2)
        respuestaSerial=cursor.fetchall() 
        self.SerialModificar=tk.StringVar()
        self.SerialModificar.set(respuestaSerial[0][4])
        cone.close()
        if len(respuesta)>0:
            self.codigoAlumno.set(respuesta[0][0])
            self.nombresAlumno.set(respuesta[0][1])
            self.apellidosAlumno.set(respuesta[0][2])
            self.programaAlumno.set(respuesta[0][3])
            self.TSerialInstrumento.set(respuesta[0][4])
            self.TDescripcion.set(respuesta[0][5])
            self.Tmedida.set(respuesta[0][6])
            self.comoboxCondicion.set(respuesta[0][7])
            self.Tcomodatito.set(respuesta[0][8])

    def delete_instrumento_alumno(self):

        cod_alumno=self.codigoAlumno.get()
        Serial=self.TSerialInstrumento.get()
        try:
            if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea borrar estos datos? "):
                query="DELETE FROM instrumento_alumno WHERE num_serial='"+Serial+"' AND cod_alumno='"+cod_alumno+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query)
                
                cone.commit()
                cone.close()
                self.clearInstrumentoAlumno()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han borrado los datos con éxito.")
                    self.TSerialInstrumento.set("")
                    self.TDescripcion.set("")
                    self.Tmedida.set("")
                    self.codigoAlumno.set("")
                    self.nombresAlumno.set("")
                    self.apellidosAlumno.set("")
                    self.programaAlumno.set("")
                else:
                    mb.showinfo("Informacion", "No existe un alumno con dicha informacion")
            else:
                return True
        except:
                mb.showwarning("Error","Introduzca la informacion que desee borrar o selecione en la tabla instrumentos asignados.")

    def update_AlumnoInstrumento(self):
        cod_alumno=self.codigoAlumno.get()
        serial=self.TSerialInstrumento.get()
        en_posesion=self.comoboxCondicion.get()
        
        

        comodato_vigente=self.Tcomodatito.get()
        

        if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea actualizar estos datos? "):
            try:
                if self.validar_contrasena(cod_alumno):
                    Ci_ClaveMod=self.SerialModificar.get()

                    query="UPDATE instrumento_alumno SET cod_alumno=%s,en_posesion=%s, num_serial=%s WHERE num_serial = '"+Ci_ClaveMod+"' AND cod_alumno='"+self.cod_alumnoID+"'"
                    cone=self.abrir()
                    cursor=cone.cursor()
                    cursor.execute(query,(cod_alumno,en_posesion,serial))
                    contador=cursor.rowcount
                    cone.commit()
                    cone.close()

                    self.clearInstrumentoAlumno()

                    query2="UPDATE instrumento SET comodato_vigente='"+comodato_vigente+"' WHERE num_serial='"+serial+"'"
                    cone=self.abrir()
                    cursor=cone.cursor()
                    cursor.execute(query2)
                    cone.commit()
                    contadorComodato=cursor.rowcount
                    
                    cone.close()

                    self.clearTreeInstrumento()

                    if contador==1 or contadorComodato==1:
                        
                        mb.showinfo("Información","Se han cargado con éxito los datos.")
                        self.TSerialInstrumento.set("")
                        self.TDescripcion.set("")
                        self.Tmedida.set("")
                        self.codigoAlumno.set("")
                        self.nombresAlumno.set("")
                        self.apellidosAlumno.set("")
                        self.programaAlumno.set("")
                    else:
                        mb.showinfo("Informacion", "No existe un alumno con dicha informacion")
                    
                else:
                    mb.showwarning("Error","Debe seleccionar los campos a modificar")
            except:
                mb.showinfo("Información","El instrumento seleccionado ya fue asignado a otro alumno")
        else:
            return True
######################## MODULO CLASES #####################################
    
    def clases(self):

        self.ocultarmostrarMenu()

        self.frame4Interactivo.place_forget()

        ########################################
        ##        Frame interactivo           ##
        ########################################

        self.frame4Interactivo=tk.Frame(self.ventana1)
        self.frame4Interactivo.config(bg='light cyan',bd=11)
        self.frame4Interactivo.place(x=-15,y=55,width=1050,height=580)

         #Label titulo frame

        self.labeltitulo=tk.Label(self.frame4Interactivo,text="Gestión de clases",bg="light cyan",font=("Times New Roman",20), fg="Black")
        self.labeltitulo.place(x=20,y=30)

        self.frameDecorativoClases=tk.Frame(self.frame4Interactivo,bg="Dark Blue",width=120,height=300)
        self.frameDecorativoClases.pack(side="bottom", fill="x")

        ###########################

        self.labelframeOpciones=tk.LabelFrame(self.frame4Interactivo,bg="light cyan",width=40,height=20,text="Opciones",font=("Times New Roman",12))
        self.labelframeOpciones.place(x=60,y=70)

        self.labelframeListaProfesores=tk.LabelFrame(self.frame4Interactivo, bg="light cyan", width=720,height=220,text="Selección profesores",font=("Times New Roman",12))
        self.labelframeListaProfesores.place(x=280,y=50)

        self.labelframeTablaProfes=tk.LabelFrame(self.frame4Interactivo, bg="light cyan",text="Tabla profesores",font=("Times New Roman",12))
        self.labelframeTablaProfes.place(x=510,y=50)

        self.labelframeTablaClases=tk.LabelFrame(self.frameDecorativoClases, bg="Dark Blue",text="Tabla Clases",font=("Times New Roman",12), width=400,height=220,fg='white')
        self.labelframeTablaClases.place(x=380,y=10)

        self.labelframeOpcionesClasesProfesor=tk.LabelFrame(self.frameDecorativoClases, bg="Dark Blue",text="",font=("Times New Roman",12), width=400,height=220,fg='white')
        self.labelframeOpcionesClasesProfesor.place(x=380,y=220)

        self.labelframeSeleccionClases=tk.LabelFrame(self.frameDecorativoClases, bg="Dark Blue",text="Selección clases",font=("Times New Roman",12), width=400,height=220,fg='white')
        self.labelframeSeleccionClases.place(x=40,y=10)

        self.frameDetalles=tk.LabelFrame(self.frameDecorativoClases,bg="light cyan",text="Buscador",font=("Times New Roman",10))
        self.frameDetalles.place(x=40,y=157)

        ########## Botones GEstión de evaluaciones y asistencias

        btnAsignar=tk.Button(self.labelframeOpciones,text="Asignar Alumno",command=self.asignarAlumno,width=20)
        btnAsignar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12))
        btnAsignar.grid(row=0,column=0,padx=2,pady=4)

        btnEvaluaciones=tk.Button(self.labelframeOpciones,text="Gestión Evaluaciones",command=self.evaluaciones,width=20)
        btnEvaluaciones.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12))
        btnEvaluaciones.grid(row=1,column=0,padx=2,pady=4)

        btnAsistencias=tk.Button(self.labelframeOpciones,text="Gestión Asistencias",command=self.asistencia,width=20)
        btnAsistencias.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12))
        btnAsistencias.grid(row=2,column=0,padx=2,pady=4)

        ###################### Agregar, modificar y eliminar 

        btnAgregar=tk.Button(self.labelframeOpcionesClasesProfesor,text="Agregar",command=self.add_new_clases,width=20)
        btnAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12))
        btnAgregar.grid(row=0,column=1,padx=2,pady=10)

        btnmodificar=tk.Button(self.labelframeOpcionesClasesProfesor,text="Modificar",command=self.update_clases_profesor,width=20)
        btnmodificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12))
        btnmodificar.grid(row=0,column=2,padx=2,pady=10)

        btneliminar=tk.Button(self.labelframeOpcionesClasesProfesor,text="Eliminar",command=self.delete_clases,width=20)
        btneliminar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12))
        btneliminar.grid(row=0,column=3,padx=2,pady=10)

        ######################## Label profesores

        labelCedula=tk.Label(self.labelframeListaProfesores,text="Cédula:",font=("Times New Roman",12),bg="light cyan")
        labelCedula.grid(row=0,column=0,padx=5,pady=5)

        labelNombre=tk.Label(self.labelframeListaProfesores,text="Nombre:",font=("Times New Roman",12),bg="light cyan")
        labelNombre.grid(row=1,column=0,padx=5,pady=5)

        labelApellido=tk.Label(self.labelframeListaProfesores,text="Apellido:",font=("Times New Roman",12),bg="light cyan")
        labelApellido.grid(row=2,column=0,padx=5,pady=5)

        labelPrograma=tk.Label(self.labelframeListaProfesores,text="Programa:",font=("Times New Roman",12),bg="light cyan")
        labelPrograma.grid(row=3,column=0,padx=5,pady=5)

        ############################ Entrys Profesores

        self.txtprofesorCI=tk.StringVar()
        self.txtNombre=tk.StringVar()
        self.txtApellido=tk.StringVar()
        self.txtPrograma=tk.StringVar()

        self.entryCedulaProfe=ttk.Entry(self.labelframeListaProfesores,textvariable=self.txtprofesorCI,font=("Times New Roman",10),state="readonly")
        self.entryCedulaProfe.grid(row=0,column=1,padx=5,pady=10)

        self.entryNombreProf=ttk.Entry(self.labelframeListaProfesores,textvariable=self.txtNombre,font=("Times New Roman",10),state="readonly")
        self.entryNombreProf.grid(row=1,column=1,padx=5,pady=10)

        self.entryApellidoProfe=ttk.Entry(self.labelframeListaProfesores,textvariable=self.txtApellido,font=("Times New Roman",10),state="readonly")
        self.entryApellidoProfe.grid(row=2,column=1,padx=5,pady=10)

        self.entryProgramaProfe=ttk.Entry(self.labelframeListaProfesores,textvariable=self.txtPrograma,font=("Times New Roman",10),state="readonly")
        self.entryProgramaProfe.grid(row=3,column=1,padx=5,pady=10)

        ######################## Label Seleccion clases

        labelidclase=tk.Label(self.labelframeSeleccionClases,text="Id clase:",font=("Times New Roman",12),bg="Dark Blue",fg="white")
        labelidclase.grid(row=0,column=0,padx=5,pady=5)

        labelCatedra=tk.Label(self.labelframeSeleccionClases,text="Cátedra:",font=("Times New Roman",12),bg="Dark Blue",fg="white")
        labelCatedra.grid(row=1,column=0,padx=5,pady=5)

        labelPrograma=tk.Label(self.labelframeSeleccionClases,text="Selección programa:",font=("Times New Roman",12),bg="Dark Blue",fg="white")
        labelPrograma.grid(row=2,column=0,padx=5,pady=5)

        ########################### Entry

        self.txtCatedra=tk.StringVar()
        self.txtidClase=tk.StringVar()

        self.entryidClase=ttk.Entry(self.labelframeSeleccionClases,textvariable=self.txtidClase,font=("Times New Roman",10))
        self.entryidClase.grid(row=0,column=1,padx=5,pady=10)

        self.entryNombreProf=ttk.Entry(self.labelframeSeleccionClases,textvariable=self.txtCatedra,font=("Times New Roman",10))
        self.entryNombreProf.grid(row=1,column=1,padx=5,pady=10)

        ############### Combobox interactivo

        self.opcionPrograma=tk.StringVar()
        self.comobox2=ttk.Combobox(self.labelframeSeleccionClases,
                                width=20,
                                textvariable=self.opcionPrograma,
                                state='readonly',
                                font=("Times New Roman",10))

        self.comobox2['value']=self.cargarComboProgramas()
        self.comobox2.current(0)
        self.comobox2.grid(row=2,column=1,padx=5,pady=1)

        #################################################################
        
        #################### Treeview Profesores

        ##Tree para mostrar columnas
        self.treeProfe = ttk.Treeview(self.labelframeTablaProfes,columns=("#1","#2","#3"),height="7")
        self.treeProfe.heading("#0",text="Cédula")
        self.treeProfe.heading("#1",text="Nombres")
        self.treeProfe.heading("#2",text="Apellidos")
        self.treeProfe.heading("#3",text="Programa")
        
            ##Tamano de columnas
        self.treeProfe.column("#0",width=90)
        self.treeProfe.column("#1",width=100)
        self.treeProfe.column("#2",width=100)
        self.treeProfe.column("#3",width=140)

        self.treeProfe.bind("<1>",self.getrow_profesoresClases)
        
        self.treeProfe.pack(side='left',padx=10)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.labelframeTablaProfes, orient="vertical", command = self.treeProfe.yview)
        scrolvert.pack(side="left",fill="y")
        self.treeProfe.config(yscrollcommand=scrolvert.set)

        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        alumno=self.treeProfe.get_children()

        for elemento in alumno:
            self.treeProfe.delete(elemento)
        try:
            cur.execute("SELECT a.cedula_identidad, a.nombres, a.apellidos, b.nombre_programa FROM profesor a, programa b WHERE a.id_programa=b.id_programa AND id_cargo NOT IN ('5','4','3') AND a.cedula_identidad NOT IN ('222222','111111') ORDER BY a.apellidos ASC")
            for row in cur:
                self.treeProfe.insert("",0,text=row[0],values=(row[1],row[2],row[3]))
        except:
            pass
        
        #################### Treeview Clases

        ##Tree para mostrar columnas
        self.treeClases = ttk.Treeview(self.labelframeTablaClases,columns=("#1","#2","#3","#4","#5"),height="7")
        self.treeClases.heading("#0",text="Id Clase")
        self.treeClases.heading("#1",text="Cátedra")
        self.treeClases.heading("#2",text="Programa")
        self.treeClases.heading("#3",text="Cédula")
        self.treeClases.heading("#4",text="Nombres")
        self.treeClases.heading("#5",text="Apellidos")
        
            ##Tamano de columnas
        self.treeClases.column("#0",width=55)
        self.treeClases.column("#1",width=120)
        self.treeClases.column("#2",width=110)
        self.treeClases.column("#3",width=90)
        self.treeClases.column("#4",width=100)
        self.treeClases.column("#5",width=100)

        self.treeClases.bind("<1>",self.getrow_asignarProfesClases)
        
        self.treeClases.pack(side='left',padx=10)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.labelframeTablaClases, orient="vertical", command = self.treeClases.yview)
        scrolvert.pack(side="left",fill="y")
        self.treeClases.config(yscrollcommand=scrolvert.set)

        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        alumno=self.treeClases.get_children()

        for elemento in alumno:
            self.treeClases.delete(elemento)
        try:
            cur.execute("SELECT a.id_clase, a.catedra, c.nombre_programa, b.cedula_identidad, b.nombres, b.apellidos  FROM clase a, profesor b, programa c WHERE a.id_programa=c.id_programa AND a.cedula_identidad=b.cedula_identidad AND b.id_cargo NOT IN ('5','4','3') AND b.cedula_identidad NOT IN ('222222','111111') ORDER BY b.apellidos ASC")
            for row in cur:
                self.treeClases.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))
        except:
            pass

        

        #################### BUSCADOR 

        label1=tk.Label(self.frameDetalles,text="Consulta por:",bg="Light cyan",font=("Times New Roman",10))
        label1.grid(row=0,column=0,padx=1,pady=1)

        self.buscadorClasess=tk.StringVar()
        self.entry1=tk.Entry(self.frameDetalles,width=30,textvariable=self.buscadorClasess,font=("Times New Roman",10))
        self.entry1.grid(row=2,column=1,padx=1,pady=1)

        self.labelprograma=tk.Label(self.frameDetalles,text="Programa:",bg="Light cyan",font=("Times New Roman",10))
        self.labelprograma.grid(row=1,column=0,padx=1,pady=1)

        ############### Combobox interactivo

        self.opcionProgramaBus=tk.StringVar()
        self.comoboxClases=ttk.Combobox(self.frameDetalles,
                                width=20,
                                textvariable=self.opcionProgramaBus,
                                state='readonly',
                                font=("Times New Roman",10))

        self.comoboxClases['value']=self.cargarComboProgramas()
        self.comoboxClases.current(0)
        self.comoboxClases.grid(row=1,column=1,padx=1,pady=1)

        #################################################################

        lableBucar=tk.Label(self.frameDetalles,text="Buscar:",bg="Light cyan",font=("Times New Roman",10))
        lableBucar.grid(row=2,column=0,padx=5,pady=5)

        self.opcionParaClases=tk.StringVar()
        opcionesBusquedaInstrumento=("Cátedra","Nombres","Apellidos","Cédula")
            
        self.comoboxInstrumentoConsulta=ttk.Combobox(self.frameDetalles,
                                    width=20,
                                    textvariable=self.opcionParaClases,
                                    values=opcionesBusquedaInstrumento,
                                    state='readonly',
                                    font=("Times New Roman",10))
        self.comoboxInstrumentoConsulta.current(1)

        
        self.comoboxInstrumentoConsulta.grid(row=0,column=1)

        btnBuscar=tk.Button(self.frameDetalles,text="Buscar",command=self.searchClases,font=("Times New Roman",10),width=9)
        btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnBuscar.grid(row=3,column=0,padx=5,pady=5)

        btnLimpiar=tk.Button(self.frameDetalles,text="Limpiar",command=self.clearListaClases,font=("Times New Roman",10),width=9)
        btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnLimpiar.grid(row=3,column=1,padx=5,pady=5)

############################## FUNCIONES MODULO CLASES

    def getrow_profesoresClases(self,event):
        rowid=self.treeProfe.identify_row(event.y)
        self.treeProfe.selection_set(rowid)
        item=self.treeProfe.item(self.treeProfe.focus())
        self.cod_ProfCI=item["text"]
        
        ############ Busca la informacion en la base de datos

        query="SELECT a.cedula_identidad, a.nombres, a.apellidos, b.nombre_programa FROM profesor a, programa b WHERE a.id_programa=b.id_programa AND id_cargo NOT IN ('5','4','3') AND a.cedula_identidad NOT IN ('222222','111111') AND a.cedula_identidad='"+self.cod_ProfCI+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()

        
        if len(respuesta)>0:
            self.txtprofesorCI.set(respuesta[0][0])
            self.txtNombre.set(respuesta[0][1])
            self.txtApellido.set(respuesta[0][2])
            self.txtPrograma.set(respuesta[0][3])

    def getrow_asignarProfesClases(self,event):
        rowid=self.treeClases.identify_row(event.y)
        self.treeClases.selection_set(rowid)
        item=self.treeClases.item(self.treeClases.focus())
        self.cod_ClaseID=item["text"]
        
        ############ Busca la informacion en la base de datos

        query="SELECT a.id_clase, a.catedra, c.nombre_programa, b.cedula_identidad, b.nombres, b.apellidos  FROM clase a, profesor b, programa c WHERE a.id_programa=c.id_programa AND a.cedula_identidad=b.cedula_identidad AND b.id_cargo NOT IN ('5','4','3') AND b.cedula_identidad NOT IN ('222222','111111') AND a.id_clase='"+self.cod_ClaseID+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()

        query2="SELECT a.id_clase, a.catedra, c.nombre_programa, b.cedula_identidad, b.nombres, b.apellidos  FROM clase a, profesor b, programa c WHERE a.id_programa=c.id_programa AND a.cedula_identidad=b.cedula_identidad AND b.id_cargo NOT IN ('5','4','3') AND b.cedula_identidad NOT IN ('222222','111111') AND a.id_clase='"+self.cod_ClaseID+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query2)
        respuestaSerial=cursor.fetchall() 
        self.IDModificar=tk.StringVar()
        self.IDModificar.set(respuestaSerial[0][3])
        self.busqueda=respuestaSerial[0][3]
        cone.close()


        query3="SELECT b.nombre_programa FROM profesor a, programa b WHERE a.id_programa=b.id_programa AND a.cedula_identidad='"+self.busqueda+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query3)
        respuestaNombreprograma=cursor.fetchall() 
        self.IDModificar=tk.StringVar()
        self.IDModificar.set(respuestaNombreprograma[0][0])
        cone.close()

        
        if len(respuesta)>0:
            self.txtidClase.set(respuesta[0][0])
            self.txtCatedra.set(respuesta[0][1])
            self.opcionPrograma.set(respuesta[0][2])
            self.txtprofesorCI.set(respuesta[0][3])
            self.txtNombre.set(respuesta[0][4])
            self.txtApellido.set(respuesta[0][5])
            self.txtPrograma.set(respuestaNombreprograma[0][0])

############################## Agregar, modificar y eliminar

    def add_new_clases (self):
        id_clase=self.txtidClase.get()
        catedra=self.txtCatedra.get()
        programa=self.definir_programa()
        ci_profesor=self.txtprofesorCI.get()
        try:
            if self.validar_contrasena(id_clase):
                
                query="INSERT INTO clase(id_clase,catedra,cedula_identidad,id_programa) VALUES(%s,%s,%s,%s)"

                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(id_clase,catedra,ci_profesor,programa))
                
                cone.commit()
                cone.close()
                self.clearListaClases()
                
                mb.showinfo("Información","Se han cargado con éxito los datos.")
                self.txtprofesorCI.set("")
                self.txtNombre.set("")
                self.txtApellido.set("")
                self.txtPrograma.set("")
                self.txtidClase.set("")
                self.txtCatedra.set("")
            else:
                mb.showwarning("Error","Debe completar los campos obligatorios (*)")
        except:
            mb.showinfo("Información","Este dato ya existe")

    def update_clases_profesor(self):
        

        id_clase=self.txtidClase.get()
        

        if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea actualizar estos datos? "):
            if self.validar_contrasena(id_clase):
                catedra=self.txtCatedra.get()
                programa=self.definir_programa()
                ci_profesor=self.txtprofesorCI.get()
                id_Sinmodificar=self.cod_ClaseID
                ci_sinmodificar=self.busqueda

                query="UPDATE clase SET id_clase=%s, catedra=%s, id_programa=%s, cedula_identidad=%s WHERE id_clase = '"+id_Sinmodificar+"' AND cedula_identidad='"+ci_sinmodificar+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(id_clase,catedra,programa,ci_profesor))
                

                cone.commit()
                cone.close()

                self.clearListaClases()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han cargado con éxito los datos.")
                    self.txtprofesorCI.set("")
                    self.txtNombre.set("")
                    self.txtApellido.set("")
                    self.txtPrograma.set("")
                    self.txtidClase.set("")
                    self.txtCatedra.set("")
                else:
                    mb.showinfo("Informacion", "No existe un campo con dicha informacion")
                
            else:
                mb.showwarning("Error","Debe seleccionar los campos a modificar")
        else:
            return True

    def delete_clases(self):
        cod_clase=self.txtidClase.get()
        ci_profesor=self.txtprofesorCI.get()
        try:
            if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea borrar estos datos? "):
                query="DELETE FROM clase WHERE id_clase='"+cod_clase+"' AND cedula_identidad='"+ci_profesor+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query)
                
                cone.commit()
                cone.close()
                self.clearListaClases()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han borrado los datos con éxito.")
                    self.txtprofesorCI.set("")
                    self.txtNombre.set("")
                    self.txtApellido.set("")
                    self.txtPrograma.set("")
                    self.txtidClase.set("")
                    self.txtCatedra.set("")
                else:
                    mb.showinfo("Informacion", "No existe un alumno con dicha informacion")
            else:
                return True
        except:
                mb.showwarning("Error","Introduzca la informacion que desee borrar o selecione en la tabla instrumentos asignados.")

######################################### LISTA CLASES

    def updateListaClases(self,respuesta):
        info=self.treeClases.get_children()

        for elemento in info:
            self.treeClases.delete(elemento)
        for row in respuesta:
            self.treeClases.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))

    def clearListaClases(self):
        query="SELECT a.id_clase, a.catedra, c.nombre_programa, b.cedula_identidad, b.nombres, b.apellidos  FROM clase a, profesor b, programa c WHERE a.id_programa=c.id_programa AND a.cedula_identidad=b.cedula_identidad AND b.id_cargo NOT IN ('5','4','3') AND b.cedula_identidad NOT IN ('222222','111111') ORDER BY b.apellidos ASC"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.buscadorClasess.set("")
        self.updateListaClases(respuesta)

    def searchClases(self):
        opcioncontrol=self.opcionParaClases.get()
        buscarLista=self.buscadorClasess.get()
        opcionPrograma=self.comoboxClases.get()
        if opcioncontrol=="Cátedra":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.id_clase, a.catedra, c.nombre_programa, b.cedula_identidad, b.nombres, b.apellidos  FROM clase a, profesor b, programa c WHERE a.id_programa=c.id_programa AND a.cedula_identidad=b.cedula_identidad AND b.id_cargo NOT IN ('5','4','3') AND b.cedula_identidad NOT IN ('222222','111111')  AND a.catedra LIKE '%"+buscarLista+"%' AND c.nombre_programa='"+opcionPrograma+"' ORDER BY b.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaClases(respuesta)

        if opcioncontrol=="Nombres":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.id_clase, a.catedra, c.nombre_programa, b.cedula_identidad, b.nombres, b.apellidos  FROM clase a, profesor b, programa c WHERE a.id_programa=c.id_programa AND a.cedula_identidad=b.cedula_identidad AND b.id_cargo NOT IN ('5','4','3') AND b.cedula_identidad NOT IN ('222222','111111')  AND b.nombres LIKE '%"+buscarLista+"%' AND c.nombre_programa='"+opcionPrograma+"' ORDER BY b.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaClases(respuesta)

        if opcioncontrol=="Apellidos":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.id_clase, a.catedra, c.nombre_programa, b.cedula_identidad, b.nombres, b.apellidos  FROM clase a, profesor b, programa c WHERE a.id_programa=c.id_programa AND a.cedula_identidad=b.cedula_identidad AND b.id_cargo NOT IN ('5','4','3') AND b.cedula_identidad NOT IN ('222222','111111')  AND b.apellidos LIKE '%"+buscarLista+"%' AND c.nombre_programa='"+opcionPrograma+"' ORDER BY b.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaClases(respuesta)

        if opcioncontrol=="Cédula":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.id_clase, a.catedra, c.nombre_programa, b.cedula_identidad, b.nombres, b.apellidos  FROM clase a, profesor b, programa c WHERE a.id_programa=c.id_programa AND a.cedula_identidad=b.cedula_identidad AND b.id_cargo NOT IN ('5','4','3') AND b.cedula_identidad NOT IN ('222222','111111')  AND b.cedula_identidad LIKE '%"+buscarLista+"%' AND c.nombre_programa='"+opcionPrograma+"' ORDER BY b.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaClases(respuesta)      

################################ MODULO ASIGNAR ALUMNO
    def asignarAlumno(self):
        self.ventana1.destroy()
        self.ventana2=tk.Tk()
        self.ventana2.title("Asignar Alumnos a Clases")
        self.ventana2.config(bg='Light cyan')
        self.ventana2.geometry("1150x650")
        self.ventana2.resizable(0,0)
        self.ventana2.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")

        #### Frame Logo

        self.frameLogo=tk.Frame(self.ventana2,bg="light blue",width=395,height=133)
        self.frameLogo.place(x=738, y= 180)

        self.imagen=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\instrumento.png")
        fondo=tk.Label(self.frameLogo,image=self.imagen,bg="light cyan").place(x=0,y=0)
        
        self.decoraframe=tk.Frame(self.ventana2,bg="dark blue",height=20)
        self.decoraframe.pack(fill="both",expand="no",side="top")

        frameoscuro=tk.Frame(self.ventana2,bg="dark blue",height=330)
        frameoscuro.pack(fill="both",expand="no",side="bottom")

        self.lista=tk.LabelFrame(self.ventana2,text="Opciones",font=("Times New Roman",10))
        self.lista.config(bg="light cyan")
        self.lista.place(x=860,y=20)

        self.tablaRepresentante=tk.LabelFrame(self.ventana2,text="Lista Clases",font=("Times New Roman",10))
        self.tablaRepresentante.config(bg="light cyan")
        self.tablaRepresentante.place(x=85,y=170)

        self.tablaAlumnos=tk.LabelFrame(self.ventana2,text="Lista Alumnos",font=("Times New Roman",10))
        self.tablaAlumnos.config(bg="light cyan")
        self.tablaAlumnos.place(x=55,y=20)

        self.labelframeRepresentantesSeleccion=tk.LabelFrame(self.ventana2,text="Selección Clases",font=("Times New Roman",15),fg="white")
        self.labelframeRepresentantesSeleccion.config(bg="dark blue")
        self.labelframeRepresentantesSeleccion.place(x=1,y=325)

        self.labelframeAlumnosSeleccion=tk.LabelFrame(self.ventana2,text="Selección Alumno",font=("Times New Roman",15),fg="white",height=100)
        self.labelframeAlumnosSeleccion.config(bg="dark blue")
        self.labelframeAlumnosSeleccion.place(x=245,y=325)

        self.labelframeTablaAlumnosRepresentantes=tk.LabelFrame(self.ventana2,text="Alumnos con Clase asignada",font=("Times New Roman",15),fg="white")
        self.labelframeTablaAlumnosRepresentantes.config(bg="dark blue")
        self.labelframeTablaAlumnosRepresentantes.place(x=490,y=325)

        self.labelframeopcionesAR=tk.LabelFrame(self.ventana2,text="Asignar Clase",font=("Times New Roman",15),fg="white")
        self.labelframeopcionesAR.config(bg="dark blue")
        self.labelframeopcionesAR.place(x=10,y=530)

        self.buscador=tk.LabelFrame(self.ventana2,text='Buscador',font=("Times New Roman",10))
        self.buscador.config(bg="light cyan")
        self.buscador.place(x= 520, y= 530)

        ###################### Ventana opciones

        btnVolver=tk.Button(self.lista,text="Volver",command=self.volver_moduloClase)
        btnVolver.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12),width=19)
        btnVolver.grid(row=0,column=1,padx=2,pady=2)

        self.hideInstrumentoAlumno=1
        btnBuscador=tk.Button(self.lista,text="Buscar Clase",command=self.ocultarMostrarDetallesBuscadorProfesoresClases)
        btnBuscador.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12),width=19)
        btnBuscador.grid(row=1,column=1,padx=2,pady=2)

        btnBuscador=tk.Button(self.lista,text="Buscar Alumno",command=self.ocultarMostrarDetallesBuscadorAlumnoClases)
        btnBuscador.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12),width=19)
        btnBuscador.grid(row=2,column=1,padx=2,pady=2)

        ########################## TREEVIEW INSTRUMENTOS

        #################### Treeview Clases

        ##Tree para mostrar columnas
        self.treeClases = ttk.Treeview(self.tablaRepresentante,columns=("#1","#2","#3","#4","#5"),height="5")
        self.treeClases.heading("#0",text="Id Clase")
        self.treeClases.heading("#1",text="Cátedra")
        self.treeClases.heading("#2",text="Programa")
        self.treeClases.heading("#3",text="Cédula")
        self.treeClases.heading("#4",text="Nombres")
        self.treeClases.heading("#5",text="Apellidos")
        
            ##Tamano de columnas
        self.treeClases.column("#0",width=55)
        self.treeClases.column("#1",width=120)
        self.treeClases.column("#2",width=140)
        self.treeClases.column("#3",width=90)
        self.treeClases.column("#4",width=100)
        self.treeClases.column("#5",width=100)

        self.treeClases.bind("<1>",self.getrow_asignarProfesClases)
        
        self.treeClases.pack(side='left',padx=10)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.tablaRepresentante, orient="vertical", command = self.treeClases.yview)
        scrolvert.pack(side="left",fill="y")
        self.treeClases.config(yscrollcommand=scrolvert.set)

        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        alumno=self.treeClases.get_children()

        for elemento in alumno:
            self.treeClases.delete(elemento)
        try:
            cur.execute("SELECT a.id_clase, a.catedra, c.nombre_programa, b.cedula_identidad, b.nombres, b.apellidos  FROM clase a, profesor b, programa c WHERE a.id_programa=c.id_programa AND a.cedula_identidad=b.cedula_identidad AND b.id_cargo NOT IN ('5','4','3') AND b.cedula_identidad NOT IN ('222222','111111') ORDER BY b.apellidos ASC")
            for row in cur:
                self.treeClases.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))
        except:
            pass
        #################### Treeview Alumnos

        self.treeAlumno = ttk.Treeview(self.tablaAlumnos,columns=("#1","#2","#3","#4","#5"),height="4")
        self.treeAlumno.heading("#0",text="Código")
        self.treeAlumno.heading("#1",text="Cédula")
        self.treeAlumno.heading("#2",text="Nombres")
        self.treeAlumno.heading("#3",text="Apellidos")
        self.treeAlumno.heading("#4",text="Programa")
        self.treeAlumno.heading("#5",text="Instrumento principal")

        self.treeAlumno.column("#0",width=100)
        self.treeAlumno.column("#1",width=70)
        self.treeAlumno.column("#2",width=130)
        self.treeAlumno.column("#3",width=130)
        self.treeAlumno.column("#4",width=160)
        self.treeAlumno.column("#5",width=160)
        
        self.treeAlumno.bind("<1>",self.getrow_seleccion_alumnos)
        self.treeAlumno.pack(side="right",fill="both",padx=5,pady=5)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.tablaAlumnos, orient="vertical", command = self.tree.yview)
        scrolvert.pack(side="left",fill="y")
        self.treeAlumno.config(yscrollcommand=scrolvert.set)
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.treeAlumno.get_children()

        for elemento in profesor:
            self.treeAlumno.delete(elemento)
        try:
            cur.execute("SELECT  a.cod_alumno,a.ci_alumno,a.nombres,a.apellidos,b.nombre_programa,a.instrumento_principal FROM alumno a, programa b WHERE a.id_programa=b.id_programa")
            rows=cur.fetchall()
            for row in rows:
                self.treeAlumno.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))
        except:
            pass

        con.close()

        #################### Labelframe seleccion Instrumentos Label

        labelCiRepresentanteSel=tk.Label(self.labelframeRepresentantesSeleccion,bg="dark blue",text="(*)ID clase:",font=("Times New Roman",10),fg="white")
        labelCiRepresentanteSel.grid(row=0,column=1,padx=1,pady=10)

        labelnombres=tk.Label(self.labelframeRepresentantesSeleccion,bg="dark blue",text="Cátedra:",font=("Times New Roman",10),fg="white")
        labelnombres.grid(row=1,column=1,padx=1,pady=10)

        labelapellidos=tk.Label(self.labelframeRepresentantesSeleccion,bg="dark blue",text="Programa:",font=("Times New Roman",10),fg="white")
        labelapellidos.grid(row=2,column=1,padx=1,pady=10)

        labelfiliacion=tk.Label(self.labelframeRepresentantesSeleccion,bg="dark blue",text="Cédula identidad:",font=("Times New Roman",10),fg="white")
        labelfiliacion.grid(row=3,column=1,padx=1,pady=10)


        ####################### Entrys
        self.txtidClase=tk.StringVar()
        self.txtCatedra=tk.StringVar()
        self.txtPrograma=tk.StringVar()
        self.txtprofesorCI=tk.StringVar()

        self.entryCedulaRepresentante=ttk.Entry(self.labelframeRepresentantesSeleccion,textvariable=self.txtidClase,font=("Times New Roman",10),state="readonly")
        self.entryCedulaRepresentante.grid(row=0,column=2,padx=1,pady=10)

        self.entrynombres=ttk.Entry(self.labelframeRepresentantesSeleccion,textvariable=self.txtCatedra,font=("Times New Roman",10),state="readonly")
        self.entrynombres.grid(row=1,column=2,padx=1,pady=10)

        self.entryApellidos=ttk.Entry(self.labelframeRepresentantesSeleccion,textvariable=self.txtPrograma,font=("Times New Roman",10),state="readonly")
        self.entryApellidos.grid(row=2,column=2,padx=1,pady=10)

        self.entryCedulaProf=ttk.Entry(self.labelframeRepresentantesSeleccion,textvariable=self.txtprofesorCI,font=("Times New Roman",10),state="readonly")
        self.entryCedulaProf.grid(row=3,column=2,padx=1,pady=10)

        #################### Labelframe seleccion representantes Label

        self.codigoAlumno=tk.StringVar()
        self.nombresAlumno=tk.StringVar()
        self.apellidosAlumno=tk.StringVar()
        self.programaAlumno=tk.StringVar()

        labelcod_alumno=tk.Label(self.labelframeAlumnosSeleccion,bg="dark blue",text="(*)Código alumno:",font=("Times New Roman",10),fg="white")
        labelcod_alumno.grid(row=0,column=1,padx=1,pady=10)

        labelnombres=tk.Label(self.labelframeAlumnosSeleccion,bg="dark blue",text="Nombres:",font=("Times New Roman",10),fg="white")
        labelnombres.grid(row=1,column=1,padx=1,pady=10)

        labelapellidos=tk.Label(self.labelframeAlumnosSeleccion,bg="dark blue",text="Apellidos:",font=("Times New Roman",10),fg="white")
        labelapellidos.grid(row=2,column=1,padx=1,pady=10)

        labelprograma=tk.Label(self.labelframeAlumnosSeleccion,bg="dark blue",text="Programa:",font=("Times New Roman",10),fg="white")
        labelprograma.grid(row=3,column=1,padx=1,pady=10)

        ####################### Entrys

        self.entryCod_alumno=ttk.Entry(self.labelframeAlumnosSeleccion,textvariable=self.codigoAlumno,font=("Times New Roman",10),state="readonly")
        self.entryCod_alumno.grid(row=0,column=2,padx=1,pady=10)

        self.entrynombres=ttk.Entry(self.labelframeAlumnosSeleccion,textvariable=self.nombresAlumno,font=("Times New Roman",10),state="readonly")
        self.entrynombres.grid(row=1,column=2,padx=1,pady=10)

        self.entryApellidos=ttk.Entry(self.labelframeAlumnosSeleccion,textvariable=self.apellidosAlumno,font=("Times New Roman",10),state="readonly")
        self.entryApellidos.grid(row=2,column=2,padx=1,pady=10)

        self.entryprogramaSeleccion=ttk.Entry(self.labelframeAlumnosSeleccion,textvariable=self.programaAlumno,font=("Times New Roman",10),state="readonly")
        self.entryprogramaSeleccion.grid(row=3,column=2,padx=1,pady=10)

        ########################## TREEVIEW ALUMNOS Y REPRESENTANTES

        self.treeAlumnosInstrumentos = ttk.Treeview(self.labelframeTablaAlumnosRepresentantes,columns=("#1","#2","#3","#4","#5","#6"),height="6")
        self.treeAlumnosInstrumentos.heading("#0",text="Código alumno")
        self.treeAlumnosInstrumentos.heading("#1",text="Nombres alumno")
        self.treeAlumnosInstrumentos.heading("#2",text="Apellidos alumno")
        self.treeAlumnosInstrumentos.heading("#3",text="Programa")
        self.treeAlumnosInstrumentos.heading("#4",text="ID clase")
        self.treeAlumnosInstrumentos.heading("#5",text="Cátedra")
        self.treeAlumnosInstrumentos.heading("#6",text="Cédula profesor")

        self.treeAlumnosInstrumentos.column("#0",width=70)
        self.treeAlumnosInstrumentos.column("#1",width=80)
        self.treeAlumnosInstrumentos.column("#2",width=85)
        self.treeAlumnosInstrumentos.column("#3",width=95)
        self.treeAlumnosInstrumentos.column("#4",width=70)
        self.treeAlumnosInstrumentos.column("#5",width=80)
        self.treeAlumnosInstrumentos.column("#6",width=80)

        self.treeAlumnosInstrumentos.bind("<1>",self.get_row_ClasesAlumnos)
        self.treeAlumnosInstrumentos.pack(side="left",fill="both",padx=5,pady=5)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.labelframeTablaAlumnosRepresentantes, orient="vertical", command = self.treeAlumnosInstrumentos.yview)
        scrolvert.pack(side="left",fill="y")
        self.treeAlumnosInstrumentos.config(yscrollcommand=scrolvert.set)
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.treeAlumnosInstrumentos.get_children()

        for elemento in profesor:
            self.treeAlumnosInstrumentos.delete(elemento)
        try:
            cur.execute("SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.id_clase, b.catedra, b.cedula_identidad FROM alumno a, clase b, clase_alumno c, programa d WHERE b.id_clase=c.id_clase AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno")
            rows=cur.fetchall()
            for row in rows:
                self.treeAlumnosInstrumentos.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6]))
        except:
            pass

        con.close()

        ###################### Agregar, modificar y eliminar 

        btnAgregar=tk.Button(self.labelframeopcionesAR,text="Agregar",command=self.add_new_claseAlumno,width=15)
        btnAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12))
        btnAgregar.grid(row=0,column=1,padx=2,pady=10)

        btnmodificar=tk.Button(self.labelframeopcionesAR,text="Modificar",command=self.update_claseAlumno,width=15)
        btnmodificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12))
        btnmodificar.grid(row=0,column=2,padx=2,pady=10)

        btneliminar=tk.Button(self.labelframeopcionesAR,text="Eliminar",command=self.delete_clasealumno,width=15)
        btneliminar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12))
        btneliminar.grid(row=0,column=3,padx=2,pady=10)

        #################### BUSCADOR 

        label1=tk.Label(self.buscador,text="Consulta por:",bg="Light cyan",font=("Times New Roman",10))
        label1.grid(row=0,column=0,padx=5,pady=5)

        self.buscador1=tk.StringVar()
        self.entry1=tk.Entry(self.buscador,width=30,textvariable=self.buscador1,font=("Times New Roman",10))
        self.entry1.grid(row=0,column=3,padx=5,pady=5)

        self.labelprograma=tk.Label(self.buscador,text="Programa:",bg="Light cyan",font=("Times New Roman",10))
        self.labelprograma.grid(row=1,column=0,padx=5,pady=5)

        ############### Combobox interactivo

        self.opcionPrograma=tk.StringVar()
        self.comobox2=ttk.Combobox(self.buscador,
                                width=20,
                                textvariable=self.opcionPrograma,
                                state='readonly',
                                font=("Times New Roman",10))

        self.comobox2['value']=self.cargarComboProgramas()
        self.comobox2.current(0)
        self.comobox2.grid(row=1,column=1,padx=5,pady=1)

        #################################################################

        lableBucar=tk.Label(self.buscador,text="Buscar:",bg="Light cyan",font=("Times New Roman",10))
        lableBucar.grid(row=0,column=2,padx=5,pady=5)

        self.opcion=tk.StringVar()
        opcionesBusqueda=("Nombres Alumno","Apellidos Alumno","Cátedra","Cédula")
         
        self.comobox1=ttk.Combobox(self.buscador,
                                width=20,
                                textvariable=self.opcion,
                                values=opcionesBusqueda,
                                state='readonly',
                                font=("Times New Roman",10))
        self.comobox1.current(1)

        self.comobox1.grid(row=0,column=1)

        btnBuscar=tk.Button(self.buscador,text="Buscar",command=self.searchClasesAlumnos,font=("Times New Roman",10),width=9)
        btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnBuscar.grid(row=1,column=2,padx=5,pady=5)

        btnLimpiar=tk.Button(self.buscador,text="Limpiar",command=self.clearListaClasesAlumnos,font=("Times New Roman",10),width=9)
        btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnLimpiar.grid(row=1,column=3,padx=5,pady=5)

    ############### CLases

    def ocultarMostrarDetallesBuscadorProfesoresClases(self):
         

        if self.hideInstrumentoAlumno==0:
            self.frameDetalles.place_forget()
            self.hideInstrumentoAlumno=1
        else:
             #################Información que aparece y desaparece
            
            self.frameDetalles=tk.LabelFrame(self.ventana2,bg="light cyan",text="Clases")
            self.frameDetalles.place(x=750,y=170,height=144,width=350)

            #################### BUSCADOR 

        

            label1=tk.Label(self.frameDetalles,text="Consulta por:",bg="Light cyan",font=("Times New Roman",10))
            label1.grid(row=0,column=0,padx=1,pady=5)

            self.buscadorClasess=tk.StringVar()
            self.entry1=tk.Entry(self.frameDetalles,width=30,textvariable=self.buscadorClasess,font=("Times New Roman",10))
            self.entry1.grid(row=2,column=1,padx=1,pady=5)

            self.labelprograma=tk.Label(self.frameDetalles,text="Programa:",bg="Light cyan",font=("Times New Roman",10))
            self.labelprograma.grid(row=1,column=0,padx=1,pady=5)

            ############### Combobox interactivo

            self.opcionProgramaBus=tk.StringVar()
            self.comoboxClases=ttk.Combobox(self.frameDetalles,
                                    width=20,
                                    textvariable=self.opcionProgramaBus,
                                    state='readonly',
                                    font=("Times New Roman",10))

            self.comoboxClases['value']=self.cargarComboProgramas()
            self.comoboxClases.current(0)
            self.comoboxClases.grid(row=1,column=1,padx=1,pady=1)

            #################################################################

            lableBucar=tk.Label(self.frameDetalles,text="Buscar:",bg="Light cyan",font=("Times New Roman",10))
            lableBucar.grid(row=2,column=0,padx=1,pady=5)

            self.opcionParaClases=tk.StringVar()
            opcionesBusquedaInstrumento=("Cátedra","Nombres","Apellidos","Cédula")
            
            self.comoboxInstrumentoConsulta=ttk.Combobox(self.frameDetalles,
                                    width=20,
                                    textvariable=self.opcionParaClases,
                                    values=opcionesBusquedaInstrumento,
                                    state='readonly',
                                    font=("Times New Roman",10))
            self.comoboxInstrumentoConsulta.current(1)

        
            self.comoboxInstrumentoConsulta.grid(row=0,column=1)

            btnBuscar=tk.Button(self.frameDetalles,text="Buscar",command=self.searchClases,font=("Times New Roman",10),width=9)
            btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnBuscar.grid(row=3,column=0,padx=5,pady=5)

            btnLimpiar=tk.Button(self.frameDetalles,text="Limpiar",command=self.clearListaClases,font=("Times New Roman",10),width=9)
            btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnLimpiar.grid(row=3,column=1,padx=5,pady=5)

            self.hideInstrumentoAlumno=0

    def ocultarMostrarDetallesBuscadorAlumnoClases(self):
         

        if self.hideInstrumentoAlumno==0:
            self.frameDetalles.place_forget()#place(x=-70,y=0,width=350,height=800)
            self.hideInstrumentoAlumno=1
        else:
                #################Información que aparece y desaparece
                
            self.frameDetalles=tk.LabelFrame(self.ventana2,bg="light cyan",text="Alumnos")
            self.frameDetalles.place(x=750,y=170,height=144,width=350)

                #################### BUSCADOR 

            

            label1=tk.Label(self.frameDetalles,text="Consulta por:",bg="Light cyan",font=("Times New Roman",10))
            label1.grid(row=0,column=0,padx=1,pady=5)

            self.buscadorAlumno=tk.StringVar()
            self.entry1=tk.Entry(self.frameDetalles,width=30,textvariable=self.buscadorAlumno,font=("Times New Roman",10))
            self.entry1.grid(row=2,column=1,padx=1,pady=5)

            self.labelprograma=tk.Label(self.frameDetalles,text="Programa:",bg="Light cyan",font=("Times New Roman",10))
            self.labelprograma.grid(row=1,column=0,padx=1,pady=5)

                ############### Combobox interactivo

            self.opcionProgramaAlumno=tk.StringVar()
            self.comoboxAlumnos=ttk.Combobox(self.frameDetalles,
                                        width=20,
                                        textvariable=self.opcionProgramaAlumno,
                                        state='readonly',
                                        font=("Times New Roman",10))

            self.comoboxAlumnos['value']=self.cargarComboProgramas()
            self.comoboxAlumnos.current(0)
            self.comoboxAlumnos.grid(row=1,column=1,padx=1,pady=1)

                #################################################################

            lableBucar=tk.Label(self.frameDetalles,text="Buscar:",bg="Light cyan",font=("Times New Roman",10))
            lableBucar.grid(row=2,column=0,padx=1,pady=5)

            self.opcionAlumno=tk.StringVar()
            opcionesBusquedaAlumno=("Nombres Alumno","Apellidos Alumno","Cédula","Instrumento Principal")
                
            self.comoboxAlumnosConsulta=ttk.Combobox(self.frameDetalles,
                                        width=20,
                                        textvariable=self.opcionAlumno,
                                        values=opcionesBusquedaAlumno,
                                        state='readonly',
                                        font=("Times New Roman",10))
            self.comoboxAlumnosConsulta.current(1)

            
            self.comoboxAlumnosConsulta.grid(row=0,column=1)

            btnBuscar=tk.Button(self.frameDetalles,text="Buscar",command=self.searchtablaAlumno,font=("Times New Roman",10),width=9)
            btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnBuscar.grid(row=3,column=0,padx=1,pady=5)

            btnLimpiar=tk.Button(self.frameDetalles,text="Limpiar",command=self.clearTreeAlumno,font=("Times New Roman",10),width=9)
            btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnLimpiar.grid(row=3,column=1,padx=1,pady=5)

            self.hideInstrumentoAlumno=0

    #################### Funciones

    def get_row_ClasesAlumnos(self,event):
        rowid=self.treeAlumnosInstrumentos.identify_row(event.y)
        self.treeAlumnosInstrumentos.selection_set(rowid)
        item=self.treeAlumnosInstrumentos.item(self.treeAlumnosInstrumentos.focus())
        self.cod_alumnoID=item["text"]
        self.cod_clase=item["values"]
        claseID=str(self.cod_clase[3])
        ############ Busca la informacion en la base de datos

        query2="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.id_clase, b.catedra, b.cedula_identidad FROM alumno a, clase b, clase_alumno c, programa d WHERE b.id_clase=c.id_clase AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno AND a.cod_alumno='"+self.cod_alumnoID+"' AND b.id_clase='"+claseID+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query2)
        respuestaCedula=cursor.fetchall() 
        self.IDClaseModificar=tk.StringVar()
        self.IDClaseModificar.set(respuestaCedula[0][4])
        cone.close()

        query="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.id_clase, b.catedra, b.cedula_identidad FROM alumno a, clase b, clase_alumno c, programa d WHERE b.id_clase=c.id_clase AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno AND a.cod_alumno='"+self.cod_alumnoID+"' AND b.id_clase='"+claseID+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()


        if len(respuesta)>0:
            self.codigoAlumno.set(respuesta[0][0])
            self.nombresAlumno.set(respuesta[0][1])
            self.apellidosAlumno.set(respuesta[0][2])
            self.programaAlumno.set(respuesta[0][3])
            self.txtPrograma.set(respuesta[0][3])
            self.txtidClase.set(respuesta[0][4])
            self.txtCatedra.set(respuesta[0][5])
            self.txtprofesorCI.set(respuesta[0][6])
    
    def updateListaClasesAlumnos(self,respuesta):
        info=self.treeAlumnosInstrumentos.get_children()

        for elemento in info:
            self.treeAlumnosInstrumentos.delete(elemento)
        for row in respuesta:
            self.treeAlumnosInstrumentos.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6]))

    def clearListaClasesAlumnos(self):
        query="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.id_clase, b.catedra, b.cedula_identidad FROM alumno a, clase b, clase_alumno c, programa d WHERE b.id_clase=c.id_clase AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno ORDER BY a.apellidos ASC"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.buscador1.set("")
        self.updateListaClasesAlumnos(respuesta)

    def searchClasesAlumnos(self):
        opcioncontrol=self.comobox1.get()
        buscarLista=self.buscador1.get()
        opcionPrograma=self.comobox2.get()
        if opcioncontrol=="Cátedra":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.id_clase, b.catedra, b.cedula_identidad FROM alumno a, clase b, clase_alumno c, programa d WHERE b.id_clase=c.id_clase AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno  AND b.catedra LIKE '%"+buscarLista+"%' AND d.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaClasesAlumnos(respuesta)

        if opcioncontrol=="Nombres Alumno":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.id_clase, b.catedra, b.cedula_identidad FROM alumno a, clase b, clase_alumno c, programa d WHERE b.id_clase=c.id_clase AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno  AND a.nombres LIKE '%"+buscarLista+"%' AND d.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaClasesAlumnos(respuesta)

        if opcioncontrol=="Apellidos Alumno":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.id_clase, b.catedra, b.cedula_identidad FROM alumno a, clase b, clase_alumno c, programa d WHERE b.id_clase=c.id_clase AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno  AND a.apellidos LIKE '%"+buscarLista+"%' AND d.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaClasesAlumnos(respuesta)

        if opcioncontrol=="Cédula":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, a.nombres, a.apellidos, d.nombre_programa, b.id_clase, b.catedra, b.cedula_identidad FROM alumno a, clase b, clase_alumno c, programa d WHERE b.id_clase=c.id_clase AND a.id_programa=d.id_programa AND a.cod_alumno=c.cod_alumno  AND b.cedula_identidad LIKE '%"+buscarLista+"%' AND d.nombre_programa='"+opcionPrograma+"' ORDER BY a.apellidos ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaClasesAlumnos(respuesta)      

######################### DELETE; UPDATE Y ADD

    def add_new_claseAlumno(self):
        id_clase=self.txtidClase.get()
        cod_alumno=self.codigoAlumno.get()

        try:
            if self.validar_contrasena(id_clase):
                
                query="INSERT INTO clase_alumno(id_clase,cod_alumno) VALUES(%s,%s)"

                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(id_clase,cod_alumno))
                
                cone.commit()
                cone.close()
                self.clearListaClasesAlumnos()
                
                mb.showinfo("Información","Se han cargado con éxito los datos.")
                self.codigoAlumno.set("")
                self.nombresAlumno.set("")
                self.apellidosAlumno.set("")
                self.programaAlumno.set("")
                self.txtPrograma.set("")
                self.txtidClase.set("")
                self.txtCatedra.set("")
                self.txtprofesorCI.set("")
            else:
                mb.showwarning("Error","Debe completar los campos obligatorios (*)")
        except:
            mb.showinfo("Información","Este dato ya existe")

    def update_claseAlumno(self):
        id_clase=self.txtidClase.get()
        if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea actualizar estos datos? "):
            if self.validar_contrasena(id_clase):
                cod_alumno=self.codigoAlumno.get()
                id_Sinmodificar=self.IDClaseModificar.get()
                codAlumno_sinmodificar=self.cod_alumnoID
            
                query="UPDATE clase_alumno SET id_clase=%s, cod_alumno=%s WHERE id_clase = '"+id_Sinmodificar+"' AND cod_alumno='"+codAlumno_sinmodificar+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(id_clase,cod_alumno))
                

                cone.commit()
                cone.close()

                self.clearListaClasesAlumnos()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han cargado con éxito los datos.")
                    self.codigoAlumno.set("")
                    self.nombresAlumno.set("")
                    self.apellidosAlumno.set("")
                    self.programaAlumno.set("")
                    self.txtPrograma.set("")
                    self.txtidClase.set("")
                    self.txtCatedra.set("")
                    self.txtprofesorCI.set("")
                else:
                    mb.showinfo("Informacion", "No existe un campo con dicha informacion")
                
            else:
                mb.showwarning("Error","Debe seleccionar los campos a modificar")
        else:
            return True

    def delete_clasealumno(self):
        cod_clase=self.txtidClase.get()
        cod_alumno=self.codigoAlumno.get()
        try:
            if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea borrar estos datos? "):
                query="DELETE FROM clase_alumno WHERE id_clase='"+cod_clase+"' AND cod_alumno='"+cod_alumno+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query)
                
                cone.commit()
                cone.close()
                self.clearListaClasesAlumnos()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han borrado los datos con éxito.")
                    self.codigoAlumno.set("")
                    self.nombresAlumno.set("")
                    self.apellidosAlumno.set("")
                    self.programaAlumno.set("")
                    self.txtPrograma.set("")
                    self.txtidClase.set("")
                    self.txtCatedra.set("")
                    self.txtprofesorCI.set("")
                else:
                    mb.showinfo("Informacion", "No existe un alumno con dicha informacion")
            else:
                return True
        except:
                mb.showwarning("Error","Introduzca la informacion que desee borrar o selecione en la tabla instrumentos asignados.")

########################################
########### VOLVER A CLASE #############

    def volver_moduloClase(self):
        
        self.ventana2.destroy()

        ###Programa estandar para las ventanas ---------------------
        self.ventana1=tk.Tk()
        self.ventana1.title("Administrador")
        self.ventana1.geometry("1050x650")
        self.ventana1.config(bg='light cyan',bd=15)
        self.ventana1.resizable(0,0)
        self.ventana1.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")

        #-------------------------------------------------------

        #Frame admin decorativo
        self.frame1=tk.Frame(self.ventana1)

        #Frame admin informacion tentativa
        self.frame2=tk.Frame(self.ventana1)

        #Frame informacion de los usuarios
        self.frame3=tk.Frame(self.ventana1)
        self.frame3.config(bg="dark blue",bd=11)
        self.frame3.place(x=-15,y=-15,width=1050,height=70)

        #label informacion de profesores
        self.label1=tk.Label(self.frame3,text="Administrador",bg="dark blue",font=("Times New Roman",20), fg="white")
        self.label1.place(x=110,y=10)

        # Información usuario
        self.id_usuario=tk.StringVar()
        self.id_usuario.set(self.UsuarioName)
        
        labelUsuario=tk.Label(self.frame3,text="Usuario: "+self.id_usuario.get(),bg="dark blue",font=("Times New Roman",15), fg="white")
        labelUsuario.place(x=830,y=7)

        ##-------------------Botones predeterminados --------------------------

        self.hidemenu=1
        self.botonmenu=tk.Button(self.frame3,text="Menu", command=self.ocultarmostrarMenu,bg="blueviolet", bd= 5,font=("Times New Roman",15), fg="white",activebackground="light blue",activeforeground="Black")
        self.photo=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\home.png")
        self.botonmenu.config( image=self.photo, compound=LEFT)
        self.botonmenu.place(x=10,y=5)

        ########################################
        ##        Frame interactivo           ##
        ########################################

        self.frame4Interactivo=tk.Frame(self.ventana1)
        self.frame4Interactivo.config(bg='light cyan',bd=11)
        self.frame4Interactivo.place(x=-15,y=55,width=1050,height=580)

         #Label titulo frame

        self.labeltitulo=tk.Label(self.frame4Interactivo,text="Gestión de clases",bg="light cyan",font=("Times New Roman",20), fg="Black")
        self.labeltitulo.place(x=20,y=30)

        self.frameDecorativoClases=tk.Frame(self.frame4Interactivo,bg="Dark Blue",width=120,height=300)
        self.frameDecorativoClases.pack(side="bottom", fill="x")

        ###########################

        self.labelframeOpciones=tk.LabelFrame(self.frame4Interactivo,bg="light cyan",width=40,height=20,text="Opciones",font=("Times New Roman",12))
        self.labelframeOpciones.place(x=60,y=70)

        self.labelframeListaProfesores=tk.LabelFrame(self.frame4Interactivo, bg="light cyan", width=720,height=220,text="Selección profesores",font=("Times New Roman",12))
        self.labelframeListaProfesores.place(x=280,y=50)

        self.labelframeTablaProfes=tk.LabelFrame(self.frame4Interactivo, bg="light cyan",text="Tabla profesores",font=("Times New Roman",12))
        self.labelframeTablaProfes.place(x=510,y=50)

        self.labelframeTablaClases=tk.LabelFrame(self.frameDecorativoClases, bg="Dark Blue",text="Tabla Clases",font=("Times New Roman",12), width=400,height=220,fg='white')
        self.labelframeTablaClases.place(x=380,y=10)

        self.labelframeOpcionesClasesProfesor=tk.LabelFrame(self.frameDecorativoClases, bg="Dark Blue",text="",font=("Times New Roman",12), width=400,height=220,fg='white')
        self.labelframeOpcionesClasesProfesor.place(x=380,y=220)

        self.labelframeSeleccionClases=tk.LabelFrame(self.frameDecorativoClases, bg="Dark Blue",text="Selección clases",font=("Times New Roman",12), width=400,height=220,fg='white')
        self.labelframeSeleccionClases.place(x=40,y=10)

        self.frameDetalles=tk.LabelFrame(self.frameDecorativoClases,bg="light cyan",text="Buscador",font=("Times New Roman",10))
        self.frameDetalles.place(x=40,y=157)

        ########## Botones GEstión de evaluaciones y asistencias

        btnAsignar=tk.Button(self.labelframeOpciones,text="Asignar Alumno",command=self.asignarAlumno,width=20)
        btnAsignar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12))
        btnAsignar.grid(row=0,column=0,padx=2,pady=4)

        btnEvaluaciones=tk.Button(self.labelframeOpciones,text="Gestión Evaluaciones",command=self.evaluaciones,width=20)
        btnEvaluaciones.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12))
        btnEvaluaciones.grid(row=1,column=0,padx=2,pady=4)

        btnAsistencias=tk.Button(self.labelframeOpciones,text="Gestión Asistencias",command=self.asistencia,width=20)
        btnAsistencias.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12))
        btnAsistencias.grid(row=2,column=0,padx=2,pady=4)

        ###################### Agregar, modificar y eliminar 

        btnAgregar=tk.Button(self.labelframeOpcionesClasesProfesor,text="Agregar",command=self.add_new_clases,width=20)
        btnAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12))
        btnAgregar.grid(row=0,column=1,padx=2,pady=10)

        btnmodificar=tk.Button(self.labelframeOpcionesClasesProfesor,text="Modificar",command=self.update_clases_profesor,width=20)
        btnmodificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12))
        btnmodificar.grid(row=0,column=2,padx=2,pady=10)

        btneliminar=tk.Button(self.labelframeOpcionesClasesProfesor,text="Eliminar",command=self.delete_clases,width=20)
        btneliminar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5,font=("Times New Roman",12))
        btneliminar.grid(row=0,column=3,padx=2,pady=10)

        ######################## Label profesores

        labelCedula=tk.Label(self.labelframeListaProfesores,text="Cédula:",font=("Times New Roman",12),bg="light cyan")
        labelCedula.grid(row=0,column=0,padx=5,pady=5)

        labelNombre=tk.Label(self.labelframeListaProfesores,text="Nombre:",font=("Times New Roman",12),bg="light cyan")
        labelNombre.grid(row=1,column=0,padx=5,pady=5)

        labelApellido=tk.Label(self.labelframeListaProfesores,text="Apellido:",font=("Times New Roman",12),bg="light cyan")
        labelApellido.grid(row=2,column=0,padx=5,pady=5)

        labelPrograma=tk.Label(self.labelframeListaProfesores,text="Programa:",font=("Times New Roman",12),bg="light cyan")
        labelPrograma.grid(row=3,column=0,padx=5,pady=5)

        ############################ Entrys Profesores

        self.txtprofesorCI=tk.StringVar()
        self.txtNombre=tk.StringVar()
        self.txtApellido=tk.StringVar()
        self.txtPrograma=tk.StringVar()

        self.entryCedulaProfe=ttk.Entry(self.labelframeListaProfesores,textvariable=self.txtprofesorCI,font=("Times New Roman",10),state="readonly")
        self.entryCedulaProfe.grid(row=0,column=1,padx=5,pady=10)

        self.entryNombreProf=ttk.Entry(self.labelframeListaProfesores,textvariable=self.txtNombre,font=("Times New Roman",10),state="readonly")
        self.entryNombreProf.grid(row=1,column=1,padx=5,pady=10)

        self.entryApellidoProfe=ttk.Entry(self.labelframeListaProfesores,textvariable=self.txtApellido,font=("Times New Roman",10),state="readonly")
        self.entryApellidoProfe.grid(row=2,column=1,padx=5,pady=10)

        self.entryProgramaProfe=ttk.Entry(self.labelframeListaProfesores,textvariable=self.txtPrograma,font=("Times New Roman",10),state="readonly")
        self.entryProgramaProfe.grid(row=3,column=1,padx=5,pady=10)

        ######################## Label Seleccion clases

        labelidclase=tk.Label(self.labelframeSeleccionClases,text="Id clase:",font=("Times New Roman",12),bg="Dark Blue",fg="white")
        labelidclase.grid(row=0,column=0,padx=5,pady=5)

        labelCatedra=tk.Label(self.labelframeSeleccionClases,text="Cátedra:",font=("Times New Roman",12),bg="Dark Blue",fg="white")
        labelCatedra.grid(row=1,column=0,padx=5,pady=5)

        labelPrograma=tk.Label(self.labelframeSeleccionClases,text="Selección programa:",font=("Times New Roman",12),bg="Dark Blue",fg="white")
        labelPrograma.grid(row=2,column=0,padx=5,pady=5)

        ########################### Entry

        self.txtCatedra=tk.StringVar()
        self.txtidClase=tk.StringVar()

        self.entryidClase=ttk.Entry(self.labelframeSeleccionClases,textvariable=self.txtidClase,font=("Times New Roman",10))
        self.entryidClase.grid(row=0,column=1,padx=5,pady=10)

        self.entryNombreProf=ttk.Entry(self.labelframeSeleccionClases,textvariable=self.txtCatedra,font=("Times New Roman",10))
        self.entryNombreProf.grid(row=1,column=1,padx=5,pady=10)

        ############### Combobox interactivo

        self.opcionPrograma=tk.StringVar()
        self.comobox2=ttk.Combobox(self.labelframeSeleccionClases,
                                width=20,
                                textvariable=self.opcionPrograma,
                                state='readonly',
                                font=("Times New Roman",10))

        self.comobox2['value']=self.cargarComboProgramas()
        self.comobox2.current(0)
        self.comobox2.grid(row=2,column=1,padx=5,pady=1)

        #################################################################
        
        #################### Treeview Profesores

        ##Tree para mostrar columnas
        self.treeProfe = ttk.Treeview(self.labelframeTablaProfes,columns=("#1","#2","#3"),height="7")
        self.treeProfe.heading("#0",text="Cédula")
        self.treeProfe.heading("#1",text="Nombres")
        self.treeProfe.heading("#2",text="Apellidos")
        self.treeProfe.heading("#3",text="Programa")
        
            ##Tamano de columnas
        self.treeProfe.column("#0",width=90)
        self.treeProfe.column("#1",width=100)
        self.treeProfe.column("#2",width=100)
        self.treeProfe.column("#3",width=140)

        self.treeProfe.bind("<1>",self.getrow_profesoresClases)
        
        self.treeProfe.pack(side='left',padx=10)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.labelframeTablaProfes, orient="vertical", command = self.treeProfe.yview)
        scrolvert.pack(side="left",fill="y")
        self.treeProfe.config(yscrollcommand=scrolvert.set)

        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        alumno=self.treeProfe.get_children()

        for elemento in alumno:
            self.treeProfe.delete(elemento)
        try:
            cur.execute("SELECT a.cedula_identidad, a.nombres, a.apellidos, b.nombre_programa FROM profesor a, programa b WHERE a.id_programa=b.id_programa AND id_cargo NOT IN ('5','4','3') AND a.cedula_identidad NOT IN ('222222','111111') ORDER BY a.apellidos ASC")
            for row in cur:
                self.treeProfe.insert("",0,text=row[0],values=(row[1],row[2],row[3]))
        except:
            pass
        
        #################### Treeview Clases

        ##Tree para mostrar columnas
        self.treeClases = ttk.Treeview(self.labelframeTablaClases,columns=("#1","#2","#3","#4","#5"),height="7")
        self.treeClases.heading("#0",text="Id Clase")
        self.treeClases.heading("#1",text="Cátedra")
        self.treeClases.heading("#2",text="Programa")
        self.treeClases.heading("#3",text="Cédula")
        self.treeClases.heading("#4",text="Nombres")
        self.treeClases.heading("#5",text="Apellidos")
        
            ##Tamano de columnas
        self.treeClases.column("#0",width=55)
        self.treeClases.column("#1",width=120)
        self.treeClases.column("#2",width=110)
        self.treeClases.column("#3",width=90)
        self.treeClases.column("#4",width=100)
        self.treeClases.column("#5",width=100)

        self.treeClases.bind("<1>",self.getrow_asignarProfesClases)
        
        self.treeClases.pack(side='left',padx=10)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.labelframeTablaClases, orient="vertical", command = self.treeClases.yview)
        scrolvert.pack(side="left",fill="y")
        self.treeClases.config(yscrollcommand=scrolvert.set)

        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        alumno=self.treeClases.get_children()

        for elemento in alumno:
            self.treeClases.delete(elemento)
        try:
            cur.execute("SELECT a.id_clase, a.catedra, c.nombre_programa, b.cedula_identidad, b.nombres, b.apellidos  FROM clase a, profesor b, programa c WHERE a.id_programa=c.id_programa AND a.cedula_identidad=b.cedula_identidad AND b.id_cargo NOT IN ('5','4','3') AND b.cedula_identidad NOT IN ('222222','111111') ORDER BY b.apellidos ASC")
            for row in cur:
                self.treeClases.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))
        except:
            pass

        

        #################### BUSCADOR 

        label1=tk.Label(self.frameDetalles,text="Consulta por:",bg="Light cyan",font=("Times New Roman",10))
        label1.grid(row=0,column=0,padx=1,pady=1)

        self.buscadorClasess=tk.StringVar()
        self.entry1=tk.Entry(self.frameDetalles,width=30,textvariable=self.buscadorClasess,font=("Times New Roman",10))
        self.entry1.grid(row=2,column=1,padx=1,pady=1)

        self.labelprograma=tk.Label(self.frameDetalles,text="Programa:",bg="Light cyan",font=("Times New Roman",10))
        self.labelprograma.grid(row=1,column=0,padx=1,pady=1)

        ############### Combobox interactivo

        ############### Combobox interactivo

        self.opcionProgramaBus=tk.StringVar()
        self.comoboxClases=ttk.Combobox(self.frameDetalles,
                                width=20,
                                textvariable=self.opcionProgramaBus,
                                state='readonly',
                                font=("Times New Roman",10))

        self.comoboxClases['value']=self.cargarComboProgramas()
        self.comoboxClases.current(0)
        self.comoboxClases.grid(row=1,column=1,padx=1,pady=1)

        #################################################################

        lableBucar=tk.Label(self.frameDetalles,text="Buscar:",bg="Light cyan",font=("Times New Roman",10))
        lableBucar.grid(row=2,column=0,padx=5,pady=5)

        self.opcionParaClases=tk.StringVar()
        opcionesBusquedaInstrumento=("Cátedra","Nombres","Apellidos","Cédula")
            
        self.comoboxInstrumentoConsulta=ttk.Combobox(self.frameDetalles,
                                    width=20,
                                    textvariable=self.opcionParaClases,
                                    values=opcionesBusquedaInstrumento,
                                    state='readonly',
                                    font=("Times New Roman",10))
        self.comoboxInstrumentoConsulta.current(1)

        
        self.comoboxInstrumentoConsulta.grid(row=0,column=1)

        btnBuscar=tk.Button(self.frameDetalles,text="Buscar",command=self.searchClases,font=("Times New Roman",10),width=9)
        btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnBuscar.grid(row=3,column=0,padx=5,pady=5)

        btnLimpiar=tk.Button(self.frameDetalles,text="Limpiar",command=self.clearListaClases,font=("Times New Roman",10),width=9)
        btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnLimpiar.grid(row=3,column=1,padx=5,pady=5)

############################# MODULO EVALUACIONES/Notas

    def evaluaciones(self):
        self.ventana1.destroy()
        self.ventana2=tk.Tk()
        self.ventana2.title("Evaluaciones")
        self.ventana2.config(bg='Light cyan')
        self.ventana2.geometry("1150x650")
        self.ventana2.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")
        
        self.decoraframe=tk.Frame(self.ventana2,bg="dark blue",height=190)
        self.decoraframe.pack(fill="both",expand="no",side="top")

        self.decoFrameabajo=tk.Frame(self.ventana2,bg="dark blue",height=90)
        self.decoFrameabajo.pack(fill="both",expand="no",side="bottom")

        self.lista=tk.LabelFrame(self.decoraframe,text="Evaluaciones realizadas",fg="white",font=("Times New Roman",10))
        self.lista.config(bg="dark blue")
        self.lista.pack(expand="no",padx=5,pady=5,ipady=10,side="top")

        self.tree = ttk.Treeview(self.lista,columns=("#1","#2","#3","#4","#5","#6","#7","#8","9"),height="7")
        self.tree.heading("#0",text="Código alumno")
        self.tree.heading("#1",text="Id evaluación")
        self.tree.heading("#2",text="Id clase")
        self.tree.heading("#3",text="Cátedra")
        self.tree.heading("#4",text="Programa")
        self.tree.heading("#5",text="Nombres")
        self.tree.heading("#6",text="Apellidos")
        self.tree.heading("#7",text="Nota")
        self.tree.heading("#8",text="Fecha")
        self.tree.heading("#9",text="Trimestre")
        

        self.tree.column("#0",width=90)
        self.tree.column("#1",width=90)
        self.tree.column("#2",width=45)
        self.tree.column("#3",width=150)
        self.tree.column("#4",width=90)
        self.tree.column("#5",width=150)
        self.tree.column("#6",width=150)
        self.tree.column("#7",width=90)
        self.tree.column("#8",width=90)
        self.tree.column("#9",width=90)
        
        
        self.tree.bind("<1>",self.get_row_Evaluacion_Clases)
        self.tree.pack(side="left",fill="both",padx=5,pady=5)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.lista, orient="vertical", command = self.tree.yview)
        scrolvert.pack(side="left",fill="y")
        self.tree.config(yscrollcommand=scrolvert.set)
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.tree.get_children()

        for elemento in profesor:
            self.tree.delete(elemento)
        try:
            cur.execute("SELECT a.cod_alumno, b.id_evaluacion, c.id_clase, e.catedra, d.nombre_programa, a.nombres, a.apellidos, b.nota, c.fecha, c.trimestre FROM alumno a, evaluacion_alumno b, evaluacion c, programa d, clase e WHERE a.cod_alumno=b.cod_alumno AND c.id_evaluacion=b.id_evaluacion AND d.id_programa=e.id_programa AND e.id_clase=c.id_clase")
            rows=cur.fetchall()
            for row in rows:
                self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
        except:
            pass

        ##########Búsqueda de información por Clase, programa y trimestre
        self.labelframebusquedaClaseProfe=tk.LabelFrame(self.ventana2,text="Información y búsqueda",bg="light cyan",width=930,height=340,font=("Times New Roman",10))
        self.labelframebusquedaClaseProfe.place(x=12,y=247)

        frameTablaCLases=tk.Frame(self.labelframebusquedaClaseProfe,bg="light cyan",width=70)
        frameTablaCLases.place(x=5,y=10)

        self.treeClases = ttk.Treeview(frameTablaCLases,columns=("#1","#2","#3"),height="5")
        self.treeClases.heading("#0",text="Cédula identidad")
        self.treeClases.heading("#1",text="Id clase")
        self.treeClases.heading("#2",text="Cátera")
        self.treeClases.heading("#3",text="Programa")

        self.treeClases.column("#0",width=90)
        self.treeClases.column("#1",width=90)
        self.treeClases.column("#2",width=150)
        self.treeClases.column("#3",width=150)

        self.treeClases.bind("<1>",self.get_row_ClasesBuscadorEvaluacion)
        self.treeClases.pack(side="left")


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(frameTablaCLases, orient="vertical", command = self.treeClases.yview)
        scrolvert.pack(side="left",fill="y")
        self.treeClases.config(yscrollcommand=scrolvert.set)

        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.treeClases.get_children()

        for elemento in profesor:
            self.treeClases.delete(elemento)
        try:
            cur.execute("SELECT a.cedula_identidad, a.id_clase, a.catedra, b.nombre_programa FROM clase a, programa b WHERE a.id_programa=b.id_programa")
            rows=cur.fetchall()
            for row in rows:
                self.treeClases.insert("",0,text=row[0],values=(row[1],row[2],row[3]))
        except:
            pass

        frameBuscadordeClases=tk.LabelFrame(self.labelframebusquedaClaseProfe,text="Buscador",bg="light cyan",width=491,height=124,font=("Times New Roman",10))
        frameBuscadordeClases.place(x=5,y=162)

        ######## Buscador clases
        label1=tk.Label(frameBuscadordeClases,text="Consulta por:",bg="Light cyan",font=("Times New Roman",10))
        label1.grid(row=1,column=0,padx=5,pady=5)

        self.buscador1=tk.StringVar()
        self.entry1=tk.Entry(frameBuscadordeClases,width=30,textvariable=self.buscador1,font=("Times New Roman",10))
        self.entry1.grid(row=4,column=1,padx=5,pady=5)

        self.labelprograma=tk.Label(frameBuscadordeClases,text="Programa:",bg="Light cyan",font=("Times New Roman",10))
        self.labelprograma.grid(row=2,column=0,padx=5,pady=5)

        ############### Combobox interactivo

        self.opcionPrograma=tk.StringVar()
        self.comobox2=ttk.Combobox(frameBuscadordeClases,
                                width=20,
                                textvariable=self.opcionPrograma,
                                state='readonly',
                                font=("Times New Roman",10))

        self.comobox2['value']=self.cargarComboProgramas()
        self.comobox2.current(0)
        self.comobox2.grid(row=2,column=1,padx=5,pady=1)

        #################################################################

        lableBucar=tk.Label(frameBuscadordeClases,text="Buscar:",bg="Light cyan",font=("Times New Roman",10))
        lableBucar.grid(row=4,column=0,padx=5,pady=5)

        self.opcion=tk.StringVar()
        opcionesBusqueda=("Cátedra","Cédula")
         
        self.comobox1=ttk.Combobox(frameBuscadordeClases,
                                width=20,
                                textvariable=self.opcion,
                                values=opcionesBusqueda,
                                state='readonly',
                                font=("Times New Roman",10))
        self.comobox1.current(1)

       
        self.comobox1.grid(row=1,column=1)

        btnBuscar=tk.Button(frameBuscadordeClases,text="Buscar",command=self.searchClasesenEv,font=("Times New Roman",10),width=15)
        btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnBuscar.grid(row=1,column=2,padx=5,pady=5)

        btnLimpiar=tk.Button(frameBuscadordeClases,text="Limpiar",command=self.clearListaClasesTree,font=("Times New Roman",10),width=15)
        btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnLimpiar.grid(row=2,column=2,padx=5,pady=5)

        ################# Frame decorativo

        decoframe=tk.Frame(self.labelframebusquedaClaseProfe,bg="dark blue",width=79,height=154)
        decoframe.place(x=422,y=152)

        #######################################################
        ############ Buscador lista evaluacion_alumno##########

        labelframeBuscadorAlumnoEvaluacion=tk.LabelFrame(self.labelframebusquedaClaseProfe,text="Selección",bg="light cyan",width=410,height=309,font=("Times New Roman",10))
        labelframeBuscadorAlumnoEvaluacion.place(x=508,y=0)

        frameSeleccion=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="light cyan",width=380,height=190)
        frameSeleccion.place(x=0,y=0)


        ############# Label column 0

        labelIdClase=tk.Label(frameSeleccion,text="Id clase:",bg="light cyan",font=("Times New Roman",10))
        labelIdClase.grid(row=1,column=0,padx=1,pady=10)

        labelcatedra=tk.Label(frameSeleccion,text="Cátedra:",bg="light cyan",font=("Times New Roman",10))
        labelcatedra.grid(row=2,column=0,padx=1,pady=10)

        labelPrograma=tk.Label(frameSeleccion,text="Programa:",bg="light cyan",font=("Times New Roman",10))
        labelPrograma.grid(row=3,column=0,padx=1,pady=10)

        ############## label column 2
        labelCedula=tk.Label(frameSeleccion,text="Cédula Identidad:",bg="light cyan",font=("Times New Roman",10))
        labelCedula.grid(row=1,column=2,padx=1,pady=10)

        labelNombreProf=tk.Label(frameSeleccion,text="Nombre Profesor:",bg="light cyan",font=("Times New Roman",10))
        labelNombreProf.grid(row=2,column=2,padx=1,pady=10)

        labelapellidoProf=tk.Label(frameSeleccion,text="Apellido Profesor:",bg="light cyan",font=("Times New Roman",10))
        labelapellidoProf.grid(row=3,column=2,padx=1,pady=10)

        ############### Entry column 1
        self.idClasetext=tk.StringVar()
        self.catedratext=tk.StringVar()
        self.programatxt=tk.StringVar()
        self.cedulatext=tk.StringVar()
        self.nombresproftext=tk.StringVar()
        self.apellidosproxtext=tk.StringVar()

        EntryIdClase=ttk.Entry(frameSeleccion,textvariable=self.idClasetext,width=18,state='readonly',font=("Times New Roman",10))
        EntryIdClase.grid(row=1,column=1,padx=1,pady=10)

        Entrycatedra=ttk.Entry(frameSeleccion,textvariable=self.catedratext,width=18,state='readonly',font=("Times New Roman",10))
        Entrycatedra.grid(row=2,column=1,padx=1,pady=10)

        EntryPrograma=ttk.Entry(frameSeleccion,textvariable=self.programatxt,width=18,state='readonly',font=("Times New Roman",10))
        EntryPrograma.grid(row=3,column=1,padx=1,pady=10)

        ############ Entry column 3
        EntryCedula=ttk.Entry(frameSeleccion,textvariable=self.cedulatext,width=18,state='readonly',font=("Times New Roman",10))
        EntryCedula.grid(row=1,column=3,padx=1,pady=10)

        EntryNombreProf=ttk.Entry(frameSeleccion,textvariable=self.nombresproftext,width=18,state='readonly',font=("Times New Roman",10))
        EntryNombreProf.grid(row=2,column=3,padx=1,pady=10)

        EntryapellidoProf=ttk.Entry(frameSeleccion,textvariable=self.apellidosproxtext,width=18,state='readonly',font=("Times New Roman",10))
        EntryapellidoProf.grid(row=3,column=3,padx=1,pady=10)

        ############### Frame deco linera

        frameLinea=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="dark blue",width=385,height=7)
        frameLinea.place(x=5,y=129)

        frameBuscar=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="light cyan",width=386,height=105)
        frameBuscar.place(x=5,y=151)

        ############ Label

        labelTrimestre=tk.Label(frameBuscar,text="Trimestre:",bg="light cyan",font=("Times New Roman",10))
        labelTrimestre.grid(row=0,column=0,padx=1,pady=3)

        labelNombreProf=tk.Label(frameBuscar,text="Fecha:",bg="light cyan",font=("Times New Roman",10))
        labelNombreProf.grid(row=1,column=0,padx=1,pady=3)

        labelapellidoProf=tk.Label(frameBuscar,text="Consulta por:",bg="light cyan",font=("Times New Roman",10))
        labelapellidoProf.grid(row=2,column=0,padx=1,pady=3)


        ################ Entry y combobox
        self.buscarTrimestretxt=tk.StringVar()
        self.buscarfechatxt=tk.StringVar()
        self.buscarEvaluacionAlumno=tk.StringVar()

        opcionesBusqueda1=("1","2","3")
         
        self.comoboxTri=ttk.Combobox(frameBuscar,
                                width=20,
                                textvariable=self.buscarTrimestretxt,
                                values=opcionesBusqueda1,
                                state='readonly',
                                font=("Times New Roman",10))
        self.comoboxTri.current(0)
        self.comoboxTri.grid(row=0,column=1)

        EntryFecha=ttk.Entry(frameBuscar,textvariable=self.buscarfechatxt,width=18,font=("Times New Roman",10))
        EntryFecha.grid(row=1,column=1,padx=1,pady=3)

        self.opcionEvaluacionAlumno=tk.StringVar()
        opcionesBusqueda=("Cátedra","Cédula","Fecha","Tres Trimestres")
         
        self.comoboxEVAL=ttk.Combobox(frameBuscar,
                                width=20,
                                textvariable=self.opcionEvaluacionAlumno,
                                values=opcionesBusqueda,
                                state='readonly',
                                font=("Times New Roman",10))
        self.comoboxEVAL.current(1)
        self.comoboxEVAL.grid(row=2,column=1)

        btnBuscar2=tk.Button(frameBuscar,text="Buscar",command=self.searchEvalaucionCLases,font=("Times New Roman",10),width=15)
        btnBuscar2.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnBuscar2.grid(row=0,column=2,padx=20,pady=3)

        btnLimpiar2=tk.Button(frameBuscar,text="Limpiar",command=self.clearListaEvaluacionClases,font=("Times New Roman",10),width=15)
        btnLimpiar2.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnLimpiar2.grid(row=2,column=2,padx=20,pady=3)

        #### Frame Logo

        self.frameLogo=tk.Frame(self.ventana2,bg="light blue",width=180,height=180)
        self.frameLogo.place(x=953, y= 380)

        self.imagen=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\Documento.png")
        fondo=tk.Label(self.frameLogo,image=self.imagen,bg="light cyan").place(x=0,y=0)

        ##################### label frame opciones

        labelopcionesFrame=tk.LabelFrame(self.ventana2,text="Opciones",bg="light cyan",width=191,height=298,font=("Times New Roman",10))
        labelopcionesFrame.place(x=950,y=250)
        ####################### Botones asignar, modificar, promedio y Vover

        btnmodificar=tk.Button(labelopcionesFrame,text="Modificar",command=self.modificar_evaluacion,font=("Times New Roman",14),width=15)
        btnmodificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnmodificar.grid(row=0,column=0,padx=5,pady=10)

        btnVolver=tk.Button(labelopcionesFrame,text="Volver",command=self.volver_moduloClase,font=("Times New Roman",14),width=15)
        btnVolver.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnVolver.grid(row=4,column=0,padx=5,pady=10)
     
############### Funciones Clear y update lista clases

    def get_row_ClasesBuscadorEvaluacion(self,event):
        rowid=self.treeClases.identify_row(event.y)
        self.treeClases.selection_set(rowid)
        item=self.treeClases.item(self.treeClases.focus())
        self.cedula_profeD=item["text"]
        self.ListaTree=item["values"]
        claseID=str(self.ListaTree[0])
        catedra=self.ListaTree[1]
        programa=self.ListaTree[2]
        ############ Busca la informacion en la base de datos

        query2="SELECT a.cedula_identidad, a.nombres, a.apellidos FROM profesor a, clase b WHERE a.cedula_identidad=b.cedula_identidad AND a.cedula_identidad='"+self.cedula_profeD+"' AND b.id_clase='"+claseID+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query2)
        respuesta=cursor.fetchall() 
        cone.close()

        if len(respuesta)>0:
            self.idClasetext.set(claseID)
            self.catedratext.set(catedra)
            self.programatxt.set(programa)
            self.cedulatext.set(respuesta[0][0])
            self.nombresproftext.set(respuesta[0][1])
            self.apellidosproxtext.set(respuesta[0][2])
    
    def updateListaClasesListaEv(self,respuesta):
        info=self.treeClases.get_children()

        for elemento in info:
            self.treeClases.delete(elemento)
        for row in respuesta:
            self.treeClases.insert("",0,text=row[0],values=(row[1],row[2],row[3]))

    def clearListaClasesTree(self):
        query="SELECT a.cedula_identidad, a.id_clase, a.catedra, b.nombre_programa FROM clase a, programa b WHERE a.id_programa=b.id_programa"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.buscador1.set("")
        self.updateListaClasesListaEv(respuesta)

    def searchClasesenEv(self):
        opcioncontrol=self.comobox1.get()
        buscarLista=self.buscador1.get()
        opcionPrograma=self.comobox2.get()
        if opcioncontrol=="Cátedra":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cedula_identidad, a.id_clase, a.catedra, b.nombre_programa FROM clase a, programa b WHERE a.id_programa=b.id_programa AND a.catedra LIKE '%"+buscarLista+"%' AND b.nombre_programa='"+opcionPrograma+"'"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaClasesListaEv(respuesta)

        if opcioncontrol=="Cédula":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cedula_identidad, a.id_clase, a.catedra, b.nombre_programa FROM clase a, programa b WHERE a.id_programa=b.id_programa AND a.cedula_identidad LIKE '%"+buscarLista+"%' AND b.nombre_programa='"+opcionPrograma+"'"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaClasesListaEv(respuesta)      

################# Funciones Clear y update lista Evaluacion Clase
    
    def get_row_Evaluacion_Clases(self,event):
        rowid=self.tree.identify_row(event.y)
        self.tree.selection_set(rowid)
        item=self.tree.item(self.tree.focus())
        self.cod_alumno=item["text"]
        self.ListaTree=item["values"]
        claseID=str(self.ListaTree[1])
        catedra=self.ListaTree[2]
        programa=self.ListaTree[3]
        fecha=self.ListaTree[7]
        trimestre=self.ListaTree[8]
        ############ Busca la informacion en la base de datos

        query2="SELECT a.cedula_identidad, a.nombres, a.apellidos FROM profesor a, clase b WHERE a.cedula_identidad=b.cedula_identidad AND b.id_clase='"+claseID+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query2)
        respuesta=cursor.fetchall() 
        cone.close()

        if len(respuesta)>0:
            self.idClasetext.set(claseID)
            self.catedratext.set(catedra)
            self.programatxt.set(programa)
            self.cedulatext.set(respuesta[0][0])
            self.nombresproftext.set(respuesta[0][1])
            self.apellidosproxtext.set(respuesta[0][2])

            self.buscarfechatxt.set(fecha)
            self.buscarTrimestretxt.set(trimestre)
    
    def updateListaEvClase(self,respuesta):
        info=self.tree.get_children()

        for elemento in info:
            self.tree.delete(elemento)
        for row in respuesta:
            self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))

    def clearListaEvaluacionClases(self):
        query="SELECT a.cod_alumno, b.id_evaluacion, c.id_clase, e.catedra, d.nombre_programa, a.nombres, a.apellidos, b.nota, c.fecha, c.trimestre FROM alumno a, evaluacion_alumno b, evaluacion c, programa d, clase e WHERE a.cod_alumno=b.cod_alumno AND c.id_evaluacion=b.id_evaluacion AND d.id_programa=e.id_programa AND e.id_clase=c.id_clase"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.idClasetext.set("")
        self.catedratext.set("")
        self.programatxt.set("")
        self.cedulatext.set("")
        self.nombresproftext.set("")
        self.apellidosproxtext.set("")
        self.buscarfechatxt.set("")
        self.updateListaEvClase(respuesta)

    def searchEvalaucionCLases(self):
        opcioncontrol=self.opcionEvaluacionAlumno.get()
        trimestre=self.buscarTrimestretxt.get()
        fecha=self.buscarfechatxt.get()
        catedra=self.catedratext.get()
        programa=self.programatxt.get()
        cedula=self.cedulatext.get()
        
        if opcioncontrol=="Cátedra":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, b.id_evaluacion, c.id_clase, e.catedra, d.nombre_programa, a.nombres, a.apellidos, b.nota, c.fecha, c.trimestre FROM alumno a, evaluacion_alumno b, evaluacion c, programa d, clase e WHERE a.cod_alumno=b.cod_alumno AND c.id_evaluacion=b.id_evaluacion AND d.id_programa=e.id_programa AND e.id_clase=c.id_clase AND e.catedra LIKE '%"+catedra+"%' AND d.nombre_programa='"+programa+"' AND c.trimestre="+trimestre+" "
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaEvClase(respuesta)

        if opcioncontrol=="Cédula":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, b.id_evaluacion, c.id_clase, e.catedra, d.nombre_programa, a.nombres, a.apellidos, b.nota, c.fecha, c.trimestre FROM alumno a, evaluacion_alumno b, evaluacion c, programa d, clase e WHERE a.cod_alumno=b.cod_alumno AND c.id_evaluacion=b.id_evaluacion AND d.id_programa=e.id_programa AND e.id_clase=c.id_clase AND e.cedula_identidad LIKE '%"+cedula+"%' AND d.nombre_programa='"+programa+"' AND c.trimestre="+trimestre+" "
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaEvClase(respuesta) 

        if opcioncontrol=="Fecha":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, b.id_evaluacion, c.id_clase, e.catedra, d.nombre_programa, a.nombres, a.apellidos, b.nota, c.fecha, c.trimestre FROM alumno a, evaluacion_alumno b, evaluacion c, programa d, clase e WHERE a.cod_alumno=b.cod_alumno AND c.id_evaluacion=b.id_evaluacion AND d.id_programa=e.id_programa AND e.id_clase=c.id_clase AND c.fecha LIKE '%"+fecha+"%' AND d.nombre_programa='"+programa+"' AND c.trimestre="+trimestre+" "
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaEvClase(respuesta) 

        if opcioncontrol=="Tres Trimestres":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, b.id_evaluacion, c.id_clase, e.catedra, d.nombre_programa, a.nombres, a.apellidos, b.nota, c.fecha, c.trimestre FROM alumno a, evaluacion_alumno b, evaluacion c, programa d, clase e WHERE a.cod_alumno=b.cod_alumno AND c.id_evaluacion=b.id_evaluacion AND d.id_programa=e.id_programa AND e.id_clase=c.id_clase AND e.catedra LIKE '%"+catedra+"%' AND d.nombre_programa='"+programa+"' "
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaEvClase(respuesta)

################# opciones gestion evaluacion

    def modificar_evaluacion(self):
        try:
            
            self.ventana2.destroy()
            self.ventana1=tk.Tk()
            self.ventana1.title("Modificar Evaluación")
            self.ventana1.config(bg='dark blue')
            self.ventana1.geometry("960x550")
            self.ventana1.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")

                ###########------------------- Formulario label frame

            ##########Búsqueda de información por Clase, programa y trimestre
            self.labelframebusquedaClaseProfe=tk.LabelFrame(self.ventana1,text="Información y búsqueda",bg="light cyan",width=930,height=340)
            self.labelframebusquedaClaseProfe.place(x=12,y=0)

            frameTablaCLases=tk.Frame(self.labelframebusquedaClaseProfe,bg="light cyan",width=70)
            frameTablaCLases.place(x=5,y=10)

            self.treeClases = ttk.Treeview(frameTablaCLases,columns=("#1","#2","#3"),height="5")
            self.treeClases.heading("#0",text="Cédula identidad")
            self.treeClases.heading("#1",text="Id clase")
            self.treeClases.heading("#2",text="Cátera")
            self.treeClases.heading("#3",text="Programa")

            self.treeClases.column("#0",width=90)
            self.treeClases.column("#1",width=90)
            self.treeClases.column("#2",width=150)
            self.treeClases.column("#3",width=150)

            self.treeClases.bind("<1>",self.get_row_ClasesBuscadorEvaluacion)
            self.treeClases.pack(side="left")


            # SCROLL VERTICAL TREEVIEW
            scrolvert = st.Scrollbar(frameTablaCLases, orient="vertical", command = self.treeClases.yview)
            scrolvert.pack(side="left",fill="y")
            self.treeClases.config(yscrollcommand=scrolvert.set)

            con=mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="", 
                                        database="bdnucleolecheria")

            cur=con.cursor()
            profesor=self.treeClases.get_children()

            for elemento in profesor:
                self.treeClases.delete(elemento)
            try:
                cur.execute("SELECT a.cedula_identidad, a.id_clase, a.catedra, b.nombre_programa FROM clase a, programa b WHERE a.id_programa=b.id_programa")
                rows=cur.fetchall()
                for row in rows:
                    self.treeClases.insert("",0,text=row[0],values=(row[1],row[2],row[3]))
            except:
                pass

            frameBuscadordeClases=tk.LabelFrame(self.labelframebusquedaClaseProfe,text="Buscador",bg="light cyan",width=491,height=124)
            frameBuscadordeClases.place(x=5,y=162)

            ######## Buscador clases
            label1=tk.Label(frameBuscadordeClases,text="Consulta por:",bg="Light cyan",font=("Times New Roman",10))
            label1.grid(row=1,column=0,padx=5,pady=5)

            self.buscador1=tk.StringVar()
            self.entry1=tk.Entry(frameBuscadordeClases,width=30,textvariable=self.buscador1,font=("Times New Roman",10))
            self.entry1.grid(row=4,column=1,padx=5,pady=5)

            self.labelprograma=tk.Label(frameBuscadordeClases,text="Programa:",bg="Light cyan",font=("Times New Roman",10))
            self.labelprograma.grid(row=2,column=0,padx=5,pady=5)

            ############### Combobox interactivo

            self.opcionPrograma=tk.StringVar()
            self.comobox2=ttk.Combobox(frameBuscadordeClases,
                                    width=20,
                                    textvariable=self.opcionPrograma,
                                    state='readonly',
                                    font=("Times New Roman",10))

            self.comobox2['value']=self.cargarComboProgramas()
            self.comobox2.current(0)
            self.comobox2.grid(row=2,column=1,padx=5,pady=1)

            #################################################################

            lableBucar=tk.Label(frameBuscadordeClases,text="Buscar:",bg="Light cyan",font=("Times New Roman",10))
            lableBucar.grid(row=4,column=0,padx=5,pady=5)

            self.opcion=tk.StringVar()
            opcionesBusqueda=("Cátedra","Cédula")
            
            self.comobox1=ttk.Combobox(frameBuscadordeClases,
                                    width=20,
                                    textvariable=self.opcion,
                                    values=opcionesBusqueda,
                                    state='readonly',
                                    font=("Times New Roman",10))
            self.comobox1.current(1)

        
            self.comobox1.grid(row=1,column=1)

            btnBuscar=tk.Button(frameBuscadordeClases,text="Buscar",command=self.searchClasesenEv,font=("Times New Roman",10),width=15)
            btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnBuscar.grid(row=1,column=2,padx=5,pady=5)

            btnLimpiar=tk.Button(frameBuscadordeClases,text="Limpiar",command=self.clearListaClasesTree,font=("Times New Roman",10),width=15)
            btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnLimpiar.grid(row=2,column=2,padx=5,pady=5)

            ################# Frame decorativo

            decoframe=tk.Frame(self.labelframebusquedaClaseProfe,bg="dark blue",width=79,height=154)
            decoframe.place(x=422,y=152)

            #######################################################
            ############ Buscador lista evaluacion_alumno##########

            labelframeBuscadorAlumnoEvaluacion=tk.LabelFrame(self.labelframebusquedaClaseProfe,text="Selección",bg="light cyan",width=410,height=309)
            labelframeBuscadorAlumnoEvaluacion.place(x=508,y=0)

            frameSeleccion=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="light cyan",width=380,height=190)
            frameSeleccion.place(x=0,y=0)


            ############# Label column 0

            labelIdClase=tk.Label(frameSeleccion,text="Id clase:",bg="light cyan")
            labelIdClase.grid(row=1,column=0,padx=1,pady=10)

            labelcatedra=tk.Label(frameSeleccion,text="Cátedra:",bg="light cyan")
            labelcatedra.grid(row=2,column=0,padx=1,pady=10)

            labelPrograma=tk.Label(frameSeleccion,text="Programa:",bg="light cyan")
            labelPrograma.grid(row=3,column=0,padx=1,pady=10)

            ############## label column 2
            labelCedula=tk.Label(frameSeleccion,text="Cédula Identidad:",bg="light cyan")
            labelCedula.grid(row=1,column=2,padx=1,pady=10)

            labelNombreProf=tk.Label(frameSeleccion,text="Nombre Profesor:",bg="light cyan")
            labelNombreProf.grid(row=2,column=2,padx=1,pady=10)

            labelapellidoProf=tk.Label(frameSeleccion,text="Apellido Profesor:",bg="light cyan")
            labelapellidoProf.grid(row=3,column=2,padx=1,pady=10)

            ############### Entry column 1
            self.idClasetext=tk.StringVar()
            self.catedratext=tk.StringVar()
            self.programatxt=tk.StringVar()
            self.cedulatext=tk.StringVar()
            self.nombresproftext=tk.StringVar()
            self.apellidosproxtext=tk.StringVar()

            EntryIdClase=ttk.Entry(frameSeleccion,textvariable=self.idClasetext,width=18,state='readonly')
            EntryIdClase.grid(row=1,column=1,padx=1,pady=10)

            Entrycatedra=ttk.Entry(frameSeleccion,textvariable=self.catedratext,width=18,state='readonly')
            Entrycatedra.grid(row=2,column=1,padx=1,pady=10)

            EntryPrograma=ttk.Entry(frameSeleccion,textvariable=self.programatxt,width=18,state='readonly')
            EntryPrograma.grid(row=3,column=1,padx=1,pady=10)

            ############ Entry column 3
            EntryCedula=ttk.Entry(frameSeleccion,textvariable=self.cedulatext,width=18,state='readonly')
            EntryCedula.grid(row=1,column=3,padx=1,pady=10)

            EntryNombreProf=ttk.Entry(frameSeleccion,textvariable=self.nombresproftext,width=18,state='readonly')
            EntryNombreProf.grid(row=2,column=3,padx=1,pady=10)

            EntryapellidoProf=ttk.Entry(frameSeleccion,textvariable=self.apellidosproxtext,width=18,state='readonly')
            EntryapellidoProf.grid(row=3,column=3,padx=1,pady=10)

            ############### Frame deco linera

            frameLinea=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="dark blue",width=385,height=7)
            frameLinea.place(x=5,y=129)

            frameBuscar=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="light cyan",width=386,height=105)
            frameBuscar.place(x=5,y=151)

            ############ Label

            labelTrimestre=tk.Label(frameBuscar,text="Trimestre:",bg="light cyan")
            labelTrimestre.grid(row=0,column=0,padx=1,pady=3)

            labelNombreProf=tk.Label(frameBuscar,text="Fecha:",bg="light cyan")
            labelNombreProf.grid(row=1,column=0,padx=1,pady=3)

            labelapellidoProf=tk.Label(frameBuscar,text="(*)Id evaluación:",bg="light cyan")
            labelapellidoProf.grid(row=2,column=0,padx=1,pady=3)


            ################ Entry y combobox
            self.buscarTrimestretxt=tk.StringVar()
            self.buscarfechatxt=tk.StringVar()
            self.buscarEvaluacionAlumno=tk.StringVar()
            self.txtIdEvaluacion=tk.StringVar()

            opcionesBusqueda1=("1","2","3")
            
            self.comoboxTri=ttk.Combobox(frameBuscar,
                                    width=20,
                                    textvariable=self.buscarTrimestretxt,
                                    values=opcionesBusqueda1,
                                    state='readonly',
                                    font=("Times New Roman",10))
            self.comoboxTri.current(0)
            self.comoboxTri.grid(row=0,column=1)

            EntryFecha=ttk.Entry(frameBuscar,textvariable=self.buscarfechatxt,width=18)
            EntryFecha.grid(row=1,column=1,padx=1,pady=3)

            
            EntryIdevaluacion=ttk.Entry(frameBuscar,textvariable=self.txtIdEvaluacion,width=18)
            EntryIdevaluacion.grid(row=2,column=1,padx=1,pady=3)

            btnAgregar=tk.Button(frameBuscar,text="Agregar",command=self.add_new_Evaluaciones,font=("Times New Roman",10),width=15)
            btnAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnAgregar.grid(row=0,column=2,padx=20,pady=3)

            btnmodificar=tk.Button(frameBuscar,text="Modificar",command=self.update_Evaluaciones,font=("Times New Roman",10),width=15)
            btnmodificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnmodificar.grid(row=1,column=2,padx=20,pady=3)

            btnEliminar=tk.Button(frameBuscar,text="Eliminar",command=self.delete_Evaluaciones,font=("Times New Roman",10),width=15)
            btnEliminar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnEliminar.grid(row=2,column=2,padx=20,pady=3)

            ##################### label frame opciones

            #############################Tabla evaluaciones

            self.labelframeEvaluacionesPLa=tk.LabelFrame(self.ventana1,text="Tabla evaluación",fg="white",bg="dark blue",width=725,height=190)
            self.labelframeEvaluacionesPLa.place(x=12,y=346)

            frameTablaEvaluaciones=tk.Frame(self.labelframeEvaluacionesPLa,bg="light cyan",width=70)
            frameTablaEvaluaciones.place(x=5,y=10)

            self.treeEvaluacion = ttk.Treeview(frameTablaEvaluaciones,columns=("#1","#2","#3","#4","#5","#6"),height="6")
            self.treeEvaluacion.heading("#0",text="id evaluación")
            self.treeEvaluacion.heading("#1",text="Id clase")
            self.treeEvaluacion.heading("#2",text="Cátera")
            self.treeEvaluacion.heading("#3",text="Programa")
            self.treeEvaluacion.heading("#4",text="Fecha")
            self.treeEvaluacion.heading("#5",text="Trimestre")
            self.treeEvaluacion.heading("#6",text="Cédula Identidad")

            self.treeEvaluacion.column("#0",width=90)
            self.treeEvaluacion.column("#1",width=90)
            self.treeEvaluacion.column("#2",width=130)
            self.treeEvaluacion.column("#3",width=130)
            self.treeEvaluacion.column("#4",width=90)
            self.treeEvaluacion.column("#5",width=70)
            self.treeEvaluacion.column("#6",width=90)

            self.treeEvaluacion.bind("<1>",self.get_row_Evaluaciones)
            self.treeEvaluacion.pack(side="left")


            # SCROLL VERTICAL TREEVIEW
            scrolvert = st.Scrollbar(frameTablaEvaluaciones, orient="vertical", command = self.treeEvaluacion.yview)
            scrolvert.pack(side="left",fill="y")
            self.treeEvaluacion.config(yscrollcommand=scrolvert.set)

            con=mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="", 
                                        database="bdnucleolecheria")

            cur=con.cursor()
            profesor=self.treeEvaluacion.get_children()

            for elemento in profesor:
                self.treeEvaluacion.delete(elemento)
            try:
                cur.execute("SELECT c.id_evaluacion, c.id_clase, a.catedra, b.nombre_programa, c.fecha, c.trimestre, c.cedula_identidad FROM clase a, programa b, evaluacion c WHERE a.id_programa=b.id_programa AND c.id_clase=a.id_clase")
                rows=cur.fetchall()
                for row in rows:
                    self.treeEvaluacion.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6]))
            except:
                pass
        
            self.labelframeOpciones=tk.LabelFrame(self.ventana1,text="Opciones",fg="white",bg="dark blue",width=206,height=73)
            self.labelframeOpciones.place(x=740,y=346)

            btnVolver=tk.Button(self.labelframeOpciones,text="Volver",command=self.evaluaciones,font=("Times New Roman",14),width=15)
            btnVolver.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnVolver.place(x=14,y=5)

           
            self.ventana1.mainloop()
        except:
            pass

##################### Funciones tree evaluacion
  
    def get_row_Evaluaciones(self,event):
        rowid=self.treeEvaluacion.identify_row(event.y)
        self.treeEvaluacion.selection_set(rowid)
        item=self.treeEvaluacion.item(self.treeEvaluacion.focus())
        self.id_evaluacion=item["text"]
        self.ListaTree=item["values"]
        self.claseID=str(self.ListaTree[0])
        catedra=self.ListaTree[1]
        programa=self.ListaTree[2]
        fecha=self.ListaTree[3]
        trimestre=self.ListaTree[4]
        ############ Busca la informacion en la base de datos

        query2="SELECT a.cedula_identidad, a.nombres, a.apellidos FROM profesor a, clase b WHERE a.cedula_identidad=b.cedula_identidad AND b.id_clase='"+self.claseID+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query2)
        respuesta=cursor.fetchall() 
        cone.close()

        if len(respuesta)>0:
            self.txtIdEvaluacion.set(self.id_evaluacion)
            self.idClasetext.set(self.claseID)
            self.catedratext.set(catedra)
            self.programatxt.set(programa)
            self.cedulatext.set(respuesta[0][0])
            self.nombresproftext.set(respuesta[0][1])
            self.apellidosproxtext.set(respuesta[0][2])

            self.buscarfechatxt.set(fecha)
            self.buscarTrimestretxt.set(trimestre)
    
    def updateListaEvaluacion(self,respuesta):
        info=self.treeEvaluacion.get_children()

        for elemento in info:
            self.treeEvaluacion.delete(elemento)
        for row in respuesta:
            self.treeEvaluacion.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6]))

    def clearListaEvaluacion(self):
        query="SELECT c.id_evaluacion, c.id_clase, a.catedra, b.nombre_programa, c.fecha, c.trimestre, c.cedula_identidad FROM clase a, programa b, evaluacion c WHERE a.id_programa=b.id_programa AND c.id_clase=a.id_clase"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.updateListaEvaluacion(respuesta)

    ############## Funciones agregar, modificar y eliminar

    def add_new_Evaluaciones (self):
        idEvaluacion=self.txtIdEvaluacion.get()
        idclase=self.idClasetext.get()
        fecha=self.buscarfechatxt.get()
        trimestre=self.buscarTrimestretxt.get()
        cedula=self.cedulatext.get()
        try:
            if self.validar_contrasena(idEvaluacion):
                
                query="INSERT INTO evaluacion(id_evaluacion,fecha,id_clase,trimestre,cedula_identidad) VALUES(%s,%s,%s,%s,%s)"

                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(idEvaluacion,fecha,idclase,trimestre,cedula))
                
                cone.commit()
                cone.close()
                self.clearListaEvaluacion()
                
                mb.showinfo("Información","Se han cargado con éxito los datos.")
                self.idClasetext.set("")
                self.catedratext.set("")
                self.programatxt.set("")
                self.cedulatext.set("")
                self.nombresproftext.set("")
                self.apellidosproxtext.set("")
                self.buscarfechatxt.set("")
            else:
                mb.showwarning("Error","Debe completar los campos obligatorios (*)")
        except:
            mb.showinfo("Información","Este dato ya existe")

    def update_Evaluaciones(self):
        idEvaluacion=self.txtIdEvaluacion.get()
        idclase=self.idClasetext.get()
        fecha=self.buscarfechatxt.get()
        trimestre=self.buscarTrimestretxt.get()
        cedula=self.cedulatext.get()

        if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea actualizar estos datos? "):
            if self.validar_contrasena(idEvaluacion):
            
                query="UPDATE evaluacion SET id_evaluacion=%s, fecha=%s, id_clase=%s, trimestre=%s, cedula_identidad=%s WHERE id_clase = '"+self.claseID+"' AND id_evaluacion='"+self.id_evaluacion+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(idEvaluacion,fecha,idclase,trimestre,cedula))
                

                cone.commit()
                cone.close()

                self.clearListaEvaluacion()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han cargado con éxito los datos.")
                    self.idClasetext.set("")
                    self.catedratext.set("")
                    self.programatxt.set("")
                    self.cedulatext.set("")
                    self.nombresproftext.set("")
                    self.apellidosproxtext.set("")
                    self.buscarfechatxt.set("")
                else:
                    mb.showinfo("Informacion", "No existe un campo con dicha informacion")
                
            else:
                mb.showwarning("Error","Debe seleccionar los campos a modificar")
        else:
            return True

    def delete_Evaluaciones(self):
        idEvaluacion=self.txtIdEvaluacion.get()
        cedula=self.cedulatext.get()
        try:
            if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea borrar estos datos? "):
                query="DELETE FROM evaluacion WHERE id_evaluacion='"+idEvaluacion+"' AND cedula_identidad='"+cedula+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query)
                
                cone.commit()
                cone.close()
                self.clearListaEvaluacion()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han borrado los datos con éxito.")
                    self.idClasetext.set("")
                    self.catedratext.set("")
                    self.programatxt.set("")
                    self.cedulatext.set("")
                    self.nombresproftext.set("")
                    self.apellidosproxtext.set("")
                    self.buscarfechatxt.set("")
                else:
                    mb.showinfo("Informacion", "No existe un alumno con dicha informacion")
            else:
                return True
        except:
                mb.showwarning("Error","Introduzca la informacion que desee borrar o selecione en la tabla instrumentos asignados.")
   
    ########## Modulo Promedio

    def asistencia(self):
        self.ventana1.destroy()
        self.ventana2=tk.Tk()
        self.ventana2.title("Asistencia")
        self.ventana2.config(bg='Light cyan')
        self.ventana2.geometry("1150x650")
        self.ventana2.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")

        #### Frame Logo

        self.frameLogo=tk.Frame(self.ventana2,bg="light blue",width=187,height=251)
        self.frameLogo.place(x=945, y= 150)

        self.imagen=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\Libros.png")
        fondo=tk.Label(self.frameLogo,image=self.imagen,bg="light cyan").place(x=0,y=0)

        self.decoraframe=tk.Frame(self.ventana2,bg="dark blue",height=190)
        self.decoraframe.pack(fill="both",expand="no",side="bottom")

        self.decoFrameabajo=tk.Frame(self.ventana2,bg="dark blue",height=90)
        self.decoFrameabajo.pack(fill="both",expand="no",side="top")

        self.lista=tk.LabelFrame(self.decoraframe,text="Asistencias Registradas",fg="white",font=("Times New Roman",10))
        self.lista.config(bg="dark blue")
        self.lista.pack(expand="no",padx=5,pady=5,ipady=10,side="top")

        self.tree = ttk.Treeview(self.lista,columns=("#1","#2","#3","#4","#5","#6","#7","#8","#9","#10","#11"),height="7")
        self.tree.heading("#0",text="Nro Asistencia")
        self.tree.heading("#1",text="Programa")
        self.tree.heading("#2",text="Id_clase")
        self.tree.heading("#3",text="Cátedra")
        self.tree.heading("#4",text="Fecha")
        self.tree.heading("#5",text="Hora inicio")
        self.tree.heading("#6",text="Hora Final")
        self.tree.heading("#7",text="Cod Alumno")
        self.tree.heading("#8",text="Cédula Alumno")
        self.tree.heading("#9",text="Nombres")
        self.tree.heading("#10",text="Apellidos")
        self.tree.heading("#11",text="Presente/Ausente")
        

        self.tree.column("#0",width=90)
        self.tree.column("#1",width=140)
        self.tree.column("#2",width=80)
        self.tree.column("#3",width=70)
        self.tree.column("#4",width=65)
        self.tree.column("#5",width=65)
        self.tree.column("#6",width=65)
        self.tree.column("#7",width=90)
        self.tree.column("#8",width=110)
        self.tree.column("#9",width=110)
        self.tree.column("#10",width=90)
        self.tree.column("#11",width=90)

        self.tree.bind("<1>",self.get_row_Asistencia)
        self.tree.pack(side="left",fill="both",padx=5,pady=5)


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(self.lista, orient="vertical", command = self.tree.yview)
        scrolvert.pack(side="left",fill="y")
        self.tree.config(yscrollcommand=scrolvert.set)
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.tree.get_children()

        for elemento in profesor:
            self.tree.delete(elemento)
        try:
            cur.execute("SELECT a.id_asistencia, d.nombre_programa, c.id_clase, c.Catedra, a.fecha, a.hora_inicio, a.hora_final, b.cod_alumno, f.ci_alumno, f.nombres, f.apellidos, b.ausente_presente FROM asistencia a, alumno_asistencia b,clase c,programa d,alumno f WHERE a.id_asistencia=b.id_asistencia AND a.id_clase=c.id_clase AND d.id_programa=a.id_programa AND b.cod_alumno=f.cod_alumno")
            rows=cur.fetchall()
            for row in rows:
                self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
        except:
            pass

        ##########Búsqueda de información por Clase, programa y trimestre
        self.labelframebusquedaClaseProfe=tk.LabelFrame(self.ventana2,text="Información y búsqueda",bg="light cyan",width=930,height=340,font=("Times New Roman",10))
        self.labelframebusquedaClaseProfe.place(x=12,y=60)

        frameTablaCLases=tk.Frame(self.labelframebusquedaClaseProfe,bg="light cyan",width=70)
        frameTablaCLases.place(x=5,y=10)

        self.treeClases = ttk.Treeview(frameTablaCLases,columns=("#1","#2","#3"),height="5")
        self.treeClases.heading("#0",text="Cédula identidad")
        self.treeClases.heading("#1",text="Id clase")
        self.treeClases.heading("#2",text="Cátera")
        self.treeClases.heading("#3",text="Programa")

        self.treeClases.column("#0",width=90)
        self.treeClases.column("#1",width=90)
        self.treeClases.column("#2",width=150)
        self.treeClases.column("#3",width=150)

        self.treeClases.bind("<1>",self.get_row_ClasesBuscadorEvaluacion)
        self.treeClases.pack(side="left")


        # SCROLL VERTICAL TREEVIEW
        scrolvert = st.Scrollbar(frameTablaCLases, orient="vertical", command = self.treeClases.yview)
        scrolvert.pack(side="left",fill="y")
        self.treeClases.config(yscrollcommand=scrolvert.set)

        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="", 
                                    database="bdnucleolecheria")

        cur=con.cursor()
        profesor=self.treeClases.get_children()

        for elemento in profesor:
            self.treeClases.delete(elemento)
        try:
            cur.execute("SELECT a.cedula_identidad, a.id_clase, a.catedra, b.nombre_programa FROM clase a, programa b WHERE a.id_programa=b.id_programa")
            rows=cur.fetchall()
            for row in rows:
                self.treeClases.insert("",0,text=row[0],values=(row[1],row[2],row[3]))
        except:
            pass

        frameBuscadordeClases=tk.LabelFrame(self.labelframebusquedaClaseProfe,text="Buscador",bg="light cyan",width=491,height=124,font=("Times New Roman",10))
        frameBuscadordeClases.place(x=5,y=162)

        ######## Buscador clases
        label1=tk.Label(frameBuscadordeClases,text="Consulta por:",bg="Light cyan",font=("Times New Roman",10))
        label1.grid(row=1,column=0,padx=5,pady=5)

        self.buscador1=tk.StringVar()
        self.entry1=tk.Entry(frameBuscadordeClases,width=30,textvariable=self.buscador1,font=("Times New Roman",10))
        self.entry1.grid(row=4,column=1,padx=5,pady=5)

        self.labelprograma=tk.Label(frameBuscadordeClases,text="Programa:",bg="Light cyan",font=("Times New Roman",10))
        self.labelprograma.grid(row=2,column=0,padx=5,pady=5)

        ############### Combobox interactivo

        self.opcionPrograma=tk.StringVar()
        self.comobox2=ttk.Combobox(frameBuscadordeClases,
                                width=20,
                                textvariable=self.opcionPrograma,
                                state='readonly',
                                font=("Times New Roman",10))

        self.comobox2['value']=self.cargarComboProgramas()
        self.comobox2.current(0)
        self.comobox2.grid(row=2,column=1,padx=5,pady=1)

        #################################################################

        lableBucar=tk.Label(frameBuscadordeClases,text="Buscar:",bg="Light cyan",font=("Times New Roman",10))
        lableBucar.grid(row=4,column=0,padx=5,pady=5)

        self.opcion=tk.StringVar()
        opcionesBusqueda=("Cátedra","Cédula")
         
        self.comobox1=ttk.Combobox(frameBuscadordeClases,
                                width=20,
                                textvariable=self.opcion,
                                values=opcionesBusqueda,
                                state='readonly',
                                font=("Times New Roman",10))
        self.comobox1.current(1)

       
        self.comobox1.grid(row=1,column=1)

        btnBuscar=tk.Button(frameBuscadordeClases,text="Buscar",command=self.searchClasesenEv,font=("Times New Roman",10),width=15)
        btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnBuscar.grid(row=1,column=2,padx=5,pady=5)

        btnLimpiar=tk.Button(frameBuscadordeClases,text="Limpiar",command=self.clearListaClasesTree,font=("Times New Roman",10),width=15)
        btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnLimpiar.grid(row=2,column=2,padx=5,pady=5)

        ################# Frame decorativo

        decoframe=tk.Frame(self.labelframebusquedaClaseProfe,bg="dark blue",width=79,height=154)
        decoframe.place(x=422,y=152)

        #######################################################
        ############ Buscador lista evaluacion_alumno##########

        labelframeBuscadorAlumnoEvaluacion=tk.LabelFrame(self.labelframebusquedaClaseProfe,text="Selección",bg="light cyan",width=410,height=309,font=("Times New Roman",10))
        labelframeBuscadorAlumnoEvaluacion.place(x=508,y=0)

        frameSeleccion=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="light cyan",width=380,height=190)
        frameSeleccion.place(x=0,y=0)

        ############# Label column 0

        labelIdClase=tk.Label(frameSeleccion,text="Id clase:",bg="light cyan",font=("Times New Roman",10))
        labelIdClase.grid(row=1,column=0,padx=1,pady=10)

        labelcatedra=tk.Label(frameSeleccion,text="Cátedra:",bg="light cyan",font=("Times New Roman",10))
        labelcatedra.grid(row=2,column=0,padx=1,pady=10)

        labelPrograma=tk.Label(frameSeleccion,text="Programa:",bg="light cyan",font=("Times New Roman",10))
        labelPrograma.grid(row=3,column=0,padx=1,pady=10)

        ############## label column 2
        labelCedula=tk.Label(frameSeleccion,text="Cédula Identidad:",bg="light cyan",font=("Times New Roman",10))
        labelCedula.grid(row=1,column=2,padx=1,pady=10)

        labelNombreProf=tk.Label(frameSeleccion,text="Nombre Profesor:",bg="light cyan",font=("Times New Roman",10))
        labelNombreProf.grid(row=2,column=2,padx=1,pady=10)

        labelapellidoProf=tk.Label(frameSeleccion,text="Apellido Profesor:",bg="light cyan",font=("Times New Roman",10))
        labelapellidoProf.grid(row=3,column=2,padx=1,pady=10)

        ############### Entry column 1
        self.idClasetext=tk.StringVar()
        self.catedratext=tk.StringVar()
        self.programatxt=tk.StringVar()
        self.cedulatext=tk.StringVar()
        self.nombresproftext=tk.StringVar()
        self.apellidosproxtext=tk.StringVar()

        EntryIdClase=ttk.Entry(frameSeleccion,textvariable=self.idClasetext,width=18,state='readonly',font=("Times New Roman",10))
        EntryIdClase.grid(row=1,column=1,padx=1,pady=10)

        Entrycatedra=ttk.Entry(frameSeleccion,textvariable=self.catedratext,width=18,state='readonly',font=("Times New Roman",10))
        Entrycatedra.grid(row=2,column=1,padx=1,pady=10)

        EntryPrograma=ttk.Entry(frameSeleccion,textvariable=self.programatxt,width=18,state='readonly',font=("Times New Roman",10))
        EntryPrograma.grid(row=3,column=1,padx=1,pady=10)

        ############ Entry column 3
        EntryCedula=ttk.Entry(frameSeleccion,textvariable=self.cedulatext,width=18,state='readonly',font=("Times New Roman",10))
        EntryCedula.grid(row=1,column=3,padx=1,pady=10)

        EntryNombreProf=ttk.Entry(frameSeleccion,textvariable=self.nombresproftext,width=18,state='readonly',font=("Times New Roman",10))
        EntryNombreProf.grid(row=2,column=3,padx=1,pady=10)

        EntryapellidoProf=ttk.Entry(frameSeleccion,textvariable=self.apellidosproxtext,width=18,state='readonly',font=("Times New Roman",10))
        EntryapellidoProf.grid(row=3,column=3,padx=1,pady=10)

        ############### Frame deco linera

        frameLinea=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="dark blue",width=385,height=7)
        frameLinea.place(x=5,y=129)

        frameBuscar=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="light cyan",width=386,height=105)
        frameBuscar.place(x=5,y=151)

        ############ Label

        labelNombreProf=tk.Label(frameBuscar,text="Fecha:",bg="light cyan",font=("Times New Roman",10))
        labelNombreProf.grid(row=0,column=0,padx=1,pady=3)

        labelapellidoProf=tk.Label(frameBuscar,text="Consulta por:",bg="light cyan",font=("Times New Roman",10))
        labelapellidoProf.grid(row=1,column=0,padx=1,pady=3)


        ################ Entry y combobox
        self.buscarfechatxt=tk.StringVar()
        EntryFecha=ttk.Entry(frameBuscar,textvariable=self.buscarfechatxt,width=18)
        EntryFecha.grid(row=0,column=1,padx=1,pady=3)

        self.opcionEvaluacionAlumno=tk.StringVar()
        opcionesBusqueda=("Cátedra","Fecha")
         
        self.comoboxEVAL=ttk.Combobox(frameBuscar,
                                width=20,
                                textvariable=self.opcionEvaluacionAlumno,
                                values=opcionesBusqueda,
                                state='readonly',
                                font=("Times New Roman",10))
        self.comoboxEVAL.current(1)
        self.comoboxEVAL.grid(row=1,column=1)

        btnBuscar2=tk.Button(frameBuscar,text="Buscar",command=self.searchAsistencias,font=("Times New Roman",10),width=15)
        btnBuscar2.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnBuscar2.grid(row=0,column=2,padx=20,pady=3)

        btnLimpiar2=tk.Button(frameBuscar,text="Limpiar",command=self.clearListaAsistencias,font=("Times New Roman",10),width=15)
        btnLimpiar2.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnLimpiar2.grid(row=2,column=2,padx=20,pady=3)

        ##################### label frame opciones

        labelopcionesFrame=tk.LabelFrame(self.ventana2,text="Opciones",bg="light cyan",width=191,height=298,font=("Times New Roman",10))
        labelopcionesFrame.place(x=950,y=60)
        ####################### Botones asignar, modificar, promedio y Vover

        btnVolver=tk.Button(labelopcionesFrame,text="Volver",command=self.volver_moduloClase,font=("Times New Roman",14),width=15)
        btnVolver.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
        btnVolver.grid(row=4,column=0,padx=5,pady=10)

    ################ Funciones Asistencia
        
    def get_row_Asistencia(self,event):
        rowid=self.tree.identify_row(event.y)
        self.tree.selection_set(rowid)
        item=self.tree.item(self.tree.focus())
        self.id_asistencia=item["text"]
        self.ListaTree=item["values"]
        self.clase_id=str(self.ListaTree[1])
        catedra=self.ListaTree[2]
        programa=self.ListaTree[0]
        fecha=self.ListaTree[3]
        ############ Busca la informacion en la base de datos
        #SELECT a.id_asistencia, d.nombre_programa, c.id_clase, c.Catedra, a.fecha, a.hora_inicio, a.hora_final, b.cod_alumno, f.ci_alumno, f.nombres, f.apellidos, b.ausente_presente FROM asistencia a, alumno_asistencia b,clase c,programa d,alumno f WHERE a.id_asistencia=b.id_asistencia AND a.id_clase=c.id_clase AND d.id_programa=a.id_programa AND b.cod_alumno=f.cod_alumno
        
        
        query2="SELECT a.cedula_identidad, a.nombres, a.apellidos FROM profesor a, clase b WHERE a.cedula_identidad=b.cedula_identidad AND b.id_clase='"+self.clase_id+"' "
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query2)
        respuesta=cursor.fetchall() 
        cone.close()

        if len(respuesta)>0:
            self.idClasetext.set(self.clase_id)
            self.catedratext.set(catedra)
            self.programatxt.set(programa)
            self.cedulatext.set(respuesta[0][0])
            self.nombresproftext.set(respuesta[0][1])
            self.apellidosproxtext.set(respuesta[0][2])

            self.buscarfechatxt.set(fecha)
    
    def updateListaAsistencia(self,respuesta):
        info=self.tree.get_children()

        for elemento in info:
            self.tree.delete(elemento)
        for row in respuesta:
            self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))

    def clearListaAsistencias(self):
        query="SELECT a.id_asistencia, d.nombre_programa, c.id_clase, c.Catedra, a.fecha, a.hora_inicio, a.hora_final, b.cod_alumno, f.ci_alumno, f.nombres, f.apellidos, b.ausente_presente FROM asistencia a, alumno_asistencia b,clase c,programa d,alumno f WHERE a.id_asistencia=b.id_asistencia AND a.id_clase=c.id_clase AND d.id_programa=a.id_programa AND b.cod_alumno=f.cod_alumno"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.idClasetext.set("")
        self.catedratext.set("")
        self.programatxt.set("")
        self.cedulatext.set("")
        self.nombresproftext.set("")
        self.apellidosproxtext.set("")
        self.buscarfechatxt.set("")
        self.updateListaAsistencia(respuesta)

    def searchAsistencias(self):
        opcioncontrol=self.opcionEvaluacionAlumno.get()
        fecha=self.buscarfechatxt.get()
        catedra=self.catedratext.get()
        programa=self.programatxt.get()
        
        if opcioncontrol=="Cátedra":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.id_asistencia, d.nombre_programa, c.id_clase, c.Catedra, a.fecha, a.hora_inicio, a.hora_final, b.cod_alumno, f.ci_alumno, f.nombres, f.apellidos, b.ausente_presente FROM asistencia a, alumno_asistencia b,clase c,programa d,alumno f WHERE a.id_asistencia=b.id_asistencia AND a.id_clase=c.id_clase AND d.id_programa=a.id_programa AND b.cod_alumno=f.cod_alumno AND c.catedra LIKE '%"+catedra+"%' AND d.nombre_programa='"+programa+"' "
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAsistencia(respuesta)

        if opcioncontrol=="Fecha":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.id_asistencia, d.nombre_programa, c.id_clase, c.Catedra, a.fecha, a.hora_inicio, a.hora_final, b.cod_alumno, f.ci_alumno, f.nombres, f.apellidos, b.ausente_presente FROM asistencia a, alumno_asistencia b,clase c,programa d,alumno f WHERE a.id_asistencia=b.id_asistencia AND a.id_clase=c.id_clase AND d.id_programa=a.id_programa AND b.cod_alumno=f.cod_alumno AND a.fecha LIKE '%"+fecha+"%' AND d.nombre_programa='"+programa+"' AND c.catedra LIKE '%"+catedra+"%' ORDER BY a.fecha ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAsistencia(respuesta) 

######################## CERRAR SESION #############################

    def logout(self):
        mb.showinfo("Informacion", "Se ha cerrando sesion correctamente")
        self.ventana1.destroy()
        app=formularios.formulariousuario.FormularioUsuario()
    
    def abrir(self):

        conexion=mysql.connector.connect(host="localhost",
                                         user="root",
                                         passwd="", 
                                         database="bdnucleolecheria")
        return conexion