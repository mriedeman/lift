from django.forms import ModelForm, Textarea
from .models import Pipes  


class PostForm(ModelForm):
    class Meta:
        model = Pipes
        fields = ('material', 'inner_diameter', 'pipe_length', 'line_type')
       # widgets = {
        #    'body': Textarea()

       # }