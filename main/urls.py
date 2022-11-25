from django.urls import path
from.import views

urlpatterns = [
path('',views.index, name='home'),
path('about-us',views.page2, name='welcome'),
path('signing',views.avtorization, name='signing'),
path('registr',views.registr, name='registr'),
]

