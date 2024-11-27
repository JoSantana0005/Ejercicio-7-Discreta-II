# Ejercicio-7-Discreta-II

<div align='center'>
<img width="50%" src="https://cdn.codegym.cc/images/article/6d117ebf-e0c0-43b6-9150-4805c456ab01/original.gif">
</div>

Este repositorio contiene implementaciones de tres algoritmos de búsqueda: A*, Búsqueda Primero la Mejor (Best-First Search) y Escalada por Máxima Pendiente (Hill Climbing). Estos algoritmos se utilizan comúnmente en la inteligencia artificial para resolver problemas de búsqueda y optimización.

## Algoritmos Implementados

### 1. Algoritmo A*

El algoritmo A* es un algoritmo de búsqueda informada que utiliza una heurística para encontrar el camino más corto desde un nodo inicial hasta un nodo objetivo. Combina las ventajas de la búsqueda de costo uniforme y la búsqueda en profundidad.

- **Complejidad Temporal**: O(b^d), donde b es el factor de ramificación y d es la profundidad de la solución.
- **Complejidad Espacial**: O(b^d).

### 2. Búsqueda Primero la Mejor (Best-First Search)

La búsqueda primero la mejor es un algoritmo de búsqueda informada que utiliza una función heurística para decidir qué nodo explorar a continuación. Este algoritmo se basa en la idea de que el nodo que parece más prometedor (el que tiene el menor costo estimado) debe ser explorado primero.

- **Complejidad Temporal**: O(b^d), donde b es el factor de ramificación y d es la profundidad de la solución.
- **Complejidad Espacial**: O(b^d).

### 3. Escalada por Máxima Pendiente (Hill Climbing)

La escalada por máxima pendiente es un algoritmo de búsqueda local que comienza en un punto aleatorio y se mueve hacia la dirección que maximiza la función objetivo. Es útil para problemas de optimización, pero puede quedar atrapado en máximos locales.

- **Complejidad Temporal**: Depende de la función de evaluación y del espacio de búsqueda.
- **Complejidad Espacial**: O(1).

## Instalación

Para ejecutar los algoritmos, asegúrate de tener Python instalado en tu sistema y clona el repositorio
