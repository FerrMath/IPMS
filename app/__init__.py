from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)
    # TODO create and register the blueprints for the pages and API
    @app.get("/health")
    def health():
        return {"status":"ok"}
    return app