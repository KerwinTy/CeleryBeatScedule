CELERY_IMPORTS = ('tasks')
CELERY_IGNORE_RESULT = False
BROKER_HOST = '127.0.0.1'
BROKER_PORT = 6379
BROKER_URL = 'redis://'

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'IMPORT-REDIS-EVERY-5-SECONDS':{
        'task': 'tasks.readredis',
        'schedule': timedelta(seconds = 5),
    },
}
