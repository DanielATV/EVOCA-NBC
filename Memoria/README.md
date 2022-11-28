# Readme

### Resumen

El siguiente código es una propuesta de mejora para el sintonizador de parámetros Evolutionary Calibrator (EVOCA). La propuesta consiste en utilizar un clasificador para determinar si se debe aplicar el operador de mutación sobre un parámetro. En esta versión el clasificador utilizado es Gaussian Naive Bayes Classifier.
 
Durante su ejecución se recopila información sobre las configuraciones que han sido añadidas a la población luego de ser mutadas. La clase 1 representa las configuraciones que fueron aceptadas. Por otro lado, la clase 0 representa las configuraciones que fueron aceptadas. El número de evaluaciones que se utilizan para recopilar datos está dado por la función "regla", la cual recibe como input la cantidad de parámetros que se van a sintonizar.
 
Una vez entrenado el modelo este utiliza la configuración del individuo cruzado y el parámetro que se va a mutar para determinar su clase. En caso de ser 1 se utiliza el operador de mutación. En el caso contrario, se cambia el parámetro a mutar de forma aleatoria y se vuelve a clasificar. Esto se repite hasta intentar con todos los parámetros, sin repetir, o hasta que el modelo clasifique con la clase 1. En el caso de haber intentado con todos los parámetros y que en todos los casos la clase sea 0, entonces no se utiliza el operador de mutación en esa iteración.
 
Al terminar su ejecución el archivo datos.txt contiene los datos utilizados para entrenar el modelo. Además, el archivo statsModelo.txt contiene una evaluación del modelo utilizando K-fold. Finalmente, el modelo utilizado se exporta en el archivo modeloEVOKA.joblib.


### Prerequisitos
Docker
sudo apt install docker.io

### Comandos útiles
Verificar instalación: sudo docker run hello-world

Estado de Docker: systemctl status docker

Activar Docker: sudo systemctl start docker

Evitar usar sudo: sudo chmod 666 /var/run/docker.sock

### Ejecucion

docker build -t danielatv/memoria .

docker run -t -d --name EVOCA danielatv/memoria

### Uso 

Acceder a la consola:
docker exec -it EVOCA bash

Ejecucion en segundo plano:
`nohup make exe > salidaOutfile &`

Salida:
exit

### Extraer Archivos

docker cp EVOCA:/NBC/AKCodEVOCA180119 $(pdw)/docker-output

### Terminar Ejecución

docker container stop EVOCA

docker container rm EVOCA

### Uso sin docker
Requisitos:
Todas las librerias explicitadas en el DockerFile

En el directorio Memoria/NBC/AKCodEVOCA180119

Compilar:
`make`

Ejecutar:
`make exe`

Ejecucion en segundo plano:
`nohup make exe > salidaOutfile &`






