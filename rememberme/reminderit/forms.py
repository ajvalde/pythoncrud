from django import forms
from .models import Remember

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Remember
        fields = ('name','content')
