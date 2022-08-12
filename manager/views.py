from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView

from manager.forms import PackingListForm
from manager.models import Agent, PackingList

class MainView(TemplateView):
    template_name = 'manager/index.html'
    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['agents'] = Agent.objects.all
        return context

class AllAgents(TemplateView):
    template_name = 'manager/all_agents.html'

    def get_context_data(self, **kwargs):
        context = super(AllAgents, self).get_context_data(**kwargs)
        context['agents'] = Agent.objects.all
        return context



class PackingLists(TemplateView):
    template_name = 'manager/packing_lists.html'
    def get_context_data(self, **kwargs):
        context = super(PackingLists, self).get_context_data(**kwargs)
        context['packing_lists'] = PackingList.objects.all
        return context


class PackingListNew(CreateView):
    template_name = 'manager/new_list.html'
    form_class = PackingListForm
    success_url = '/packing_lists/'

    def form_valid(self, form):
        return super().form_valid(form)

class PackingListDelete(DeleteView):
    model = PackingList
    template_name = "manager/delite_list.html"
    success_url = '/packing_lists/'

    def delete(self, request, *args, **kwargs):
       self.object = self.get_object()
       self.object.delete()
       return redirect('packing_lists')


class About(TemplateView):
    template_name = 'manager/about.html'