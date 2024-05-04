<h1 align="center"> CENTRO UNIVERSITARIO DE CIENCIAS EXACTAS E INGENIERIAS </h1>
<h1 align="center"> DEPARTAMENTO DE CIENCIAS COMPUTACIONALES </h1>

<h1 align="center"> UNIVERSIDAD DE GUADALAJARA </h1>

<div align="center">
  <img src="Imagenes/Image1.png" alt="Logo UDG" width="200" />
</div>


# Nombre: Rodriguez de León Ricardo Emmanuel

<h1 align="center"> Instalacion y Uso basico de Docker </h1>

# Indice

* [Introducción](#introducción)

* [Contenido](#contenido)

* [Conclusion](#conclusion)

* [Bibliografia](#bibliografia)


# Introduccion
En esta actividad se realizara la instalacion de docker, una breve descripcion de que es y para que sirve, ademas de un ejemplo de como generar una aplicacion.

# Contenido
Para poder utilizar Docker, se debera de instalar (en Windows) la apliacion desde su pagina oficial, se instalara y una vez instalado, se debera de descargar el subsistema de Linux para poder ejecutarlo.

    Se llama WSL, se descarga desde la pagina oficial de microsoft.

Una vez descargado esto, se descaragara una distribucion de Linux, en este caso se escogio Ubuntu.

<img src="Docker/Imagenes/Image2.png" />

Cuando se haya instalado te pedira que ingreses un usuario y contraseña, luego de eso, tienes que abrir docker.

<img src="Imagenes/Image3.png" />

Como se observa en la imagen no hay nada.

<img src="Imagenes/Image4.png" />

Al observar la imagen, se puede ver que la primera ves que use:

    docker run -d -p 80:80 docker/getting-started

Me dio un error, esto es porque se tiene que usar de esta manera:

    sudo docker run -d -p 80:80 docker/getting-started

Se debe de agregar la palabra "sudo" al inicio, para que puedas dar permisos de administrador, y asi en la aplicacion de Docker se vera de esta manera.

<img src="Imagenes/Image5.png" />

# Conclusion
Esta actividad me trajo muchos problemas al instalarlo, porque no sabia bien de los errores que me arrojaba, pero con un poco de investigación podia saber como solucionarlo, eso si, quise hacerlo desde una maquina virtual, pero me daba mas problemas, por eso, instale todo esto desde windows, ademas de que te permite utilizar Linux, como un subsistema y eso facilita las cosas.

# Bibliografia
    Docker Desktop: The #1 Containerization Tool for Developers | Docker. (2023, 21 diciembre). Docker. https://www.docker.com/products/docker-desktop/

    Craigloewen-Msft. (2023, 20 noviembre). Manual installation steps for older versions of WSL. Microsoft Learn. https://learn.microsoft.com/en-us/windows/wsl/install-manual

    https://www.youtube.com/watch?v=_et7H0EQ8fY

