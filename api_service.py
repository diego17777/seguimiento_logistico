import requests

API_URL = "http://127.0.0.1:5001/envios"


def consultar_envio(numero_guia):
    try:
        url = f"{API_URL}/{numero_guia}"

        respuesta = requests.get(url, timeout=5)

        if respuesta.status_code == 404:
            return {
                "exito": False,
                "codigo": 404,
                "error": "No se encontró un envío con ese número de guía."
            }

        respuesta.raise_for_status()

        datos = respuesta.json()

        return {
            "exito": True,
            "codigo": respuesta.status_code,
            "datos": datos
        }

    except requests.exceptions.Timeout:
        return {
            "exito": False,
            "codigo": 504,
            "error": "La solicitud superó el tiempo máximo de espera."
        }

    except requests.exceptions.RequestException as error:
        return {
            "exito": False,
            "codigo": 502,
            "error": f"Error en la comunicación con la API: {error}"
        }