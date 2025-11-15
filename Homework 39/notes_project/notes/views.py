from django.shortcuts import render

def home(request):
    notes = [
        {"title": "Перша нотатка", "text": "Це тестовий запис."},
        {"title": "Друга нотатка", "text": "CSS винесений у static."},
        {"title": "Третя нотатка", "text": "Mожна пмінити на ORM або API, коли буде потрібно."},
    ]
    return render(request, "notes/home.html", {"notes": notes})

