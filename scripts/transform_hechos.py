from turtle import pd


def transform_hechos(df, dim_vehiculo, dim_geo, dim_prop, dim_tiempo):
    fact = df.copy()
    # Convertir campos numéricos
    fact['AVALÚO'] = pd.to_numeric(fact['AVALÚO'].str.replace(',', ''), errors='coerce').fillna(0)
    fact['CILINDRAJE'] = pd.to_numeric(fact['CILINDRAJE'], errors='coerce').fillna(0)
    
    # Crear columna de conteo
    fact['CONTEO'] = 1
    
    # Merge con dimensiones para obtener claves sustitutas
    fact = fact.merge(dim_vehiculo, how='left', left_on=['MARCA', 'MODELO', 'AÑO MODELO', 'CLASE', 'SUB CLASE', 'TIPO COMBUSTIBLE', 'CATEGORÍA'],
                      right_on=['MARCA', 'MODELO', 'AÑO MODELO', 'CLASE', 'SUB CLASE', 'TIPO COMBUSTIBLE', 'CATEGORÍA'])
    fact = fact.merge(dim_geo, how='left', left_on='CANTÓN', right_on='CANTÓN')
    fact = fact.merge(dim_prop, how='left', left_on=['PERSONA NATURAL - JURÍDICA', 'TIPO TRANSACCIÓN', 'TIPO SERVICIO', 'COLOR 1', 'COLOR 2'],
                      right_on=['PERSONA NATURAL - JURÍDICA', 'TIPO TRANSACCIÓN', 'TIPO SERVICIO', 'COLOR 1', 'COLOR 2'])
    
    # Merge con dim_tiempo por fecha
    fact['FECHA COMPRA'] = pd.to_datetime(fact['FECHA COMPRA (DD/MM/AA)'], dayfirst=True)
    fact = fact.merge(dim_tiempo, how='left', left_on='FECHA COMPRA', right_on='fecha_compra')
    
    # Seleccionar solo columnas relevantes para la tabla de hechos
    fact_final = fact[['ID_VEHICULO', 'ID_GEO', 'ID_PROPIETARIO', 'anio', 'mes', 'dia', 'AVALÚO', 'CILINDRAJE', 'CONTEO']]
    return fact_final