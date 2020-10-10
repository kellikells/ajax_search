
from django.conf.urls import url, include


urlpatterns = [

    url(r'^search/', include('apps.search_app.urls')),

    
]