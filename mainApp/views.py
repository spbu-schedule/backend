from django.shortcuts import render
from django.views.generic.list import ListView
from mainApp.models import Faculty
import teachers

def index(request):
    return render(request, 'mainApp/index.html')


def instruments(request):
    instruemnts_name = request.GET.get('name') or []
    facultys = Faculty.objects.all()

    items = []
    for _ in instruemnts_name.split(','):

        items.append(_)

    if not items:
        items.append("Не переданны имена инструментов")

    return render(request, 'mainApp/parameters.html', {'values': items, 'name': facultys})


def test(request):
    items = teachers.tool_2_2_2('Математико-механический факультет', 'Алгебра')
    return render(request, 'mainApp/test.html',{'photo': items})

