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
# ---------------------------------------------
# get the first page using pagination
# def on_load(request):

#     leads_list = Lead.objects.all()

#     return render(request, 'pagination_app/table.html', {'leads': leads })
