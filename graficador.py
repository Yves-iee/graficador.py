import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el archivo de datos
try:
    # Cargamos el archivo que ya subiste
    df = pd.read_csv('repuestos.csv', low_memory=False) 
    
    # 2. Definir los códigos de interés
    # 301: Obsoletos, 109: Sin movimiento, 206: Movimiento mínimo
    codigos_interes = {
        301: 'Obsoletos (301)', 
        109: 'Sin Mov. (109)', 
        206: 'Mov. Min. (206)'
    }
    
    # 3. Limpiar la columna 'clase de movimiento'
    # Convertimos a número para evitar errores si vienen como texto
    df['clase de movimiento'] = pd.to_numeric(df['clase de movimiento'], errors='coerce')
    
    # Contar cuántas veces aparece cada código
    conteos = df['clase de movimiento'].value_counts()
    
    # Organizar los datos para la gráfica
    etiquetas = list(codigos_interes.values())
    cantidades = [int(conteos.get(c, 0)) for c in codigos_interes.keys()]

    # 4. Configurar la gráfica
    plt.figure(figsize=(10, 6))
    colores = ['#e74c3c', '#f1c40f', '#3498db'] # Rojo, Amarillo, Azul
    barras = plt.bar(etiquetas, cantidades, color=colores, edgecolor='black')
    
    # Poner el número sobre cada barra
    for barra in barras:
        yval = barra.get_height()
        plt.text(barra.get_x() + barra.get_width()/2, yval + 0.1, yval, ha='center', va='bottom', fontweight='bold')

    plt.title('Reporte de Repuestos: Obsoletos y Sin Movimiento', fontsize=14)
    plt.ylabel('Cantidad de Repuestos')
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    
    # 5. Guardar la imagen
    plt.savefig('grafica_actualizada.png', bbox_inches='tight')
    print("¡Gráfica generada con éxito!")

except Exception as e:
    print(f"Error procesando los datos: {e}")
