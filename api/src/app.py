from flask import Flask
from shared.settings import Settings

# routes
from api.src.modules.users import register_users_routes


# app start up
def create_app():
    app = Flask(__name__)
    # setup .env variables
    app.config.from_object(Settings)

    @app.get("/health")
    def health():
        return dict(status="ok", env_name=app.config["ENV_NAME"])

    # register routes
    register_users_routes(app)

    return app


app = create_app()  # export a singleton app
