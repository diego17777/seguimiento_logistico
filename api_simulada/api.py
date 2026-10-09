from flask import Flask, jsonify

app = Flask(__name__)


envios = {
    "LG-1001": {
        "numero_guia": "LG-1001",
        "estado": "En tránsito",
        "origen": "Cali",
        "destino": "Cartagena",
        "transportadora": "LogiExpress",
        "ultima_actualizacion": "2026-10-07 18:30:00"
    },
    "LG-1002": {
        "numero_guia": "LG-1002",
        "estado": "Entregado",
        "origen": "Bogotá",
        "destino": "Medellín",
        "transportadora": "LogiExpress",
        "ultima_actualizacion": "2026-10-07 15:45:00"
    },
    "LG-1003": {
        "numero_guia": "LG-1003",
        "estado": "Preparando envío",
        "origen": "Barranquilla",
        "destino": "Cali",
        "transportadora": "LogiExpress",
        "ultima_actualizacion": "2026-10-07 17:10:00"
    }
}


@app.route("/envios/<numero_guia>", methods=["GET"])
def consultar_envio(numero_guia):

    envio = envios.get(numero_guia)

    if envio is None:
        return jsonify({
            "exito": False,
            "error": "No se encontró un envío con ese número de guía."
        }), 404

    return jsonify({
        "exito": True,
        "envio": envio
    }), 200


if __name__ == "__main__":
    app.run(port=5001, debug=True)