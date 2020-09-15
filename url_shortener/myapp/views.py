# Vendor
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
# Local
from .validators import validate_link
from .utils import generate_token
from .models import ShortLink


@api_view(['GET'])
def generate_link(request, *args, **kwargs):
    """Генеририуем короткий линк"""
    link = request.query_params.get('link')
    check_link = validate_link(link)
    if check_link:
        return check_link

    token = generate_token()
    short_link = ShortLink.objects.create(
        token=token,
        original_link=link
    )
    return Response({'token': short_link.token})


@api_view(['GET'])
def goto(request, *args, **kwargs):
    """Редиректим на оригинальную ссылку"""
    token = kwargs.get('token')
    short_link = get_object_or_404(ShortLink, token=token)
    return redirect(short_link.original_link)
