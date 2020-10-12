from django import http
from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import *
import bcrypt
from django.contrib import messages # flash messages
from .models import *

from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from datetime import datetime
from datetimerange import DateTimeRange
import datetime as otherdatetime
import pytz
# ==========================================

def index(request):

    return render(request, 'search_app/index.html')

# ---------------------------------------------

def create(request):

    if request.method == 'POST':

        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            context = {
                'errors': errors
            }
            return render(request, 'search_app/index.html', context)
        
        else:
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], gender=request.POST['gender'], image_path=request.POST['image_path'], sport=request.POST['sport'])

            return redirect('/')

# ---------------------------------------------

def show(request):
    if request.method == 'POST':

        # if the input is empty, show all users
        if len(request.POST['perPage']) == 0:
            users = User.objects.all().order_by('-id')
            return render(request, 'search_app/table.html', {'users': users})
    
        else:
            # save input to <limit> and change to interval
            limit = int(request.POST['perPage'])
            users = User.objects.all().order_by('-id')[:limit]
        
            return render(request, 'search_app/table.html', {'users': users})

# =============================================
#                search page 
# =============================================

def search(request):

    return render(request, 'search_app/search_page.html')





# ********* figure out how to remove when unchecked

# ---------------------------------------------
# creating 'searches' dictionary to store input data 
searches = {'gender':[], 'sport':[]}

def search_results(request):

    # if data includes an input with name='gender'
    if request.POST.get('gender') != None:

        # if input is not already part of the key: gender, add value to dict: searches
        if request.POST['gender'] not in searches['gender']:
        
            new = {'g': request.POST['gender']}

            # add postData gender to the key 'gender'
            searches['gender'].append(new['g'])

    # if data includes an input with name='sport'
    if request.POST.get('sport') != None:

        if request.POST['sport'] not in searches['sport']:
            new = {'s': request.POST['sport']}

            # add postData sport to the key 'sport'
            searches['sport'].append(new['s'])


        



    # ........ loop through stored values to filter .......
    # if there are values in the dictionary for gender/sport 

    all_users = {'user': []}
    # as long as not both genders are selected: filter gender selected
    if len(searches['gender']) == 1:


        # all_users['user'].append(User.objects.filter(gender = searches['gender']))


        
        all_users = User.objects.filter(gender = searches['gender'])







    # as long as a sport is checked, but not all: filter 
    if 0 < len(searches['sport']) < 5 :
        for each in searches['sport']:

            # all_users['user'].append(User.objects.filter(sport = each))
        
      
            all_users = User.objects.filter(sport = each)









        # ------------------------------------
    
        # # input for name 
        # if request.POST['name']:
        #     users = User.objects.filter(first_name__startswith = request.POST['name'])


        # users = User.objects.filter(gender='male')
    return render(request, 'search_app/search_results.html', {'users': all_users} )


#



# ---------------------------------------------



# ---------------------------------------------





