# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** grid_svc
- **Plataforma de despliegue:** railway
- **Requisitos técnicos:** Python 3.10.12, FastAPI 0.99.1, Scikit-learn 1.2.2(especial cuidado)
- **Requisitos de seguridad:** Ninguno


## Código de despliegue

- **Archivo principal:** main.py
- **Rutas de acceso a los archivos:** /predict
- **Variables de entorno:** Ninguna

## Documentación del despliegue

- **Instrucciones de instalación:** Se debe contar con los 4 archivos en donde se tiene el modelo, la api, los librerias requeridas y el archivo de configuracion de railway 
- **Instrucciones de configuración:** El metodo usado fue tener estos 4 archivos juntos en una carpeta de un repositorio github y hacer la configuracion desde railway para conectar el repositorio con la carpeta que contiene los 4 archivos
- **Instrucciones de uso:** Generando en railway un dominio podemos mantener una url estatica para poder hacer una peticion al path predict, en mi caso el url se ve:https://pruebafast-production.up.railway.app/predict. A este url le enviamos un arreglo de numero flotantes con la informacion de:Edad, glucosa, insulina,	Indice de masa corporal y numero de embarazos. Lo que nos responde el endpoint es un numero 1 para decir que se tiene diabetes y 0 para indicar que no se tiene diabetes
- **Instrucciones de mantenimiento:** El modelo puede ser ajustado para luego reemplazar el archivo model.joblib para desplegar la nuevar version del modelo