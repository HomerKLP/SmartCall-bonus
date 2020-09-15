# Vendor
from rest_framework.response import Response
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_link(link: str):
    """Валидируем указанную ссылку"""
    if not link:
        return Response(data={"msg": "Необходимо указать параметр: link"},
                        status=400)

    validate = URLValidator()
    try:
        validate(link)
    except ValidationError as e:
        return Response(data={"msg": 'Указанная ссылка не является валидной'},
                        status=400)

    return None


