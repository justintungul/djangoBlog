from django.db import models
from django import forms

import bcrypt

# Create your models here.
class User(models.Model):
    # DEFAULT_ROLE = 1
    full_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    following = models.ManyToManyField("self", blank=True, related_name="followers", symmetrical = False)

    # admin
    def __str__(self):
        return self.full_name.title()

    def upper_case_name(self):
        return self.full_name.title()
    upper_case_name.short_description = 'Name'
    
    # user methods
    def create_password_hash(self):
        self.password = bcrypt.hashpw(self.password.encode(), bcrypt.gensalt()).decode('utf-8')
        return

    def verify_password_hash(self, inputPassword):
        return bcrypt.checkpw(inputPassword.encode(), self.password.encode())
        
    def create_user_hash(self):
        string_to_hash = str(self.created_at) + 'justDontBruh'
        return bcrypt.hashpw(string_to_hash.encode(), bcrypt.gensalt()).decode('utf-8')

    def verify_user_hash(self, target_hash):
        secret_salt = str(self.created_at) + 'justDontBruh'
        return bcrypt.checkpw(secret_salt.encode(), target_hash.encode())

class Post(models.Model):
    title = models.CharField(max_length = 255)
    headline = models.CharField(max_length = 255)
    hero_image = models.ImageField(upload_to = 'media/pictures')
    body = models.TextField()
    author = models.ForeignKey(User, related_name='posts', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # admin
    def __str__(self):
        return self.title.title()

# Forms
class UserForm(forms.Form):
    full_name = forms.CharField(max_length = 100)
    email = forms.EmailField(max_length = 100)
    password = forms.CharField(max_length = 32, min_length = 8)

class PostForm(forms.Form):
    title = forms.CharField(max_length = 255)
    headline = forms.CharField(max_length = 255)
    body = forms.CharField()
    hero_image = forms.ImageField()