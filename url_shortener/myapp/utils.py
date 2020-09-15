# Vendor
from django.conf import settings
import secrets
# Local
from .models import ShortLink


def check_token(token: str) -> str:
    """Проверка токена на уникальность"""
    try:
        ShortLink.objects.get(token=token)
    except ShortLink.DoesNotExist:
        return token
    else:
        return generate_token()


def generate_token():
    """Генерация токена"""
    generated_token = secrets.token_urlsafe(settings.TOKEN_LENGTH)
    return check_token(generated_token)
