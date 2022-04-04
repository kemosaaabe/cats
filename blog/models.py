from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.conf import settings


def validate_max_or_min(value):
    if value <= 0 or value > 30:
        raise ValidationError(f'Возраст котика неправильный! Не издевайся, над котиком..')


class Cat(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=30, verbose_name="Кличка",
                            validators=[validators.RegexValidator(regex=r'[А-Яа-я]+',
                                                                  message="Не издевайся на котиком...")])
    # Добавил валидатор на проверку имени, чтобы в кличке были только русские буквы

    age = models.IntegerField(verbose_name="Возраст", validators=[validators.MinValueValidator(0),
                                                                  validators.MaxValueValidator(30)],
                              error_messages={'min_value': 'Не издевайся над котиком!'})
    # Добавил валидатор на проверку возраста, можно вставить свой валидатор.
    # error_message: если значение меньше, будет выведено такое значение

    text = models.TextField(null=True, blank=True, verbose_name="Описание")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата публикации")
    breed = models.ForeignKey('Breed', on_delete=models.PROTECT, verbose_name="Порода")

    img = models.ImageField(verbose_name='Изображение', upload_to='', null=True)

    def delete(self, *args, **kwargs):
        self.img.delete(save=False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Котик"
        verbose_name_plural = "Котики"
        ordering = ['published']


class Breed(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name="Порода")
    text = models.TextField(verbose_name="Описание породы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"
        ordering = ['name']



