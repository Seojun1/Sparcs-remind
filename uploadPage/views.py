from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random

# 미리 준비된 문장들
predefined_sentences = [
    "오늘 하루도 수고 많으셨어요.",
    "일상의 소중한 순간을 잘 담아내셨네요.",
    "사진에서 행복한 기운이 느껴집니다.",
    "오늘의 경험이 좋은 추억으로 남길 바랍니다.",
    "새로운 도전을 한 것 같아 보여요. 멋집니다!",
    "일상의 작은 기쁨을 잘 포착하셨어요.",
    "오늘 하루 잘 마무리하셨나요?",
    "내일도 좋은 하루 되시길 바랍니다.",
    "사진 속 풍경이 정말 아름답네요.",
    "소중한 사람들과 함께한 시간이 보이네요."
]

@csrf_exempt
def uploadPage(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        image_url = data.get('image_url')
        description = data.get('description')
        
        # 여기서 실제로 데이터를 저장하지 않고, 성공 응답만 반환합니다.
        return JsonResponse({
            'success': True,
            'message': '이미지와 설명이 성공적으로 저장되었습니다.',
            'report': random.choice(predefined_sentences)
        })
    
    # GET 요청 시 메인 페이지 렌더링
    return render(request, 'main/upload.html')