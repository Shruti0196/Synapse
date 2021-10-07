from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('post/<str:pk>',views.posts,name='post'),
    path('addblog',views.addblog,name='addblog'),
    path('addblogdisplay',views.addblogdisplay,name='addblogdisplay'),
    path('deleteblog',views.deleteblog,name='deleteblog'),
    path('displaydeleteblog',views.displaydeleteblog,name='displaydeleteblog')
]