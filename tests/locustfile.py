from locust import HttpUser, task, between


class UsuarioSeguimiento(HttpUser):
    wait_time = between(1, 2)

    @task(3)
    def consultar_envio_existente(self):
        with self.client.get(
            "/api/envio/LG-1001",
            name="/api/envio/[guia existente]",
            catch_response=True
        ) as respuesta:

            if respuesta.status_code == 200:
                respuesta.success()
            else:
                respuesta.failure(
                    f"Respuesta inesperada: {respuesta.status_code}"
                )

    @task(1)
    def consultar_envio_inexistente(self):
        with self.client.get(
            "/api/envio/LG-9999",
            name="/api/envio/[guia inexistente]",
            catch_response=True
        ) as respuesta:

            if respuesta.status_code == 404:
                respuesta.success()
            else:
                respuesta.failure(
                    f"Respuesta inesperada: {respuesta.status_code}"
                )
