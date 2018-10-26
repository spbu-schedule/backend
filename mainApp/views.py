from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/index.html')


def instruments(request):
    instruemnts_name = request.GET.get('name') or []

    items = []
    for _ in instruemnts_name.split(','):

        items.append("На странице отобразится инструмент с именем - {}".format(_))

    if not items:
        items.append("Не переданны имена инструментов")

    return render(request, 'mainApp/main.html', {'values': items})
