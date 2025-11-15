# Notes Project (Django)

- головна HTML‑сторінка з нотатками  
- view із тестовими даними  
- CSS винесений у `static`

---

## Запуск проєкту

### 1. Клонування репозиторію
```bash
git clone https://github.com/<твій-юзернейм>/<repo-name>.git
cd <repo-name>/notes_project

 Встановлення

Linux/MacOS

python3 -m venv venv
source venv/bin/activate



Windows

python -m venv venv
venv\Scripts\activate

Встановлення залежностей
pip install -r requirements.txt

Міграції та запуск сервера
python manage.py migrate
python manage.py runserver

Перевірка
http://127.0.0.1:8000


Структура проєкту

notes_project/
├── manage.py
├── notes_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── notes/
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── notes/
│   │       └── home.html
│   └── static/
│       └── notes/
│           └── css/
│               └── main.css
└── requirements.txt


Використані технології
Python 3.14

Django 5.2.8


Extra
CSS винесений у окремий файл у static/notes/css/main.css

Легко розширити: можна додати модель Note і адмінку
