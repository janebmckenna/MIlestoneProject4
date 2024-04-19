from django import forms

from .models import Fixture
from clubadmin.models import Team


class FixtureForm(forms.ModelForm):

    model = Fixture
    fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        teams = Team.objects.all()
        team_names = [(team.id, team.get_friendly_name()) for team in teams]
    
    self.fields['team'].choices = team_names
    for field_name, field in self.fields.items():
        field.widget.attrs['class'] = 'fixture-form'
