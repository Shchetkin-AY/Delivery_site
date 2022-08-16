from django.utils.translation import gettext_lazy as _

from django.forms import forms, ModelForm

from manager.models import PackingList, Agent

class PackingListForm(ModelForm):
    class Meta:
        model = PackingList
        fields = '__all__'
        labels = {'sender': _('Отправитель'),
                  'destination': _('Получатель'),
                  'content': _('Описание груза'),
                  'weight': _('Вес'),
                  'volume': _('Объем'),
                  'places_count': _('Количество мест'),
                  'price': _('Стоимость')
                  }

class AgentForm(ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'
        labels = {'company': _('Название'),
                  'phone': _('Номер телефона'),
                  'inn_number': _('ИНН'),
                  }

        # error_messages = {'company': { 'value is less': ('Неверный формат названия компании')},
                         # 'phone': ('Неверный формат номера телефона'),
                         # 'inn_number': {'max_length': ('ИНН должен состоять из 10 цифр')}
                         #               }
