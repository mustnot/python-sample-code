import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class DefaultConfig(object):
    ENV = "default"
    SECRET_KEY = os.environ.get("SECRET_KEY", "*r_y%w65qdxpf9thh%$3%eyx1h0l^3@!!flo*um3-@e9!%)4xc")
    DATABASE_URI = os.environ.get("DATABASE_URI", os.path.join("sqlite://", BASE_DIR, "db.sqlite3"))


class ProductionConfig(DefaultConfig):
    ENV = "production"


class DevelopmentConfig(DefaultConfig):
    ENV = "development"
    DEBUG = True


class TestingConfig(DefaultConfig):
    ENV = "testing"
    TESTING = True