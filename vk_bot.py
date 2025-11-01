import os
import random

import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType

from helper_dialogflow import detect_intent_texts

from dotenv import load_dotenv


def echo(event, vk_api):
    dialogflow_response = detect_intent_texts(
        project_id=os.getenv('PROJECT_ID'),
        session_id=event.user_id,
        user_message=event.text,
        language_code='ru'
        )
    vk_api.messages.send(
        user_id=event.user_id,
        message=dialogflow_response,
        random_id=random.randint(1,1000)
    )


if __name__ == "__main__":
    load_dotenv()
    api_key = os.environ['API_KEY_VK_BOT']
    vk_session = vk.VkApi(token=api_key)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            echo(event, vk_api)
