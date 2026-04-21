import pandas as pd
import matplotlib.pyplot as plt

try:
    # Intentamos leer el archivo detectando automáticamente si usa coma o punto y coma
    df = pd.read_csv('repuestos.csv', sep=None, engine='python', encoding='latin-1')
    
    # Limpiamos los nombres de las columnas por si tienen espacios invisibles
    df.columns = df.columns.str.strip()
    
    columna = 'Clase de movimiento'
    
    if columna not in df.columns:
        print(f"Error: No encuentro la columna '{columna}'")
        print(f"Columnas detectadas: {df.columns.tolist()}")
    else:
        # Convertimos a números y contamos
        df[columna] = pd.to_numeric(df[columna], errors='coerce')
        codigos = {301: 'Obsoletos', 109: 'Sin Mov (2 años)', 206: 'Mov Minimo'}
        
        counts = df[columna].value_counts()
        labels = list(codigos.values())
        values = [int(counts.get(k, 0)) for k in codigos.keys()]

        # Creamos la gráfica
        plt.figure(figsize=(10, 6))
        plt.bar(labels, values, color=['#ff4d4d', '#ffa64d', '#4dabff'])
        plt.title('Reporte de Repuestos')
        plt.ylabel('Cantidad')
        
        # Guardamos la imagen
        plt.savefig('grafica_actualizada.png')
        print("¡Gráfica creada con éxito!")

except Exception as e:
    print(f"Error: {e}")
