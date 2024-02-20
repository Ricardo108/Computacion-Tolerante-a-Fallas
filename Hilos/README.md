# CENTRO UNIVERSITARIO DE CIENCIAS EXACTAS E INGENIERIAS
# DEPARTAMENTO DE CIENCIAS COMPUTACIONALES

# UNIVERSIDAD DE GUADALAJARA

<div style="text-align: center;">
  <img src="/Hilos/image.png" alt="Logo UDG" width="200" />
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
  <img src="/Hilos/image-1.png" width="200" />
</div>

Aqui ya se le asigno una palabra a adivinar.
<div style="text-align: center;">
  <img src="/Hilos/image-2.png" width="200" />
</div>

En esta parte del juego, ya se abra guardado la partida por si se llegara a cerrar el juego, como se observa, esta a punto de ganar.
<div style="text-align: center;">
  <img src="/Hilos/image-3.png" width="200" />
</div>

Aqui se volvio a abrir, por eso, no aparecen los intentos restantes, pero puede continuar donde lo dejo.
<div style="text-align: center;">
  <img src="/Hilos/image-4.png" width="200" />
</div>
