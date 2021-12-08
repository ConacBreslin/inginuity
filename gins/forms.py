"""The form for adding Gins to the site."""

from django import forms
from .widgets import CustomClearableFileInput
from .models import Gin


class GinForm(forms.ModelForm):
    """Form to add a gin"""
    class Meta:
        """Layout of ginform"""
        model = Gin
        fields = '__all__'
        exclude = ['rating']

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
