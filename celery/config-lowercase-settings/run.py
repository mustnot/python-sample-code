import os
from celery import Celery

app = Celery()
os.environ.setdefault("CELERY_CONFIG_MODULE", "settings")

app.config_from_envvar('CELERY_CONFIG_MODULE')