# Matesydados

Mateydados es un sistema de consulta y recomendación de juegos de mesa.
el proyecto busca ayudar a elegir y recomendar juegos para cada persona segun sus necesidades y preferencias, como cantidad de jugadores, duracion, edad minima o calificaciones.

## Integrantes
 - Jonathan Maximiliano Hauff (Proyecto individual)

## Requisitos
- Pyton 3 instalado.

## Instalación
Clonár el repositorio:
```bash
git clone https://github.com/jonihauff/Matesydados
```
Ingresá a la carpeta del proyecto:
```bash
cd Matesydados
```
Tambien podes abrir directamente la carpeta con VSC u otro editor de código.

## Funcionalidades

- Buscar juegos por nombre usando un árbol AVL.
- Explorar categorías por grupos usando un árbol general.
- Listar todos los juegos disponibles.
- Mostrar el Top 10 por rating usando un MaxHeap.
  En caso de empate, los juegos se ordenan alfabéticamente por nombre.
- Construir un grafo no dirigido y ponderado de juegos relacionados
  por categorías y mecánicas compartidas. Las mecánicas del dataset
  de trabajo están traducidas al español.
- Demostrar BFS desde un juego inicial, mostrando los juegos alcanzables en orden por niveles.
- Demostrar DFS iterativo desde un juego inicial, mostrando los juegos alcanzables en orden de exploración en profundidad.

### Menú de terminal

1. Buscar juego por nombre
2. Buscar por categoría
3. Mostrar todos los juegos
4. Mostrar ranking Top 10
5. Salir
6. Demostración BFS
7. Demostración DFS

## Documentación:
- [Requerimientos](docs/01-requerimientos.md)
- [Casos de uso](docs/02-casos-de-uso.md)
- [Diagrama de clases](docs/03-diagrama-clases.md)
- [Diagrama de datos](docs/04-diagrama-datos.md)
- [Gestión del proyecto](docs/05-gestion-proyecto.md)
- [Análisis TP 3](docs/07-analisis-tp3.md)
- [Análisis TP 4-5](docs/08-analisis-tp4-5.md)
- [Análisis TP 8](docs/09-analisis-tp8.md)

## Generación de datasets

Los datasets JSON se generan a partir de un CSV basado en datos de BoardGameGeek.

1. Descargar el dataset original desde [https://www.kaggle.com/datasets/sujaykapadnis/board-games].
2. Guardarlo como `datos/origen/board_games.csv`.
3. Ejecutar:
```bash
python datos/generar_datasets.py
```

## Estado del proyecto
| Entrega |   Estado   |
|  ---    |    ---     |
| TP0     | Completado |
| TP1     | Completado |
| TP2     | Completado |
| TP3     | Completado |
| TP4     | Completado |
| TP5     | Completado |
| TP6     | Completado |
| TP7     | Completado |
| TP8     | Completado |
| TP9     |  Pendiente |
| TP10    |  Pendiente |