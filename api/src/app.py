from flask import Flask


# app start up
def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return dict(status="ok")

    return app


app = create_app()  # export a singleton app
