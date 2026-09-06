# Mateydados - Propuesta (TP0) 
Sistema de recomendación de juegos de mesa, permite buscar juegos para cada usuario segun preferencias, ordenar y recomendar juegos a partir de uno dado.

## 1. Dominio elegido y justificación
Dominio: juegos de mesa.
Justificación: Es de interes del grupo, hay datos disponibles por medio de API y datasets, permite adaptarse perfectamente con las estructuras planteadas en la cursada.

## 2. Problema que resuelve
Quiero elegir un juego para jugar con mis 4 amigos adultos con partidas cortas y que sea de dados o cartas. 
Quiero regalarle un juego a mi hijo de 7 años para que juegue con sus amigos y que sea cooperativo, que no compitan entre ellos.

## 3. Usuario Objetivo
A. joni, 33 años. Busca un juego similar a su juego favorito pero prefiere que las partidas sean mas cortas.
B. Ale, 46 años. Busca un juego de mesa para niños de 8 años que sea cooperativo. Sabe que a su hijo le gusta la aventura/fantasía.

## 4. Funcionalidades iniciales

| ID | Funcionalidad |
|----|---|
| F1 | Buscar un elemento por nombre |
| F2 | Filtrar elementos por categoria |
| F3 | Ordenar por Atributo
| F4 | Recomendar a partir de uno dado |
| F5 | Top 10 rankeados |

## 5. Ejemplo de uso

========================================
      Mateydados — TERMINAL
========================================
1. Buscar juego
2. Explorar categorías
3. Ordenar
4. Buscar parecido
5. Top 10
0. Salir

----------------------------------------
Opción: 1
Buscar: Monopoly

Monopoly
jugadores: 2 a 8
Edad: 8+
Tiempo de juego min: 60 min 
categoria: Recursos
mecanismo: trading
victoria: Competitivo
Rating 0-10: 5.0

## 6. Requerimientos

### 6.1 Requerimientos funcionales

- RF01 — El sistema debe permitir buscar un juego por nombre.
- RF02 — El sistema debe mostrar la información principal de un juego.
- RF03 — El sistema debe permitir listar los juegos disponibles.
- RF04 — El sistema debe permitir filtrar juegos por categoría.
- RF05 — El sistema debe permitir mostrar los 10 juegos mejor calificados.


### 6.2 Requerimientos no funcionales

- RNF01 — El sistema debe desarrollarse en Python.
- RNF02 — El sistema debe funcionar mediante una interfaz de terminal.
- RNF03 — La búsqueda por nombre no debe distinguir entre mayúsculas y minúsculas.
- RNF04 — El sistema debe mostrar mensajes claros cuando no encuentre un juego o cuando se ingrese una opción inválida.
- RNF05 — El sistema debe estar organizado en módulos para separar los datos.

## 7. Fuera de alcance (por ahora)
- No hay autenticación ni perfiles de usuario.
- No hay sistema de recomendaciones similares a otro juego.