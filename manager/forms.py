from django.forms import forms, ModelForm

from manager.models import PackingList

class PackingListForm(ModelForm):
    class Meta:
        model = PackingList
        fields = '__all__'