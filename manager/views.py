from django.shortcuts import render
from django.views.generic import TemplateView

# from manager.models import Agent

class MainView(TemplateView):
    template_name = 'manager/index.html'

class AllAgents(TemplateView):
    template_name = 'manager/all_agents.html'

    # def get_context_data(self, **kwargs):
    #     contest = super(AllAgents, self).get_context_data(**kwargs)
    #     contest['agents'] = Agent.objects.all
    #     return contest



class PackingLists(TemplateView):
    template_name = 'manager/packing_lists.html'

class About(TemplateView):
    template_name = 'manager/about.html'