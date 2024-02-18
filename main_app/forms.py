from django import forms
from .models import userLink, socialPlatform

class UserLinkForm(forms.ModelForm):
    class Meta:
        model = userLink
        fields = ['belongs_to_socialplatform', 'link', 'text']
        widgets = {
            'belongs_to_socialplatform': forms.Select(choices=[(sp.id, sp.name) for sp in socialPlatform.objects.all()]),
            'link': forms.TextInput(attrs={'placeholder': 'https://example.com'}),
            'text': forms.TextInput(attrs={'placeholder': 'Your link description'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserLinkForm, self).__init__(*args, **kwargs)
        self.fields['belongs_to_socialplatform'].queryset = socialPlatform.objects.all()
