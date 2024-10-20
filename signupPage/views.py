from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import SignUp
from datetime import datetime

def signup(request):
    if request.method == 'POST':
        # 폼 데이터 받기
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        username = request.POST.get('username')
        birthdate = request.POST.get('birthdate')
        gender = request.POST.get('gender')
        email = request.POST.get('email')

        # 생년월일을 나이로 변환
        try:
            birth_date = datetime.strptime(birthdate, '%Y-%m-%d')
            today = datetime.now()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        except ValueError:
            return JsonResponse({'success': False, 'error': '올바른 생년월일 형식이 아닙니다.'})

        # 성별 변환 (female -> F, male -> M)
        gender = 'F' if gender == 'female' else 'M'

        # SignUp 모델 인스턴스 생성 및 저장
        signup = SignUp(
            user_id=user_id,
            user_password=password,
            username=username,
            age=age,
            email=email,
            gender=gender
        )

        try:
            signup.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': '회원가입이 완료되었습니다.'})
            else:
                messages.success(request, '회원가입이 완료되었습니다.')
                # 세션에 이름 저장
                request.session['username'] = username
                print(f"세션에 저장된 사용자 이름: {request.session.get('username')}")  # 세션 값 로그 출력

                return redirect('/cognitive_test')  # 로그인 페이지로 리다이렉트

        except Exception as e:
            messages.error(request, f'회원가입 중 오류가 발생했습니다: {str(e)}')
            return render(request, 'main/signup.html')

    return render(request, 'main/signup.html')
