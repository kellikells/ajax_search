from __future__ import unicode_literals
from django.db import models
from django import forms
# for regular expressions 
import re 
# for validating an Email 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

# ------------------------------------------
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors['enter a first name'] = "Enter a first name"
        if len(postData['last_name']) < 1:
            errors['enter a last name'] = "Enter a last name"
        if len(postData['sport']) < 1:
            errors['please choose a sport'] = "Please choose a sport"
        if not (postData['first_name']).isalpha() or not (postData['last_name']).isalpha():
            errors['Name only include letters'] = "Name only include letters"
        return errors


# ------------------------------------------
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    gender = models.CharField(max_length = 255)
    image_path = models.TextField()
    sport = models.CharField(max_length = 30)

    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)

    objects = UserManager()

    def __str__(self):
        return('first_name= ' + self.first_name + ', last_name= ' + self.last_name + ', gender= ' + self.gender + ', image_path= ' + self.image_path + ', sport= ' + self.sport)
    

# ------------------------------------------
# class SPORT(models.Model):




# ------------------------------------------




# ------------------------------------------
# class User(models.Model):
#     BASKETBALL = 1
#     VOLLEYBALL = 2
#     BASEBALL = 3
#     SOCCER = 4
#     FOOTBALL = 5
#     SPORT_CHOICES = (
#         (BASKETBALL, 'Basketball'),
#         (VOLLEYBALL, 'Volleyball'),
#         (BASEBALL, 'Baseball'),
#         (SOCCER, 'Soccer'),
#         (FOOTBALL, 'Football'),
#     )

#     first_name = models.CharField(max_length = 255)
#     last_name = models.CharField(max_length = 255)
#     gender = models.CharField(max_length = 255)
#     image_path = models.TextField()
#     sport = models.IntegerField(
#         choices = SPORT_CHOICES,
#     )

#     created_at = models.DateField(auto_now_add = True)
#     updated_at = models.DateField(auto_now = True)

#     def __str__(self):
#         return('first_name= ' + self.first_name + ', last_name= ' + self.last_name + ', gender= ' + self.gender + ', image_path= ' + self.image_path)
# ------------------------------------------