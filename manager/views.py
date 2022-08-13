from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from manager.forms import PackingListForm, AgentForm
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

class AgentNew(CreateView):
    template_name = 'manager/new_agent.html'
    form_class = AgentForm
    success_url = '/all_agents/'

    def form_valid(self, form):
        return super().form_valid(form)

class AgentEdit(CreateView):
    template_name = 'manager/new_agent.html'
    form_class = AgentForm
    success_url = '/all_agents/'

    # def get_queryset(self):
    #     self.company = get_object_or_404(Agent, pk=self.kwargs["pk"])
    #     self.queryset = self.company.objects.all()
    #     return super(AgentEdit, self).get_queryset()

    def get_context_data(self, **kwargs):
        context = super(AgentEdit, self).get_context_data(**kwargs)
        context['agents'] = Agent.objects.filter(id=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        return super().form_valid(form)


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