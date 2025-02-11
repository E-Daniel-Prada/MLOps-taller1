# -*- coding: utf-8 -*-
"""Modelos.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1i1p4kdYfLRwZasZs8QGDOBhLl684triV
"""

import pandas as pd

# Cargar el dataset
file_path = "/content/sample_data/penguins_size.csv"
df = pd.read_csv(file_path)

# Mostrar primeras filas
print(df.head())

from sklearn.preprocessing import LabelEncoder, StandardScaler

# qEliminar filas con valores nulos
df.replace("NA", pd.NA, inplace=True)  # Convertir "NA" en va

df.dropna(inplace=True)

# Convertir variables categóricas a numéricas
label_encoders = {}
for col in ['species', 'island', 'sex']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le  # Guardamos los encoders para usarlos después en inferencia

# Separar variables predictoras (X) y variable objetivo (y)
X = df.drop(columns=['species'])  # Características
y = df['species']  # Variable objetivo

# Escalar los datos numéricos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X

from sklearn.model_selection import train_test_split

# Dividir datos en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

X_test

import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, GridSearchCV


# Definir modelos
models = {
    "DecisionTree": DecisionTreeClassifier(random_state=42),
    "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
    "LogisticRegression": LogisticRegression(max_iter=1000, random_state=42)
}

# Espacios de búsqueda de hiperparámetros
param_grid = {
    "DecisionTree": {
        "criterion": ["gini", "entropy"],
        "max_depth": [3, 5, 10, None],
        "min_samples_split": [2, 5, 10]
    },
    "RandomForest": {
        "n_estimators": [10, 20, 50, 100, 200],
        "max_depth": [3, 5, 10, 20, None],
        "min_samples_split": [2, 5, 10, 20, 50]
    },
    "LogisticRegression": {
        "C": [0.01, 0.1, 1, 10, 100, 300],
        "solver": ["liblinear", "lbfgs"]
    }
}

# Aplicar GridSearch para encontrar los mejores hiperparámetros
best_models = {}
for name, model in models.items():
    print(f" Optimizando {name}...")
    grid_search = GridSearchCV(model, param_grid[name], cv=5, scoring="accuracy", n_jobs=-1)
    grid_search.fit(X_train, y_train)
    best_models[name] = grid_search.best_estimator_
    print(f" Mejor configuración para {name}: {grid_search.best_params_}")

# Evaluar modelos optimizados
optimized_scores = {}
for name, model in best_models.items():
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    optimized_scores[name] = acc
    print(f" {name} Accuracy después de optimización: {acc:.2f}")

# Guardar los mejores modelos entrenados
for name, model in best_models.items():
    with open(f"{name}_optimized.pkl", "wb") as file:
        pickle.dump(model, file)

print(" Modelos optimizados guardados correctamente")
