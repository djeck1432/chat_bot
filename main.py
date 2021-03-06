import requests
import telegram
import os
from dotenv import load_dotenv
import logging


class MyLogsHandler(logging.Handler):
    def __init__(self, telegram_log_access_token, telegram_log_chat_id):
        logging.Handler.__init__(self)
        self.telegram_access_token = telegram_log_access_token
        self.telegram_log_chat_id = telegram_log_chat_id
        self.bot_log = telegram.Bot(token=telegram_log_access_token )

    def emit(self, record):
        log_entry = self.format(record)
        return self.bot_log.send_message(chat_id=self.telegram_log_chat_id, text=log_entry)


def get_devman_response(devman_access_token, params):
    url = 'https://dvmn.org/api/long_polling/'
    headers = {'Authorization': 'Token ' + devman_access_token}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


def start_bot(devman_access_token, bot, telegram_chat_id):
    while True:
        params = {'timestamp': ''}
        try:
            response_devman = get_devman_response(devman_access_token, params)
            if response_devman['status'] == 'found':
                if response_devman['new_attempts']:
                    result = 'К сожалению, в работе нашлись ошибки.'
                else:
                    result = 'Преподавателю всё понавилось, можно приступать к следующему уроку!'

                lesson_url = 'https://dvmn.org{}#review-tabs'.format(response_devman['new_attempts'][0]['lesson_url'])
                text_message = 'У вас проверили работу "{lesson_title}"\n\n{result}\n\nОткрыть урок можно по ссылке ниже{lesson_url}'.format(
                    lesson_title=response_devman['new_attempts'][0]['lesson_title'],
                    result=result,
                    lesson_url=lesson_url
                )
                bot.send_message(chat_id=telegram_chat_id, text=text_message)
                params['timestamp'] = response_devman['last_attempt_timestamp']
            else:
                params['timestamp'] = response_devman['timestamp_to_request']

        except requests.exceptions.ReadTimeout:
            continue
        except ConnectionError:
            continue


def main():
    load_dotenv()
    devman_access_token = os.getenv('DEVMAN_ACCESS_TOKEN')
    telegram_access_token = os.getenv('TELEGRAM_ACCESS_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    telegram_log_access_token = os.getenv('TELEGRAM_LOG_BOT_TOKEN')
    telegram_log_chat_id = os.getenv('TELEGRAM_LOG_BOT_CHAT_ID')

    bot = telegram.Bot(token=telegram_access_token)
    bot_log = MyLogsHandler(telegram_log_access_token, telegram_log_chat_id)

    logger = logging.getLogger("DevmanBot")
    logger.setLevel(logging.INFO)
    logger.addHandler(bot_log)

    logger.info('Bot was starting')
    while True:
        try:
            start_bot(devman_access_token, bot, telegram_chat_id)
        except:
            logger.info('Bot was down')
            logger.exception()


if __name__ == '__main__':
    main()
