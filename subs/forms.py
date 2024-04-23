from django import forms
from django.utils import timezone

from .models import TeamSubs
from clubadmin.models import Team, Player


class SubsForm(forms.ModelForm):

    class Meta:
        model = TeamSubs
        exclude = ('product', 'order', 'is_paid', 'price',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        players = Player.objects.all()
        display_names = [(p.id, p.get_display_name()) for p in players]
        teams = Team.objects.all()

        self.fields['player'].choices = display_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'subs-form'
    
    def clean(self):
        cleaned_data = super().clean()
        period = cleaned_data.get('period')
        team = cleaned_data.get('team')

        if period < 1:
            self.add_error('period', "Period must be at least 1.")

        if not team:
            self.add_error('team', "Please select a team.")

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Ensure that the date field is updated to the current date and time
        instance.date = timezone.now()
        if commit:
            instance.save()
        return instance
