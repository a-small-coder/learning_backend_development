# learning_backend_development
Разбираемся на практике с различными задачами 

## Django start app
python -m venv venv_name - создание виртуального окружения python

venv_name\Scripts\activate.bat - активация виртуального окружения

pip install django  установка джанго
 
django-admin startproject project_name  создание джанго проекта

cd project_name - переход в папку проекта

python manage.py startapp main_app_name - создание приложения внутри проекта

python manage.py migrate  = миграции

python manage.py runserver - запуск сервера

### зависимости python
pip freeze > requirements.txt - задать зависимости
pip install -r requirements.txt - установить пакеты из зависимостей
