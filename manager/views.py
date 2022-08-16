from django.shortcuts import redirect, render

from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, View

from wkhtmltopdf.views import PDFTemplateResponse

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


class PackingListNew(CreateView, View):
    template_name = 'manager/new_list.html'
    form_class = PackingListForm
    success_url = '/packing_lists/'

    def get_ajax(self, request):
        if request.is_ajax():
            weight = request.POST.post('weight')
            print()
            print(weight)
            print()
            # return render(request, 'manager/new_list.html')


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

class MyPDF(DetailView):
    template_name = 'manager/print_pdf.html'
    context= {'title': 'Накладная'}
    model = PackingList

    def get(self, request, *args, **kwargs):
        self.context['list'] = self.get_object()

        response = PDFTemplateResponse(request=request,
                                     template=self.template_name,
                                     filename ="Накладная.pdf",
                                     context=self.context,
                                     show_content_in_browser=True,
                                     cmd_options={'margin-top': 10,}
                                     )
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