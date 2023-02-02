# Instrucciones para Instrumentar una aplicación de Python para Prometheus

## Pre-requisitos
* Tener Python instalado (Python 3.8.10 de preferencia)
* Tener git instalado 
* Estar en alguna distribución de Linux (Ubuntu de preferencia)

## Pasos
* Clonamos este repo
`git clone https://github.com/jcroyoaun/cerouno-prom-python-inst`
* Corremos la app 
* * Ex.
`python3 app.py`
* Abrimos un navegador en localhost:8000

![image](https://user-images.githubusercontent.com/83674541/132585717-3c952bdb-0caf-4b58-9cb9-95166f755089.png)

* Instalamos prometheus_client en nuestra computadora :
`sudo apt install python3-pip`
`pip install prometheus_client` 

* (agregar el siguiente codigo en la linea #2) - Importar start_http_server de prometheus client 
`from prometheus_client import start_http_server`

* (agregar el siguiente codigo en la linea #17) - 
`start_http_server(METRICS_PORT)`

* (agregar el siguiente codigo en la linea #5)
`METRICS_PORT = 8001`


# Use case - Counter type metrics
Calcularemos el numero de http requests hechos a nuestra app.

## Pasos (agregando un counter que se incrementa por 1)
* (agregar el siguiente codigo en la linea #2) - Importamos counter en nuestra aplicacion

`from prometheus_client import start_http_server, Counter`

* (agregar el siguiente codigo en la linea #4) - El primer valor es nuestra metrica y el segundo es el #HELP

`REQUEST_COUNT = Counter('app_request_count', 'Total app http request count')`


* (agregar el siguiente codigo en la linea 12)

`REQUEST_COUNT.inc()`


Y probamos (accedemos puerto 8000 y damos refresh varias veces)...

## Pasos 2 (agregando un counter que se incrementa random)
* (agregar el siguiente codigo en la linea #3) - Importamos random en nuestra aplicacion

`import random`


* (agregar el siguiente codigo en la linea #6) - El primer valor es nuestra metrica y el segundo es el #HELP

`RANDOM_COUNT = Counter('app_random_count', 'Incrementing the counter by random value')`

* (agregar el siguiente codigo en la linea 15 y 16) - 

```
random_val = random.random()*10
RANDOM_COUNT.inc(random_val)
```

# Apendix
# # Convencionalidades para nombrar metricas
* Debe empezar con una letra, y puede ser seguido de cualquier numero de letras, numeros o guiones bajos (_).
* Debe tener nombres unicos. los Client libraries deben reportar un error si tratamos de registrar la misma metrica dos veces en nuestra aplicacion.
* En casos aplicables, cuando expongamos los time series de un tipo de metrica counter, el sufijo "_total" debe ser parte del nombre.

