# 📝 Proyecto Papeleria 📝

(Sirve para colocar la descrición de tu proyecto) 

* 1.- Objetivo: ¿Que buscas programar/simular? Simular un flujo de datos de una papeleria ficticia.
* 2.- Descripción: (a) Simulando la información de manera aleatoria con Random . . . (b) Montamos una base de datos . . . 
    (c) Automatizamos el flujo de datos implementando . . . 
* 3.- Resultado: Creamos nuestra porpia libreria para automatizar . . .  y obtuvimos al final un excel que ocupamos como como insumo para Powe BI
  
# Python 
# Power BI 

Reportamos el historico de las ventas usando tal grafico para ver tal cosa. . .
....
Library_Papeleria.py: Este archivo tiene el codigo de la clase tools . . .  tiene las funciones . . .  y es donde tenemos el flujo de datos. 

##  📝 Proyecto Papelería 📝 

Este proyecto simula un sistema de generación de ventas de una papelería con varias sucursales. 

### 🔹 Funcionalidades principales:
- **Generación de ventas diarias que osilan entre 10,000 y 20,000 al día** 
- **Almacenamiento de la base de atos creada para la simulación de venta de productos en las papelería** (`Ventas.db`).
- **Control de inserción de datos**:
  - `replace` → Crea o reinicia la tabla, la cual en este proyecto la llamamos `Ventas_2025`.
  - `append` → Esta función agrega información en una tabla ya existente, la cual utilizamos para no borrar los datos ya agregados.
- **Mas tarde integramos SQL para poder hacer consultas de la información generada de las ventas de la papeleria en sus diferentes sucursales.
- **Con la cual creamos un documento formato csv para poderlo manejar en Power Bi y de esta forma dar un informe de ventas. 

### 🔹 Paqueterias utilizadas:
- Pandas
- SQLite3
- Random (para simulación de datos)

### 🔹 Uso general de cada una de las paqueterias utilizadas:
- Pandas: Generar bases de datos de prueba para análisis.
- SQLite3: Practicar consultas SQL con información simulada.
- Random: Probar técnicas de análisis de datos con Pandas.
