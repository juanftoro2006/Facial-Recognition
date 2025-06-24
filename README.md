
# 🎯 Facial Recognition - Python Project

Este proyecto de reconocimiento facial fue originalmente desarrollado por terceros como una solución educativa. Mi aporte consistió en adaptarlo a mi entorno de trabajo, resolver dependencias específicas en mi equipo y hacerlo completamente funcional con asistencia de herramientas de inteligencia artificial. Fue uno de mis primeros acercamientos al uso práctico de modelos de visión computacional en Python, y me permitió entender a fondo la integración de bibliotecas como dlib, face_recognition y OpenCV.


## 🚀 Características principales

- ✅ Detección facial con modelos **HOG** o **CNN**.
- 🧠 Reconocimiento personalizado con entrenamiento previo.
- 🖼️ Soporte para imágenes locales y **cámara en vivo**.
- 🧩 Arquitectura modular y fácil de mantener o extender.

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

Desde la terminal:

```bash
python detector.py imagen.jpg
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