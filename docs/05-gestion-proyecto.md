# Matesydados

## Trello
[link a tablero público] (https://trello.com/b/FK8FIHJg/mateydados)

## Sprints:

### TP-0:
#### Objetivos
- Crear una propuesta de trabajo con un universo que se adapte a los requerimientos de la cursada.
- Crear primer repo con la documentacion inicial.
#### Historias de usuario
- Quiero que el usuario pueda buscar, filtrar y recibir recomendaciones de juegos de mesa
#### Criterio de aceptación
- Los objetos del universo elegido deben contar con atributos propieos que permitan ordenar, clasificar y filtrar.
- Los objetos deben relacionarse entre si y tener clasificaciones.
- Debe haber disponibles datos reales, tener volumen y calidad para adaptarse al TP sin que sea forzado.
- Deben tener una utilidad real y resolver un problema real.
#### Retrospectiva
La elección del universo fue rápida, ya es de interes de los miembros del equipo y eventualmente representa una solucion para estos y otros usuarios. Los datos fueron accesibles por medio de sitios con API y datasets ya armados.
Fue retador pero enriquecedor incorporar nuevas herramientas y sistemas de trabajo como los registros de avances del proyecto, trello y este mismo documento de gestion.
La mayor dificultad fue pasar de una idea a ordenar todo un proyecto por etapas, en equipo, en orden y la división de tareas.

### TP-1:
#### Objetivos
- Crear las clases necesarias.
- Crear una interfaz.
- Finalizar con una primera version funcional.
#### Historias de usuario
- Quiero que el usuario pueda interactuar con la terminal y solicitar una busqueda facilmente.
- Quiero que el usuario pueda buscar un juego ingresando el nombre completo o parte de el.
- Quiero que el usuario pueda filtrar los juegos por preferencia.
- Quiero que el usuario pueda ver el catalogo completo de juegos.

#### Criterio de aceptación
- El menú se ejecuta en un bucle continuo (`while True`) hasta que el usuario elija la opción de salir (`4`).
- Muestra un mensaje de error si se ingresa una opción inválida sin que el programa cierre inesperadamente.
- La búsqueda es case-insensitive.
- Si no hay coincidencias o el usuario no igresa nada, el sistema muestra un mensaje informativo sin interrumpir el bucle de la aplicación.
- El sistema obtiene las categorias disponibles y se las muestra al usuario.
- Retorna todos los juegos que incluyan la categoría consultada.
- La clase Catalogo almacena las instancias en una lista interna y notifica por consola la cantidad total de juegos cargados.
- Se imprime al usuario cada juego con sus detalles del catalogo completo disponible.

#### Retrospectiva
Que salió bien:
Creo que hubo una buena separacion en las responsabilidades del codigo, para que la terminal, catalogo, juego y main tuvieran tareas definidas.
Hubo una incorporacion de lambda por primera vez para simplificar funciones.
La primera versión de la aplicacion se encuentra funcionando y sin errores hasta el momento.
Se incorporaron nuevos datasets de 500 y 10.000 juegos adaptados al TP, fueron creados a partir de un dataset padre basado en datos de https://boardgamegeek.com/ con un scrip generador, ambos obtenidos con apoyo de una IA. fueron creados con la finalidad de probar el programa con volumenes mas grandes de datos.
El mayor desafio fueron las integraciones entre el catálogo y la terminal, los errores que generaron y encontrar cual es el error para poder solucionarlo. 

Que se puede mejorar:
Trabajar con ramas independientes para cada parte del proyecto (aunque sea yo el único autor) para aprender a trabajar en diferentes ramas como lo haría en un equipo en un trabajo real.
Hacer un commit por cada tarea resuelta.
Agregar mas comentarios al código que describan funcionalidades por segmentos.