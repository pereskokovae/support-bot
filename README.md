# Support-bot
Данный проект представляет собой систему ботов для автоматического ответа пользователям через Telegram или VK, с интеграцией через DialogFlow.
Боты принимают сообщения от пользователей, передают их в DialogFlow, получают обработанные ответы и отправляют пользователю.

Цель проекта: ускорить ответы и автоматизировать обработку часто задаваемых вопросов.

### Окружение
- Python 3.11+
- DialogFlow API(Google Cloud)

## Зависимости
Все зависимости указаны в `requirements.txt`. Установите их с помощью команды:
```bash
pip install -r requirements.txt
```
### Переменные окружения
Перед запуском создайте файл `.env` в корне проекта и добавьте туда ваши ключи и токены:
```bash
API_KEY_TG_BOT=токен_вашего_тг_бота
GOOGLE_APPLICATION_CREDENTIALS=путь_к_файлу_service_account.json
PROJECT_ID=идентификатор_вашего_dialogflow_проекта
API_KEY_VK_BOT=токен_вашего_вк_бота
```
#### Как получить

| Переменная    | Описание      |
| ------------- | ------------- |
| API_KEY_TG_BOT | токен вашего Telegram бота, чтобы его получить, создайте бота в [@BotFather](https://telegram.me/BotFather).  |
| GOOGLE_APPLICATION_CREDENTIALS | путь к json файлу сервисного аккаунта Google, который вы получили при настройки [DialogFlow](https://dialogflow.cloud.google.com/).|
| PROJECT_ID  | идентификатор вашего проекта в Google Cloud, который вы получили при настройки DialogFlow.  |
| API_KEY_VK_BOT | токен вашего VK бота, полученный в настройках группы во вкладке "Работа с API" --> "Создать ключ доступа".  |

## Запуск проекта
1. Склонируйте репозиторий
```bash
git clone http://github.com/pereskokovae/support-bot.git
```

2. Создайте и активируйте виртуальное окружение
Для Windows:
```bash
python -m venv venv
```
```bash
venv\Scripts\activate
```
Для Linux/macOS:
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```

3. Установите зависимости
```bash
pip install -r requirements.txt
```

4. Запуск ботов
После настройки `.env` вы можете запустить бота для Telegram или VK:
```bash
python tg_bot.py
python vk_bot.py
```

Работа с DialogFlow

Файл helper_dialogflow.py содержит функции для взаимодействия с DialogFlow API.
Основная функция — create_intent(), которая позволяет добавлять новые интенты напрямую из кода.

#### Как добавить новый интент
1. Ручной способ:
Добавьте интент через консоль DialogFlow Console.

2. Программный способ:
Чтобы создать все интенты из файла questions.json, выполните команду:
```bash
python helper_dialogflow.py
```

Скрипт:
- считает данные из questions.json,
- создаст интенты в DialogFlow,
- выведет в консоль количество успешно добавленных интентов.

Вы можете отредактировать файл под себя или воспользоваться тем, который уже есть в проекте.

### Пример работы бота в Telegram:
![Support-bot gif](media/tg_bot.gif)


