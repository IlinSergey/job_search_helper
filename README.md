# job_search_helper

Телеграмм бот для поиска вакансий на HeadHunter, уведомления о новых вакансиях и формирования сопроводительного письма для понравившейся вакансии(опционально).

## Установка

### Два варианта установки:

#### Вручную:

1. Клонируйте репозиторий с github
2. Создайте виртуальное окружение
3. Установите зависимости `pip install requirements.txt`
4. Создайте файл `.env`
5. Впишите в `.env` переменные согласно образцу `.env.axample`
6. При необходимости изменить параметры поиска(город, график и т.п.) в файле `services/hh.py` в переменной `params`
а так же в файле `bot.py` в функции `run` интервалы запуска проверок и расссылок вакансий(`interval=сек`)
7. В файле `services/jobs.py` в функции `send_vacation` есть проверка id для отображения функционала сервиса YaGPT, поменять на свой id!
8. Запустите бота командой `python bot.py`

#### С использованием Docker:

1. Клонируйте репозиторий с github
2. Убедитесь, что установлен и запущен Docker
3. Создайте файл `.env`
4. Впишите в `.env` переменные согласно образцу `.env.axample`
5. При необходимости изменить параметры поиска(город, график и т.п.) в файле `hh.py` в переменной `params`
а так же в файле `bot.py` в функции run интервалы запуска проверок и расссылок вакансий(`interval=сек`)
6. В файле `jobs.py` в функции `send_vacation` есть проверка id для отображения функционала сервиса OpenAI, поменять на свой id!
7. Выполните комманду `docker compose --env-file .env up`



### Функционал бота

1. `/start` команда сохранит информацию о текущем пользователе, а так же запросит информацию для поискового запроса.
2. `/run` команда запустит задачи которые в автоматическом режиме будут производить поиск и рассылку вакансий.
3. `/stop` команда остановит задачи которые в автоматическом режиме производят поиск и рассылку вакансий.
