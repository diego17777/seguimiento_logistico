import logging
import time
from flask import Flask, jsonify
from api_service import consultar_envio as consultar_envio_api
from database import crear_tabla, guardar_envio, consultar_envio_bd

app = Flask(__name__)
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
crear_tabla()

@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "Sistema de seguimiento logístico",
        "estado": "Funcionando correctamente"
    })


@app.route("/salud")
def salud():
    return jsonify({
        "servicio": "seguimiento-logistico",
        "estado": "activo"
    })


@app.route("/api/envio/<numero_guia>")
def consultar_envio(numero_guia):

    tiempo_inicio = time.perf_counter()

    logger.info(f"Consulta de envío iniciada: {numero_guia}")

    resultado = consultar_envio_api(numero_guia)

    if resultado["exito"]:

        envio = resultado["datos"]["envio"]

        logger.info(
            f"API respondió correctamente para la guía: {numero_guia}"
        )

        guardar_envio(envio)

        logger.info(
            f"Envío almacenado en la base de datos: {numero_guia}"
        )

        tiempo_fin = time.perf_counter()
        tiempo_respuesta = tiempo_fin - tiempo_inicio

        logger.info(
            f"Tiempo de respuesta para {numero_guia}: "
            f"{tiempo_respuesta:.4f} segundos"
        )

        return jsonify({
            "exito": True,
            "codigo": 200,
            "mensaje": "Envío consultado y almacenado correctamente.",
            "tiempo_respuesta_segundos": round(tiempo_respuesta, 4),
            "envio": envio
        }), 200

    logger.warning(
        f"No fue posible consultar la guía: {numero_guia}. "
        f"Error: {resultado.get('error')}"
    )

    tiempo_fin = time.perf_counter()
    tiempo_respuesta = tiempo_fin - tiempo_inicio

    logger.info(
        f"Tiempo de respuesta para {numero_guia}: "
        f"{tiempo_respuesta:.4f} segundos"
    )

    return jsonify({
        **resultado,
        "tiempo_respuesta_segundos": round(tiempo_respuesta, 4)
    }), resultado["codigo"]


@app.route("/api/bd/envio/<numero_guia>")
def consultar_envio_guardado(numero_guia):
    envio = consultar_envio_bd(numero_guia)

    if envio is None:
        return jsonify({
            "exito": False,
            "codigo": 404,
            "error": "El envío no se encuentra almacenado en la base de datos."
        }), 404

    return jsonify({
        "exito": True,
        "codigo": 200,
        "mensaje": "Envío encontrado en la base de datos.",
        "envio": envio
    }), 200


if __name__ == "__main__":
    app.run(debug=False)