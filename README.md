# Cards# forms
WEB приложение для кредитных карт

## Запуск проекта:

Откройте консоль

Перейдите в папку, в которой будет храниться проект

cd <путь до папки>

Склонируйте проект
git clone https://github.com/SimonaSoloduha/Cards

## Перейдите в папку проекта
cd Cards

## Создайте виртуальное окружение venv
python3 -m venv venv

## Активируйте виртуальное окружение venv
source venv/bin/activate

## Установите необходимые пакеты:

cd cards
pip3 install -r requirements.txt
(Все используемые библиотеки представлены в файле requirements.txt)

## При необходимости обновите pip и отдельно установить следующие пакеы: 

python3 -m pip install django

# Запустите миграции 

python3 manage.py migrate  

# Запустите проект через консоль 

python3 manage.py runserver 

* Для работы с картами перейдите на сайт: 
http://127.0.0.1:8000

* Для завершения работы ввеите в консоли "Contril + C"
