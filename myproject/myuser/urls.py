from django.urls import path
from myuser.views import *
urlpatterns = [
    path('Login/',Login),
    path('Logout/',Logout),
    path('Register/',Register),
]