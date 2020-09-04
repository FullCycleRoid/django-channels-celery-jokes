# jokes/tasks.py
import logging
from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
import requests


logger = logging.getLogger()


@shared_task
def get_joke():
    res = requests.get("http://api.icndb.com/jokes/random").json()
    joke = res["value"]["joke"]
    logger.info(joke)
    # Передаем сообщение типа `jokes.joke` через channel_layer
    # всем потребителям, которые подключены к группе `jokes`.
    async_to_sync(channel_layer.group_send)(
        "jokes", {"type": "jokes.joke", "text": joke}
    )
