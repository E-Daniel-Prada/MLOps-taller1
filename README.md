# FastAPI ML Service

Este repositorio contiene un ejercicio de ejemplo que expone un modelo de Machine Learning a través de una API implementada con [FastAPI](https://fastapi.tiangolo.com/) y desplegada en un contenedor [Docker](https://www.docker.com/).


## Integrantes del Grupo
- Elkin Daniel Prada
- Jorge Linares
- Jeison Ibañez


## Tabla de Contenidos

- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación y Ejecución](#instalación-y-ejecución)
- [Uso de la API](#uso-de-la-api)
- [Integrantes del Grupo](#integrantes-del-grupo)

## Estructura del Proyecto

La estructura de carpetas y archivos es la siguiente:

```plaintext
taller1/                     # Directorio raíz del proyecto
├── app/                     # Código fuente de la API
│   ├── __init__.py          # Indica que 'app' es un paquete Python
│   ├── main.py              # Punto de entrada de la aplicación
│   ├── models/                               # Carpeta para los modelos de IA
│   │   ├── __init__.py                       #
│   │   └── DecisionTree_optimized.pkl        # Modelo 1
|   |   └── LogisticRegression_optimized.pkl  # Modelo 2
|   |   └── RandomForest_optimized.pkl        # Modelo 3  
|   |   └── train.py                          # Codigo de los modelos (Realizado en Colab)
│   └── routes/              # Carpeta para los endpoints de la API
│       ├── __init__.py      #
│       ├── predict.py       # Endpoint para realizar predicciones
│       └── api_test.py      # Endpoint para verificar el estado de la API
├── requirements.txt         # Lista de dependencias del proyecto
├── Dockerfile               # Instrucciones para construir la imagen Docker
└── README.md                # Este archivo
```

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
docker run -p 8989:8989 fastapi-ml-service
```

Para probar la API

Se tienen 3 modelos cargados en el api

model_files = {
    1: "app/models/LogisticRegression_optimized.pkl",
    2: "app/models/DecisionTree_optimized.pkl",
    3: "app/models/RandomForest_optimized.pkl"
}

Segun el modelo a utilizar en la predicción se solicita el codigo al final del path del servicio POST

```bash
http://localhost:8989/predict/{id}
```
Ejemplo de consumo

```bash
curl -X POST "http://localhost:8989/predict/1" -H "Content-Type: application/json" -d '[0, 47.2, 13.7, 214.0, 4925.0, 1]'
```
