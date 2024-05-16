from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('noticiaCS1/', noticiaCS1, name="noticiaCS1"),
    path('noticiaCS2/', noticiaCS2, name="noticiaCS2"),
    path('noticiaCS3/', noticiaCS3, name="noticiaCS3"),
    path('noticiaCS4/', noticiaCS4, name="noticiaCS4"),
    path('cs2/', cs2, name="cs2"),
    path('lol/', lol, name="lol"),
    path('noticiaLol1/', noticiaLol1, name="noticiaLol1"),
    path('noticiaLol2/', noticiaLol2, name="noticiaLol2"),
    path('noticiaLol3/', noticiaLol3, name="noticiaLol3"),
    path('noticiaLol4/', noticiaLol4, name="noticiaLol4"),
    path('login/', login, name="login"),
    path('loginRegistro/', loginRegistro , name="loginRegistro")
]