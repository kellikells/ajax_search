from __future__ import unicode_literals
from django.db import models
from django import forms
# for regular expressions 
import re 
# for validating an Email 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    gender = models.CharField(max_length = 255)
    image_path = 
    sport = 

    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)



    def __str__(self):
        return('first_name= ' + self.first_name)