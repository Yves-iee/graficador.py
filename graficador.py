import pandas as pd
import matplotlib.pyplot as plt

try:
    # Intentamos leer con coma, si falla intentamos con punto y coma
    try:
        df = pd.read_csv('repuestos.csv', sep=',', low_memory=False)
        if 'Clase de movimiento' not in df.columns:
            raise ValueError
    except:
        df = pd.read_csv('repuestos.csv', sep=';', low_memory=False)

    # Nombre exacto de tu columna según la foto
    columna_objetivo = 'Clase de movimiento'
    
    # Definir los códigos (301, 109, 206)
    codigos_interes = {
        301: 'Obsoletos (301)', 
        109: 'Sin Mov. (109)', 
        206: 'Mov. Mín. (206)'
    }
    
    # Limpieza de datos
    df[columna_objetivo] = pd.to_numeric(df[columna_objetivo], errors='coerce')
    conteos = df[columna_objetivo].value_counts()
    
    etiquetas = list(codigos_interes.values())
    cantidades = [int(conteos.get(c, 0)) for c in codigos_interes.keys()]

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    colores = ['#e74c3c', '#f1c40f', '#3498db']
    barras = plt.bar(etiquetas, cantidades, color=colores, edgecolor='black')
    
    for barra in barras:
        yval = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2, yval + 0.1, yval, ha='center', va='bottom', fontweight='bold')

    plt.title('Reporte de Repuestos Actualizado', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    
    # Guardar
    plt.savefig('grafica_actualizada.png', bbox_inches='tight')
    print("¡Gráfica generada con éxito!")

except Exception as e:
    print(f"Error detectado: {e}")
