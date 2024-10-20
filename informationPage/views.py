from django.shortcuts import render

# Create your views here.
def information(request):

    return render(request,'main/information.html')
