from django.shortcuts import render

def search(request):
    return render(request, 'search_audience/search.html')

def time(request):
    return render(request,'search_audience/hello.html')
