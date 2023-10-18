from django.urls import path,include
from .views import home,text,getdata

app_name = 'mainapp'
urlpatterns = [
    path('',home,name='home'),
    path('link/',text,name='text'),
    path('link/getdata/<str:src_lang_code>/<str:tgt_lang_code>/<str:input>',getdata,name='getdata')
]
