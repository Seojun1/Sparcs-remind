from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import json
import openai
from datetime import datetime
from django.contrib.auth.decorators import login_required

def cognitive_test(request):
    name = request.session.get('username', '이름 없음')  # 세션에서 이름 가져오기
    
    return render(request, 'main/cognitive_test.html', {'name': name})
