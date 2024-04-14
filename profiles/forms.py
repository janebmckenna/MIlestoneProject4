from django import forms

from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """ 
        Set the placeholders and labels for the form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_full_name' : "Full Name",
            'default_email' : "Email Address", 
            'default_phone_number' : "Phone Number", 
            'default_house_number' : "House Number or Name", 
            'default_street' : 'Street' , 
            'default_town_or_city' : 'Town or City', 
            'default_county' : "County", 
            'default_postcode' : "Postcode",
        }

        self.fields['default_full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-form'
            self.fields[field].label = False 