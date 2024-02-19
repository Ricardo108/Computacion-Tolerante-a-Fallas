# CENTRO UNIVERSITARIO DE CIENCIAS EXACTAS E INGENIERIAS
# DEPARTAMENTO DE CIENCIAS COMPUTACIONALES

# Universidad de Guadalajara

<div style="text-align: center;">
  <img src="/Hilos/image.png" alt="Logo UDG" width="200" />
</div>


# Rodriguez de Leon Ricardo Emmanuel

# Computacion Tolerante a Fallas

# An Introduction to Scaling Distributed Python Applications


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
