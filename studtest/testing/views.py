from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.decorators import login_required


@login_required()
class MainTestPage(TemplateView):
    template_name = 'test/maintest.html'


@login_required()
class TestPage(DetailView):
    template_name = 'test/test.html'
