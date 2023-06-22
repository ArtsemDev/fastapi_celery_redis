## Celery + Redis

### Порядок запуска

* Beat
* Worker
* Flower
* Application

### INSTALATION

`pip install -r requirements.txt`

### Run Workers

`celery -A src.celery:celery worker -l INFO --concurrency=5`

### Run Beat

`celery -A src.celery:celery beat -l INFO`

### Run Flower

`celery -A src.celery:celery flower --port=8080`

## Redis

### Get

`get key_name`

### Set

`set key_name value`

### Delete

`del key_name`

### Delete All

`flushall`