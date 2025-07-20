from django import forms
from BranePhr.models import *

class CarouselForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CarouselForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


    class Meta:
        model = Carousel
        fields = '__all__'

class PhotoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Images
        exclude = ('image',)