from django.forms import ModelForm
from django.core import validators
from django.core.exceptions import ValidationError
from django import forms
from django.forms.widgets import Select
from .models import Cat, Breed
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class CatForm(ModelForm):
    name = forms.CharField(label='Имя', validators=[validators.RegexValidator(regex=r'[А-Яа-я]+')],
                           error_messages={'invalid': 'Введите корректное имя!'})
    age = forms.IntegerField(label='Возраст', min_value=0, max_value=30)
    text = forms.CharField(label='Описание', widget=forms.widgets.Textarea(),
                           initial="Хороший котик Хороший котик Хороший котик Хороший котик Хороший котик ")
    breed = forms.ModelChoiceField(queryset=Breed.objects.all(),
                                   label='Порода', help_text='Укажите породу!',
                                   widget=forms.widgets.Select(), empty_label=None)
    img = forms.ImageField(label='Изображение', validators=[validators.FileExtensionValidator(
        allowed_extensions=('gif', 'jpg', 'png')
    )], error_messages={
        'invalid_extension': 'Этот формат не поддерживается'
    })

    def clean_age(self):
        value = self.cleaned_data['age']
        if value == 5:
            raise ValidationError('Ну ты еблан')
        else:
            return value

    class Meta:
        model = Cat
        fields = ('name', 'age', 'text', 'breed', 'img')


class UserRegistrationForm(ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.widgets.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.widgets.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise ValidationError(r'Passwords don\'t match.')
        return cd['password2']
