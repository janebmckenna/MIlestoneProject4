from django.apps import AppConfig
from django import forms

from .models import Order


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        import checkout.signals


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'house_number', 'street', 'town_or_city',
                  'county', 'country', 'postcode',)

    def __init__(self, *args, **kwargs):
        """
        Set the placeholders and labels for the form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': "Email Address",
            'phone_number': "Phone Number",
            'house_number': "House Number or Name",
            'street': 'Street',
            'town_or_city': 'Town or City',
            'county': "County",
            'postcode': "Postcode",
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = '''
            stripe-style-input text-uppercase'''
            self.fields[field].label = False
