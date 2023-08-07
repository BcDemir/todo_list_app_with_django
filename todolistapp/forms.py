from django.forms import ModelForm
from .models import ToDos


class ToDosForm(ModelForm):
    class Meta:
        model = ToDos
        fields = '__all__'
