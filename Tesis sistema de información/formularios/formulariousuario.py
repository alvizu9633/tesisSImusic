import tkinter as tk
from tkinter import PhotoImage, messagebox as mb
from tkinter import scrolledtext as st
import mysql.connector

import mongoengine
import sqlalchemy

import formularios.formularioadmin
import formularios.formularioprofe

class FormularioUsuario:

    def __init__(self):
        
        ###Programa estandar para las ventanas ---------------------
        self.ventana1=tk.Tk()
        self.ventana1.title("Iniciar sesion")
        self.ventana1.geometry("1050x650")
        self.ventana1.config(bg='light cyan',bd=15)
        self.ventana1.resizable(0,0)
        self.ventana1.iconbitmap("C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_aCJ_icon.ico")
        #-------------------------------------------------------
        
        ########## Frame Logo fundamusical

        self.frameLogo2=tk.Frame(self.ventana1,bg="light blue",width=601,height=89)
        self.frameLogo2.place(x=470, y=42)

        imagen2=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\logo_fundamusical692_102.png")
        fondo2=tk.Label(self.frameLogo2,image=imagen2,bg="light cyan").place(x=0,y=0)

        #Frame admin decorativo
        self.frameDecorativo=tk.Frame(self.ventana1)
        self.frameDecorativo.config(bg="dark blue")
        self.frameDecorativo.place(x=-20,y=-20,width=506,height=649)

             #### Frame Logo

        self.frameLogo=tk.Frame(self.frameDecorativo,bg="light blue",width=506,height=649)
        self.frameLogo.place(x=0,y= 0)

        self.imagen1=tk.PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\borde_menu.png")
        fondo2=tk.Label(self.frameLogo,image=self.imagen1,bg="light cyan").place(x=0,y=0)

        
        #Frame usuario
        self.frame1=tk.Frame(self.ventana1, bg='white')
        self.frame1.config(bg="dark blue")
        self.frame1.place(x=0,y=-20,width=450,height=800)

        #label bienvenido
        self.label1=tk.Label(self.frame1,text="Bienvenido",bg="dark blue",font=("Times New Roman",30), fg="white")
        self.label1.place(x=140,y=40)
        

        #Label nombre de usuario
        self.label2=tk.Label(self.frame1,text="Nombre de usuario:",bg="dark blue",font=("Times New Roman",20), fg="white")
        self.label2.place(x=20,y=130)
        
        #Entry nombre de usuario
        self.nombreusuario=tk.StringVar()
        self.entry1=tk.Entry(self.frame1,textvariable=self.nombreusuario,width=20,font=("Times New Roman",20))
        self.entry1.place(x=20,y=190,width=300,height=50)

        #Label contrasena
        self.label2=tk.Label(self.frame1,text="Contraseña:",bg="dark blue",font=("Times New Roman",20), fg="white")
        self.label2.place(x=20,y=250)
        
        #Entry contrasena
        self.contrasenausuario=tk.StringVar()
        self.entry2=tk.Entry(self.frame1,textvariable=self.contrasenausuario,width=20,show='*',font=("Times New Roman",20))
        self.entry2.place(x=20,y=310,width=300,height=50)

        #Boton ingresar
        self.boton1=tk.Button(self.frame1,text="Ingresar",font=("Times New Roman",20), command=self.login)
        self.boton1.config(background="blueviolet",activebackground="light blue",activeforeground="Black",fg="White",bd=5) ##9321C4
        self.boton1.place(x=30,y=400,width=200,height=50)

        #### Frame Logo Nucleo lecheria

        self.frameLogo=tk.Frame(self.ventana1,bg="light blue",width=485,height=308)
        self.frameLogo.place(x=510, y= 170)

        imagen=PhotoImage(file="C:\\Users\\alviz\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\Tesis sistema de información\\image\\AN-N-LECHERÍAHorizontal485x308.png")
        fondo=tk.Label(self.frameLogo,image=imagen,bg="light cyan").place(x=0,y=0)
        

        
        #Mainloop
        self.ventana1.mainloop()

    def login(self):
     
        respuesta1=self.consultaSiexiste()
        if len(respuesta1)>0:
            #Dentro de esta condición se verifica los privilegios
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select b.funcion  from usuario a, tipo_usuario b where a.privilegio=b.privilegio AND a.nombre_usuario='"+self.nombreusuario.get()+"' AND a.contraseña='"+self.contrasenausuario.get()+"'"
            cursor.execute(sql)
            respuesta2=cursor.fetchall() #Recordar que esto es una lista plis
            verificar=respuesta2[0][0]
            cone.close()

            if verificar == "Administrador":
                #Enlace a las clase formularioadministrador
                mb.showinfo("Informacion", "Inicio de sesión exitosa, "+ self.nombreusuario.get()+" bienvenido administrador")
                self.usuario=self.nombreusuario.get()
                self.ventana1.destroy()
                self.mostrar_admin()

            if verificar  == "Profesor":
                #Enlace a las clase formularioprofesor
                mb.showinfo("Informacion", "Inicio de sesión exitosa, "+ self.nombreusuario.get()+" bienvenido profesor")
                self.usuario=self.nombreusuario.get()
                self.ventana1.destroy()
                self.mostrar_profe()
        else:
            mb.showwarning("Cuidado", "El usuario no existe")

    def abrir(self):

        conexion=mysql.connector.connect(host="localhost",
                                         user="root",
                                         passwd="", 
                                         database="bdnucleolecheria")
        return conexion
        
    def consultaSiexiste(self):
       try: 
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select nombre_usuario from usuario where nombre_usuario='"+self.nombreusuario.get()+"' AND contraseña='"+self.contrasenausuario.get()+"'"
            cursor.execute(sql)
            cone.close()
            return cursor.fetchall()
       except:
            mb.showerror("Error","No se puede establecer la conexión a la base de datos")

    #Llamada al formularioadmin
    def mostrar_admin(self):
        app=formularios.formularioadmin.Administrador(self.usuario)

    def mostrar_profe(self):
        app=formularios.formularioprofe.Profesor(self.usuario)