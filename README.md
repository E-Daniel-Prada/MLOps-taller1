# FastAPI ML Service

Este repositorio contiene un ejercicio de ejemplo que expone un modelo de Machine Learning a través de una API implementada con [FastAPI](https://fastapi.tiangolo.com/) y desplegada en un contenedor [Docker](https://www.docker.com/).


# Integrantes del Grupo
Juan Pérez
María García
Carlos Rodríguez


## Tabla de Contenidos

- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación y Ejecución](#instalación-y-ejecución)
- [Uso de la API](#uso-de-la-api)
- [Integrantes del Grupo](#integrantes-del-grupo)

## Estructura del Proyecto

La estructura de carpetas y archivos es la siguiente:

taller1/ # Directorio raíz del proyecto ├── app/ # Código fuente de la API │ ├── init.py # Indica que 'app' es un paquete Python │ ├── main.py # Punto de entrada de la aplicación │ ├── models/ # Carpeta para el modelo de IA │ │ ├── init.py # (Opcional) Permite tratar 'models' como paquete │ │ └── model.pkl # Modelo serializado (puede ser .pkl, .onnx, etc.) │ └── routes/ # Carpeta para los endpoints de la API │ ├── init.py # (Opcional) Permite tratar 'routes' como paquete │ ├── predict.py # Endpoint para realizar predicciones │ └── health.py # Endpoint para verificar el estado de la API ├── requirements.txt # Lista de dependencias del proyecto ├── Dockerfile # Instrucciones para construir la imagen Docker └── README.md # Este archivo

> **Importante:**  
> Construir la imagen Docker desde el directorio raíz del proyecto (donde se encuentra el archivo `Dockerfile`), de modo que se copie toda la estructura y se reconozcan correctamente los paquetes.

## Requisitos

- [Docker](https://www.docker.com/) instalado en la máquina donde se ejecutará.

## Instalación y Ejecución

### 1. Construir la Imagen Docker

Desde el directorio raíz del proyecto (`taller1`), ejecuta el siguiente comando:

```bash
docker build -t fastapi-ml-service .
```

Ejecutar el contenedor

```bash
docker run -p 8000:8000 fastapi-ml-service
```