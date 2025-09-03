<h3 align="center">📝 Proyecto Papelería 📝</h3>

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

 ### 📂 Las listas que definimos para crear la información de las ventas en la papelería: 📂

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
  
### 📦 Inicialización de listas vacías 📦

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
## 🎓 Creación de las variables con el primer "for" del codigo. 🎓 

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

La estructura resutante de este codigo es mas o menos la siguiente: 

```python
{
    "Fecha": [fecha1, fecha2, fecha3, ..., fechaN],
    "Producto": [producto1, producto2, producto3, ..., productoN],
    "Clave": [clave1, clave2, clave3, ..., claveN],
    "Cantidad": [cantidad1, cantidad2, cantidad3, ..., cantidadN],
    "Precio": [precio1, precio2, precio3, ..., precioN],
    "Total": [total1, total2, total3, ..., totalN],
    "Sucursal": [sucursal1, sucursal2, sucursal3, ..., sucursalN]
}
```
En el cual se estria agregando la información de cada variable con el "bucle for" que se genero.

### 📝 Creación del DataFrame con la información de ventas generada. 📝

En esta parte del código se encarga de **guardar los datos generados en la base de datos**, así como de definir funciones para inicializar ventas, generar rangos de fechas y realizar consultas de las ventas generadas.

---

```python
df_2 = pd.DataFrame(dict_pre_ventas)
print(f"Información generada al {fecha} con éxito")
```

dict_pre_ventas → Es el diccionario que contiene listas de cada venta (producto, cantidad, precio, etc.).

pd.DataFrame() → Convierte ese diccionario en un DataFrame o una tabla con la información de las ventas. 

print(f"Información generada al {fecha} con éxito") → confirma que la información fue creada para la fecha indicada.

## 🎓 Conexión con la base de datos SQLite 🎓

```python
conexion = sql.connect("Ventas.db")
```
Se conecta o se crea si no existe la información, la base de datos Ventas.db en SQLite.

Esta base será el repositorio donde se guardarán todas las ventas.

## 🫙Guardado en la tabla Ventas_2025 🫙

En esta parte del codigo usaremos las funciones de "replace" y "append", para asi poder cargar la información de las ventas diarias de las papeleria y ademas irlas agregando a nuestra base de datos. 

```python

if boolVentas == True:
    df_2.to_sql("Ventas_2025", conexion, if_exists="replace")
else:
    df_2.to_sql("Ventas_2025", conexion, if_exists="append")
```

En el primer caso se usa (replace) al final y → si boolVentas == True → Significa que es la primera carga. Se reemplaza la tabla completa.

En el segundocaso usando (append) → si boolVentas == False → Significa que ya existe información previa así que los nuevos registros se agregan a la tabla existente.

Esto permite simular ventas de un día o de muchos días sin borrar los datos de ventas anteriores.

## 🔐 Cerrar la conexión 🔐

```python
conexion.close()
print(f"Información subida a la bbdd al {fecha} con éxito")
```
Siempre se debe cerrar la conexión a la base de datos para evitar errores o bloqueos.

Se imprime un mensaje de confirmación indicando que la información se guardó con éxito en la base de datos. 

## 📄Ultimas funciones para poder usar la información del dataframe y crear consultas para su manipulación con SQL.📄

Estas funciones permiten automatizar el proceso de generación de ventas y consultas.

- Inicializador(fecha)

```python
def inicializador(fecha):
    tools.generar_df_ventas(fecha, True)
```
Genera ventas para una sola fecha específica.

Llama a la función "generar_df_ventas" indicando que es la primera vez (True) → por lo tanto, se reemplaza la tabla.

- La siguiente linea de codigo "rango_fechas(fecha1, fecha2)" se crea para crear información de fechas con ventas entre dos fechas en especifico. 

```python
def rango_fechas(fecha1, fecha2):
    import pandas as pd
    rango_fechas = pd.date_range(start=fecha1, end=fecha2, freq="d")

    for fecha in rango_fechas:
        tools.generar_df_ventas(fecha, False)
```

- Utilizamos "pd.date_range()" para generar todas las fechas entre fecha1 y fecha2.

Por cada fecha en ese rango, se ejecuta la generación de ventas.

La función "append" indicando siempre con un  "False" los registros se apilan o se agregan en la tabla sin reemplazar los anteriores.

- Utilización de "consulta(sentenciaSQL)"

```python

def consulta(sentenciaSQL):
    import pandas as pd
    import sqlite3 as sql
    
    conexion = sql.connect("Ventas.db")
    df_consulta = pd.read_sql_query(sentenciaSQL, conexion)
    conexion.close()

    return df_consulta
```
Permite ejecutar cualquier sentencia SQL sobre la base Ventas.db.

Devuelve el resultado en un DataFrame de Pandas, listo para análisis o sus consultas. 

<h3 align="center">🎓🎓🎓Resultado 🎓🎓🎓</h3>
 
### 📦 Creación de la librería **lpym** 📦

Creamos nuestra propia librería llamada **`lpym`**, con el objetivo de **automatizar los procesos de consultas** y facilitar la creación de una base de datos con los datos de ventas simuladas generados en el código. Los resultados se guardaron en **formato CSV**, ya que este tipo de archivo permite almacenar grandes cantidades de información de manera estructurada y compatible con diversas herramientas.  

Este archivo CSV fue utilizado como insumo para **Power BI**, lo que nos permitió construir reportes interactivos de las ventas:  
- 📅 **Diarias**  
- 📈 **Mensuales**  
- 📊 **Anuales**  

De esta manera, logramos conectar la simulación de datos con una herramienta de análisis real, mostrando visualmente el comportamiento de las ventas.

## 📂 Archivos del proyecto 📂

- **lpym.py**
  
Contiene el código de la clase **`tools`**, la cual incluye las funciones necesarias para simular las ventas de las diferentes papelerías.  
  A partir de estas simulaciones se obtiene un flujo de datos que se almacena en una base de datos, lo que permite:  
  - Manipular la información.  
  - Generar informes sobre las ventas.  
  - Consultar y analizar los datos almacenados.  

---

- **Reporte de ventas papeleria.png**
  
  Este archivo muestra el informe **"Histórico de Ventas - Julio"**, que incluye:  
  - 📈 Una gráfica con las fluctuaciones de ventas de las diferentes sucursales.  
  - 📊 La visualización **"Suma de Total por Sucursal"**, donde se observa que la sucursal con mayores ventas en julio fue **C.U.**, con **1.61 mil millones** de unidades monetarias.  
  - 🔎 Dos filtros interactivos:  
    - **Filtro por fecha** → permite consultar ventas de un día específico o de un rango de días.  
    - **Filtro por sucursal** → facilita la búsqueda de ventas de una sucursal en particular.  

---

- **Reporte de ventas papeleria 2.png**
  
  Este archivo muestra la gráfica **"Suma de Total por Producto"**, presentada en forma de barras:  
  - El eje **X** representa los productos vendidos en la papelería.  
  - El eje **Y** indica la cantidad total vendida de cada producto.  
  - Incluye los mismos filtros por **fecha** y por **sucursal**, lo que facilita el análisis detallado de la información.  


