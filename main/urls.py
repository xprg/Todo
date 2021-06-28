from django.urls import path
from . import views

urlpatterns=[
path('',views.empty,name='empty'),

path('view/',views.index,name='viewlist'),

 path('home/',views.home,name='home'),

 path('<int:id>',views.show,name='show'),

 path('create/',views.create,name='create')

]