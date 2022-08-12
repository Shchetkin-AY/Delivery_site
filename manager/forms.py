from django.utils.translation import gettext_lazy as _

from django.forms import forms, ModelForm,TextInput, ModelChoiceField

from manager.models import PackingList

class PackingListForm(ModelForm):
    class Meta:
        model = PackingList
        fields = '__all__'
        labels = {'sender': _('Отправитель'),
                  'destination': _('Получатель'),
                  'content': _('Описание груза'),
                  'weight': _('Вес'),
                  'volume': _('Объем'),
                  'places_count': _('Количество мест')
                  }
