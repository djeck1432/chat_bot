import requests
import telegram
import os
from dotenv import load_dotenv



def main():
    load_dotenv()
    devman_access_token = os.getenv('DEVMAN_ACCESS_TOKEN')
    telegram_access_token = os.getenv('TELEGRAM_ACCESS_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    bot = telegram.Bot(token=telegram_access_token)

    url = 'https://dvmn.org/api/long_polling/'
    headers = {'Authorization': 'Token ' + devman_access_token}
    params = {'timestamp': ''}

    while True:
        try:
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            response_devman = response.json()

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


if __name__ == '__main__':
    main()
