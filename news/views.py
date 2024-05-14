from django.contrib.auth import logout
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import News


# Create your views here.

class News_View(ListView):
    model = News
    template_name = 'home.html'


class News_Detail(DetailView):
    model = News
    template_name = 'detail.html'
    context_object_name = 'post'


class News_Create(CreateView):
    model = News
    template_name = 'Createpost.html'
    fields = ['title', 'text', 'author']


class News_Edit(UpdateView):
    model = News
    template_name = "editpage.html"
    fields = ['title', 'text']


class News_Delete(DeleteView):
    model = News
    template_name = "deletepost.html"
    fields = ['title', 'text']
    success_url = '/'

def Log_out(request):
    logout(request)
    return render(request, 'registration/logout.html')
