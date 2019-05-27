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

    def createHash(self):
        self.password = bcrypt.hashpw(self.password.encode(), bcrypt.gensalt()).decode('utf-8')
        return

    def verifyHash(self, inputPassword):
        pass
        return

class UserForm(forms.Form):
    full_name = forms.CharField(max_length = 100)
    email = forms.EmailField(max_length = 100)
    password = forms.CharField(max_length = 32, min_length = 8)