class tools:

  def generar_df_ventas(fecha, boolVentas):
    import pandas as pd
    import sqlite3 as sql
    import random as r
    abcdario = [
      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
      'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
      'U', 'V', 'W', 'X', 'Y', 'Z'
      ]

    papelerias = [
      'Xochimilco', 'Cuemanco', 'Coapa', 'Milpa Alta',
      'CU', 'Zócalo', 'Narvarte', 'Santa Fé', 'Polanco',
      'Centro'
      ]

    lineas = [
        'Cuadernos', 'Libretas', 'Lápices', 'Plumones', 'Borradores', 'Sacapuntas',
        'Laptops', 'Tablets', 'Mochilas', 'Bolsas', 'Cajas', 'Pegamento', 'Tijeras',
        'Monitores', 'Teclados', 'Mouse', 'Audífonos', 'Cables', 'Cargadores', 'Baterías',
        'Pc', 'Uniformes', 'Pinturas', 'Pinceles', 'Papel', 'Cartulinas'
        ]

    fechas = []
    productos = []
    claves = []
    cantidades = []
    precios = []
    totales = []
    sucursales = []

    for i in range(1, r.randint(1001, 20001)):
        # Zona de definicion de variables
        producto = r.choice(lineas)
        clave = r.choice(abcdario) + r.choice(abcdario) + r.choice(abcdario) + '-' + str(r.randint(1, 9)) + str(r.randint(1, 9)) + str(r.randint(1, 9))
        cantidad = r.randint(1, 50)
        precio = round(r.randint(1, 10000) * r.random(), 2)
        total = round(precio * cantidad, 2)
        sucursal = r.choice(papelerias)

        # Agregamos los datos a las listas
        fechas.append(fecha)
        productos.append(producto)
        claves.append(clave)
        cantidades.append(cantidad)
        precios.append(precio)
        totales.append(total)
        sucursales.append(sucursal)

    dict_pre_ventas = {
        # clave: valores asociados
        "Fecha": fechas,
        "Producto": productos,
        "Clave": claves,
        "Cantidad": cantidades,
        "Precio": precios,
        "Total": totales,
        "Sucursal": sucursales
    }

    df_2 = pd.DataFrame(dict_pre_ventas)

    print(f"Información generada al {fecha} con éxito")

    # =========================================================================

    conexion = sql.connect("Ventas.db")

    if boolVentas == True:
      # accion 1: crear la tabla por primera vez
      df_2.to_sql("Ventas_2025", conexion, if_exists="replace")
    else:
      # accion 2: apilamos la info
      df_2.to_sql("Ventas_2025", conexion, if_exists="append")

    # Cerramos la conexion
    conexion.close()

    print(f"Información subida a la bbdd al {fecha} con éxito")
  def inicializador(fecha):
    tools.generar_df_ventas(fecha, True)
    
  def rango_fechas(fecha1, fecha2):
    import pandas as pd
    # pd.date_range(start=f1, end=f2, freq="d"): genera un rango de fechas entre la fecha
    # f1 y f2 de manera diaria
    rango_fechas = pd.date_range(start=fecha1, end=fecha2, freq="d")

    # Despues de generar el rango de fechas, lo recorremos
    # y ejecutamos nuestra funcion
    for fecha in rango_fechas:
      tools.generar_df_ventas(fecha, False)

  def consulta(sentenciaSQL):
    import pandas as pd
    import sqlite3 as sql
    # ==========================================
    #             CONSULTAS EN SQL
    # ==========================================
    # 1. realizamos la conexion
    conexion = sql.connect("Ventas.db")

    # 2. Accedemos a la info mediante pandas
    df_consulta = pd.read_sql_query(sentenciaSQL, conexion)

    # 3. Cerramos la conexion
    conexion.close()

    return df_consulta