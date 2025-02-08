from django import forms
from django.contrib.auth.models import User
from .models import Passwords

class PasswordsForm(forms.ModelForm):
    class Meta:
        model = Passwords
        fields = ['name', 'url', 'password', 'shared_with']
        
        widgets = {
            'name': forms.TextInput(attrs={'autocomplete': 'off'}),
            'url': forms.URLInput(attrs={'autocomplete': 'off'}),
            'password': forms.Textarea(attrs={'autocomplete': 'new-password'}),  # Better for passwords
            'shared_with': forms.SelectMultiple(attrs={'autocomplete': 'off'}),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['shared_with'].queryset = User.objects.exclude(id=user.id)
    
    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user and not instance.pk:
            instance.created_by = user

        if commit:
            instance.save()  # Save the instance to generate the ID
            if user:  # Add the user to the shared_with field after saving
                instance.shared_with.add(user)
            self.save_m2m()  # Save many-to-many relationships (for shared_with)
        return instance