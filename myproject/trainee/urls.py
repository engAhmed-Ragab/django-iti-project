from .views import *
from django.urls import path
urlpatterns = [
    path('alltrainees/',alltrainees,name='alltrainees'),
    path('trainee/<int:id>',gettraineebyid,name='gettraineebyid'),
    path('inserttrainee/',inserttrainee, name='inserttrainee'),
    path('deletetrainee/<int:id>',deletetrainee,name='deletetrainee'),
    path('updatetrainee/<int:id>', updatetrainee, name='updatetrainee'),
]