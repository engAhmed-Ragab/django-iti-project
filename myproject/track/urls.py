from django.urls import path
from .views import *
urlpatterns = [
    path('alltracks/',alltracks,name='alltracks'),
    path('track/<int:id>',gettrackbyid,name='gettrackbyid'),
    path('inserttrack/',inserttrack, name='inserttrack'),
    path('deletetrack/<int:id>',deletetrack,name='deletetrack'),
    path('updatetrack/<int:id>',updatetrack, name='updatetrack')
]