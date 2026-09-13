from flask import Flask
from shared.settings import Settings


# app start up
def create_app():
    app = Flask(__name__)
    # setup .env variables
    app.config.from_object(Settings)

    @app.get("/health")
    def health():
        return dict(status="ok", env_name=app.config["ENV_NAME"])

    return app


app = create_app()  # export a singleton app
