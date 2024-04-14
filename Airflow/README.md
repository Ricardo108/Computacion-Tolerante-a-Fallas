<h1 align="center"> CENTRO UNIVERSITARIO DE CIENCIAS EXACTAS E INGENIERIAS </h1>
<h1 align="center"> DEPARTAMENTO DE CIENCIAS COMPUTACIONALES </h1>

<h1 align="center"> UNIVERSIDAD DE GUADALAJARA </h1>

<div align="center">
  <img src="Imagenes\Image1.png" alt="Logo UDG" width="200" />
</div>


# Nombre: Rodriguez de León Ricardo Emmanuel

<h1 align="center"> Airflow </h1>

# Indice

* [Introducción](#introduccion)

* [Contenido](#contenido)

* [Conclusion](#conclusion)

* [Bibliografia](#bibliografia)

# Introduccion
En esta actividad se realizara un pequeño programa en donde se aprendera a utlizar el Apadhe Airflow, tanto su instalacion, como su uso.

# Contenido

## Apache Airflow
El apache Airflow es una herramienta que nos permitiraa gestionar, monitorizar y planificar flujos de trabajho, usado como orquestador de servicios, en este caso al ser un prorgama muy basico, el cual hara el uso de esta herramienta, para ver descuentos que se estan dando en la pagina de Ddtech, que es una tienda de tecnologia.

## Instalacion
Para la instalacion de Apache Airflow en tu entorno dew python, se debera de utilizar "pip install virtualenv" para la creacion de un entorno virtual para el correcto funcionamiento de la herramienta, tambien se debera de usar "pip install apache-airflow" el cual es para intalar la herramienta, despues se tiene que usar "airflow db init" solo sera la primera vez, es para inicializar una base de datos, luego de eso "airflow webserver --port 8080" se usara esto, el cual el port, si tienes el puerto 8080, se debera de cambiar por uno que no estes usando de otra base de datos, por ultimo se usara "airflow scheduler" el cual es para ejecutar las tareas programadas.

## Codigo
El codigo es muy sencillo, el cual es un simple llamado por decirlo asi, a una pagina web, donde se debera de buscar descuentos en la URL que se asigno y este mostrara los resultados.

    Tambien se debera de instalar "pip install requests beautifulsoup4" en su entorno virtual, para poder "manipular" los datos de la pagina web.

# Conclusion
Es importante conocer herramientas que nos pueden ayudar a realizar tareas mas rapido y sencillo, como ejemplo seria el mismo programa que se realizo, al usarlo en vez de meterte al navegador y luego a la pagina web, simplemente se ejecutaria el programa y ya te estaria mandando descuentos, que son lo mas importante en este caso.

# Bibliografia
    Fernandez, O. (2023, 23 octubre). ¿Qué es Apache Airflow? Introducción. Aprender BIG DATA. https://aprenderbigdata.com/apache-airflow/

    Quick start — Airflow documentation. (s. f.). https://airflow.apache.org/docs/apache-airflow/stable/start.html

