from django.urls import path
from .views import about_view, home_view

urlpatterns = [
    path('', home_view.as_view(), name='home'),
    path('about/', about_view.as_view(), name='about'),
]