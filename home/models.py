from django.db import models

# Create your models here.
class News_Category(models.Model):

    class Meta:
        verbose_name_plural = 'News Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class News(models.Model):

    class Meta:
        verbose_name_plural = 'News'
    
    news_category = models.ForeignKey('News_Category', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=254, null=True, blank=True)
    team = models.BooleanField(default=False, null=True, blank=True)
    story = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name