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
    users = User.objects.all()
    

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

# ------------------------------------
#         if request.POST['gender']: 

#             # creating variable for KEY string 'gender'
#             gender_var = 'gender'

#             # if it already exists, create new string 
#             if gender_var in searches:

#                 gender_var +='1'    #create new string
#                 # add value from POST to key
#                 searches[gender_var] = request.POST['gender']



#             else:
#                  # add value from POST to key
#                 searches[gender_var] = request.POST['gender']


#         # if request.POST['sport']:
#         #     searches['sport'] = request.POST['sport']
        
#         # else:
#         #     print('none')


#         print('-'*30)
#         print(searches)
#         --------------------------------------




        # if request.POST['gender'] or request.POST['sport']:

       
    #     print('-'*30)
    #     print(len(request.POST['gender']))
        
    # # if request.POST['gender2']:
    # #     print('-'*30)
    # #     print('g2')
     
    # if request.POST['sport']:
    #     print('-'*30)
    #     print('g3')
    

    
        # # input for name 
        # if request.POST['name']:
        #     users = User.objects.filter(first_name__startswith = request.POST['name'])


   
        



        # if request.POST['gender1']:
        #     users = User.objects.filter(gender = request.POST['gender1'])
        # if request.POST['gender2']:
            # users = User.objects.filter(gender = request.POST['gender2'])


          
    #   >>> a = User.objects.filter(gender__contains='female')
        
   
        # users = User.objects.filter(gender='male')
    return render(request, 'search_app/search_results.html', {'users': users} )


#



# ---------------------------------------------



# ---------------------------------------------





# ---------------------------------------------
# get the first page using pagination
# def on_load(request):

#     leads_list = Lead.objects.all()

#     return render(request, 'pagination_app/table.html', {'leads': leads })
