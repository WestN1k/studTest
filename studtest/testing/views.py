from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.decorators import login_required
from .models import *


class MainTestPage(TemplateView):
    template_name = 'test/maintest.html'

    def get_context_data(self, **kwargs):
        context = super(MainTestPage, self).get_context_data(**kwargs)
        context['tests'] = TestPage.objects.filter('')

class TestPage(DetailView):
    template_name = 'test/test.html'
