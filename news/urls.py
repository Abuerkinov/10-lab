from django.urls import path
from .views import News_View, News_Detail, News_Create, News_Edit, News_Delete, Log_out

urlpatterns = [
    path('post/<int:pk>/delete/', News_Delete.as_view(), name='deletepost'),
    path('post/<int:pk>/edit/', News_Edit.as_view(), name='editpost'),
    path('post/new', News_Create.as_view(), name='newspost'),
    path('post/<int:pk>', News_Detail.as_view(), name='detail'),
    path('', News_View.as_view(), name='news'),
    path('logout/', Log_out, name='logout')
]

