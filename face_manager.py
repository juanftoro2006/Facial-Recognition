# face_manager.py
"""

NOTA DE JUAN TORO:   SE HA DETENIDO ESTE AVANCE DEL PROYECTO POR QUE 
SE DEBE TRABAJAR EN PUBLICAR EL PROYECTO EN GITHUB Y HACER UN MANUAL DE USO.
LAS MEJORAS QUE SE PUEDEN HACER SON:
- Implementar una interfaz gráfica de usuario (GUI) para facilitar la interacción.
- Añadir más modelos de reconocimiento facial y permitir al usuario elegir.
- Se modificara en bloque las imagenes para que no pesen tanto.
- Mejorar la gestión de errores y excepciones.



Script base para centralizar y gestionar funciones relacionadas con el reconocimiento facial.
Más adelante servirá como backend para integrarlo con un frontend o una API.



"""

# Importamos módulos necesarios
from pathlib import Path
import face_recognition
import pickle
from PIL import Image, ImageDraw, ImageOps
from collections import Counter

# Ruta por defecto para guardar/leer las codificaciones de rostros conocidos
DEFAULT_ENCODINGS_PATH = Path("output/encodings.pkl")

# Colores usados para dibujar sobre las imágenes
BOUNDING_BOX_COLOR = "blue"
TEXT_COLOR = "white"

# Función para cargar las codificaciones entrenadas
def load_encodings(encodings_path=DEFAULT_ENCODINGS_PATH):
    """
    Carga las codificaciones desde un archivo pickle.
    """
    with encodings_path.open("rb") as f:
        return pickle.load(f)

# Función para reconocer rostros en una imagen
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
        draw_face(draw, location, name)

    pillow_image.show()

# Función que compara un rostro desconocido con los conocidos
def get_best_match(unknown_encoding, loaded_encodings):
    matches = face_recognition.compare_faces(loaded_encodings["encodings"], unknown_encoding)
    votes = Counter(
        name for match, name in zip(matches, loaded_encodings["names"]) if match
    )
    return votes.most_common(1)[0][0] if votes else None

# Dibuja el recuadro y nombre sobre la imagen
def draw_face(draw, location, name):
    top, right, bottom, left = location
    draw.rectangle(((left, top), (right, bottom)), outline=BOUNDING_BOX_COLOR)
    draw.text((left, bottom + 5), name, fill=TEXT_COLOR)

# Prueba rápida (modo script directo)
if __name__ == "__main__":
    # Acá podrías probar directamente desde consola
    test_image = "validation/validacion-1.jpg"
    recognize_faces_from_image(test_image)
