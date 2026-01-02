"""
Script para quitar el fondo de todas las imágenes en 'img/Nueva carpeta'
"""
import os
from pathlib import Path
from rembg import remove
from PIL import Image

# Directorio base
base_dir = Path(r"c:\Users\Core i7\Desktop\Trabajos\pagina guatera\img\Nueva carpeta")

# Extensiones de imagen soportadas
image_extensions = {'.png', '.jpg', '.jpeg', '.webp'}

# Contador de imágenes procesadas
processed = 0
errors = 0

# Recorrer recursivamente todos los archivos
for root, dirs, files in os.walk(base_dir):
    for file in files:
        file_path = Path(root) / file
        
        # Verificar si es una imagen
        if file_path.suffix.lower() in image_extensions:
            print(f"Procesando: {file_path.name}...", end=" ")
            
            try:
                # Abrir imagen
                with Image.open(file_path) as img:
                    # Convertir a RGBA si es necesario
                    if img.mode != 'RGBA':
                        img = img.convert('RGBA')
                    
                    # Quitar fondo
                    output = remove(img)
                    
                    # Guardar con el mismo nombre (sobreescribir)
                    output.save(file_path, 'PNG')
                    
                print("✓ Completado")
                processed += 1
                
            except Exception as e:
                print(f"✗ Error: {e}")
                errors += 1

print(f"\n{'='*50}")
print(f"Proceso finalizado:")
print(f"  - Imágenes procesadas: {processed}")
print(f"  - Errores: {errors}")
print(f"{'='*50}")
