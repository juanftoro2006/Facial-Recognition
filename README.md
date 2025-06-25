
# 🎯 Facial Recognition - Python Project

Este proyecto de reconocimiento facial fue originalmente desarrollado por terceros como una solución educativa. Mi aporte consistió en adaptarlo a mi entorno de trabajo, resolver dependencias específicas en mi equipo y hacerlo completamente funcional con asistencia de herramientas de inteligencia artificial. Fue uno de mis primeros acercamientos al uso práctico de modelos de visión computacional en Python, y me permitió entender a fondo la integración de bibliotecas como dlib, face_recognition y OpenCV.

Este proyecto fue clave para entender cómo funciona la visión por computador. Tuve retos técnicos, como instalar correctamente las librerías, pero logré superar cada uno. Me ayudó a ganar confianza en la manipulación de video en tiempo real y el uso de modelos preentrenados.



## 🚀 Características principales

- ✅ Detección facial con modelos **HOG** o **CNN**.
- 🧠 Reconocimiento personalizado con entrenamiento previo.
- 🖼️ Soporte para imágenes locales y **cámara en vivo**.
- 🧩 Arquitectura modular y fácil de mantener o extender.
- ✅ Detección de rostros en tiempo real desde cámara web.
- ✅ Reconocimiento facial comparando con imágenes almacenadas.
- ✅ Ejecución local sin necesidad de conexión a internet.



## 📦 Requisitos

- Python 3.8 o superior
- `dlib`
- `face_recognition`
- `numpy`
- `Pillow`
- `opencv-python`

Puedes instalar las dependencias con:

```bash
pip install -r requirements.txt
```

## ▶️ Uso


1. Clona el repositorio:
   git clone https://github.com/tu_usuario/face-recognition-app.git

2. Instala las dependencias:
   pip install -r requirements.txt

3. Ejecuta el script:
   python app.py

Asegúrate de tener una cámara activa y permisos habilitados.


## 🚀 Comandos para ejecutar el programa

A continuación te muestro cómo correr cada una de las funcionalidades principales del proyecto de reconocimiento facial:

---

### 🔧 Entrenamiento
Escanea las imágenes en la carpeta `known_faces/` para registrar los rostros conocidos:

```bash
python detector.py --train -m hog
````

📌 El parámetro `-m` indica el modelo de detección:

* `hog`: más rápido y compatible con CPU
* `cnn`: más preciso pero requiere GPU (CUDA)

---

### 🔍 Validación

Valida que los rostros entrenados se hayan procesado correctamente:

```bash
python detector.py --validate
```

---

### 🧪 Prueba con imagen desconocida

Compara una imagen con los rostros registrados para intentar identificarla:

```bash
python detector.py --test -f unknown.jpg
```

📌 Asegúrate de que la imagen `unknown.jpg` esté en el directorio raíz o especifica la ruta correcta con `-f`.

---

### 🗂️ Estructura esperada del directorio `known_faces/`

```
known_faces/
├── juan/
│   └── juan1.jpg
├── maria/
│   └── maria1.jpg
```

Cada subcarpeta debe tener el nombre de la persona y al menos una imagen del rostro.

---

### 💡 Recomendaciones

* Usa imágenes bien iluminadas, enfocadas y con el rostro centrado.
* Para mejor rendimiento en CPU, utiliza el modelo `hog`.
* Si optas por `cnn`, asegúrate de tener una GPU compatible con CUDA.
* Verifica que la cámara esté activa y que tu sistema tenga los permisos adecuados.

---

```

También puedes ejecutarlo desde un entorno como **VS Code** o **PyCharm**.


## 🧪 Estructura sugerida

```
Facial-Recognition/
├── src/                    # Código fuente
├── data/                   # Imágenes de entrada
├── models/                 # Modelos entrenados
├── detector.py             # Script principal
├── README.md
├── .gitignore
└── requirements.txt
```

## 🙋‍♂️ Autor

**Juan Fernando Toro Isaza**  
Adaptación y desarrollo del sistema de reconocimiento facial con fines educativos y exploratorios.
```