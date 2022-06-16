from django.urls import path

from . import views

app_name = 'Contact'
urlpatterns = [
    path('', views.KontakView, name='kontakForm'),
    path('list', views.KontakList.as_view(), name='kontakList'),
    path('add', views.ContactCreate.as_view(), name='add-contact'),
]