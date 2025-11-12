import os
import logging

from telegram import Update
from telegram.ext import (
    Updater, MessageHandler, Filters, CallbackContext
    )

from google.cloud import api_keys_v2
from functools import partial

from dotenv import load_dotenv

from helper_dialogflow import detect_intent_texts


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def create_api_key(project_id):
    client = api_keys_v2.ApiKeysClient()

    key = api_keys_v2.Key()
    key.display_name = "My first API key"

    request = api_keys_v2.CreateKeyRequest()
    request.parent = f"projects/{project_id}/locations/global"
    request.key = key

    response = client.create_key(request=request).result()
    return response


def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Здравствуйте!"
        )


def echo_dialogflow(update: Update, context: CallbackContext, project_id):
    dialogflow_response = detect_intent_texts(
        project_id=project_id,
        session_id=update.effective_chat.id,
        user_message=update.message.text,
        language_code='ru'
    )
    text = dialogflow_response.query_result.fulfillment_text
    update.message.reply_text(text=text)


def main():
    load_dotenv()
    api_key = os.environ['API_KEY_TG_BOT']
    project_id = os.environ['PROJECT_ID']
    updater = Updater(api_key, use_context=True)

    dispatcher = updater.dispatcher

    echo_handler = partial(echo_dialogflow, project_id=project_id)
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, echo_handler
    ))

    updater.start_polling()
    updater.idle()

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
