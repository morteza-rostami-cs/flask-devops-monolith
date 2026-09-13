from flask import Flask
from shared.settings import Settings
import atexit  # for shutdown events

# routes
from api.src.modules.users import register_users_routes

# db connection
from shared.database import get_pool, pool


# app start up
def create_app():
    app = Flask(__name__)
    # setup .env variables
    app.config.from_object(Settings)

    @app.get("/health")
    def health():
        return dict(status="ok", env_name=app.config["ENV_NAME"])

    # postgres health
    @app.get("/health/db")
    def health_db():
        # with get_connection() as conn:
        #     conn.execute("select 1")

        # borrows and return to pool -- instead of creating and closing
        with get_pool().connection() as conn:
            conn.execute("select 1")

        return dict(status="ok")

    # register routes
    register_users_routes(app)

    # shutdown handler
    def shutdown():
        # close postgres pool
        pool.close()

    # run this on shutdown
    atexit.register(shutdown)

    # return flask app
    return app


app = create_app()  # export a singleton app
