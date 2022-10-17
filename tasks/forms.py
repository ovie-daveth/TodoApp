from .models import tasks
from django.forms import ModelForm

class taskform(ModelForm):
    
    class Meta:
        model = tasks
        fields = '__all__'