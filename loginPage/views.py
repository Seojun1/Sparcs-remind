# loginPage/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from signupPage.models import SignUp

def login(request):
    if request.method == 'POST':
        user_id = request.POST.get('username')
        password = request.POST.get('password')
        
        users = SignUp.objects.filter(user_id=user_id)
        
        if users.exists():
            user = users.first()
            if user.user_password == password:  # 주의: 실제로는 암호화된 비밀번호를 사용해야 합니다
                # 로그인 성공
                request.session['user_id'] = user.user_id
                request.session['username'] = user.username  # user_name 대신 username 사용
                request.session['user_age'] = user.age
                request.session['gender'] = user.gender
                request.session['is_logged_in'] = True
                
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': True, 'message': '로그인 성공', 'redirect': '/home'})
                else:
                    messages.success(request, '로그인 성공')
                    return redirect('/home')
            else:
                # 비밀번호 불일치
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'message': '아이디 또는 비밀번호가 올바르지 않습니다.'})
                else:
                    messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
        else:
            # 사용자가 존재하지 않음
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': '아이디 또는 비밀번호가 올바르지 않습니다.'})
            else:
                messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
    
    return render(request, 'main/login.html')