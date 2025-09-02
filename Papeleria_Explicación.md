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
- Mas tarde integramos SQL para poder hacer consultas de la información generada de las ventas de la papeleria en sus diferentes sucursales.
- Con la cual creamos un documento formato csv para poderlo manejar en Power Bi y de esta forma dar un informe de ventas. 

### 🔹 Paqueterias utilizadas:
- Pandas
- SQLite3
- Random (para simulación de datos)

### 🔹 Uso general de cada una de las paqueterias utilizadas:
- Pandas: Generar bases de datos de prueba para análisis.
- SQLite3: Practicar consultas SQL con información simulada.
- Random: Probar técnicas de análisis de datos con Pandas.

 ### 📂 Las listas que definimos para crear la información de las ventas en la papelería: 

Para la generación de ventas ficticias se definieron tres listas principales:

- **Sucursales (`papelerias`)**  
  Contiene los nombres de las delegaciones en donde se encuentran las sucursales ficticias de papelerias simuladas, donde se realizan las ventas.  
  ```python
   papelerias = [
    'Xochimilco', 'Cuemanco', 'Coapa', 'Milpa Alta',
    'CU', 'Zócalo', 'Narvarte', 'Santa Fé', 'Polanco',
    'Centro'
  ]
  ``` 

- **Productos (`lineas`)**  
  Esta lista contiene la información de los productos que se venden en cada una de las papelerias.  
    ```python
    lineas = [
    'Cuadernos', 'Libretas', 'Lápices', 'Plumones', 'Borradores', 'Sacapuntas',
    'Laptops', 'Tablets', 'Mochilas', 'Bolsas', 'Cajas', 'Pegamento', 'Tijeras',
    'Monitores', 'Teclados', 'Mouse', 'Audífonos', 'Cables', 'Cargadores', 'Baterías',
    'Pc', 'Uniformes', 'Pinturas', 'Pinceles', 'Papel', 'Cartulinas' ] 
    ```

- **Abecedario (`abcdario`)**  
  Incluye todas las letras de la A a la Z en mayúsculas.  
  Su función es **generar claves únicas de producto** combinando letras y números, imitando un código de inventario o SKU.  
  ```python
  abcdario = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z' ]
  ```
  
### 📦 Inicialización de listas vacías

Antes de generar las ventas de los productos, se crean listas vacías que funcionarán como contenedores.  
Cada una almacenará un tipo de información específica que se completará dentro del bucle `for`.

```python
# Guardará la fecha en la que ocurre cada venta
fechas = []

# Guardará el nombre del producto vendido
productos = []

# Guardará la clave única de cada producto (Por ejemplo: "ABC-123")
claves = []

# Guardará la cantidad de productos vendidos
cantidades = []

# Guardará el precio unitario del producto
precios = []

# Guardará el total de cada venta (cantidad * precio)
totales = []

# Guardará el nombre de la sucursal donde ocurrió la venta
sucursales = []
```
## 🎓 Creación de las variables con el primer "for" del codigo. 

En esta parte del codigo se creo el primer "for" para poder crear las ventas aleatorias de las sucursales, definiendo cada variable y su contenido. 

```python
for i in range(1, r.randint(1001, 20001)):
    # Zona de definición de variables
    producto = r.choice(lineas)
    clave = r.choice(abcdario) + r.choice(abcdario) + r.choice(abcdario) + '-' + str(r.randint(1, 9)) + str(r.randint(1, 9)) + str(r.randint(1, 9))
    cantidad = r.randint(1, 50)
    precio = round(r.randint(1, 10000) * r.random(), 2)
    total = round(precio * cantidad, 2)
    sucursal = r.choice(papelerias)
```
Despues agregamos la información generada en cada una de las listas con la función ".append", como se muestra en el siguiente codigo: 

```python
 fechas.append(fecha)
        productos.append(producto)
        claves.append(clave)
        cantidades.append(cantidad)
        precios.append(precio)
        totales.append(total)
        sucursales.append(sucursal)
```
Se crea un diccionario donde cada clave (productos, claves, cantidades, precios, totales, sucursales), la cual representa una categoría de datos y su valor es la lista completa de estos: 
```python
dict_pre_ventas = {
        # clave: valores asociados
        "Fecha": fechas,
        "Producto": productos,
        "Clave": claves,
        "Cantidad": cantidades,
        "Precio": precios,
        "Total": totales,
        "Sucursal": sucursales
```
