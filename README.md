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
### TP-1
- Buscar juego por nombre.
- Listar juegos disponibles
- Mostrar los datos de cada juego.
- Filtrar por categoria.
- Salir del programa

## Documentación:
- [Requerimientos](docs/01-requerimientos.md)
- [Casos de uso](docs/02-casos-de-uso.md)
- [Diagrama de clases](docs/03-diagrama-clases.md)
- [Diagrama de datos](docs/04-diagrama-datos.md)
- [Gestión del proyecto](docs/05-gestion-proyecto.md)

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
| TP2     | En progreso|
| TP3     |  Pendiente |
| TP4     |  Pendiente |
| TP5     |  Pendiente |
| TP6     |  Pendiente |
| TP7     |  Pendiente |
| TP8     |  Pendiente |
| TP9     |  Pendiente |
| TP10    |  Pendiente |