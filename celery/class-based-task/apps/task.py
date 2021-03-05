from celery import Task

class SampleTask(Task):
    name = "sample"

    def __init__(self) -> None:
        super().__init__()

    def run(self, x: int, y: int) -> int:
        return x + y
