# Отправляем уведомления о проверке работ с помощью Telegram bot 

Данный ```telegram bot``` поможет ученикам <a href='https://dvmn.org/'>Devman</a> получать уведомления о проверке работ.
Теперь, вы никогда не пропустите, когда ваше задания пришло с проверки.

## Переменные окружения 

```DEVMAN_ACCESS_TOKEN``` - токен, от сайта <a href='https://dvmn.org/'>Devman</a>, его можно получить по этой <a href='https://dvmn.org/api/docs/'>ссылке</a>.
<br>

```TELEGRAM_ACCESS_TOKEN``` - токен от ```telegram```, как получить, смотрите по <a href='https://romua1d.ru/kak-poluchit-token-bota-telegram-api/'>ссылке</a>. <br>
```TELEGRAM_LOG_BOT_TOKEN``` - токен от бота, который будет отправлять вам логи.
</br>

```TELEGRAM_CHAT_ID``` - имя вашего бота в ```telegram```. <br>
```TELEGRAM_LOG_BOT_CHAT_ID``` - имя вашего бота, куда будут приходить ```loggs``` программы.<br>
Его можно посмотреть во вкладке```Chanel info```, выглядит так: ```@test```.

## Инструкция по запуску кода на сервере

### Регистрация и установка Heroku

Зарегистрируйтесь  на этом <a href='https://signup.heroku.com/dc'>сайте</a>.
<br>
Для работы через терминал, установите ```CLI``` для ```Heroku```, для этого
откройте у себя на компьютере ```bash``` и в нем пропишите следующие команды: 
<br>
Для ```Linux``` -<br>
```sudo snap install heroku --classic```
<br>
Для ```MacOs``` - <br>
```brew install heroku/brew/heroku```
<br>
Оставаясь в терминал, зайдите через ```bash``` в ваш аккаунт на ```Heroku```:
<br>
```heroku login```
<br>
### Загрузка кода на сервер Heroku

Загрузите с ```github``` ваш репозиторий на компьютер: 
<br>
```git clone https://github.com/djeck1432/chat_bot.git```
<br>
Откройте папку:
<br>
```cd chat_bot ```
<br>
Создайте приложения в ```Heroku``` :
<br>
```heroku create```
<br>
Загрузите ваш репозиторий на сервер ```Heroku```:
<br>
```git push heroku master```
<br>

### Настройка окружения и запуск сервера

Перейдите по <a href='https://dashboard.heroku.com/apps'>ссылке</a>, выберете свое приложения и откройте его
<br>
В меню навигации, перейдите на вкладку ```Settings```.
<br>
В разделе ```Config vars```, передайте ваши переменные окружения.
<br>
В терминале, выполните следующую команду для запуска кода на сервере:<br>
```heroku ps:scale bot=1```
<br>
Поздравляю, теперь ваш ```Bot``` работает постоянно, вне зависимости, включен ваш компьютер или нет.


