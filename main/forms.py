from .models import *
from django import forms


class CourseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Course
        fields = ['title', 'description', 'duration', 'price', 'category', 'language', 'tags', 'image']



class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsView
        fields = ['title', 'content', 'image', 'author']