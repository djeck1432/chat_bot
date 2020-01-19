# Отправляем уведомления о проверке работ с помощью Telegram bot 

Данный ```telegram bot``` поможет ученикам <a href='https://dvmn.org/'>Devman</a> получать уведомления о проверке работ.
Теперь, вы никогда не пропустите, когда ваше задания пришло с проверки.

## Переменные окружения 

```DEVMAN_ACCESS_TOKEN``` - токен, от сайта <a href='https://dvmn.org/'>Devman</a>, его можно получить по этой <a href='https://dvmn.org/api/docs/'>ссылке</a>.
<br>

```TELEGRAM_ACCESS_TOKEN``` - токен от ```telegram```, как получить, смотрите по <a href='https://romua1d.ru/kak-poluchit-token-bota-telegram-api/'>ссылке</a>.<br>
```TELEGRAM_LOG_BOT_TOKEN``` - токен от бота, который будет отправлять вам логи.

<br>
```TELEGRAM_CHAT_ID``` - имя вашего бота в ```telegram```. <br>
```TELEGRAM_LOG_BOT_CHAT_ID``` - имя вашего бота, куда будут приходить ```log``` программы.<br>
Его можно посмотреть во вкладке```Chanel info```, выглядит так: ```@test```.

## Инструкция по запуску  

Откройте у себя на компьютере ```bash``` и в нем пропишите следующие команды: 
<br>
```git clone https://github.com/djeck1432/chat_bot.git```
<br>
Откройте папку:
<br>
```cd chat_bot ```
<br>
Установиту необходимые библиотеки и модули:
<br>
```pip install -r requirements.txt```
<br>
Запустите код: 
<br>
```python main.py ```
<br>
Готово, ваш сервер запущен и как только преподаватель проверит вашу работу, вам прийдут уведомления об этом. 
