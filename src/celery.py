from celery import Celery

from src.settings import SETTINGS

celery = Celery(
    broker=SETTINGS.REDIS_URL,
    backend=SETTINGS.REDIS_URL
)
celery.autodiscover_tasks(
    packages=['src']
)
celery.conf.beat_schedule = {
    'spammer': {
        'task': 'src.tasks.tasks.spam_machine',
        'args': ('выключи меня', 'thommy.python.dev@gmail.com'),
        'schedule': 10.0
    }
}
