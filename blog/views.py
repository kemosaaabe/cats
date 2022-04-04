from django.shortcuts import render
from django.http import FileResponse, HttpResponseRedirect
from .models import Cat
from .forms import CatForm, UserRegistrationForm
from django.urls import reverse
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.decorators import login_required


def start(request):
    cats = Cat.objects.all()
    user = request.user
    context = {'cats': cats, 'user': user}
    return render(request, 'blog/index.html', context)


@login_required
def create_cat(request):
    if request.method == "POST":
        catf = CatForm(request.POST, request.FILES)
        if catf.is_valid():
            post = catf.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('start'))
        else:
            context = {'form': catf}
            return render(request, 'blog/create_cat.html', context)
    else:
        catf = CatForm()
        context = {'form': catf}
        return render(request, 'blog/create_cat.html', context)


@login_required
def edit_cat(request, cat_id):
    cat = Cat.objects.get(pk=cat_id)
    if request.method == "POST":
        catf = CatForm(request.POST, request.FILES, instance=cat)
        if catf.is_valid():
            post = catf.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('cat', kwargs={'cat_id': cat.pk}))
        else:
            context = {'form': catf}
            return render(request, 'blog/edit_cat.html', context)
    else:
        catf = CatForm(instance=cat)
        context = {'form': catf}
        return render(request, 'blog/edit_cat.html', context)


@login_required
def delete_cat(request, cat_id):
    cat = Cat.objects.get(pk=cat_id)
    cat.delete()
    return HttpResponseRedirect(reverse('start'))


def index(request):
    filename = r'c:/Users/Саня/Desktop/image.jpg'
    return FileResponse(open(filename, 'rb'))


@login_required
def cats(request):
    my_cats = Cat.objects.filter(author=request.user)
    context = {'my_cats': my_cats}
    return render(request, 'blog/your_cats.html', context)


def show_cat(request, cat_id):
    cat = Cat.objects.get(pk=cat_id)
    context = {'cat': cat}
    return render(request, 'blog/cat.html', context)


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/registration.html', {'user_form': user_form})


class UserLogin(LoginView):
    redirect_field_name = 'start'
    template_name = 'accounts/login.html'


# Сброс пароля
class UserResetPassword(PasswordResetView):
    template_name = 'blog/pass_reset/pass_reset.html'
    subject_template_name = 'accounts/registration/password_reset_subject.txt'
    email_template_name = 'accounts/registration/email_template_text.txt'
    html_email_template_name = None
    success_url = 'login'
    from_email = 'linkoln27as@mail.ru'


class UserPasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'blog/pass_reset/pass_reset_confirm.html'
    success_url = 'login'


# Профиль
@login_required
def profile(request):
    return render(request, 'blog/profile.html')


# Практика bbcode
def bbcode(request):
    cat = Cat.objects.get(pk=1)
    catf = CatForm()
    return render(request, 'blog/bbcode.html', {'form': catf, 'cat': cat})
