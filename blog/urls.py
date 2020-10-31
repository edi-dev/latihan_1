from django.urls import path
from . import views

urlpatterns = [
    path('class/<slug:cat>/<slug:detailview>', views.SingleView.as_view(), name='singleview'),
    path('class/<slug:catList>', views.CategoryView.as_view(), name='cat-list'),
    path('<slug:category>/<slug:detail>', views.SingleFunc, name='single'),
    path('<slug:catInput>/', views.CategoryIndexF, name='cat-index'),
    path('', views.IndexFunc, name='index'),
    path('classview', views.IndexView.as_view(), name='indexView'),
]