# Título: Sistema de información para la gestión administrativa de una fundación musical

# Resúmen

La presente tesis está enfocada en el área de Ingeniería de Sistemas, tiene como objetivo desarrollar un sistema de información que permita realizar la gestión administrativa de la fundación musical núcleo Lechería. El personal administrativo tendrá un mayor control en la información referente a instrumentos disponibles, las calificaciones, asistencias y población estudiantil, al igual que un control de los profesores en la institución; por otro lado los profesores tendrán la facultad de llevar un control de asistencias y calificar el rendimiento estudiantil sin llegar a perder la información durante el año escolar. Dentro de las herramientas implementadas para delimitar los problemas, se utilizó la entrevista no estructurada y la observación directa para la obtención de los parámetros para la solución del problema presentado. Para el desarrollo del proyecto se empleó la metodología Proceso Racional Unificado (RUP), en conjunto con el anterior se utilizó el Lenguaje Unificado de Modelado (UML) como técnica de diagramación para representar el diseño del sistema. Se utilizó el lenguaje de programación Python, en conjunto con el sistema de gestión de base de datos MySQL para desarrollar el sistema de información.

## Herramientas de desarrollo

En una breve descripción del sistema de información implementado, se presenta como una aplicación de escritorio. Provista de su base de datos estructurada con su gestor **XAMPP - PHPMyAdmin**, donde su base de datos se importa de manera sencilla y manejable a través de los archivos. Utilizando como capa operativa, nombramos el lenguaje de programación **Python** para crear el entorno Frontend con las librerias *Tkinter*. Encargado también de la comunicación Backend entre **MySQL** y la interacción del usuario con el entorno por cada información requerida.

## Manual de usuario

Se contempla el manual del usuario (Dentro del repositorio) para el correcto manejo del sistema de información. Las rutas y opciones son explicadas de manera detallada con sus propias imágenes referenciales. 

### Despliegue del sistema

  1. Instalación de [XAMPP](https://www.apachefriends.org/es/download.html).
  
     Se debe contemplar el uso de PHPmyAdmin, el servidor apache y el servidor MySQL. Por lo tanto, se instala en el ordenador dicha distribución donde va a ejecutar el sistema.
  
  2. Despliegue de la base de datos.
  
      Finalizada la instalación, se activa el servidor local apache y el MySQL para posteriormente exportar la estructura de la [base de datos](https://github.com/alvizu9633/tesisSImusic/tree/main/Base%20de%20datos/Estructura) que se encuentra dentro del repositorio.
      
  3. Instalación del lenguaje de programación [Python](https://www.python.org/downloads/) versión 2.6 o superior.
  
      Posteriormente, se instala el lenguaje de programación requerido, para que el sistema pueda ejecutarse en el escritorio del dispositivo.
      
  4. Ejecución del archivo *principal.py*.
  
      Para finalizar se da inicio al programa en el archivo **principal.py** (Dentro del manual de usuario se logra comprender el cómo manejar el sistema en su totalidad).
