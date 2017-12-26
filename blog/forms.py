from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta: #어떤 모델이 쓰이는지 명시하기 위해 필요함
        model = Post #이런식으로 말이지
        fields = ('title','text')
