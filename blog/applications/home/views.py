import datetime
#
from .models import Home,Suscribers
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView
)
from applications.entrada.models import Entry
from .forms import Suscribersform
class HomePageView(TemplateView):
    template_name = "home/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['home']= Home.objects.latest('created')
        context['portada']= Entry.objects.entrada_en_portada()
        context['entradas_home']= Entry.objects.entradas_en_home()
        context['entradas_recientes']= Entry.objects.entradas_recientes()
        context['form']= Suscribersform
        return context  


class SuscriberCreateView(CreateView):
    form_class=Suscribersform
    success_url='.'



