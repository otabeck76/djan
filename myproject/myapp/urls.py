# myapp/urls.py

from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('',views.index, name='index'), 
     path('',views.index, name='about'), 
      path('',views.index, name='blog'), 
       path('',views.index, name='class'), 

    
    
]




