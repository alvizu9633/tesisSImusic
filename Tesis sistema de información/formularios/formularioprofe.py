from cProfile import label
from cgitb import text
from distutils import command
from msilib.schema import File
from random import triangular
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

class Profesor:

   def __init__(self,usuario):
      ###Programa estandar para las ventanas ---------------------

      self.ventana1=tk.Tk()
      self.ventana1.title("Profesor")
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
      self.label1=tk.Label(self.frame3,text="Profesor",bg="dark blue",font=("Times New Roman",20), fg="white")
      self.label1.place(x=120,y=10)

      # Información usuario

      self.UsuarioName=usuario
      self.id_usuario=tk.StringVar()
      self.id_usuario.set(self.UsuarioName)
    
      labelUsuario=tk.Label(self.frame3,text="Usuario: "+self.id_usuario.get(),bg="dark blue",font=("Times New Roman",15), fg="white")
      labelUsuario.place(x=830,y=7)

        ##-------------------Botones predeterminados --------------------------

      #Boton menu
      self.hidemenu=0
      self.botonmenu=tk.Button(self.frame3,text="Menu", command=self.ocultarmostrarMenu,bg="blueviolet", bd= 5,font=("Times New Roman",15), fg="white",activebackground="light blue",activeforeground="Black")
      self.photo=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\home.png")
      self.botonmenu.config( image=self.photo, compound=LEFT)
      self.botonmenu.place(x=10,y=5)
        
      self.evaluaciones()
        #Mainloop

      mixer.init()
      mixer.music.load("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\Sonido\\Inicio.mp3")
      mixer.music.play()
      #ffile="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\Sonido\\Inicio3.mp3"
      #playsound(ffile)
      self.ventana1.mainloop()

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
         self.frame2.config(bg="light blue") #dark turquoise
         self.frame2.place(x=-15,y=55,width=300,height=800)

         ##-------------------Botones predeterminados --------------------------

                #Boton menu
         self.hidemenu=0

        
         #Boton gestion asistencias
         self.boton1=tk.Button(self.frame2,text="Gestionar Asistencias",command=self.asistencia,bg="blueviolet", bd= 5,font=("Times New Roman",15), fg="white")
         self.boton1.place(x=40,y=20,width=200,height=50)

            #Boton gestion evaluaciones
         self.boton2=tk.Button(self.frame2,text="Gestionar Evaluaciones",command=self.evaluaciones,bg="blueviolet", bd= 5,font=("Times New Roman",15), fg="white")
         self.boton2.place(x=40,y=100,width=200,height=50)

            #Boton gestion cerrar sesion
         self.boton3=tk.Button(self.frame2,text="Cerrar sesión",command=self.logout,bg="blueviolet", bd= 5,font=("Times New Roman",15), fg="white")
         self.boton3.place(x=40,y=180,width=200,height=50)

   ############### Restricciones

   def validar_Cedula(self,ci):
        cedula=ci
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

   def validar_contrasena(self,passwordR):
        password=passwordR
        validar=re.match('^[a-z\áéíóúñàèìòù0-999999 ]+$',password,re.I)
        if password=="":
            #self.entryci.config(border='1 px solid yellow')
            return False
        elif not validar:
            #self.entryci.config(border='1 px solid red')
            return False
        else:
            #self.entryci.config(border='1 px solid green')
            return True

   ########################### Modulo evaluaciones

   def evaluaciones(self):

            self.ocultarmostrarMenu()
            ########################################
            ##        Frame interactivo           ##
            ########################################

            self.frame4Interactivo=tk.Frame(self.ventana1)
            self.frame4Interactivo.config(bg='light cyan',bd=11)
            self.frame4Interactivo.place(x=-15,y=55,width=1050,height=580)

            self.frameDeco=tk.Frame(self.frame4Interactivo,bg="dark blue",height=230)
            self.frameDeco.pack(side='bottom', fill='both')

               #Label titulo frame
            self.labeltitulo=tk.Label(self.frame4Interactivo,text="Gestión evaluaciones",bg="light cyan",font=("Times New Roman",20), fg="Black")
            self.labeltitulo.place(x=20,y=15)

               ##########Búsqueda de información por Clase, programa y trimestre
            self.labelframebusquedaClaseProfe=tk.LabelFrame(self.frame4Interactivo,text="Información y búsqueda",bg="light cyan",width=930,height=260,font=("Times New Roman",10))
            self.labelframebusquedaClaseProfe.place(x=50,y=60)

            frameTablaCLases=tk.Frame(self.labelframebusquedaClaseProfe,bg="light cyan",width=70)
            frameTablaCLases.place(x=5,y=10)

            self.treeClases = ttk.Treeview(frameTablaCLases,columns=("#1","#2","#3"),height="3")
            self.treeClases.heading("#0",text="Cédula identidad")
            self.treeClases.heading("#1",text="Id clase")
            self.treeClases.heading("#2",text="Cátera")
            self.treeClases.heading("#3",text="Programa")

            self.treeClases.column("#0",width=90)
            self.treeClases.column("#1",width=70)
            self.treeClases.column("#2",width=150)
            self.treeClases.column("#3",width=150)

            self.treeClases.bind("<1>",self.get_row_ClasesBuscadorEvaluacion)
            self.treeClases.pack(side="left")

            # SCROLL VERTICAL TREEVIEW
            scrolvert = st.Scrollbar(frameTablaCLases, orient="vertical", command = self.treeClases.yview)
            scrolvert.pack(side="left",fill="y")
            self.treeClases.config(yscrollcommand=scrolvert.set)

            query="SELECT cedula_identidad FROM usuario WHERE nombre_usuario LIKE '%"+self.UsuarioName+"%'"
            cone=self.abrir()
            cursor=cone.cursor()
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            self.cedula=respuesta[0][0]

            con=mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="", 
                                          database="bdnucleolecheria")

            cur=con.cursor()
            profesor=self.treeClases.get_children()

            for elemento in profesor:
                  self.treeClases.delete(elemento)
            try:
                  cur.execute("SELECT a.cedula_identidad, a.id_clase, a.catedra, b.nombre_programa FROM clase a, programa b WHERE a.id_programa=b.id_programa AND a.cedula_identidad='"+self.cedula+"'")
                  rows=cur.fetchall()
                  for row in rows:
                     self.treeClases.insert("",0,text=row[0],values=(row[1],row[2],row[3]))
            except:
                  pass

            frameBuscadordeClases=tk.LabelFrame(self.labelframebusquedaClaseProfe,text="Buscador",bg="light cyan",width=491,height=124,font=("Times New Roman",10))
            frameBuscadordeClases.place(x=5,y=100)

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

            decoframe=tk.Frame(self.labelframebusquedaClaseProfe,bg="dark blue",width=79,height=134)
            decoframe.place(x=422,y=110)

            #######################################################
            ############ Buscador lista evaluacion_alumno##########

            labelframeBuscadorAlumnoEvaluacion=tk.LabelFrame(self.labelframebusquedaClaseProfe,text="Selección",bg="light cyan",width=410,height=225,font=("Times New Roman",10))
            labelframeBuscadorAlumnoEvaluacion.place(x=508,y=0)

            frameSeleccion=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="light cyan",width=380,height=190)
            frameSeleccion.place(x=0,y=0)

            ############# Label column 0

            labelIdClase=tk.Label(frameSeleccion,text="Id clase:",bg="light cyan",font=("Times New Roman",10))
            labelIdClase.grid(row=1,column=0,padx=1,pady=2)

            labelcatedra=tk.Label(frameSeleccion,text="Cátedra:",bg="light cyan",font=("Times New Roman",10))
            labelcatedra.grid(row=2,column=0,padx=1,pady=2)

            labelPrograma=tk.Label(frameSeleccion,text="Programa:",bg="light cyan",font=("Times New Roman",10))
            labelPrograma.grid(row=3,column=0,padx=1,pady=2)

            ############## label column 2

            labelCedula=tk.Label(frameSeleccion,text="Cédula Identidad:",bg="light cyan",font=("Times New Roman",10))
            labelCedula.grid(row=1,column=2,padx=1,pady=2)

            labelNombreProf=tk.Label(frameSeleccion,text="Nombre Profesor:",bg="light cyan",font=("Times New Roman",10))
            labelNombreProf.grid(row=2,column=2,padx=1,pady=2)

            labelapellidoProf=tk.Label(frameSeleccion,text="Apellido Profesor:",bg="light cyan",font=("Times New Roman",10))
            labelapellidoProf.grid(row=3,column=2,padx=1,pady=2)

            ############### Entry column 1
            self.idClasetext=tk.StringVar()
            self.catedratext=tk.StringVar()
            self.programatxt=tk.StringVar()
            self.cedulatext=tk.StringVar()
            self.nombresproftext=tk.StringVar()
            self.apellidosproxtext=tk.StringVar()

            EntryIdClase=ttk.Entry(frameSeleccion,textvariable=self.idClasetext,width=18,state='readonly',font=("Times New Roman",10))
            EntryIdClase.grid(row=1,column=1,padx=1,pady=2)

            Entrycatedra=ttk.Entry(frameSeleccion,textvariable=self.catedratext,width=18,state='readonly',font=("Times New Roman",10))
            Entrycatedra.grid(row=2,column=1,padx=1,pady=2)

            EntryPrograma=ttk.Entry(frameSeleccion,textvariable=self.programatxt,width=18,state='readonly',font=("Times New Roman",10))
            EntryPrograma.grid(row=3,column=1,padx=1,pady=2)

            ############ Entry column 3
            EntryCedula=ttk.Entry(frameSeleccion,textvariable=self.cedulatext,width=18,state='readonly',font=("Times New Roman",10))
            EntryCedula.grid(row=1,column=3,padx=1,pady=2)

            EntryNombreProf=ttk.Entry(frameSeleccion,textvariable=self.nombresproftext,width=18,state='readonly',font=("Times New Roman",10))
            EntryNombreProf.grid(row=2,column=3,padx=1,pady=2)

            EntryapellidoProf=ttk.Entry(frameSeleccion,textvariable=self.apellidosproxtext,width=18,state='readonly',font=("Times New Roman",10))
            EntryapellidoProf.grid(row=3,column=3,padx=1,pady=2)

            ############### Frame deco linera

            frameLinea=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="dark blue",width=385,height=7)
            frameLinea.place(x=5,y=90)

            frameBuscar=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="light cyan",width=386,height=90)
            frameBuscar.place(x=5,y=110)

            ############ Label

            labelTrimestre=tk.Label(frameBuscar,text="Trimestre:",bg="light cyan",font=("Times New Roman",10))
            labelTrimestre.grid(row=0,column=0,padx=1,pady=3)

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

            btnmostrar=tk.Button(frameBuscar,text="Mostrar",command=self.mostrarLista,font=("Times New Roman",10),width=15)
            btnmostrar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnmostrar.grid(row=0,column=2,padx=20,pady=3)

            btnLimpiar=tk.Button(frameBuscar,text="Limpiar",command=self.clearListaEvaluacion,font=("Times New Roman",10),width=15)
            btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnLimpiar.grid(row=2,column=2,padx=5,pady=5)

            #########################################################
            ############ label frame y frame decorativo

            self.labelframeTablaEv=tk.LabelFrame(self.frameDeco,text="Evaluaciones planifiacadas",bg="dark blue",fg="white",width=989,height=210,font=("Times New Roman",10))
            self.labelframeTablaEv.pack(side='top')

            frameTablaEvaluaciones=tk.Frame(self.labelframeTablaEv,bg="light cyan",width=70)
            frameTablaEvaluaciones.place(x=5,y=20)

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
                cur.execute("SELECT c.id_evaluacion, c.id_clase, a.catedra, b.nombre_programa, c.fecha, c.trimestre, c.cedula_identidad FROM clase a, programa b, evaluacion c WHERE a.id_programa=b.id_programa AND c.id_clase=a.id_clase AND a.cedula_identidad='"+self.cedula+"'")
                rows=cur.fetchall()
                for row in rows:
                    self.treeEvaluacion.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6]))
            except:
                pass

            ####################### LabelFrame Nueva evalación

            self.labelframeNuevaeva=tk.LabelFrame(self.labelframeTablaEv,text="Nueva evaluación",fg="white",bg="dark blue",width=255,height=165,font=("Times New Roman",10))
            self.labelframeNuevaeva.place(x=723,y=15)

            frameNuevaEv=tk.Frame(self.labelframeNuevaeva,bg="dark blue",width=100,height=73)
            frameNuevaEv.place(x=0,y=0)

            ############ Label

            labelNombreProf=tk.Label(frameNuevaEv,text="Fecha:",bg="dark blue",fg="white",font=("Times New Roman",10))
            labelNombreProf.grid(row=1,column=0,padx=1,pady=3)

            labelapellidoProf=tk.Label(frameNuevaEv,text="(*)Id evaluación:",bg="dark blue",fg="white",font=("Times New Roman",10))
            labelapellidoProf.grid(row=2,column=0,padx=1,pady=3)

            ####################### ENtry
            self.buscarfechatxt=tk.StringVar()
            self.txtIdEvaluacion=tk.StringVar()

            EntryFecha=ttk.Entry(frameNuevaEv,textvariable=self.buscarfechatxt,width=18,font=("Times New Roman",10))
            EntryFecha.grid(row=1,column=1,padx=1,pady=3)
            
            EntryIdevaluacion=ttk.Entry(frameNuevaEv,textvariable=self.txtIdEvaluacion,width=18,font=("Times New Roman",10))
            EntryIdevaluacion.grid(row=2,column=1,padx=1,pady=3)

            ############################# labelframe opciones

            self.labelframeOpciones=tk.LabelFrame(self.labelframeNuevaeva,text="Opciones",fg="white",bg="dark blue",width=236,height=63,font=("Times New Roman",10))
            self.labelframeOpciones.place(x=7,y=50)

            btnAgregar=tk.Button(self.labelframeOpciones,text="Agregar",command=self.add_new_Evaluaciones,font=("Times New Roman",10),width=14)
            btnAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnAgregar.grid(row=0,column=0,padx=2,pady=3)

            btnModificar=tk.Button(self.labelframeOpciones,text="Modificar",command=self.update_Evaluaciones,font=("Times New Roman",10),width=14)
            btnModificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnModificar.grid(row=0,column=1,padx=2,pady=3)

            btnEliminar=tk.Button(self.labelframeOpciones,text="Eliminar",command=self.delete_Evaluaciones,font=("Times New Roman",10),width=14)
            btnEliminar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnEliminar.grid(row=1,column=0,padx=2,pady=3)

            btnEvaluar=tk.Button(self.labelframeOpciones,text="Evaluar",command=self.evaluar,font=("Times New Roman",10),width=14)
            btnEvaluar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnEvaluar.grid(row=1,column=1,padx=2,pady=3)

            

   ###################### Funciones
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
        query="SELECT c.id_evaluacion, c.id_clase, a.catedra, b.nombre_programa, c.fecha, c.trimestre, c.cedula_identidad FROM clase a, programa b, evaluacion c WHERE a.id_programa=b.id_programa AND c.id_clase=a.id_clase AND a.cedula_identidad='"+self.cedula+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.updateListaEvaluacion(respuesta)


    ############# Funciones Clear y update lista clases

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
        query="SELECT a.cedula_identidad, a.id_clase, a.catedra, b.nombre_programa FROM clase a, programa b WHERE a.id_programa=b.id_programa AND a.cedula_identidad='"+self.cedula+"'"
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
            query="SELECT a.cedula_identidad, a.id_clase, a.catedra, b.nombre_programa FROM clase a, programa b WHERE a.id_programa=b.id_programa AND a.catedra LIKE '%"+buscarLista+"%' AND b.nombre_programa='"+opcionPrograma+"' AND a.cedula_identidad='"+self.cedula+"'"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaClasesListaEv(respuesta)

        if opcioncontrol=="Cédula":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cedula_identidad, a.id_clase, a.catedra, b.nombre_programa FROM clase a, programa b WHERE a.id_programa=b.id_programa AND a.cedula_identidad LIKE '%"+buscarLista+"%' AND b.nombre_programa='"+opcionPrograma+"' AND a.cedula_identidad='"+self.cedula+"'"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaClasesListaEv(respuesta)      

      ###############################################

   def mostrarLista(self):
      query="SELECT c.id_evaluacion, c.id_clase, a.catedra, b.nombre_programa, c.fecha, c.trimestre, c.cedula_identidad FROM clase a, programa b, evaluacion c WHERE a.id_programa=b.id_programa AND c.id_clase=a.id_clase AND a.cedula_identidad='"+self.cedula+"' AND a.Catedra='"+self.catedratext.get()+"' AND b.nombre_programa='"+self.programatxt.get()+"' AND c.trimestre='"+self.buscarTrimestretxt.get()+"'"
      cone=self.abrir()
      cursor=cone.cursor()
      cursor.execute(query)
      respuesta=cursor.fetchall() 
      cone.close()
      self.updateListaEvaluacion(respuesta)

   def evaluar(self):

      ci=self.cedula
      self.id_evaluacionEV=self.txtIdEvaluacion.get()
      Trimestre=self.buscarTrimestretxt.get()
      catedra=self.catedratext.get()
      self.id_clase=self.idClasetext.get()
      fecha=self.buscarfechatxt.get()
      programa=self.programatxt.get()

      try:
         if self.validar_contrasena(self.id_evaluacion):
            self.ventana1.destroy()
            self.ventana2=tk.Tk()
            self.ventana2.title("Evaluar")
            self.ventana2.config(bg='Light cyan')
            self.ventana2.geometry("1150x650")
            self.ventana2.resizable(0,0)
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
                  cur.execute("SELECT a.cod_alumno, b.id_evaluacion, c.id_clase, e.catedra, d.nombre_programa, a.nombres, a.apellidos, b.nota, c.fecha, c.trimestre FROM alumno a, evaluacion_alumno b, evaluacion c, programa d, clase e WHERE a.cod_alumno=b.cod_alumno AND c.id_evaluacion=b.id_evaluacion AND d.id_programa=e.id_programa AND e.id_clase=c.id_clase AND c.id_clase='"+self.idClasetext.get()+"'")
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
            self.treeClases.heading("#0",text="Código alumno")
            self.treeClases.heading("#1",text="Cátedra")
            self.treeClases.heading("#2",text="Nombres")
            self.treeClases.heading("#3",text="Apellidos")

            self.treeClases.column("#0",width=90)
            self.treeClases.column("#1",width=90)
            self.treeClases.column("#2",width=150)
            self.treeClases.column("#3",width=150)

            self.treeClases.bind("<1>",self.get_row_Clases)
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
                  cur.execute("SELECT b.cod_alumno, a.Catedra, c.nombres, c.apellidos FROM clase a, clase_alumno b, alumno c WHERE a.id_clase=b.id_clase AND c.cod_alumno=b.cod_alumno AND a.id_clase='"+self.id_clase+"'")
                  rows=cur.fetchall()
                  for row in rows:
                     self.treeClases.insert("",0,text=row[0],values=(row[1],row[2],row[3]))
            except:
                  pass

            frameBuscadordeClases=tk.LabelFrame(self.labelframebusquedaClaseProfe,text="Buscador",bg="light cyan",width=491,height=124)
            frameBuscadordeClases.place(x=5,y=150)

            ######## Buscador clases
            label1=tk.Label(frameBuscadordeClases,text="Consulta por:",bg="Light cyan",font=("Times New Roman",10))
            label1.grid(row=1,column=0,padx=5,pady=5)

            self.buscador1=tk.StringVar()
            self.entry1=tk.Entry(frameBuscadordeClases,width=30,textvariable=self.buscador1,font=("Times New Roman",10))
            self.entry1.grid(row=2,column=1,padx=5,pady=5)

            #################################################################

            lableBucar=tk.Label(frameBuscadordeClases,text="Buscar:",bg="Light cyan",font=("Times New Roman",10))
            lableBucar.grid(row=2,column=0,padx=5,pady=5)

            self.opcion=tk.StringVar()
            opcionesBusqueda=("Apellidos","Nombres")
               
            self.comobox1=ttk.Combobox(frameBuscadordeClases,
                                    width=20,
                                    textvariable=self.opcion,
                                    values=opcionesBusqueda,
                                    state='readonly',
                                    font=("Times New Roman",10))
            self.comobox1.current(1)

            
            self.comobox1.grid(row=1,column=1)

            btnBuscar=tk.Button(frameBuscadordeClases,text="Buscar",command=self.searchAlumnosClases,font=("Times New Roman",10),width=15)
            btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnBuscar.grid(row=1,column=2,padx=5,pady=5)

            btnLimpiar=tk.Button(frameBuscadordeClases,text="Limpiar",command=self.clearListaAlumnosClase,font=("Times New Roman",10),width=15)
            btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnLimpiar.grid(row=2,column=2,padx=5,pady=5)

            ##################### frame botones

            frameBotones=tk.Frame(self.labelframebusquedaClaseProfe,bg="light cyan",width=415,height=51)
            frameBotones.place(x=9,y=266)

            btnAgregar=tk.Button(frameBotones,text="Agregar",command=self.add_new_Calificacion,font=("Times New Roman",10),width=15)
            btnAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnAgregar.grid(row=0,column=0,padx=9,pady=3)

            btnmodificar=tk.Button(frameBotones,text="Modificar",command=self.update_Calificacion,font=("Times New Roman",10),width=15)
            btnmodificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnmodificar.grid(row=0,column=1,padx=9,pady=3)

            btnEliminar=tk.Button(frameBotones,text="Eliminar",command=self.delete_Calificacion,font=("Times New Roman",10),width=15)
            btnEliminar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnEliminar.grid(row=0,column=2,padx=9,pady=3)


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

            labelIdClase=tk.Label(frameSeleccion,text="Id evaluación:",bg="light cyan",font=("Times New Roman",10))
            labelIdClase.grid(row=1,column=0,padx=1,pady=10)

            labelcatedra=tk.Label(frameSeleccion,text="Cátedra:",bg="light cyan",font=("Times New Roman",10))
            labelcatedra.grid(row=2,column=0,padx=1,pady=10)

            labelPrograma=tk.Label(frameSeleccion,text="Programa:",bg="light cyan",font=("Times New Roman",10))
            labelPrograma.grid(row=3,column=0,padx=1,pady=10)

            ############## label column 2
            labelCedula=tk.Label(frameSeleccion,text="cod_alumno:",bg="light cyan",font=("Times New Roman",10))
            labelCedula.grid(row=1,column=2,padx=1,pady=10)

            labelNombreProf=tk.Label(frameSeleccion,text="Nombres:",bg="light cyan",font=("Times New Roman",10))
            labelNombreProf.grid(row=2,column=2,padx=1,pady=10)

            labelapellidoProf=tk.Label(frameSeleccion,text="Apellidos:",bg="light cyan",font=("Times New Roman",10))
            labelapellidoProf.grid(row=3,column=2,padx=1,pady=10)

            
            ############### Entry column 1
            self.idClasetext=tk.StringVar() #Evaluacion
            self.catedratext=tk.StringVar() 
            self.programatxt=tk.StringVar()
            self.cedulatext=tk.StringVar() #Fecha
            self.nombresproftext=tk.StringVar()
            self.apellidosproxtext=tk.StringVar()

            

            self.idClasetext.set(self.id_evaluacion)
            self.catedratext.set(catedra)
            self.programatxt.set(programa)

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

            labelapellidoProf=tk.Label(frameBuscar,text="Calificación:",bg="light cyan",font=("Times New Roman",10))
            labelapellidoProf.grid(row=2,column=0,padx=1,pady=3)

            labela=tk.Label(frameBuscar,text="Consulta por:",bg="light cyan",font=("Times New Roman",10))
            labela.grid(row=3,column=0,padx=1,pady=3)


            ################ Entry y combobox
            self.buscarTrimestretxt=tk.StringVar()
            self.buscarfechatxt=tk.StringVar()
            self.buscarEvaluacionAlumno=tk.StringVar()

            self.buscarTrimestretxt.set(Trimestre)
            self.buscarfechatxt.set(fecha)

            EntryTrimestre=ttk.Entry(frameBuscar,textvariable=self.buscarTrimestretxt,width=18,state='readonly',font=("Times New Roman",10))
            EntryTrimestre.grid(row=0,column=1,padx=1,pady=3)

            EntryFecha=ttk.Entry(frameBuscar,textvariable=self.buscarfechatxt,width=18,state='readonly',font=("Times New Roman",10))
            EntryFecha.grid(row=1,column=1,padx=1,pady=3)

            EntryCalificacion=ttk.Entry(frameBuscar,textvariable=self.buscarEvaluacionAlumno,width=18,font=("Times New Roman",10))
            EntryCalificacion.grid(row=2,column=1,padx=1,pady=3)

            self.opcionEvaluacionAlumno=tk.StringVar()
            opcionesBusqueda=("Nombres","Apellidos")
               
            self.comoboxEVAL=ttk.Combobox(frameBuscar,
                                    width=20,
                                    textvariable=self.opcionEvaluacionAlumno,
                                    values=opcionesBusqueda,
                                    state='readonly',
                                    font=("Times New Roman",10))
            self.comoboxEVAL.current(1)
            self.comoboxEVAL.grid(row=3,column=1)

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

            btnVolver=tk.Button(labelopcionesFrame,text="Volver",command=self.voler_evaluacion,font=("Times New Roman",14),width=15)
            btnVolver.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnVolver.grid(row=1,column=0,padx=5,pady=10)
         else:
            mb.showerror("Informacion","Debe seleccionar la evaluación a evaluar")
      except:
            pass

   #################### 

   def get_row_Clases(self,event):
        rowid=self.treeClases.identify_row(event.y)
        self.treeClases.selection_set(rowid)
        item=self.treeClases.item(self.treeClases.focus())
        self.cod_alumno=item["text"]
        self.ListaTree=item["values"]
        catedra=str(self.ListaTree[0])
        nombre=self.ListaTree[1]
        apellido=self.ListaTree[2]
        ############ Busca la informacion en la base de datos
        self.catedratext.set(catedra)
        self.cedulatext.set(self.cod_alumno)
        self.nombresproftext.set(nombre)
        self.apellidosproxtext.set(apellido)
    
   def updateListaAlumnoClase(self,respuesta):
        info=self.treeClases.get_children()

        for elemento in info:
            self.treeClases.delete(elemento)
        for row in respuesta:
            self.treeClases.insert("",0,text=row[0],values=(row[1],row[2],row[3]))

   def clearListaAlumnosClase(self):
        query="SELECT b.cod_alumno, a.Catedra, c.nombres, c.apellidos FROM clase a, clase_alumno b, alumno c WHERE a.id_clase=b.id_clase AND c.cod_alumno=b.cod_alumno AND a.id_clase='"+self.id_clase+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.buscador1.set("")
        self.updateListaAlumnoClase(respuesta)

   def searchAlumnosClases(self):
        opcioncontrol=self.comobox1.get()
        buscarLista=self.buscador1.get()
        if opcioncontrol=="Nombres":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT b.cod_alumno, a.Catedra, c.nombres, c.apellidos FROM clase a, clase_alumno b, alumno c WHERE a.id_clase=b.id_clase AND c.cod_alumno=b.cod_alumno AND a.id_clase='"+self.id_clase+"' AND c.nombres LIKE '%"+buscarLista+"%'"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAlumnoClase(respuesta)

        if opcioncontrol=="Apellidos":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT b.cod_alumno, a.Catedra, c.nombres, c.apellidos FROM clase a, clase_alumno b, alumno c WHERE a.id_clase=b.id_clase AND c.cod_alumno=b.cod_alumno AND a.id_clase='"+self.id_clase+"' AND c.apellidos LIKE '%"+buscarLista+"%'"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAlumnoClase(respuesta)      

      ###############################################

   ############ volver

   def voler_evaluacion(self):
            self.ventana2.destroy()

            ###Programa estandar para las ventanas ---------------------
            self.ventana1=tk.Tk()
            self.ventana1.title("Profesor")
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
            self.label1=tk.Label(self.frame3,text="Profesor",bg="dark blue",font=("Times New Roman",20), fg="white")
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

            self.frameDeco=tk.Frame(self.frame4Interactivo,bg="dark blue",height=230)
            self.frameDeco.pack(side='bottom', fill='both')

               #Label titulo frame
            self.labeltitulo=tk.Label(self.frame4Interactivo,text="Gestión evaluaciones",bg="light cyan",font=("Times New Roman",20), fg="Black")
            self.labeltitulo.place(x=20,y=15)

               ##########Búsqueda de información por Clase, programa y trimestre
            self.labelframebusquedaClaseProfe=tk.LabelFrame(self.frame4Interactivo,text="Información y búsqueda",bg="light cyan",width=930,height=260,font=("Times New Roman",10))
            self.labelframebusquedaClaseProfe.place(x=50,y=60)

            frameTablaCLases=tk.Frame(self.labelframebusquedaClaseProfe,bg="light cyan",width=70)
            frameTablaCLases.place(x=5,y=10)

            self.treeClases = ttk.Treeview(frameTablaCLases,columns=("#1","#2","#3"),height="3")
            self.treeClases.heading("#0",text="Cédula identidad")
            self.treeClases.heading("#1",text="Id clase")
            self.treeClases.heading("#2",text="Cátera")
            self.treeClases.heading("#3",text="Programa")

            self.treeClases.column("#0",width=90)
            self.treeClases.column("#1",width=70)
            self.treeClases.column("#2",width=150)
            self.treeClases.column("#3",width=150)

            self.treeClases.bind("<1>",self.get_row_ClasesBuscadorEvaluacion)
            self.treeClases.pack(side="left")

            # SCROLL VERTICAL TREEVIEW
            scrolvert = st.Scrollbar(frameTablaCLases, orient="vertical", command = self.treeClases.yview)
            scrolvert.pack(side="left",fill="y")
            self.treeClases.config(yscrollcommand=scrolvert.set)

            query="SELECT cedula_identidad FROM usuario WHERE nombre_usuario LIKE '%"+self.UsuarioName+"%'"
            cone=self.abrir()
            cursor=cone.cursor()
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            self.cedula=respuesta[0][0]

            con=mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="", 
                                          database="bdnucleolecheria")

            cur=con.cursor()
            profesor=self.treeClases.get_children()

            for elemento in profesor:
                  self.treeClases.delete(elemento)
            try:
                  cur.execute("SELECT a.cedula_identidad, a.id_clase, a.catedra, b.nombre_programa FROM clase a, programa b WHERE a.id_programa=b.id_programa AND a.cedula_identidad='"+self.cedula+"'")
                  rows=cur.fetchall()
                  for row in rows:
                     self.treeClases.insert("",0,text=row[0],values=(row[1],row[2],row[3]))
            except:
                  pass

            frameBuscadordeClases=tk.LabelFrame(self.labelframebusquedaClaseProfe,text="Buscador",bg="light cyan",width=491,height=124,font=("Times New Roman",10))
            frameBuscadordeClases.place(x=5,y=100)

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

            decoframe=tk.Frame(self.labelframebusquedaClaseProfe,bg="dark blue",width=79,height=134)
            decoframe.place(x=422,y=110)

            #######################################################
            ############ Buscador lista evaluacion_alumno##########

            labelframeBuscadorAlumnoEvaluacion=tk.LabelFrame(self.labelframebusquedaClaseProfe,text="Selección",bg="light cyan",width=410,height=225,font=("Times New Roman",10))
            labelframeBuscadorAlumnoEvaluacion.place(x=508,y=0)

            frameSeleccion=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="light cyan",width=380,height=190)
            frameSeleccion.place(x=0,y=0)

            ############# Label column 0

            labelIdClase=tk.Label(frameSeleccion,text="Id clase:",bg="light cyan",font=("Times New Roman",10))
            labelIdClase.grid(row=1,column=0,padx=1,pady=2)

            labelcatedra=tk.Label(frameSeleccion,text="Cátedra:",bg="light cyan",font=("Times New Roman",10))
            labelcatedra.grid(row=2,column=0,padx=1,pady=2)

            labelPrograma=tk.Label(frameSeleccion,text="Programa:",bg="light cyan",font=("Times New Roman",10))
            labelPrograma.grid(row=3,column=0,padx=1,pady=2)

            ############## label column 2

            labelCedula=tk.Label(frameSeleccion,text="Cédula Identidad:",bg="light cyan",font=("Times New Roman",10))
            labelCedula.grid(row=1,column=2,padx=1,pady=2)

            labelNombreProf=tk.Label(frameSeleccion,text="Nombre Profesor:",bg="light cyan",font=("Times New Roman",10))
            labelNombreProf.grid(row=2,column=2,padx=1,pady=2)

            labelapellidoProf=tk.Label(frameSeleccion,text="Apellido Profesor:",bg="light cyan",font=("Times New Roman",10))
            labelapellidoProf.grid(row=3,column=2,padx=1,pady=2)

            ############### Entry column 1
            self.idClasetext=tk.StringVar()
            self.catedratext=tk.StringVar()
            self.programatxt=tk.StringVar()
            self.cedulatext=tk.StringVar()
            self.nombresproftext=tk.StringVar()
            self.apellidosproxtext=tk.StringVar()

            EntryIdClase=ttk.Entry(frameSeleccion,textvariable=self.idClasetext,width=18,state='readonly',font=("Times New Roman",10))
            EntryIdClase.grid(row=1,column=1,padx=1,pady=2)

            Entrycatedra=ttk.Entry(frameSeleccion,textvariable=self.catedratext,width=18,state='readonly',font=("Times New Roman",10))
            Entrycatedra.grid(row=2,column=1,padx=1,pady=2)

            EntryPrograma=ttk.Entry(frameSeleccion,textvariable=self.programatxt,width=18,state='readonly',font=("Times New Roman",10))
            EntryPrograma.grid(row=3,column=1,padx=1,pady=2)

            ############ Entry column 3
            EntryCedula=ttk.Entry(frameSeleccion,textvariable=self.cedulatext,width=18,state='readonly',font=("Times New Roman",10))
            EntryCedula.grid(row=1,column=3,padx=1,pady=2)

            EntryNombreProf=ttk.Entry(frameSeleccion,textvariable=self.nombresproftext,width=18,state='readonly',font=("Times New Roman",10))
            EntryNombreProf.grid(row=2,column=3,padx=1,pady=2)

            EntryapellidoProf=ttk.Entry(frameSeleccion,textvariable=self.apellidosproxtext,width=18,state='readonly',font=("Times New Roman",10))
            EntryapellidoProf.grid(row=3,column=3,padx=1,pady=2)

            ############### Frame deco linera

            frameLinea=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="dark blue",width=385,height=7)
            frameLinea.place(x=5,y=90)

            frameBuscar=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="light cyan",width=386,height=90)
            frameBuscar.place(x=5,y=110)

            ############ Label

            labelTrimestre=tk.Label(frameBuscar,text="Trimestre:",bg="light cyan",font=("Times New Roman",10))
            labelTrimestre.grid(row=0,column=0,padx=1,pady=3)

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

            btnmostrar=tk.Button(frameBuscar,text="Mostrar",command=self.mostrarLista,font=("Times New Roman",10),width=15)
            btnmostrar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnmostrar.grid(row=0,column=2,padx=20,pady=3)

            btnLimpiar=tk.Button(frameBuscar,text="Limpiar",command=self.clearListaEvaluacion,font=("Times New Roman",10),width=15)
            btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnLimpiar.grid(row=2,column=2,padx=5,pady=5)

            #########################################################
            ############ label frame y frame decorativo

            self.labelframeTablaEv=tk.LabelFrame(self.frameDeco,text="Evaluaciones planifiacadas",bg="dark blue",fg="white",width=989,height=210,font=("Times New Roman",10))
            self.labelframeTablaEv.pack(side='top')

            frameTablaEvaluaciones=tk.Frame(self.labelframeTablaEv,bg="light cyan",width=70)
            frameTablaEvaluaciones.place(x=5,y=20)

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
                cur.execute("SELECT c.id_evaluacion, c.id_clase, a.catedra, b.nombre_programa, c.fecha, c.trimestre, c.cedula_identidad FROM clase a, programa b, evaluacion c WHERE a.id_programa=b.id_programa AND c.id_clase=a.id_clase AND a.cedula_identidad='"+self.cedula+"'")
                rows=cur.fetchall()
                for row in rows:
                    self.treeEvaluacion.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6]))
            except:
                pass

            ####################### LabelFrame Nueva evalación

            self.labelframeNuevaeva=tk.LabelFrame(self.labelframeTablaEv,text="Nueva evaluación",fg="white",bg="dark blue",width=255,height=165,font=("Times New Roman",10))
            self.labelframeNuevaeva.place(x=723,y=15)

            frameNuevaEv=tk.Frame(self.labelframeNuevaeva,bg="dark blue",width=100,height=73)
            frameNuevaEv.place(x=0,y=0)

            ############ Label

            labelNombreProf=tk.Label(frameNuevaEv,text="Fecha:",bg="dark blue",fg="white",font=("Times New Roman",10))
            labelNombreProf.grid(row=1,column=0,padx=1,pady=3)

            labelapellidoProf=tk.Label(frameNuevaEv,text="(*)Id evaluación:",bg="dark blue",fg="white",font=("Times New Roman",10))
            labelapellidoProf.grid(row=2,column=0,padx=1,pady=3)

            ####################### ENtry
            self.buscarfechatxt=tk.StringVar()
            self.txtIdEvaluacion=tk.StringVar()

            EntryFecha=ttk.Entry(frameNuevaEv,textvariable=self.buscarfechatxt,width=18,font=("Times New Roman",10))
            EntryFecha.grid(row=1,column=1,padx=1,pady=3)
            
            EntryIdevaluacion=ttk.Entry(frameNuevaEv,textvariable=self.txtIdEvaluacion,width=18,font=("Times New Roman",10))
            EntryIdevaluacion.grid(row=2,column=1,padx=1,pady=3)

            ############################# labelframe opciones

            self.labelframeOpciones=tk.LabelFrame(self.labelframeNuevaeva,text="Opciones",fg="white",bg="dark blue",width=236,height=63,font=("Times New Roman",10))
            self.labelframeOpciones.place(x=7,y=50)

            btnAgregar=tk.Button(self.labelframeOpciones,text="Agregar",command=self.add_new_Evaluaciones,font=("Times New Roman",10),width=14)
            btnAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnAgregar.grid(row=0,column=0,padx=2,pady=3)

            btnModificar=tk.Button(self.labelframeOpciones,text="Modificar",command=self.update_Evaluaciones,font=("Times New Roman",10),width=14)
            btnModificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnModificar.grid(row=0,column=1,padx=2,pady=3)

            btnEliminar=tk.Button(self.labelframeOpciones,text="Eliminar",command=self.delete_Evaluaciones,font=("Times New Roman",10),width=14)
            btnEliminar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnEliminar.grid(row=1,column=0,padx=2,pady=3)

            btnEvaluar=tk.Button(self.labelframeOpciones,text="Evaluar",command=self.evaluar,font=("Times New Roman",10),width=14)
            btnEvaluar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnEvaluar.grid(row=1,column=1,padx=2,pady=3)

            self.ventana1.mainloop()

   ####################### Funciones      
   def get_row_Evaluacion_Clases(self,event):
        rowid=self.tree.identify_row(event.y)
        self.tree.selection_set(rowid)
        item=self.tree.item(self.tree.focus())
        self.cod_alumno=item["text"]
        self.ListaTree=item["values"]
        self.id_evaluacion=self.ListaTree[0]
        nombre=str(self.ListaTree[4])
        apellido=self.ListaTree[5]
        nota=self.ListaTree[6]
        fecha=self.ListaTree[7]
        trimestre=self.ListaTree[8]
        ############ Busca la informacion en la base de datos 
        self.cedulatext.set(self.cod_alumno)
        self.nombresproftext.set(nombre)
        self.apellidosproxtext.set(apellido)
        self.buscarfechatxt.set(fecha)
        self.buscarTrimestretxt.set(trimestre)
        self.buscarEvaluacionAlumno.set(nota)
    
   def updateListaEvClase(self,respuesta):
        info=self.tree.get_children()

        for elemento in info:
            self.tree.delete(elemento)
        for row in respuesta:
            self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))

   def clearListaEvaluacionClases(self):
        query="SELECT a.cod_alumno, b.id_evaluacion, c.id_clase, e.catedra, d.nombre_programa, a.nombres, a.apellidos, b.nota, c.fecha, c.trimestre FROM alumno a, evaluacion_alumno b, evaluacion c, programa d, clase e WHERE a.cod_alumno=b.cod_alumno AND c.id_evaluacion=b.id_evaluacion AND d.id_programa=e.id_programa AND e.id_clase=c.id_clase AND c.id_evaluacion='"+self.idClasetext.get()+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        self.buscarEvaluacionAlumno.set("")
        self.cedulatext.set("")
        self.nombresproftext.set("")
        self.apellidosproxtext.set("")
        self.updateListaEvClase(respuesta)

   def searchEvalaucionCLases(self):
        opcioncontrol=self.opcionEvaluacionAlumno.get()
        nombre=self.nombresproftext.get()
        apellido=self.apellidosproxtext.get()
        cod_alumno=self.idClasetext.get()
        id_evaluacion=self.id_evaluacion

        if opcioncontrol=="Nombres":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, b.id_evaluacion, c.id_clase, e.catedra, d.nombre_programa, a.nombres, a.apellidos, b.nota, c.fecha, c.trimestre FROM alumno a, evaluacion_alumno b, evaluacion c, programa d, clase e WHERE a.cod_alumno=b.cod_alumno AND c.id_evaluacion=b.id_evaluacion AND d.id_programa=e.id_programa AND e.id_clase=c.id_clase AND a.nombres LIKE '%"+nombre+"%' AND b.id_evaluacion='"+id_evaluacion+"'"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaEvClase(respuesta) 

        if opcioncontrol=="Apellidos":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.cod_alumno, b.id_evaluacion, c.id_clase, e.catedra, d.nombre_programa, a.nombres, a.apellidos, b.nota, c.fecha, c.trimestre FROM alumno a, evaluacion_alumno b, evaluacion c, programa d, clase e WHERE a.cod_alumno=b.cod_alumno AND c.id_evaluacion=b.id_evaluacion AND d.id_programa=e.id_programa AND e.id_clase=c.id_clase AND a.apellidos LIKE '%"+apellido+"%' AND b.id_evaluacion='"+id_evaluacion+"'"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaEvClase(respuesta) 

   ##################### Evaluaciones agregar, editar y borrar Evaluaciones planificadas

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
                self.txtIdEvaluacion.set("")
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
                    self.txtIdEvaluacion.set("")
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
                    self.txtIdEvaluacion.set("")
                else:
                    mb.showinfo("Informacion", "No existe un alumno con dicha informacion")
            else:
                return True
        except:
                mb.showwarning("Error","Introduzca la informacion que desee borrar o selecione en la tabla instrumentos asignados.")
   
   ########################## Evaluaciones agregar, editar y borrar Calificaciones

   def add_new_Calificacion (self):
        cod_alumno=self.cedulatext.get()
        id_evaluacion=self.id_evaluacionEV
        nota=self.buscarEvaluacionAlumno.get()
        try:
            if self.validar_contrasena(cod_alumno):
                
                query="INSERT INTO evaluacion_alumno(id_evaluacion,nota,cod_alumno) VALUES(%s,%s,%s)"

                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(id_evaluacion,nota,cod_alumno))
                
                cone.commit()
                cone.close()
                self.clearListaEvaluacionClases()
                
                mb.showinfo("Información","Se han cargado con éxito los datos.")

                self.cedulatext.set("")
                self.nombresproftext.set("")
                self.apellidosproxtext.set("")
                self.buscarEvaluacionAlumno.set("")
            else:
                mb.showwarning("Error","Debe completar los campos obligatorios (*)")
        except:
            mb.showinfo("Información","Este dato ya existe")

   def update_Calificacion(self):
        cod_alumno=self.cedulatext.get()
        id_evaluacion=self.id_evaluacionEV
        nota=self.buscarEvaluacionAlumno.get()

        if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea actualizar estos datos? "):
            if self.validar_contrasena(cod_alumno):
            
                query="UPDATE evaluacion_alumno SET id_evaluacion=%s, nota=%s, cod_alumno=%s WHERE id_evaluacion = '"+self.id_evaluacion+"' AND cod_alumno='"+self.cod_alumno+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(id_evaluacion,nota,cod_alumno))
                

                cone.commit()
                cone.close()

                self.clearListaEvaluacionClases()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han cargado con éxito los datos.")

                    self.cedulatext.set("")
                    self.nombresproftext.set("")
                    self.apellidosproxtext.set("")
                    self.buscarEvaluacionAlumno.set("")

                else:
                    mb.showinfo("Informacion", "No existe un campo con dicha informacion")
                
            else:
                mb.showwarning("Error","Debe seleccionar los campos a modificar")
        else:
            return True

   def delete_Calificacion(self):
        cod_alumno=self.cedulatext.get()
        id_evaluacion=self.id_evaluacionEV
        nota=self.buscarEvaluacionAlumno.get()
        try:
            if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea borrar estos datos? "):
                query="DELETE FROM evaluacion_alumno WHERE id_evaluacion='"+id_evaluacion+"' AND cod_alumno='"+cod_alumno+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query)
                
                cone.commit()
                cone.close()
                self.clearListaEvaluacionClases()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han borrado los datos con éxito.")

                    self.cedulatext.set("")
                    self.nombresproftext.set("")
                    self.apellidosproxtext.set("")

                    self.buscarEvaluacionAlumno.set("")
                else:
                    mb.showinfo("Informacion", "No existe un alumno con dicha informacion")
            else:
                return True
        except:
                mb.showwarning("Error","Introduzca la informacion que desee borrar o selecione en la tabla instrumentos asignados.")
   
   ############################## Modulo asistencias

   def asistencia(self):
            self.ocultarmostrarMenu()

            self.frame4Interactivo.place_forget()

            ########################################
            ##        Frame interactivo           ##
            ########################################

            self.frame4Interactivo=tk.Frame(self.ventana1)
            self.frame4Interactivo.config(bg='light cyan',bd=11)
            self.frame4Interactivo.place(x=-15,y=55,width=1050,height=580)

            #### Frame Logo

            self.frameLogo=tk.Frame(self.frame4Interactivo,bg="light blue",width=390,height=227)
            self.frameLogo.place(x=534, y= 77)

            self.imagen=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\profesImagenes.png")
            fondo=tk.Label(self.frameLogo,image=self.imagen,bg="light cyan").place(x=0,y=0)


                #Label titulo frame
            self.labeltitulo=tk.Label(self.frame4Interactivo,text="Gestión asistencias",bg="light cyan",font=("Times New Roman",20), fg="Black")
            self.labeltitulo.place(x=20,y=15)

            ##### Labelframe Selleccion

            labelframeBuscadorAlumnoEvaluacion=tk.LabelFrame(self.frame4Interactivo,text="Selección",bg="light cyan",width=410,height=350,font=("Times New Roman",10))
            labelframeBuscadorAlumnoEvaluacion.place(x=36,y=50)

            frameSeleccion=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="light cyan",width=380,height=190)
            frameSeleccion.place(x=0,y=0)

            ############# Label column 0

            labelIdClase=tk.Label(frameSeleccion,text="Id clase:",bg="light cyan",font=("Times New Roman",10))
            labelIdClase.grid(row=1,column=0,padx=1,pady=2)

            labelcatedra=tk.Label(frameSeleccion,text="Cátedra:",bg="light cyan",font=("Times New Roman",10))
            labelcatedra.grid(row=2,column=0,padx=1,pady=2)

            labelPrograma=tk.Label(frameSeleccion,text="Programa:",bg="light cyan",font=("Times New Roman",10))
            labelPrograma.grid(row=3,column=0,padx=1,pady=2)

            ############## label column 2

            labelCedula=tk.Label(frameSeleccion,text="Cédula Identidad:",bg="light cyan",font=("Times New Roman",10))
            labelCedula.grid(row=1,column=2,padx=1,pady=2)

            labelNombreProf=tk.Label(frameSeleccion,text="Nombre Profesor:",bg="light cyan",font=("Times New Roman",10))
            labelNombreProf.grid(row=2,column=2,padx=1,pady=2)

            labelapellidoProf=tk.Label(frameSeleccion,text="Apellido Profesor:",bg="light cyan",font=("Times New Roman",10))
            labelapellidoProf.grid(row=3,column=2,padx=1,pady=2)

            ############### Entry column 1
            self.idClasetext=tk.StringVar()
            self.catedratext=tk.StringVar()
            self.programatxt=tk.StringVar()
            self.cedulatext=tk.StringVar()
            self.nombresproftext=tk.StringVar()
            self.apellidosproxtext=tk.StringVar()

            EntryIdClase=ttk.Entry(frameSeleccion,textvariable=self.idClasetext,width=18,state='readonly',font=("Times New Roman",10))
            EntryIdClase.grid(row=1,column=1,padx=1,pady=2)

            Entrycatedra=ttk.Entry(frameSeleccion,textvariable=self.catedratext,width=18,state='readonly',font=("Times New Roman",10))
            Entrycatedra.grid(row=2,column=1,padx=1,pady=2)

            EntryPrograma=ttk.Entry(frameSeleccion,textvariable=self.programatxt,width=18,state='readonly',font=("Times New Roman",10))
            EntryPrograma.grid(row=3,column=1,padx=1,pady=2)

            ############ Entry column 3
            EntryCedula=ttk.Entry(frameSeleccion,textvariable=self.cedulatext,width=18,state='readonly',font=("Times New Roman",10))
            EntryCedula.grid(row=1,column=3,padx=1,pady=2)

            EntryNombreProf=ttk.Entry(frameSeleccion,textvariable=self.nombresproftext,width=18,state='readonly',font=("Times New Roman",10))
            EntryNombreProf.grid(row=2,column=3,padx=1,pady=2)

            EntryapellidoProf=ttk.Entry(frameSeleccion,textvariable=self.apellidosproxtext,width=18,state='readonly',font=("Times New Roman",10))
            EntryapellidoProf.grid(row=3,column=3,padx=1,pady=2)

            ############### Frame deco linera

            frameLinea=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="dark blue",width=385,height=7)
            frameLinea.place(x=5,y=90)

            frameBuscar=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="light cyan",width=386,height=90)
            frameBuscar.place(x=5,y=110)

            ############ Label

            labelFecha=tk.Label(frameBuscar,text="Fecha:",bg="light cyan",font=("Times New Roman",10))
            labelFecha.grid(row=0,column=0,padx=1,pady=2)

            labelhoraInicio=tk.Label(frameBuscar,text="Hora Inicio:",bg="light cyan",font=("Times New Roman",10))
            labelhoraInicio.grid(row=1,column=0,padx=1,pady=2)

            labelhoraFinal=tk.Label(frameBuscar,text="Hora Final:",bg="light cyan",font=("Times New Roman",10))
            labelhoraFinal.grid(row=2,column=0,padx=1,pady=2)

            ################ Entry y combobox
            self.txtHrinicio=tk.StringVar()
            self.txtHrfinal=tk.StringVar()
            self.textFecha=tk.StringVar()
            self.txtid_asistencia=tk.StringVar()

            EntryFecha=ttk.Entry(frameBuscar,textvariable=self.textFecha,width=18,font=("Times New Roman",10))
            EntryFecha.grid(row=0,column=1,padx=1,pady=2)

            EntryHoraInicio=ttk.Entry(frameBuscar,textvariable=self.txtHrinicio,width=18,font=("Times New Roman",10))
            EntryHoraInicio.grid(row=1,column=1,padx=1,pady=2)

            EntryHoraFinal=ttk.Entry(frameBuscar,textvariable=self.txtHrfinal,width=18,font=("Times New Roman",10))
            EntryHoraFinal.grid(row=2,column=1,padx=1,pady=2)

            ################ Columna 2 y 3

            labelIdAsistencia=tk.Label(frameBuscar,text="Id asistencia:",bg="light cyan",font=("Times New Roman",10))
            labelIdAsistencia.grid(row=0,column=2,padx=1,pady=2)

            EntryIdAsistencia=ttk.Entry(frameBuscar,textvariable=self.txtid_asistencia,width=18,font=("Times New Roman",10))
            EntryIdAsistencia.grid(row=0,column=3,padx=1,pady=2)

            btnmostrar=tk.Button(frameBuscar,text="Mostrar",command=self.mostrarListaAsistencia,font=("Times New Roman",10),width=15)
            btnmostrar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnmostrar.grid(row=1,column=3,padx=1,pady=2)

            btnLimpiar=tk.Button(frameBuscar,text="Limpiar",command=self.clearListaAsistencia,font=("Times New Roman",10),width=15)
            btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnLimpiar.grid(row=2,column=3,padx=1,pady=2)

            ############ Tree

            frameTablaCLases=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="light cyan",width=396, height=110)
            frameTablaCLases.place(x=5,y=219)

            self.treeClases = ttk.Treeview(frameTablaCLases,columns=("#1","#2","#3"),height="4")
            self.treeClases.heading("#0",text="Cédula identidad")
            self.treeClases.heading("#1",text="Id clase")
            self.treeClases.heading("#2",text="Cátera")
            self.treeClases.heading("#3",text="Programa")

            self.treeClases.column("#0",width=90)
            self.treeClases.column("#1",width=45)
            self.treeClases.column("#2",width=120)
            self.treeClases.column("#3",width=120)

            self.treeClases.bind("<1>",self.get_row_ClasesBuscadorEvaluacion)
            self.treeClases.pack(side="left")

            # SCROLL VERTICAL TREEVIEW
            scrolvert = st.Scrollbar(frameTablaCLases, orient="vertical", command = self.treeClases.yview)
            scrolvert.pack(side="left",fill="y")
            self.treeClases.config(yscrollcommand=scrolvert.set)

            query="SELECT cedula_identidad FROM usuario WHERE nombre_usuario LIKE '%"+self.UsuarioName+"%'"
            cone=self.abrir()
            cursor=cone.cursor()
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            self.cedula=respuesta[0][0]

            con=mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="", 
                                          database="bdnucleolecheria")

            cur=con.cursor()
            profesor=self.treeClases.get_children()

            for elemento in profesor:
                  self.treeClases.delete(elemento)
            try:
                  cur.execute("SELECT a.cedula_identidad, a.id_clase, a.catedra, b.nombre_programa FROM clase a, programa b WHERE a.id_programa=b.id_programa AND a.cedula_identidad='"+self.cedula+"'")
                  rows=cur.fetchall()
                  for row in rows:
                     self.treeClases.insert("",0,text=row[0],values=(row[1],row[2],row[3]))
            except:
                  pass
            
            ##### Frame botones

            labelframeBotones=tk.LabelFrame(self.frame4Interactivo,text="Opciones",bg="light cyan",width=380,height=106,font=("Times New Roman",10))
            labelframeBotones.place(x=46,y=420)

            frameBotones=tk.Frame(labelframeBotones,bg="light cyan",width=380,height=190)
            frameBotones.place(x=0,y=0)

            btnAgregar=tk.Button(frameBotones,text="Agregar",command=self.add_new_Asistencias,font=("Times New Roman",10),width=23)
            btnAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnAgregar.grid(row=0,column=0,padx=5,pady=3)

            btnModificar=tk.Button(frameBotones,text="Modificar",command=self.update_Asistencias,font=("Times New Roman",10),width=23)
            btnModificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnModificar.grid(row=0,column=1,padx=5,pady=3)

            btnEliminar=tk.Button(frameBotones,text="Eliminar",command=self.delete_Asistencias,font=("Times New Roman",10),width=23)
            btnEliminar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnEliminar.grid(row=1,column=0,padx=5,pady=3)

            btnRegistrar=tk.Button(frameBotones,text="Registrar",command=self.Registrar,font=("Times New Roman",10),width=23)
            btnRegistrar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnRegistrar.grid(row=1,column=1,padx=5,pady=3)

            ############### Frame deco

            framedecorativoTabla=tk.Frame(self.frame4Interactivo,bg="dark blue",width=579,height=235)
            framedecorativoTabla.place(x=455,y=325)

            labelframeTabla=tk.LabelFrame(framedecorativoTabla,text="Tabla asistencias",bg="dark Blue",fg="white",width=560,height=220,font=("Times New Roman",10))
            labelframeTabla.place(x=5,y=5)

            ######################### Frame tabla

            frametabla=tk.Frame(labelframeTabla,bg="light blue",width=500,height=200)
            frametabla.place(x=10,y=5)

            self.tree = ttk.Treeview(frametabla,columns=("#1","#2","#3","#4","#5"),height="8")
            self.tree.heading("#0",text="Id Asistencia")
            self.tree.heading("#1",text="Id clase")
            self.tree.heading("#2",text="Programa")
            self.tree.heading("#3",text="Fecha")
            self.tree.heading("#4",text="Inicio")
            self.tree.heading("#5",text="Final")

            self.tree.column("#0",width=70)
            self.tree.column("#1",width=50)
            self.tree.column("#2",width=120)
            self.tree.column("#3",width=95)
            self.tree.column("#4",width=90)
            self.tree.column("#5",width=90)

            self.tree.bind("<1>",self.get_row_Asistencia)
            self.tree.pack(side="left")

            # SCROLL VERTICAL TREEVIEW
            scrolvert = st.Scrollbar(frametabla, orient="vertical", command = self.tree.yview)
            scrolvert.pack(side="left",fill="y")
            self.tree.config(yscrollcommand=scrolvert.set)

            query="SELECT cedula_identidad FROM usuario WHERE nombre_usuario LIKE '%"+self.UsuarioName+"%'"
            cone=self.abrir()
            cursor=cone.cursor()
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            self.cedula=respuesta[0][0]

            con=mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="", 
                                          database="bdnucleolecheria")

            cur=con.cursor()
            profesor=self.tree.get_children()

            for elemento in profesor:
                  self.tree.delete(elemento)
            try:
                  cur.execute("SELECT a.id_asistencia,a.id_clase,b.nombre_programa,a.fecha,a.hora_inicio,a.hora_final FROM asistencia a, programa b, clase c WHERE a.id_clase=c.id_clase AND a.id_programa=b.id_programa AND a.cedula_identidad='"+self.cedula+"'")
                  rows=cur.fetchall()
                  for row in rows:
                     self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))
            except:
                  pass

    ############################## Funciones Asistencia

   def get_row_Asistencia(self,event):
        rowid=self.tree.identify_row(event.y)
        self.tree.selection_set(rowid)
        item=self.tree.item(self.tree.focus())
        self.id_asistencia=item["text"]
        self.ListaTree=item["values"]
        self.id_clase=self.ListaTree[0]
        programa=str(self.ListaTree[1])
        fecha=self.ListaTree[2]
        hrInicio=self.ListaTree[3]
        hrFinal=self.ListaTree[4]

        query="SELECT c.Catedra, b.nombres, b.apellidos FROM asistencia a , profesor b, clase c WHERE a.cedula_identidad=b.cedula_identidad AND c.id_clase=a.id_clase AND a.cedula_identidad='"+self.cedula+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        ############ Busca la informacion en la base de datos 
        self.cedulatext.set(self.cedula)
        self.nombresproftext.set(respuesta[0][1])
        self.apellidosproxtext.set(respuesta[0][2])
        self.idClasetext.set(self.id_clase)
        self.catedratext.set(respuesta[0][0])
        self.programatxt.set(programa)

        self.txtHrinicio.set(hrInicio)
        self.txtHrfinal.set(hrFinal)
        self.textFecha.set(fecha)
        self.txtid_asistencia.set(self.id_asistencia)
    
   def updateListaAsistencia(self,respuesta):
        info=self.tree.get_children()

        for elemento in info:
            self.tree.delete(elemento)
        for row in respuesta:
            self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))

   def clearListaAsistencia(self):
        query="SELECT a.id_asistencia,a.id_clase,b.nombre_programa,a.fecha,a.hora_inicio,a.hora_final FROM asistencia a, programa b, clase c WHERE a.id_clase=c.id_clase AND a.id_programa=b.id_programa AND a.cedula_identidad='"+self.cedula+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()
        
        self.textFecha.set("")
        self.txtHrfinal.set("")
        self.txtHrinicio.set("")
        self.txtid_asistencia.set("")
        self.idClasetext.set("")
        self.catedratext.set("")
        self.programatxt.set("")

        self.cedulatext.set("")
        self.nombresproftext.set("")
        self.apellidosproxtext.set("")
        self.updateListaAsistencia(respuesta)

   def mostrarListaAsistencia(self):
            query="SELECT a.id_asistencia,a.id_clase,b.nombre_programa,a.fecha,a.hora_inicio,a.hora_final FROM asistencia a, programa b, clase c WHERE a.id_clase=c.id_clase AND a.id_programa=b.id_programa AND a.cedula_identidad='"+self.cedula+"' AND a.id_clase='"+self.idClasetext.get()+"' AND b.nombre_programa='"+self.programatxt.get()+"' AND a.fecha LIKE '%"+self.textFecha.get()+"%'"
            cone=self.abrir()
            cursor=cone.cursor()
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAsistencia(respuesta)

################ Agregar, eliminar y modificar Asistencias

   def definir_programa(self):
        opcioncontrol=self.programatxt.get()
        query="SELECT id_programa FROM programa WHERE nombre_programa='"+opcioncontrol+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()

        return respuesta[0][0]

   def add_new_Asistencias (self):
        idAsistencia=self.txtid_asistencia.get()
        horaFinal=self.txtHrfinal.get()
        fecha=self.textFecha.get()
        horaInicio=self.txtHrinicio.get()
        cedula=self.cedulatext.get()
        id_clase=self.idClasetext.get()
        try:
            if self.validar_contrasena(idAsistencia):

                programa=self.definir_programa()
                
                query="INSERT INTO asistencia(id_asistencia,cedula_identidad,fecha,hora_inicio,hora_final,id_programa,id_clase) VALUES(%s,%s,%s,%s,%s,%s,%s)"

                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(idAsistencia,cedula,fecha,horaInicio,horaFinal,programa,id_clase))
                
                cone.commit()
                cone.close()
                self.clearListaAsistencia()
                
                mb.showinfo("Información","Se han cargado con éxito los datos.")
                self.idClasetext.set("")
                self.catedratext.set("")
                self.programatxt.set("")
                self.cedulatext.set("")
                self.nombresproftext.set("")
                self.apellidosproxtext.set("")
                self.textFecha.set("")
                self.txtid_asistencia.set("")
                self.txtHrinicio.set("")
                self.txtHrfinal.set("")
            else:
                mb.showwarning("Error","Debe completar los campos obligatorios (*)")
        except:
            mb.showinfo("Información","Este dato ya existe")

   def update_Asistencias(self):
        idAsistencia=self.txtid_asistencia.get()
        horaFinal=self.txtHrfinal.get()
        fecha=self.textFecha.get()
        horaInicio=self.txtHrinicio.get()
        cedula=self.cedulatext.get()
        
        id_clase=self.idClasetext.get()

        if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea actualizar estos datos? "):
            if self.validar_contrasena(idAsistencia):

                programa=self.definir_programa()
            
                query="UPDATE asistencia SET id_asistencia=%s,cedula_identidad=%s,fecha=%s,hora_inicio=%s,hora_final=%s,id_programa=%s,id_clase=%s WHERE id_asistencia = '"+self.id_asistencia+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(idAsistencia,cedula,fecha,horaInicio,horaFinal,programa,id_clase))
                

                cone.commit()
                cone.close()

                self.clearListaAsistencia()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han cargado con éxito los datos.")
                    self.idClasetext.set("")
                    self.catedratext.set("")
                    self.programatxt.set("")
                    self.cedulatext.set("")
                    self.nombresproftext.set("")
                    self.apellidosproxtext.set("")
                    self.textFecha.set("")
                    self.txtid_asistencia.set("")
                    self.txtHrinicio.set("")
                    self.txtHrfinal.set("")
                else:
                    mb.showinfo("Informacion", "No existe un campo con dicha informacion")
                
            else:
                mb.showwarning("Error","Debe seleccionar los campos a modificar")
        else:
            return True

   def delete_Asistencias(self):
        id_asistencia=self.txtid_asistencia.get()
        try:
            if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea borrar estos datos? "):
                query="DELETE FROM asistencia WHERE id_asistencia='"+id_asistencia+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query)
                
                cone.commit()
                cone.close()
                self.clearListaAsistencia()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han borrado los datos con éxito.")
                    self.idClasetext.set("")
                    self.catedratext.set("")
                    self.programatxt.set("")
                    self.cedulatext.set("")
                    self.nombresproftext.set("")
                    self.apellidosproxtext.set("")
                    self.textFecha.set("")
                    self.txtid_asistencia.set("")
                    self.txtHrinicio.set("")
                    self.txtHrfinal.set("")
                else:
                    mb.showinfo("Informacion", "No existe un alumno con dicha informacion")
            else:
                return True
        except:
                mb.showwarning("Error","Introduzca la informacion que desee borrar o selecione en la tabla Asistencias.")
   
   ############# Registrar

   def Registrar(self):

      ci=self.cedula
      self.id_evaluacionEV=self.txtIdEvaluacion.get()
      hora=""+self.txtHrinicio.get()+" - "+self.txtHrfinal.get()+""
      catedra=self.catedratext.get()
      self.id_clase=self.idClasetext.get()
      fecha=self.textFecha.get()
      programa=self.programatxt.get()

      try:
         if self.validar_contrasena(self.id_asistencia):
            self.ventana1.destroy()
            self.ventana2=tk.Tk()
            self.ventana2.title("Registrar Asistencia")
            self.ventana2.config(bg='Light cyan')
            self.ventana2.geometry("1150x650")
            self.ventana2.resizable(0,0)
            self.ventana2.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")
            
            self.decoraframe=tk.Frame(self.ventana2,bg="dark blue",height=190)
            self.decoraframe.pack(fill="both",expand="no",side="top")

            self.decoFrameabajo=tk.Frame(self.ventana2,bg="dark blue",height=90)
            self.decoFrameabajo.pack(fill="both",expand="no",side="bottom")

            

            self.lista=tk.LabelFrame(self.decoraframe,text="Asistencias registradas",fg="white",font=("Times New Roman",10))
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

            self.tree.bind("<1>",self.get_row_Asistencia_clases)
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
                cur.execute("SELECT a.id_asistencia, d.nombre_programa, c.id_clase, c.Catedra, a.fecha, a.hora_inicio, a.hora_final, b.cod_alumno, f.ci_alumno, f.nombres, f.apellidos, b.ausente_presente FROM asistencia a, alumno_asistencia b,clase c,programa d,alumno f WHERE a.id_asistencia=b.id_asistencia AND a.id_clase=c.id_clase AND d.id_programa=a.id_programa AND b.cod_alumno=f.cod_alumno AND a.id_asistencia='"+self.id_asistencia+"'")
                rows=cur.fetchall()
                for row in rows:
                    self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
            except:
                pass

            ##########Búsqueda de información por Clase, programa y trimestre
            self.labelframebusquedaClaseProfe=tk.LabelFrame(self.ventana2,text="Información y búsqueda",bg="light cyan",width=930,height=340,font=("Times New Roman",10))
            self.labelframebusquedaClaseProfe.place(x=12,y=247)

            frameTablaCLases=tk.Frame(self.labelframebusquedaClaseProfe,bg="light cyan",width=70)
            frameTablaCLases.place(x=5,y=10)

            self.treeClases = ttk.Treeview(frameTablaCLases,columns=("#1","#2","#3"),height="5")
            self.treeClases.heading("#0",text="Código alumno")
            self.treeClases.heading("#1",text="Cátedra")
            self.treeClases.heading("#2",text="Nombres")
            self.treeClases.heading("#3",text="Apellidos")

            self.treeClases.column("#0",width=90)
            self.treeClases.column("#1",width=90)
            self.treeClases.column("#2",width=150)
            self.treeClases.column("#3",width=150)

            self.treeClases.bind("<1>",self.get_row_Clases)
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
                  cur.execute("SELECT b.cod_alumno, a.Catedra, c.nombres, c.apellidos FROM clase a, clase_alumno b, alumno c WHERE a.id_clase=b.id_clase AND c.cod_alumno=b.cod_alumno AND a.id_clase='"+self.id_clase+"'")
                  rows=cur.fetchall()
                  for row in rows:
                     self.treeClases.insert("",0,text=row[0],values=(row[1],row[2],row[3]))
            except:
                  pass

            frameBuscadordeClases=tk.LabelFrame(self.labelframebusquedaClaseProfe,text="Buscador",bg="light cyan",width=491,height=124,font=("Times New Roman",10))
            frameBuscadordeClases.place(x=5,y=150)

            ######## Buscador clases
            label1=tk.Label(frameBuscadordeClases,text="Consulta por:",bg="Light cyan",font=("Times New Roman",10))
            label1.grid(row=1,column=0,padx=5,pady=5)

            self.buscador1=tk.StringVar()
            self.entry1=tk.Entry(frameBuscadordeClases,width=30,textvariable=self.buscador1,font=("Times New Roman",10))
            self.entry1.grid(row=2,column=1,padx=5,pady=5)

            #################################################################

            lableBucar=tk.Label(frameBuscadordeClases,text="Buscar:",bg="Light cyan",font=("Times New Roman",10))
            lableBucar.grid(row=2,column=0,padx=5,pady=5)

            self.opcion=tk.StringVar()
            opcionesBusqueda=("Apellidos","Nombres")
               
            self.comobox1=ttk.Combobox(frameBuscadordeClases,
                                    width=20,
                                    textvariable=self.opcion,
                                    values=opcionesBusqueda,
                                    state='readonly',
                                    font=("Times New Roman",10))
            self.comobox1.current(1)

            
            self.comobox1.grid(row=1,column=1)

            btnBuscar=tk.Button(frameBuscadordeClases,text="Buscar",command=self.searchAlumnosClases,font=("Times New Roman",10),width=15)
            btnBuscar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnBuscar.grid(row=1,column=2,padx=5,pady=5)

            btnLimpiar=tk.Button(frameBuscadordeClases,text="Limpiar",command=self.clearListaAlumnosClase,font=("Times New Roman",10),width=15)
            btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnLimpiar.grid(row=2,column=2,padx=5,pady=5)

            ##################### frame botones

            frameBotones=tk.Frame(self.labelframebusquedaClaseProfe,bg="light cyan",width=415,height=51)
            frameBotones.place(x=9,y=266)

            btnAgregar=tk.Button(frameBotones,text="Agregar",command=self.add_new_AsistenciaRegistro,font=("Times New Roman",10),width=15)
            btnAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnAgregar.grid(row=0,column=0,padx=9,pady=3)

            btnmodificar=tk.Button(frameBotones,text="Modificar",command=self.update_AsistenciaRegistro,font=("Times New Roman",10),width=15)
            btnmodificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnmodificar.grid(row=0,column=1,padx=9,pady=3)

            btnEliminar=tk.Button(frameBotones,text="Eliminar",command=self.delete_AsistenciaRegistro,font=("Times New Roman",10),width=15)
            btnEliminar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnEliminar.grid(row=0,column=2,padx=9,pady=3)


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

            labelIdClase=tk.Label(frameSeleccion,text="Id asistencia:",bg="light cyan",font=("Times New Roman",10))
            labelIdClase.grid(row=1,column=0,padx=1,pady=10)

            labelcatedra=tk.Label(frameSeleccion,text="Cátedra:",bg="light cyan",font=("Times New Roman",10))
            labelcatedra.grid(row=2,column=0,padx=1,pady=10)

            labelPrograma=tk.Label(frameSeleccion,text="Programa:",bg="light cyan",font=("Times New Roman",10))
            labelPrograma.grid(row=3,column=0,padx=1,pady=10)

            ############## label column 2
            labelCedula=tk.Label(frameSeleccion,text="cod_alumno:",bg="light cyan",font=("Times New Roman",10))
            labelCedula.grid(row=1,column=2,padx=1,pady=10)

            labelNombreProf=tk.Label(frameSeleccion,text="Nombres:",bg="light cyan",font=("Times New Roman",10))
            labelNombreProf.grid(row=2,column=2,padx=1,pady=10)

            labelapellidoProf=tk.Label(frameSeleccion,text="Apellidos:",bg="light cyan",font=("Times New Roman",10))
            labelapellidoProf.grid(row=3,column=2,padx=1,pady=10)

            
            ############### Entry column 1
            self.idClasetext=tk.StringVar() #Evaluacion
            self.catedratext=tk.StringVar() 
            self.programatxt=tk.StringVar()
            self.cedulatext=tk.StringVar() #Fecha
            self.nombresproftext=tk.StringVar()
            self.apellidosproxtext=tk.StringVar()

            self.idClasetext.set(self.id_asistencia)
            self.catedratext.set(catedra)
            self.programatxt.set(programa)

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

            labelHoraInicioFIn=tk.Label(frameBuscar,text="Hora Inicio-fin:",bg="light cyan",font=("Times New Roman",10))
            labelHoraInicioFIn.grid(row=0,column=0,padx=1,pady=3)

            labelNombreProf=tk.Label(frameBuscar,text="Fecha:",bg="light cyan",font=("Times New Roman",10))
            labelNombreProf.grid(row=1,column=0,padx=1,pady=3)

            labelapellidoProf=tk.Label(frameBuscar,text="Presente/Ausente:",bg="light cyan",font=("Times New Roman",10))
            labelapellidoProf.grid(row=2,column=0,padx=1,pady=3)

            labela=tk.Label(frameBuscar,text="Consulta por:",bg="light cyan",font=("Times New Roman",10))
            labela.grid(row=3,column=0,padx=1,pady=3)


            ################ Entry y combobox
            self.txthora=tk.StringVar()
            self.buscarfechatxt=tk.StringVar()
            self.buscarEvaluacionAlumno=tk.StringVar()

            self.txthora.set(hora)
            self.buscarfechatxt.set(fecha)

            EntryHora=ttk.Entry(frameBuscar,textvariable=self.txthora,width=18,state='readonly',font=("Times New Roman",10))
            EntryHora.grid(row=0,column=1,padx=1,pady=3)

            EntryFecha=ttk.Entry(frameBuscar,textvariable=self.buscarfechatxt,width=18,state='readonly',font=("Times New Roman",10))
            EntryFecha.grid(row=1,column=1,padx=1,pady=3)

            self.opcionPresenteAusente=tk.StringVar()
            opcionesPA=("P","A")
               
            self.comoboxPResente=ttk.Combobox(frameBuscar,
                                    width=20,
                                    textvariable=self.opcionPresenteAusente,
                                    values=opcionesPA,
                                    state='readonly',
                                    font=("Times New Roman",10))
            self.comoboxPResente.current(1)
            self.comoboxPResente.grid(row=2,column=1)

            self.opcionEvaluacionAlumno=tk.StringVar()
            opcionesBusqueda=("Nombres","Apellidos")
               
            self.comoboxEVAL=ttk.Combobox(frameBuscar,
                                    width=20,
                                    textvariable=self.opcionEvaluacionAlumno,
                                    values=opcionesBusqueda,
                                    state='readonly',
                                    font=("Times New Roman",10))
            self.comoboxEVAL.current(1)
            self.comoboxEVAL.grid(row=3,column=1)

            btnBuscar2=tk.Button(frameBuscar,text="Buscar",command=self.searchAsistenciasClase,font=("Times New Roman",10),width=15)
            btnBuscar2.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnBuscar2.grid(row=0,column=2,padx=20,pady=3)

            btnLimpiar2=tk.Button(frameBuscar,text="Limpiar",command=self.clearListaAsistenciaClases,font=("Times New Roman",10),width=15)
            btnLimpiar2.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnLimpiar2.grid(row=2,column=2,padx=20,pady=3)

            #### Frame Logo

            self.frameLogo=tk.Frame(self.ventana2,bg="light blue",width=249,height=220)
            self.frameLogo.place(x=945, y= 325)

            self.imagen=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\saxo.png")
            fondo=tk.Label(self.frameLogo,image=self.imagen,bg="light cyan").place(x=0,y=0)

            ##################### label frame opciones

            labelopcionesFrame=tk.LabelFrame(self.ventana2,text="Opciones",bg="light cyan",width=191,height=298,font=("Times New Roman",10))
            labelopcionesFrame.place(x=950,y=250)
            ####################### Botones asignar, modificar, promedio y Vover

            btnVolver=tk.Button(labelopcionesFrame,text="Volver",command=self.voler_asistencia,font=("Times New Roman",14),width=15)
            btnVolver.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnVolver.grid(row=1,column=0,padx=5,pady=10)
         else:
            mb.showerror("Informacion","Debe seleccionar la asistencia a registrar")
      except:
            mb.showerror("Informacion","Debe seleccionar la asistencia a registrar")
    ###################### Funciones Treeview

   def get_row_Asistencia_clases(self,event):
        rowid=self.tree.identify_row(event.y)
        self.tree.selection_set(rowid)
        item=self.tree.item(self.tree.focus())
        self.id_asistencia=item["text"]
        self.ListaTree=item["values"]
        self.cod_alumno=self.ListaTree[6]
        nombre=str(self.ListaTree[8])
        apellido=self.ListaTree[9]
        presenteAusente=self.ListaTree[10]


        ############ Busca la informacion en la base de datos 
        self.cedulatext.set(self.cod_alumno)
        self.nombresproftext.set(nombre)
        self.apellidosproxtext.set(apellido)

        self.opcionPresenteAusente.set(presenteAusente)
    
   def updateListaAsistenciaClases(self,respuesta):
        info=self.tree.get_children()

        for elemento in info:
            self.tree.delete(elemento)
        for row in respuesta:
            self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))

   def clearListaAsistenciaClases(self):
        query="SELECT a.id_asistencia, d.nombre_programa, c.id_clase, c.Catedra, a.fecha, a.hora_inicio, a.hora_final, b.cod_alumno, f.ci_alumno, f.nombres, f.apellidos, b.ausente_presente FROM asistencia a, alumno_asistencia b,clase c,programa d,alumno f WHERE a.id_asistencia=b.id_asistencia AND a.id_clase=c.id_clase AND d.id_programa=a.id_programa AND b.cod_alumno=f.cod_alumno AND a.id_asistencia='"+self.id_asistencia+"'"
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute(query)
        respuesta=cursor.fetchall() 
        cone.close()


        self.cedulatext.set("")
        self.nombresproftext.set("")
        self.apellidosproxtext.set("")
        self.updateListaAsistenciaClases(respuesta)

   def searchAsistenciasClase(self):
        opcioncontrol=self.opcionEvaluacionAlumno.get()
        Nombres=self.nombresproftext.get()
        Apellidos=self.apellidosproxtext.get()
        
        if opcioncontrol=="Nombres":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.id_asistencia, d.nombre_programa, c.id_clase, c.Catedra, a.fecha, a.hora_inicio, a.hora_final, b.cod_alumno, f.ci_alumno, f.nombres, f.apellidos, b.ausente_presente FROM asistencia a, alumno_asistencia b,clase c,programa d,alumno f WHERE a.id_asistencia=b.id_asistencia AND a.id_clase=c.id_clase AND d.id_programa=a.id_programa AND b.cod_alumno=f.cod_alumno AND f.nombres LIKE '%"+Nombres+"%' AND a.id_asistencia='"+self.id_asistencia+"' "
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAsistenciaClases(respuesta)

        if opcioncontrol=="Apellidos":
            cone=self.abrir()
            cursor=cone.cursor()
            query="SELECT a.id_asistencia, d.nombre_programa, c.id_clase, c.Catedra, a.fecha, a.hora_inicio, a.hora_final, b.cod_alumno, f.ci_alumno, f.nombres, f.apellidos, b.ausente_presente FROM asistencia a, alumno_asistencia b,clase c,programa d,alumno f WHERE a.id_asistencia=b.id_asistencia AND a.id_clase=c.id_clase AND d.id_programa=a.id_programa AND b.cod_alumno=f.cod_alumno AND f.apellidos LIKE '%"+Apellidos+"%' AND a.id_asistencia='"+self.id_asistencia+"' ORDER BY a.fecha ASC"
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            cone.close()
            self.updateListaAsistenciaClases(respuesta) 
    
    ###################### Modificar, agregar y eliminar

   def add_new_AsistenciaRegistro(self):
        idAsistencia=self.id_asistencia
        ausentePresente=self.opcionPresenteAusente.get()
        cod_alumno=self.cedulatext.get()
        try:
            if self.validar_contrasena(cod_alumno):
                
                query="INSERT INTO alumno_asistencia(cod_alumno,ausente_presente,id_asistencia) VALUES(%s,%s,%s)"

                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(cod_alumno,ausentePresente,idAsistencia))
                
                cone.commit()
                cone.close()
                self.clearListaAsistenciaClases()
                
                mb.showinfo("Información","Se han cargado con éxito los datos.")
                self.cedulatext.set("")
                self.nombresproftext.set("")
                self.apellidosproxtext.set("")
            else:
                mb.showwarning("Error","Debe completar los campos obligatorios (*)")
        except:
            mb.showinfo("Información","Este dato ya existe")

   def update_AsistenciaRegistro(self):
        idAsistencia=self.id_asistencia
        ausentePresente=self.opcionPresenteAusente.get()
        cod_alumno=self.cedulatext.get()
        

        if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea actualizar estos datos? "):
            if self.validar_contrasena(cod_alumno):
                query="UPDATE alumno_asistencia SET id_asistencia=%s,ausente_presente=%s,cod_alumno=%s WHERE id_asistencia = '"+self.id_asistencia+"' AND cod_alumno='"+self.cod_alumno+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query,(idAsistencia,ausentePresente,cod_alumno))
                

                cone.commit()
                cone.close()

                self.clearListaAsistenciaClases()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han cargado con éxito los datos.")
                    self.cedulatext.set("")
                    self.nombresproftext.set("")
                    self.apellidosproxtext.set("")
                else:
                    mb.showinfo("Informacion", "No existe un campo con dicha informacion")
                
            else:
                mb.showwarning("Error","Debe seleccionar los campos a modificar")
        else:
            return True

   def delete_AsistenciaRegistro(self):
        id_asistencia=self.txtid_asistencia.get()
        cod_alumno=self.cedulatext.get()
        try:
            if mb.askyesno("Confirmar","Se realizaran cambios permanentes.\n ¿Esta seguro que desea borrar estos datos? "):
                query="DELETE FROM alumno_asistencia WHERE id_asistencia='"+id_asistencia+"' AND cod_alumno='"+cod_alumno+"'"
                cone=self.abrir()
                cursor=cone.cursor()
                cursor.execute(query)
                
                cone.commit()
                cone.close()
                self.clearListaAsistenciaClases()
                if cursor.rowcount==1:
                    mb.showinfo("Información","Se han borrado los datos con éxito.")
                    self.cedulatext.set("")
                    self.nombresproftext.set("")
                    self.apellidosproxtext.set("")
                else:
                    mb.showinfo("Informacion", "No existe un alumno con dicha informacion")
            else:
                return True
        except:
                mb.showwarning("Error","Introduzca la informacion que desee borrar o selecione en la tabla Asistencias.")
   
    ############ volver

   def voler_asistencia(self):
            self.ventana2.destroy()

            ###Programa estandar para las ventanas ---------------------
            self.ventana1=tk.Tk()
            self.ventana1.title("Profesor")
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
            self.label1=tk.Label(self.frame3,text="Profesor",bg="dark blue",font=("Times New Roman",20), fg="white")
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

            self.frameLogo=tk.Frame(self.frame4Interactivo,bg="light blue",width=390,height=227)
            self.frameLogo.place(x=534, y= 77)

            self.imagen=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\profesImagenes.png")
            fondo=tk.Label(self.frameLogo,image=self.imagen,bg="light cyan").place(x=0,y=0)


                #Label titulo frame
            self.labeltitulo=tk.Label(self.frame4Interactivo,text="Gestión asistencias",bg="light cyan",font=("Times New Roman",20), fg="Black")
            self.labeltitulo.place(x=20,y=15)

            ##### Labelframe Selleccion

            labelframeBuscadorAlumnoEvaluacion=tk.LabelFrame(self.frame4Interactivo,text="Selección",bg="light cyan",width=410,height=350,font=("Times New Roman",10))
            labelframeBuscadorAlumnoEvaluacion.place(x=36,y=50)

            frameSeleccion=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="light cyan",width=380,height=190)
            frameSeleccion.place(x=0,y=0)

            ############# Label column 0

            labelIdClase=tk.Label(frameSeleccion,text="Id clase:",bg="light cyan",font=("Times New Roman",10))
            labelIdClase.grid(row=1,column=0,padx=1,pady=2)

            labelcatedra=tk.Label(frameSeleccion,text="Cátedra:",bg="light cyan",font=("Times New Roman",10))
            labelcatedra.grid(row=2,column=0,padx=1,pady=2)

            labelPrograma=tk.Label(frameSeleccion,text="Programa:",bg="light cyan",font=("Times New Roman",10))
            labelPrograma.grid(row=3,column=0,padx=1,pady=2)

            ############## label column 2

            labelCedula=tk.Label(frameSeleccion,text="Cédula Identidad:",bg="light cyan",font=("Times New Roman",10))
            labelCedula.grid(row=1,column=2,padx=1,pady=2)

            labelNombreProf=tk.Label(frameSeleccion,text="Nombre Profesor:",bg="light cyan",font=("Times New Roman",10))
            labelNombreProf.grid(row=2,column=2,padx=1,pady=2)

            labelapellidoProf=tk.Label(frameSeleccion,text="Apellido Profesor:",bg="light cyan",font=("Times New Roman",10))
            labelapellidoProf.grid(row=3,column=2,padx=1,pady=2)

            ############### Entry column 1
            self.idClasetext=tk.StringVar()
            self.catedratext=tk.StringVar()
            self.programatxt=tk.StringVar()
            self.cedulatext=tk.StringVar()
            self.nombresproftext=tk.StringVar()
            self.apellidosproxtext=tk.StringVar()

            EntryIdClase=ttk.Entry(frameSeleccion,textvariable=self.idClasetext,width=18,state='readonly',font=("Times New Roman",10))
            EntryIdClase.grid(row=1,column=1,padx=1,pady=2)

            Entrycatedra=ttk.Entry(frameSeleccion,textvariable=self.catedratext,width=18,state='readonly',font=("Times New Roman",10))
            Entrycatedra.grid(row=2,column=1,padx=1,pady=2)

            EntryPrograma=ttk.Entry(frameSeleccion,textvariable=self.programatxt,width=18,state='readonly',font=("Times New Roman",10))
            EntryPrograma.grid(row=3,column=1,padx=1,pady=2)

            ############ Entry column 3
            EntryCedula=ttk.Entry(frameSeleccion,textvariable=self.cedulatext,width=18,state='readonly',font=("Times New Roman",10))
            EntryCedula.grid(row=1,column=3,padx=1,pady=2)

            EntryNombreProf=ttk.Entry(frameSeleccion,textvariable=self.nombresproftext,width=18,state='readonly',font=("Times New Roman",10))
            EntryNombreProf.grid(row=2,column=3,padx=1,pady=2)

            EntryapellidoProf=ttk.Entry(frameSeleccion,textvariable=self.apellidosproxtext,width=18,state='readonly',font=("Times New Roman",10))
            EntryapellidoProf.grid(row=3,column=3,padx=1,pady=2)

            ############### Frame deco linera

            frameLinea=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="dark blue",width=385,height=7)
            frameLinea.place(x=5,y=90)

            frameBuscar=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="light cyan",width=386,height=90)
            frameBuscar.place(x=5,y=110)

            ############ Label

            labelFecha=tk.Label(frameBuscar,text="Fecha:",bg="light cyan",font=("Times New Roman",10))
            labelFecha.grid(row=0,column=0,padx=1,pady=2)

            labelhoraInicio=tk.Label(frameBuscar,text="Hora Inicio:",bg="light cyan",font=("Times New Roman",10))
            labelhoraInicio.grid(row=1,column=0,padx=1,pady=2)

            labelhoraFinal=tk.Label(frameBuscar,text="Hora Final:",bg="light cyan",font=("Times New Roman",10))
            labelhoraFinal.grid(row=2,column=0,padx=1,pady=2)

            ################ Entry y combobox
            self.txtHrinicio=tk.StringVar()
            self.txtHrfinal=tk.StringVar()
            self.textFecha=tk.StringVar()
            self.txtid_asistencia=tk.StringVar()

            EntryFecha=ttk.Entry(frameBuscar,textvariable=self.textFecha,width=18,font=("Times New Roman",10))
            EntryFecha.grid(row=0,column=1,padx=1,pady=2)

            EntryHoraInicio=ttk.Entry(frameBuscar,textvariable=self.txtHrinicio,width=18,font=("Times New Roman",10))
            EntryHoraInicio.grid(row=1,column=1,padx=1,pady=2)

            EntryHoraFinal=ttk.Entry(frameBuscar,textvariable=self.txtHrfinal,width=18,font=("Times New Roman",10))
            EntryHoraFinal.grid(row=2,column=1,padx=1,pady=2)

            ################ Columna 2 y 3

            labelIdAsistencia=tk.Label(frameBuscar,text="Id asistencia:",bg="light cyan",font=("Times New Roman",10))
            labelIdAsistencia.grid(row=0,column=2,padx=1,pady=2)

            EntryIdAsistencia=ttk.Entry(frameBuscar,textvariable=self.txtid_asistencia,width=18,font=("Times New Roman",10))
            EntryIdAsistencia.grid(row=0,column=3,padx=1,pady=2)

            btnmostrar=tk.Button(frameBuscar,text="Mostrar",command=self.mostrarListaAsistencia,font=("Times New Roman",10),width=15)
            btnmostrar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnmostrar.grid(row=1,column=3,padx=1,pady=2)

            btnLimpiar=tk.Button(frameBuscar,text="Limpiar",command=self.clearListaAsistencia,font=("Times New Roman",10),width=15)
            btnLimpiar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnLimpiar.grid(row=2,column=3,padx=1,pady=2)

            ############ Tree

            frameTablaCLases=tk.Frame(labelframeBuscadorAlumnoEvaluacion,bg="light cyan",width=396, height=110)
            frameTablaCLases.place(x=5,y=219)

            self.treeClases = ttk.Treeview(frameTablaCLases,columns=("#1","#2","#3"),height="4")
            self.treeClases.heading("#0",text="Cédula identidad")
            self.treeClases.heading("#1",text="Id clase")
            self.treeClases.heading("#2",text="Cátera")
            self.treeClases.heading("#3",text="Programa")

            self.treeClases.column("#0",width=90)
            self.treeClases.column("#1",width=45)
            self.treeClases.column("#2",width=120)
            self.treeClases.column("#3",width=120)

            self.treeClases.bind("<1>",self.get_row_ClasesBuscadorEvaluacion)
            self.treeClases.pack(side="left")

            # SCROLL VERTICAL TREEVIEW
            scrolvert = st.Scrollbar(frameTablaCLases, orient="vertical", command = self.treeClases.yview)
            scrolvert.pack(side="left",fill="y")
            self.treeClases.config(yscrollcommand=scrolvert.set)

            query="SELECT cedula_identidad FROM usuario WHERE nombre_usuario LIKE '%"+self.UsuarioName+"%'"
            cone=self.abrir()
            cursor=cone.cursor()
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            self.cedula=respuesta[0][0]

            con=mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="", 
                                          database="bdnucleolecheria")

            cur=con.cursor()
            profesor=self.treeClases.get_children()

            for elemento in profesor:
                  self.treeClases.delete(elemento)
            try:
                  cur.execute("SELECT a.cedula_identidad, a.id_clase, a.catedra, b.nombre_programa FROM clase a, programa b WHERE a.id_programa=b.id_programa AND a.cedula_identidad='"+self.cedula+"'")
                  rows=cur.fetchall()
                  for row in rows:
                     self.treeClases.insert("",0,text=row[0],values=(row[1],row[2],row[3]))
            except:
                  pass
            
            ##### Frame botones

            labelframeBotones=tk.LabelFrame(self.frame4Interactivo,text="Opciones",bg="light cyan",width=380,height=106,font=("Times New Roman",10))
            labelframeBotones.place(x=46,y=420)

            frameBotones=tk.Frame(labelframeBotones,bg="light cyan",width=380,height=190)
            frameBotones.place(x=0,y=0)

            btnAgregar=tk.Button(frameBotones,text="Agregar",command=self.add_new_Asistencias,font=("Times New Roman",10),width=23)
            btnAgregar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnAgregar.grid(row=0,column=0,padx=5,pady=3)

            btnModificar=tk.Button(frameBotones,text="Modificar",command=self.update_Asistencias,font=("Times New Roman",10),width=23)
            btnModificar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnModificar.grid(row=0,column=1,padx=5,pady=3)

            btnEliminar=tk.Button(frameBotones,text="Eliminar",command=self.delete_Asistencias,font=("Times New Roman",10),width=23)
            btnEliminar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnEliminar.grid(row=1,column=0,padx=5,pady=3)

            btnRegistrar=tk.Button(frameBotones,text="Registrar",command=self.Registrar,font=("Times New Roman",10),width=23)
            btnRegistrar.config(bg="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5)
            btnRegistrar.grid(row=1,column=1,padx=5,pady=3)

            ############### Frame deco

            framedecorativoTabla=tk.Frame(self.frame4Interactivo,bg="dark blue",width=579,height=235)
            framedecorativoTabla.place(x=455,y=325)

            labelframeTabla=tk.LabelFrame(framedecorativoTabla,text="Tabla asistencias",bg="dark Blue",fg="white",width=560,height=220,font=("Times New Roman",10))
            labelframeTabla.place(x=5,y=5)

            ######################### Frame tabla

            frametabla=tk.Frame(labelframeTabla,bg="light blue",width=500,height=200)
            frametabla.place(x=10,y=5)

            self.tree = ttk.Treeview(frametabla,columns=("#1","#2","#3","#4","#5"),height="8")
            self.tree.heading("#0",text="Id Asistencia")
            self.tree.heading("#1",text="Id clase")
            self.tree.heading("#2",text="Programa")
            self.tree.heading("#3",text="Fecha")
            self.tree.heading("#4",text="Inicio")
            self.tree.heading("#5",text="Final")

            self.tree.column("#0",width=70)
            self.tree.column("#1",width=50)
            self.tree.column("#2",width=120)
            self.tree.column("#3",width=95)
            self.tree.column("#4",width=90)
            self.tree.column("#5",width=90)

            self.tree.bind("<1>",self.get_row_Asistencia)
            self.tree.pack(side="left")

            # SCROLL VERTICAL TREEVIEW
            scrolvert = st.Scrollbar(frametabla, orient="vertical", command = self.tree.yview)
            scrolvert.pack(side="left",fill="y")
            self.tree.config(yscrollcommand=scrolvert.set)

            query="SELECT cedula_identidad FROM usuario WHERE nombre_usuario LIKE '%"+self.UsuarioName+"%'"
            cone=self.abrir()
            cursor=cone.cursor()
            cursor.execute(query)
            respuesta=cursor.fetchall() 
            self.cedula=respuesta[0][0]

            con=mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="", 
                                          database="bdnucleolecheria")

            cur=con.cursor()
            profesor=self.tree.get_children()

            for elemento in profesor:
                  self.tree.delete(elemento)
            try:
                  cur.execute("SELECT a.id_asistencia,a.id_clase,b.nombre_programa,a.fecha,a.hora_inicio,a.hora_final FROM asistencia a, programa b, clase c WHERE a.id_clase=c.id_clase AND a.id_programa=b.id_programa AND a.cedula_identidad='"+self.cedula+"'")
                  rows=cur.fetchall()
                  for row in rows:
                     self.tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))
            except:
                  pass

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

