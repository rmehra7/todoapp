from flask import Flask
from flask_restplus import Api, Resource, fields, Namespace
from server.app_config import environment_config


class Server:

    def __init__(self):
        self.app = Flask(__name__,
            template_folder='../templates',
            static_folder='../templates',
            instance_relative_config=True
        )
        self.app.secret_key = '88e99a7815624e378e4e62eb0d7759d3'
        self.api = Api(self.app, 
            version='1.0',
            default='Todo Demo Project',
            title='Todo Demo Project',
            description='Todo Demo Project with cred operations, \
                swagger ui, docker, restplus rest apis.',
            doc = environment_config["swagger-url"]
        )

    def run(self):
        """Application initial point"""
        self.app.run(
                debug = environment_config["debug"], 
                port = environment_config["port"],
                host='0.0.0.0'
            )

server = Server()
