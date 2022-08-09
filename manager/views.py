from django.shortcuts import render
from django.views.generic import TemplateView
class MainView(TemplateView):
    template_name = 'manager/index.html'

class AllAgents(TemplateView):
    template_name = 'manager/all_agents.html'
