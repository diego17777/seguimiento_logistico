# Sistema de Seguimiento Logístico

## 1. Descripción del proyecto

Este proyecto implementa un prototipo de seguimiento logístico que permite consultar el estado de un envío mediante su número de guía, almacenar la información obtenida en una base de datos local y revisar los eventos registrados durante la ejecución.

El sistema fue desarrollado con Python y Flask. Utiliza una API simulada para proporcionar los datos de los envíos, SQLite para el almacenamiento, el módulo `logging` para registrar eventos y Locust para realizar pruebas de carga.

**Importante:** los datos de los envíos son simulados. La base de datos es SQLite local y no corresponde a una base de datos institucional. No se ha verificado una conexión con un proveedor logístico real.

## 2. Tecnologías utilizadas

- Python
- Flask
- Requests
- SQLite
- Logging
- Locust

## 3. Estructura del proyecto

```text
seguimiento_logistico/
│
├── app.py
├── api_service.py
├── database.py
├── requirements.txt
├── README.md
│
├── database/
│   └── envios.db
│
├── logs/
│   └── app.log
│
├── api_simulada/
│   └── api.py
│
├── tests/
│   └── locustfile.py
│
└── evidencias/
```

La carpeta `database` contiene la base de datos local; `logs` almacena los registros; `api_simulada` contiene el servicio de prueba; y `tests` contiene el archivo utilizado para las pruebas de carga. La carpeta `evidencias` se utiliza para guardar capturas y reportes de las pruebas.

## 4. Requisitos previos

Se necesita tener instalado Python y una terminal compatible con Windows. También se recomienda utilizar un entorno virtual para mantener las dependencias del proyecto organizadas.

## 5. Instalación

Abre una terminal en la carpeta principal del proyecto y ejecuta:

```bash
python -m venv venv
```

Activa el entorno virtual en Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Si utilizas el símbolo del sistema de Windows (CMD), puedes activar el entorno con:

```bat
venv\Scripts\activate
```

Instala las dependencias:

```bash
python -m pip install -r requirements.txt
```

## 6. Ejecución del sistema

Es necesario ejecutar la API simulada y la aplicación principal en terminales separadas.

### Terminal 1: iniciar la API simulada

Desde la carpeta principal del proyecto, ejecuta:

```bash
python api_simulada/api.py
```

Este servicio debe quedar disponible en el puerto 5001.

### Terminal 2: iniciar la aplicación principal

Abre otra terminal, activa el mismo entorno virtual y ejecuta:

```bash
python app.py
```

La aplicación principal debe quedar disponible en el puerto 5000.

### Terminal 3: iniciar Locust

Abre una tercera terminal, activa el entorno virtual y ejecuta:

```bash
locust -f tests/locustfile.py --host http://127.0.0.1:5000
```

Después abre `http://localhost:8089` en el navegador para configurar y ejecutar la prueba de carga.

## 7. Rutas disponibles

| Ruta | Función |
|---|---|
| `/` | Comprueba que la aplicación responde. |
| `/salud` | Consulta el estado del servicio. |
| `/api/envio/LG-1001` | Consulta un envío en la API simulada y lo almacena en SQLite. |
| `/api/envio/LG-9999` | Comprueba el manejo de una guía inexistente. |
| `/api/bd/envio/LG-1001` | Consulta un envío almacenado en la base de datos. |
| `/api/bd/envio/LG-9999` | Comprueba el comportamiento cuando la guía no está guardada en SQLite. |

Las rutas de ejemplo utilizan números de guía de prueba. Para consultar otros envíos, sustituye el número de guía en la URL.

## 8. Pruebas realizadas

Se realizaron pruebas funcionales para verificar la consulta de guías existentes e inexistentes, el almacenamiento de la información y la recuperación de los registros guardados.

También se ejecutó una prueba de carga con Locust utilizando 10 usuarios simulados y una tasa de incorporación de 2 usuarios por segundo.

En la ejecución corregida se registraron 400 solicitudes, un tiempo medio de respuesta de 26,68 milisegundos y cero fallos inesperados contabilizados por Locust. Las respuestas HTTP 404 esperadas para las guías inexistentes se clasificaron como respuestas válidas del escenario de prueba.

Estos resultados corresponden al entorno local y no garantizan el mismo rendimiento en producción.

## 9. Observabilidad

Los eventos y tiempos de respuesta se registran en:

```text
logs/app.log
```

Este archivo permite revisar el inicio de las consultas, las respuestas de la API, el almacenamiento de datos y los errores detectados.

## 10. Limitaciones y mejoras futuras

La solución utiliza una API simulada y una base de datos SQLite local. Para una versión futura se propone integrar un proveedor logístico real con autorización, utilizar la base de datos institucional si se dispone de acceso, ampliar las pruebas de carga y evaluar el comportamiento en un entorno de despliegue.

## 11. Evidencias

La carpeta `evidencias` debe contener el reporte HTML de Locust y capturas de las pruebas funcionales, la base de datos, los registros y los componentes principales del código.