from django.urls import path
from . import views
urlpatterns=[
    path('',views.display,name='display'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('counter',views.counter,name='counter'),
    path('result',views.result,name='result'),
    path('logout',views.logout,name="logout")
]
