from celery import shared_task


@shared_task(name="plus")
def plus(x: int, y: int) -> int:
    return x + y