from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
#def home_view(request):
    #return render(request, 'home.html')

#def about_view(request):
 #   return render(request, 'about.html')

class home_view(TemplateView):
    template_name = 'home.html'

class about_view(TemplateView):
    template_name = 'about.html'