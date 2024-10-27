from django.urls import path
from app import views
urlpatterns=[
    path("hi",views.hi,name="hi"),
    path("even",views.even,name="even"),
    path('armstrong',views.armstrong,name='armstrongNumber'),
    path('prime',views.prime,name='primeNumbers'),
    path('perfect',views.perfect,name='perfectNumbers'),
    
]