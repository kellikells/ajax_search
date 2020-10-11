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

# ---------------------------------------------

def search(request):
    return render(request, 'search_app/search_page.html')


# ---------------------------------------------




# ---------------------------------------------



# ---------------------------------------------





# ---------------------------------------------
# get the first page using pagination
# def on_load(request):

#     leads_list = Lead.objects.all()

#     return render(request, 'pagination_app/table.html', {'leads': leads })
