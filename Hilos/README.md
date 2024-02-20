# CENTRO UNIVERSITARIO DE CIENCIAS EXACTAS E INGENIERIAS
# DEPARTAMENTO DE CIENCIAS COMPUTACIONALES

# UNIVERSIDAD DE GUADALAJARA

<div style="text-align: center;">
  <img src="/Hilos/Imagenes/image.png" alt="Logo UDG" width="200" />
</div>

# Nombre: Rodriguez de Leon Ricardo Emmanuel

# Materia: Computacion Tolerante a Fallas

# Actividad: An Introduction to Scaling Distributed Python Applications


# Hilos
    Los hilos son una secuencia de instrucciones que puede ser ejecutada por el sistema operativo

# Demonios
    Es un proceso en segundo plano que se ejecuta sin interaccion con el usuario o con otros programas.

# Concurrencia
    Es la capacidad de un programa para realizar varias tareas simultaneamente.

# Desarrollo

# Hilos
Los hilos en este programa (juego del ahorcado) se utiliza en variois puntos del codigo, por ejemplo, en la parte del metodo "guardar_partida_automaticamente"
se ejecuta en un hilo separado para guardar cambios automaticamente cada 10 segundos, y el metodo "adivinar_letra" utiliza "threading.Thread(target=self.mostrar_tablero).start()"
para mostrar el tablero sin bloquear la interfaz del usuario.

# Concurrencia
Para la concurrencia en este programa se usa la clase "ThreadPoolExecutor" del modulo "concurrent.futures" para ejecutar varias tareas al mismo tiempo y gestionar
un conjunto de hilos.

# Demonios
Como tal no se integraron los procesos de demonio, pero los hilos como tal, se ejecutan en segundo plano como los utlizados en "guardar_partida_automaticamente",
pueden ser terminados cuando la apliacion principal finaliza.


# Ejecucion
Asi se ve el juego antes de iniciar una partida.
<div style="text-align: center;">
  <img src="/Hilos/Imagenes/image-1.png" />
</div>

Aqui ya se le asigno una palabra a adivinar.
<div style="text-align: center;">
  <img src="/Hilos/Imagenes/image-2.png" />
</div>

En esta parte del juego, ya se habra guardado la partida por si se llegara a cerrar el juego, como se observa, esta a punto de ganar.
<div style="text-align: center;">
  <img src="/Hilos/Imagenes/image-3.png" />
</div>

Aqui se volvio a abrir, por eso, no aparecen los intentos restantes en color rojo como advertencia, pero puede continuar donde lo dejo.
<div style="text-align: center;">
  <img src="/Hilos/Imagenes/image-4.png" />
</div>

# Conclusion
Es muy importante conocer estos temas de los hilos, demonios y de concurrencia, ya que asi podras realizar programas mas optimos, por dar un ejemplo, los hilos
nos permitiran que un programa realice varias tareas simultaneamente, esto en pocas palabras es mayor rendimiento y eficacia. Ademas los hilos comparten la memoria y otros
recursos de un proceso, lo cual hace que sean mas eficientes que los procesos separados.