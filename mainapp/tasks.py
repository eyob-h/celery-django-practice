from celery import shared_task

@shared_task(bind=True)
def test_task(self):
    for i in range(100):
        print(f"Task Number {i}")
    return "Completed"