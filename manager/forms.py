from django.utils.translation import gettext_lazy as _

from django.forms import  ModelForm

from manager.models import PackingList, Agent

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
        fields = []
        labels = {'company': _('Название'),
                  'phone': _('Номер телефона'),
                  'inn_number': _('ИНН'),
                  }

