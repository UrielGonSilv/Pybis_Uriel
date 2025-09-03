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

### 📝 Crear el DataFrame con la información generada. 

Este bloque de código se encarga de **guardar los datos generados en la base de datos**, así como de definir funciones para inicializar ventas, generar rangos de fechas y realizar consultas.

---

```python
df_2 = pd.DataFrame(dict_pre_ventas)
print(f"Información generada al {fecha} con éxito")
dict_pre_ventas → es el diccionario que contiene listas con los campos de cada venta (producto, cantidad, precio, etc.).

pd.DataFrame() → convierte ese diccionario en un DataFrame de Pandas, que es la estructura de datos tabular.

print(...) → confirma que la información fue creada para la fecha indicada.
```
2️⃣ Conexión con la base de datos SQLite
```python
conexion = sql.connect("Ventas.db")
```
Se conecta (o crea, si no existe) la base de datos Ventas.db en SQLite.

Esta base será el repositorio donde se guardarán todas las ventas ficticias.

3️⃣ Guardado en la tabla Ventas_2025
```python

if boolVentas == True:
    df_2.to_sql("Ventas_2025", conexion, if_exists="replace")
else:
    df_2.to_sql("Ventas_2025", conexion, if_exists="append")
```
Caso 1 (replace) → si boolVentas == True, significa que es la primera carga. Se reemplaza la tabla completa.

Caso 2 (append) → si boolVentas == False, significa que ya existe información previa. Los nuevos registros se agregan a la tabla existente.

📌 Esto permite simular ventas de un día o de muchos días sin borrar los datos anteriores.

4️⃣ Cerrar la conexión
```python

conexion.close()
print(f"Información subida a la bbdd al {fecha} con éxito")
```
Siempre se debe cerrar la conexión a la base de datos para evitar errores o bloqueos.

Se imprime un mensaje de confirmación indicando que la información se guardó con éxito.

🔧 Funciones auxiliares
Estas funciones permiten automatizar el proceso de generación de ventas y consultas.

5️⃣ inicializador(fecha)
```python

def inicializador(fecha):
    tools.generar_df_ventas(fecha, True)
```
Genera ventas para una sola fecha específica.

Llama a la función generar_df_ventas indicando que es la primera vez (True) → por lo tanto, se reemplaza la tabla.

6️⃣ rango_fechas(fecha1, fecha2)
```python

def rango_fechas(fecha1, fecha2):
    import pandas as pd
    rango_fechas = pd.date_range(start=fecha1, end=fecha2, freq="d")

    for fecha in rango_fechas:
        tools.generar_df_ventas(fecha, False)
```
Utiliza pd.date_range() para generar todas las fechas entre fecha1 y fecha2.

Por cada fecha en ese rango, se ejecuta la generación de ventas.

El parámetro False indica que los registros se apilan (append) en la tabla sin reemplazar los anteriores.

📌 Ejemplo: generar ventas del 1 al 7 de enero 2025.

7️⃣ consulta(sentenciaSQL)
```python
Copiar código
def consulta(sentenciaSQL):
    import pandas as pd
    import sqlite3 as sql
    
    conexion = sql.connect("Ventas.db")
    df_consulta = pd.read_sql_query(sentenciaSQL, conexion)
    conexion.close()

    return df_consulta
```
Permite ejecutar cualquier sentencia SQL sobre la base Ventas.db.

Devuelve el resultado en un DataFrame de Pandas, listo para análisis.

📌 Ejemplo de uso:

```python
Copiar código
df = consulta("""
    SELECT Sucursal, SUM(Total) as Ventas_Totales
    FROM Ventas_2025
    GROUP BY Sucursal
""")
print(df)
```
