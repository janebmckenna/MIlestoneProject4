from django import forms
from django.utils import timezone

from .models import Team, NewsCategory, News, Player
from subs.models import TeamSubs
from kit.models import Category


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        news_categories = NewsCategory.objects.all()
        friendly_names = [(c.id, c.get_news_friendly_name()) for c in news_categories]
        teams = Team.objects.all()
        

        self.fields['news_category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'news-form'
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        # Ensure that the date field is updated to the current date and time
        instance.date = timezone.now()  # Import timezone if not already imported
        if commit:
            instance.save()
        return instance

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        teams = Team.objects.all()
        friendly_names = [(t.id, t.get_friendly_name()) for t in teams]

        self.fields['team'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'player-form'
