from django.shortcuts import render

# Create your views here.
def doors(request):
    return render(request,'doors.html')
def form(request):
    return render(request,'form.html')
def layouts(request):
    return render(request,'layouts.html')
def universal(request):
    return render(request,'universal.html')