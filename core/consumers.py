# jokes/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class JokesConsumer(WebsocketConsumer):
    def connect(self):
        # Подключает канал с именем `self.channel_name`
        # к группе `jokes`
        async_to_sync(self.channel_layer.group_add)(
            "jokes", self.channel_name
        )
        # Принимает соединение
        self.accept()

    def disconnect(self, close_code):
        # Отключает канал с именем `self.channel_name`
        # от группы `jokes`
        async_to_sync(self.channel_layer.group_discard)(
            "jokes", self.channel_name
        )

    # Метод `jokes_joke` - обработчик события `jokes.joke`
    def jokes_joke(self, event):
        # Отправляет сообщение по вебсокету
        self.send(text_data=event["text"])