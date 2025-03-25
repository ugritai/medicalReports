# %%
import os
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
#import dask.dataframe as dd

# %%
# CARGAR DATOS EN SUBCONJUNTOS
# Ruta principal donde están las carpetas con los CSV
ruta_principal = r"/home/raulmartinez/medicalReports/mimic-iv-3.1"

# Función para leer archivos y dividirlo en dos subconjuntos
def cargar_y_dividir_datos(ruta_modulo):
    archivos = [archivo for archivo in os.listdir(ruta_modulo) if archivo.endswith(".gz")]
    total_archivos = len(archivos)
    tam_subconjunto = total_archivos // 4

    for i, archivo in enumerate(archivos):
        ruta_gz = os.path.join(ruta_modulo, archivo)
        nombre_tabla = archivo.replace(".csv.gz", "")  # Nombre de la tabla sin la extensión

        if i < tam_subconjunto:
            parte = "subconjunto1"
        elif i < 2*tam_subconjunto:
            parte = "subconjunto2"
        elif i < 3*tam_subconjunto:
            parte = "subconjunto3"
        else:
            parte = "subconjunto4"
        
        print(f"Procesando: {nombre_tabla} ({parte})")
        
        df = pd.read_csv(ruta_gz, compression="gzip", low_memory=False)
        df.to_csv(f"datasets/icu/{parte}_{nombre_tabla}.csv", index=False)
        print(f"Guardado: {parte}_{nombre_tabla}.csv ({df.shape[0]} filas)")

# Cargar datos de hosp
ruta_icu = os.path.join(ruta_principal, "icu")
print ("Cargando datos de icu...")
cargar_y_dividir_datos(ruta_icu)


