from django.db import models


class ShortLink(models.Model):
    class Meta:
        verbose_name = 'Короткая ссылка'
        verbose_name_plural = 'Короткие ссылки'

    token = models.CharField(
        "Сгенеренный токен",
        primary_key=True,
        max_length=10
    )
    original_link = models.CharField(
        "Оригинальная ссылка",
        max_length=5000,
        db_index=True
    )
    generated_at = models.DateTimeField(
        "Сгенерировано",
        auto_now_add=True
    )
