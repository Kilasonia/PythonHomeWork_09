***Структура проекта (модули)***

>1. main (основной модуль)
>>2. logger (модуль логирования) 
>>>3. bot.py (модуль телеграм-бота) 
>>>>4. crude (создание, чтение, обновление, удаление)
>>>>>5. user_interface (модуль взаимодействия с пользователем)
>>>>>>6. data_generation (модуль генерации БД)






***Как запустить проект (рекомендую использовать VCS)***

>1. Для запуска с помощью консоли:
- скачать проект в локальный репозиторий;
- в консоли ввести команду "python3 main.py";
- в случае необходимости создания рандомной базы контактов раскомментировать строку #7 (метод dg.start()) модуля main.py;
- следовать инструкциям в консоли.
>>2. Для запуска телеграм-бота:
- скачать проект в локальный репозиторий;
- обновить  Python минимум до версии 3.10.5;
- настроить окружение, введя в консоли поочередно команды: 
    - python3 -m venv .libraries;
    - pip install pyTelegramBotAPI;
- при необходимости обновить библиотеку до последней версии (следуя инструкциям в консоли)
- перезапустить консоль;
- в корневой папке проекта создать файл с названием "token.csv", в котором в первой строке добавить индивидуальный токен телеграм-бота, после чего сохранить изменения файла;
- инструкция по созданию индивидуального токена телеграм-бота здесь: https://core.telegram.org/bots
- в консоли ввести команду "python3 bot.py" или "python bot.py" (при необходимости установить минимум версию Python 3.10.5)