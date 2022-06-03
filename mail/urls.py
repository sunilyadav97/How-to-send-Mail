from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('send-mail',SendMail, name='sendmail')
]
