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


class UserForm(forms.Form):
    full_name = forms.CharField(max_length = 100)
    email = forms.EmailField(max_length = 100)
    password = forms.CharField(max_length = 32, min_length = 8)