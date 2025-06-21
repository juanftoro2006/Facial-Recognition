#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

# Lectura segura de README y HISTORY (si existen)
try:
    with open('README.rst') as readme_file:
        readme = readme_file.read()
except FileNotFoundError:
    readme = ''

try:
    with open('HISTORY.rst') as history_file:
        history = history_file.read()
except FileNotFoundError:
    history = ''

# Requisitos principales del proyecto
requirements = [
    'face_recognition_models>=0.3.0',
    'Click>=6.0',
    'dlib>=19.7',
    'numpy',
    'Pillow'
]

# Requisitos para pruebas y calidad
test_requirements = [
    'tox',
    'flake8'
]

setup(
    name='face_recognizer',  # Tu propio nombre de proyecto
    version='0.1.0',
    description="Proyecto de reconocimiento facial en Python usando dlib y face_recognition",
    long_description=readme + '\n\n' + history,
    author="Juan Fernando Toro Isaza",
    author_email='juanf.toroi@gmail.com',
    url='https://github.com/tu_usuario/face_recognizer',  # Reemplazá si querés
    py_modules=['detector', 'app'],  # Módulos que están sueltos en raíz
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='face recognition, python, dlib, reconocimiento facial',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Spanish',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
