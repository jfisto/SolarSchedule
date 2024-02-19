from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from solar_schedule.models import Users


def login(username: str, password: str) -> dict:
    if not username or not password:
        return {'status': False, 'token': None, 'err': 'Данные не предоставленны'}

    user = authenticate(username=username, password=password)
    if user is None:
        return {'status': False, 'token': None, 'err': 'Неправильные логин или пароль'}

    if not user.is_active:
        return {'status': False, 'token': None, 'err': 'Пользователь заморожен или удалён'}

    try:
        return {'status': True, 'token': Token.objects.get(user=user).key, 'err': None}
    except:
        Token.objects.create(user=user)
        return {'status': True, 'token': user.auth_token.key, 'err': None}


def registration(username: str, password: str, email: str, first_name: str = '',
                             last_name: str = ''):
    if not email or not username or not password:
        return {'status': False, 'token': None, 'err': 'Данные не предоставленны'}

    if Users.objects.filter(email=email).exists():
        return {'status': False, 'token': None, 'err': 'Этот адрес электронной почту уже используется'}

    if Users.objects.filter(username=username).exists():
        return {'status': False, 'token': None, 'err': 'Это имя пользователя уже занято'}

    if len(password) < 8:
        return {'status': False, 'token': None, 'err': 'Пароль слишком короткий'}

    user = Users.objects.create_user(
        email=email,
        username=username,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )
    Token.objects.create(user=user)
    return {'status': True, 'token': user.auth_token.key, 'err': None}