import os
from flask import Flask


def create_app(config: str = "config.DefaultConfig") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    return app


if __name__ == "__main__":
    config = os.environ.get("PROJECT_CONFIG", "config.DefaultConfig")
    app = create_app(config)
    app.run()