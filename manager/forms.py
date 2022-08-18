from django import forms
from django.forms import ModelForm, TextInput
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import UserCreationForm, UsernameField, PasswordChangeForm

from manager.models import PackingList, Agent, User

class CreateUserForm(UserCreationForm):

    username = forms.RegexField(label=_('Логин'),
                                max_length=150,
                                regex=r"^[\w.@+-]+$",
                                help_text=_('Не более 150 символов. Только буквы, цифры и @/./+/-/_.'),
                                error_messages={
                                    'invalid': _("Это поле может содержать только буквы, цифры и "
                                                 "@/./+/-/_ символы.")},
                                widget=TextInput(attrs={'class': 'form-control',
                                                        'required': 'true',
                                                        })
                                )

    first_name = forms.CharField(label=_("Имя"),
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'type': 'text',
                                                              'required': False,
                                                              }),
                                 )

    password1 = forms.CharField(label=_("Пароль"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'required': 'true',
                                                                  }),
                                error_messages={
                                                'invalid': _("Не соблюдены требования к паролю.")
                                                },
                                help_text=_('Ваш пароль должен содержать не менее 8 символов.'
                                            'Ваш пароль не может быть широко используемым паролем. '
                                            'Ваш пароль не может быть полностью числовым.'),
                                )
    password2 = forms.CharField(label=_("Подтверждение пароля"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'type': 'password',
                                                                  'required': 'true',
                                                                  }),
                                error_messages={
                                                'error': _("Пароли не совпадают.")
                                                },
                                help_text=_("Повторите пароль для подтвверждения.")
                                )
    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  ]

class LoginUserForm(AuthenticationForm):

    username = UsernameField(label=_('Логин'),
                                widget=TextInput(attrs={'class': 'form-control',
                                                        'required': 'true',
                                                        'autofocus': True
                                                        })
                                )
    password = forms.CharField(label=_('Пароль'),
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                        'required': 'true',
                                                        'autofocus': True
                                                        }),
                                error_messages = {
                                                'invalid': _("Неверный логин или пароль.")
                                                },
                                )
    class Meta:
        model = User
        fields = [
                  'username',
                   'password'
                    ]
        error_messages = {
                            'invalid': _("Неверный логин или пароль.")
                        },

class PackingListForm(ModelForm):
    class Meta:
        model = PackingList
        fields = '__all__'
        labels = {'sender': _('Отправитель'),
                  'destination': _('Получатель'),
                  'content': _('Описание груза'),
                  'weight': _('Вес, кг'),
                  'volume': _('Объем, м.куб'),
                  'places_count': _('Количество мест, шт.'),
                  'price': _('Стоимость, руб.')
                  }
class AgentForm(ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'
        labels = {'company': _('Название'),
                  'phone': _('Номер телефона'),
                  'inn_number': _('ИНН'),
                  }

