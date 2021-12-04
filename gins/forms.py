from django import forms
from .widgets import CustomClearableFileInput
from .models import Gin, Distillery


class GinForm(forms.ModelForm):

    class Meta:
        model = Gin
        fields = '__all__'
        exclude = ['rating']

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'