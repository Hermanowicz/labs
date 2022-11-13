import time
from locust import HttpUser, task, between


class SimpleUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_uuid(self):
        self.client.get("/uuid")

    @task(2)
    def get_xml(self):
        self.client.get("/xml")
        time.sleep(1)

    @task(3)
    def get_json(self):
        self.client.get("/json")
        time.sleep(1)

    @task
    def get_bytes(self):
        self.client.get("/bytes/128")

    def on_start(self):
        self.client.get("/headers")
        self.client.get("/ip")
        self.client.get("/user-agent")
        