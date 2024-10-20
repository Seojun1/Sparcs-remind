from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'user': request.user  # Assuming you're using Django's authentication system
    }
    return render(request, 'main/index.html', context)