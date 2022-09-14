from django.shortcuts import render

from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from django.shortcuts import redirect

from manager.forms import CreateUserForm, LoginUserForm

# Страница регистрации нового пользователя. При создании идет проверка соответствия требованиям
class RegisterUserView(CreateView):
    template_name = 'manager/registration.html'
    form_class = CreateUserForm
    success_url = 'authentication'
    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect('login')
        return super(RegisterUserView, self).form_valid(form)


# страница аутентификации пользователя
class LoginUserView(LoginView):
    template_name = 'manager/login.html'
    authentication_form = LoginUserForm
    next_page = 'main'