from turtle import pd


def transformar_dim_tiempo(df):
    df['FECHA COMPRA'] = pd.to_datetime(df['FECHA COMPRA (DD/MM/AA)'], dayfirst=True)
    dim_tiempo = pd.DataFrame()
    dim_tiempo['fecha_compra'] = df['FECHA COMPRA']
    dim_tiempo['anio'] = df['FECHA COMPRA'].dt.year
    dim_tiempo['mes'] = df['FECHA COMPRA'].dt.month
    dim_tiempo['dia'] = df['FECHA COMPRA'].dt.day
    dim_tiempo = dim_tiempo.drop_duplicates().reset_index(drop=True)
    return dim_tiempo

def transformar_dim_vehiculo(df):
    dim_vehiculo = df[['MARCA', 'MODELO', 'AÑO MODELO', 'CLASE', 'SUB CLASE', 'TIPO COMBUSTIBLE', 'CATEGORÍA']].copy()
    for col in dim_vehiculo.columns:
        dim_vehiculo[col] = dim_vehiculo[col].astype(str).str.strip().str.upper()
    dim_vehiculo = dim_vehiculo.drop_duplicates().reset_index(drop=True)
    # Crear ID_Vehiculo como clave sustituta
    dim_vehiculo['ID_VEHICULO'] = dim_vehiculo.index + 1
    return dim_vehiculo

def transformar_dim_geografia(df):
    # Aquí debes crear un diccionario de cantones a provincias, ejemplo simplificado:
    cantones_a_provincias = {1: 'Pichincha', 2: 'Guayas', 3: 'Azuay'}  # Completar según datos reales
    dim_geo = df[['CANTÓN']].copy()
    dim_geo['PROVINCIA'] = dim_geo['CANTÓN'].map(cantones_a_provincias)
    dim_geo['PAIS'] = 'ECUADOR'  # Fijo para este caso
    dim_geo = dim_geo.drop_duplicates().reset_index(drop=True)
    # Crear ID_Geografia como clave sustituta
    dim_geo['ID_GEO'] = dim_geo.index + 1
    return dim_geo

def transformar_dim_propietario(df):
    dim_prop = df[['PERSONA NATURAL - JURÍDICA', 'TIPO TRANSACCIÓN', 'TIPO SERVICIO', 'COLOR 1', 'COLOR 2']].copy()
    for col in ['PERSONA NATURAL - JURÍDICA', 'TIPO TRANSACCIÓN', 'TIPO SERVICIO']:
        dim_prop[col] = dim_prop[col].str.strip().str.upper()
    dim_prop[['COLOR 1', 'COLOR 2']] = dim_prop[['COLOR 1', 'COLOR 2']].fillna('DESCONOCIDO').apply(lambda x: x.str.upper())
    dim_prop = dim_prop.drop_duplicates().reset_index(drop=True)
    # Crear ID_Propietario como clave sustituta
    dim_prop['ID_PROPIETARIO'] = dim_prop.index + 1
    return dim_prop
