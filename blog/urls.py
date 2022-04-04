from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('', views.start, name='start'),
    path('create/', views.create_cat, name='create_cat'),
    path('index/', views.index),
    path('bbcode/', views.bbcode),
    path('my_cats/', views.cats, name='my_cats'),
    path('cat/<int:cat_id>', views.show_cat, name='cat'),
    path('edit/<int:cat_id>', views.edit_cat, name='edit_cat'),
    path('delete/<int:cat_id>', views.delete_cat, name='delete_cat'),
    path('profile/', views.profile, name='profile'),
    path('accounts/login/', views.UserLogin.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/register/', views.register, name='register'),
    # Сброс пароля ниже 4 ссылки, пока хз как отправлять письма электронные, поэтому оставлю на потом
    path('accounts/reset/', views.UserResetPassword.as_view(), name='pass_reset'),
    path('accounts/reset_done/', PasswordResetDoneView.as_view(
        template_name='blog/pass_reset/pass_reset_done.html'), name='pass_reset_done'),
    path('accounts/reset_confirm/', views.UserPasswordResetConfirm.as_view(), name='pass_reset_confirm'),
    path('accounts/reset_complete/', PasswordResetCompleteView.as_view(
        template_name='blog/pass_reset/pass_reset_complete.html'), name='pass_reset_complete'),
    # Смена пароля
    path('accounts/change_pass/', PasswordChangeView.as_view(
        template_name='accounts/change_pass/password_change_form.html'), name='password_change_form'),
    path('accounts/change_done/', PasswordChangeDoneView.as_view(
        template_name='accounts/change_pass/password_change_done.html'), name='password_change_done'),
]