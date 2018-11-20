from django.shortcuts import render
from django.views.generic.list import ListView
from mainApp.models import Faculty
import teachers, rooms, lesson

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
    global put
    put = request.get_full_path()
    put = put.replace('/instruments/?name=','')

    return render(request, 'mainApp/parameters.html', {'values': items, 'name': facultys})


def test(request):
    faculty = request.POST.get('post_faculty')
    group = request.POST.get('post_group')
    discipline = request.POST.get('post_discipline')
    name_teacher = request.POST.get('post_name_teacher')
    date_week = request.POST.get('post_date_week')
    audience = request.POST.get('post_audience')
    adress = request.POST.get('post_adress')
    date_range = request.POST.get('post_date_range')
    date_start = request.POST.get('post_date_start')


    if put == '1-1':
        items = rooms.tool_1_1()
    elif put == '1-2':
        items = rooms.tool_1_2()
    elif put == '1-3':
        tool = adress + ', ' + audience
        items = rooms.tool_1_3(tool)
    elif put == '2-1':
        items = teachers.tool_2_1_1(faculty, group)
    elif put == '2-2':
        items = teachers.tool_2_1_2(faculty, discipline)
    elif put == '2-3':
        items = teachers.tool_2_2_1(faculty, group)
    elif put == '2-4':
        items = teachers.tool_2_2_2(faculty, discipline)
    elif put == '2-5':
        items = teachers.tool_2_3(faculty,name_teacher,date_week)
    elif put == '3-1':
        items = lesson.tool_3_1(faculty,group,date_week)
    elif put == '3-2':
        items = lesson.tool_3_2(faculty, group, discipline)
    elif put == '3-3':
        items = lesson.tool_3_3(faculty, group, date_week)
    elif put == '3-4':
        items = lesson.tool_3_4(faculty, group, discipline)
    elif put == '3-5':
        items = lesson.tool_3_5(faculty, date_week)
    return render(request, 'mainApp/test.html',{'photo': items,'tt': discipline, 'dd': group,'oo': put})

