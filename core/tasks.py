import requests
import logging
from celery import shared_task


logger = logging.getLogger()


@shared_task
def get_joke():
    res = requests.get("http://api.icndb.com/jokes/random").json()
    joke = res["value"]["joke"]
    logger.info(joke)
