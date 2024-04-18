from django import forms

from .models import Team, NewsCategory, News
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