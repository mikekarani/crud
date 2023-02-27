from django.shortcuts import render

def HOME(request):
    return render(request,'index.html')