### Prueba el juego 🎮​
__Si quieres probar el juego, puedes descargar su version compilada, solo debes descargar el archivo `Code of Legends Portable.zip` dentro del cual se encuentra el ejecutable.__

# Code of Legends

Este proyecto comenzó como una practica en el uso de clases en el contexto de la Programacion Orientada a Objetos. Bajo esta lógica, se programo 5 clases de personaje diferentes: Caballero, Mago, Berserker, Exorcista y Alquimista, los cuales se enfrentan en combates por turno de uno contra uno. Asi se desencadenó el desarrollo de "Code of Legends".

![image](imagenes\screenshots\Captura1-1.png)

## Tecnologías usadas
La primera version funcional de Code of Legends está programada en Python puro, haciendo uso de las bibliotecas:
- **Pandas**, para registrar personajes,guardar y leer sus cambios de stats (Nivel, Fuerza, Inteligencia, Defensa,Karma Y Vida).
- **TKinter**, para la construcción de interfaz grafica.
- **Pygame**, para la reproduccion de audio.

## Mecanicas de juego
### Personajes diferentes, ataques diferentes ⚔️​
Elpersonaje que se use definira una forma de jugar totalmente diferente: método atacar, usado para infligir daño basico al contrincante en Code of Legends, funciona de formas totalmente diferentes en cada clase de personaje. Por ejemplo, mientras un personaje de la clase Caballero infringe daño con la suma de sus stats de Fuerza y Arma restándose a la Defensa de su contrincante, un Alquimista usará su Arma, su Fuerza y cierto porcentaje de su inteligencia, restándose ante el stat defensivo más bajo del contrincante (Defensa o Karma). De esta forma se pone en practica al maximo el polimorfismo, un concepto en la Programacion Orientada a Objetos, en la forma en que los personajes del juego luchan entre si.
![image](imagenes\screenshots\Captura2.png)
Junto a lo anterior, cada tipo de personaje tiene sus stats nivelados de diferentes maneras acorde a su clase, generandose asi una disparidad tanto positiva como negativa que los jugadores deberan aprender y sortear para equilibrar el tablero.
### Habilidades de Clases 🧿​​⚡⚖️​💣​​
Cada clase de personaje posee un conjunto de habilidades acorde a su modo de juego, algunas de las cuales estan programadas con efectos tan locos que podrian cambiar el rumbo del combate de maneras insospechadas.
![image](imagenes\screenshots\Captura3.png)

## EStrucutra y funcionamiento
--- Trabajando aun en la descripcion --- 

## Primera (y de momento unica) version estable 
Hay una gran cantidad de ideas aun por implementar, pero el objetivo inicial impuesto era tener algo usable y con una interfaz grafica, lo cual se ha logrado y es ya comprobable en su primera version compilada denominada como la 0.0.1. En dicha version, es posible registrar un personaje, elegir entre uno existente y utilizar este para combatir contra un enemigo cuya clase, nombre y acciones durante cada turno son aleatorias, mientras que su nivel se equipara automaticamente al del personaje jugador. En dicha version, el personaje del jugador esta capacitado para subir de nivel, registrandose los cambios respectivos de sus stats en un archivo CSV junto al del resto de personajes creados.

## Proximas funciones 📅​
### A corto plazo
- Sistema de gestion de armas
- Mas habilidades de clases y mejoras en las ya existentes
- Nuevos enemigos NPC
### A largo plazo
- Añadido de objetos/amuletos coleccionables con efectos pasivos en combate.
- Lore para personajes e items.
- Migracion a framework Django para despliegue de una version web (esto conlleva cambio de interfaz grafica al completo)
- Animaciones para sprites de personajes, ataques, habilidades y cambios de estado.