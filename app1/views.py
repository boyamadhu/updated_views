from django.shortcuts import render
from app1.models import *
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView

class Home(TemplateView):
    template_name='app1/home.html'

class SchoolList(ListView):
    model = School
    context_object_name='schools'

class detail(DetailView):
    model=School
    # template_name='school_detail.html'
    context_object_name='DO'

class Create_View(CreateView):
    model=School
    fields='__all__'

class update_view(UpdateView):
    model=School
    fields='__all__'

class delete_view(DeleteView):
    model=School
    context_object_name='DO'
    success_url=reverse_lazy('SchoolList')