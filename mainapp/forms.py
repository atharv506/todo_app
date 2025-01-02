from mainapp.models import TODO
from django.forms import ModelForm


class TODOform(ModelForm):
    class Meta:
        model = TODO   
        fields = ['title','status','priority']