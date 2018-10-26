from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html',{'values':['Позвоните по телефону: ', '89995354005']})


def instruments(request):
    instruemnts_name = request.GET.get('name') or []

    items = []
    for _ in instruemnts_name.split(','):
        if _ == '1':
            items.append("На странице отобразится инструмент с именем - {}".format(_))

    if not items:
        items.append("Не переданны имена инструментов")

    return render(request, 'mainApp/main.html', {'values': items})
