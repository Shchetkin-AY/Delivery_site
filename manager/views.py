from django.shortcuts import redirect, get_object_or_404

from django.http import HttpResponse

from django.template.loader import get_template

from xhtml2pdf import pisa

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

class AgentEdit(UpdateView):
    template_name = 'manager/new_agent.html'
    form_class = AgentForm
    success_url = '/all_agents/'

    def get_object(self, **kwargs):
        company = Agent.objects.get(id=self.kwargs['pk'])
        return company

    def form_valid(self, form):
        return super().form_valid(form)


class PackingLists(TemplateView):
    template_name = 'manager/packing_lists.html'

    def get_context_data(self, **kwargs):
        context = super(PackingLists, self).get_context_data(**kwargs)
        context['packing_lists'] = PackingList.objects.all().order_by('id')
        return context


class PackingListNew(CreateView):
    template_name = 'manager/new_list.html'
    form_class = PackingListForm
    success_url = '/packing_lists/'

    def form_valid(self, form):
        return super().form_valid(form)

class PackingListEdit(UpdateView):
    template_name = 'manager/new_list.html'
    form_class = PackingListForm
    success_url = '/packing_lists/'

    def get_object(self, **kwargs):
        list = PackingList.objects.get(id=self.kwargs['pk'])
        return list

    def form_valid(self, form):
        return super().form_valid(form)

def render_pdf_view(request, *args, **kwargs):
   pk = kwargs.get('pk')
   list = get_object_or_404(PackingList, pk=pk)

   template_path = 'manager/print_pdf.html'
   context = {'list': list}
   response = HttpResponse(content_type='application/pdf')

   response['Content-Disposition'] = 'filename="report.pdf"'

   template = get_template(template_path)
   html = template.render(context)

   pisa_status = pisa.CreatePDF(
      html, dest=response)
   if pisa_status.err:
      return HttpResponse('We had some errors <pre>' + html + '</pre>')
   return response

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