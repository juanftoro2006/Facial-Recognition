# face_manager.py

"""
NOTA DE JUAN TORO: SE HA DETENIDO ESTE AVANCE DEL PROYECTO PORQUE 
SE DEBE TRABAJAR EN PUBLICAR EL PROYECTO EN GITHUB Y HACER UN MANUAL DE USO.
LAS MEJORAS QUE SE PUEDEN HACER SON:
- Implementar una interfaz gráfica de usuario (GUI) para facilitar la interacción.
- Añadir más modelos de reconocimiento facial y permitir al usuario elegir.
- Se modificará en bloque las imágenes para que no pesen tanto.
- Mejorar la gestión de errores y excepciones.

Script base para centralizar y gestionar funciones relacionadas con el reconocimiento facial.
Más adelante servirá como backend para integrarlo con un frontend o una API.
"""

# Importamos módulos necesarios
from pathlib import Path
import face_recognition
import pickle
from PIL import Image, ImageDraw, ImageOps, ImageFont
from collections import Counter

# Ruta por defecto para guardar/leer las codificaciones de rostros conocidos
DEFAULT_ENCODINGS_PATH = Path("output/encodings.pkl")

# Colores usados para dibujar sobre las imágenes
BOUNDING_BOX_COLOR = "blue"
TEXT_COLOR = "white"

# ---------------------------- #
# CARGA DE CODIFICACIONES
# ---------------------------- #
def load_encodings(encodings_path=DEFAULT_ENCODINGS_PATH):
    """
    Carga las codificaciones desde un archivo pickle.
    """
    with encodings_path.open("rb") as f:
        return pickle.load(f)

# ---------------------------- #
# RECONOCIMIENTO EN IMAGEN
# ---------------------------- #
def recognize_faces_from_image(image_path, model="hog"):
    """
    Reconoce rostros en una imagen dada y dibuja los resultados.
    """
    print(f"Procesando imagen: {image_path}")
    loaded_encodings = load_encodings()
    
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image, model=model)
    face_encodings = face_recognition.face_encodings(image, face_locations)

    # Corregimos la orientación si viene girada
    pillow_image = Image.fromarray(image)
    pillow_image = ImageOps.exif_transpose(pillow_image)
    draw = ImageDraw.Draw(pillow_image)

    for location, encoding in zip(face_locations, face_encodings):
        name = get_best_match(encoding, loaded_encodings)
        name = name if name else "Desconocido"
        draw_face(draw, location, name, font_size=22)  # Tamaño de letra ajustable

    pillow_image.show()

# ---------------------------- #
# MEJOR COINCIDENCIA DE ROSTRO
# ---------------------------- #
def get_best_match(unknown_encoding, loaded_encodings):
    """
    Compara un rostro desconocido con los conocidos y devuelve el nombre con más coincidencias.
    """
    matches = face_recognition.compare_faces(loaded_encodings["encodings"], unknown_encoding)
    votes = Counter(
        name for match, name in zip(matches, loaded_encodings["names"]) if match
    )
    return votes.most_common(1)[0][0] if votes else None

# ---------------------------- #
# DIBUJAR RECUADRO Y NOMBRE
# ---------------------------- #
def draw_face(draw, location, name, font_size=18):
    """
    Dibuja un recuadro y el nombre sobre la cara detectada con tamaño de fuente ajustable.
    """
    top, right, bottom, left = location
    draw.rectangle(((left, top), (right, bottom)), outline=BOUNDING_BOX_COLOR)

    # Intentamos usar una fuente TrueType (ej: Arial)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    draw.text((left, bottom + 5), name, fill=TEXT_COLOR, font=font)

# ---------------------------- #
# EJECUCIÓN DIRECTA DESDE TERMINAL
# ---------------------------- #
if __name__ == "__main__":
    # Prueba directa desde consola
    test_image = "validation/validacion-1.jpg"
    recognize_faces_from_image(test_image)
