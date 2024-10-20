# context_processors.py

def user_info(request):
    return {
        'user_info': {
            'is_logged_in': request.session.get('is_logged_in', False),
            'user_id': request.session.get('user_id'),
            'username': request.session.get('username'),  # user_name 대신 username 사용
            'user_age': request.session.get('user_age'),
            'gender': request.session.get('gender'),
        }
    }