from django import forms
from django.forms import DateInput

from .models import Fixture


class MyDateInput(forms.widgets.DateInput):
    input_type = 'date'


class FixtureForm(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=True)
    
    class Meta:
        model = Fixture
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'date':
                field.widget.attrs['input_type'] = 'date'
            else:
                field.widget.attrs['class'] = 'fixture-form'

