from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now() #포스트 하는 순간의 시간을 저장
        self.save()

    def __str__(self):
        return self.title

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
