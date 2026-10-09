import sqlite3

DATABASE = "database/envios.db"


def conectar():
    return sqlite3.connect(DATABASE)


def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS envios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_guia TEXT UNIQUE NOT NULL,
            estado TEXT NOT NULL,
            origen TEXT NOT NULL,
            destino TEXT NOT NULL,
            transportadora TEXT NOT NULL,
            ultima_actualizacion TEXT NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()


def guardar_envio(envio):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO envios (
            numero_guia,
            estado,
            origen,
            destino,
            transportadora,
            ultima_actualizacion
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        envio["numero_guia"],
        envio["estado"],
        envio["origen"],
        envio["destino"],
        envio["transportadora"],
        envio["ultima_actualizacion"]
    ))

    conexion.commit()
    conexion.close()


def consultar_envio_bd(numero_guia):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            numero_guia,
            estado,
            origen,
            destino,
            transportadora,
            ultima_actualizacion
        FROM envios
        WHERE numero_guia = ?
    """, (numero_guia,))

    resultado = cursor.fetchone()

    conexion.close()

    if resultado is None:
        return None

    return {
        "numero_guia": resultado[0],
        "estado": resultado[1],
        "origen": resultado[2],
        "destino": resultado[3],
        "transportadora": resultado[4],
        "ultima_actualizacion": resultado[5]
    }