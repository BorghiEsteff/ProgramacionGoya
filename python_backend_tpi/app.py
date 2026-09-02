productos = [
{"nombre":"Laptop", "precio":1200, "stock": 15},
{"nombre": "Mouse", "precio": 25, "stock": 5},
{"nombre": "Teclado", "precio": 75, "stock": 25},
{"nombre": "Monitor", "precio": 300, "stock": 8},
]
#print (productos [1] ["nombre"] ) #Imprime : mouse
#print (productos [2] ["precio"] ) #imprime : 75

# Crea una lista vacía para guardar los resultados.
#productos_bajo_stock = []
# Itera sobre cada elemento de la lista de productos.
#for producto in productos:
    # Imprime en consola el nombre y el precio.
    #print(f"Producto: {producto['nombre']}, Precio: ${producto ['precio']}")
    # Verifica si el stock es menor a 10 unidades.
    #if producto['stock'] < 10: 
        # Agrega el producto a la lista de resultados.
       # productos_bajo_stock.append(producto)       
# Imprime un título con un salto de línea previo.
#print("\nProductos con bajo stock:")
# Muestra la lista final ya filtrada.
#print(productos_bajo_stock)

# Define una función que recibe una lista como parámetro.
#def calcular_promedio_precio(lista):
    # Verifica si la lista está vacía.
 #   if not lista:
        # Retorna 0 para evitar un error de división por cero.
  #      return 0 
    # Suma los precios de todos los productos usando una expresión generadora.
   # total_precio = sum(p['precio'] for p in lista)
    # Calcula y devuelve el promedio (total dividido por la cantidad de elementos).
    #return total_precio / len(lista)
# Llama a la función pasándole la lista 'productos' y guarda el resultado.
#precio_promedio = calcular_promedio_precio(productos)
# Imprime el resultado con un salto de línea y limitado a 2 decimales (.2f).
#print(f"\nEl precio promedio de los productos es: ${precio_promedio:.2f}")

import csv
import os  # Importamos esta librería para manejar rutas de archivos

# 1. Calculamos la ruta exacta donde está guardado este código (app.py)
ruta_carpeta = os.path.dirname(os.path.abspath(__file__))

# 2. Unimos esa ruta con el nombre de nuestro archivo
ruta_csv = os.path.join(ruta_carpeta, 'datos.csv')

productos_desde_csv = []

# 3. Usamos la 'ruta_csv' segura en lugar de solo 'datos.csv'
with open(ruta_csv, mode='r', encoding="utf-8") as archivo_csv:
    lector_diccionario = csv.DictReader(archivo_csv)
    
    for fila in lector_diccionario:
        fila['id'] = int(fila['id'])
        fila['precio'] = int(fila['precio'])
        fila['stock'] = int(fila['stock'])
        
        productos_desde_csv.append(fila)

# Presentación visual
print("\n LISTA DE PRODUCTOS DESDE EL ARCHIVO CSV")
print("-" * 50)
print(f"{'ID':<5} | {'NOMBRE':<15} | {'PRECIO':<10} | {'STOCK':<5}")
print("-" * 50)

for p in productos_desde_csv:
    print(f"{p['id']:<5} | {p['nombre']:<15} | ${p['precio']:<9} | {p['stock']:<5}")
    
print("-" * 50)