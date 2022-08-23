from django.http import HttpResponseNotFound, HttpResponseServerError

from django.shortcuts import redirect

from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView, View

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django_pdfkit import PDFView

from wkhtmltopdf.views import PDFTemplateResponse

from manager.forms import PackingListForm, AgentForm, CreateUserForm, LoginUserForm
from manager.models import Agent, PackingList


# Страница регистрации нового пользователя. При создании идет проверка соответствия требованиям
class RegisterUserView(CreateView):
    template_name = 'manager/registration.html'
    form_class = CreateUserForm
    success_url = 'authentication'
    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect('authentication')
        return super(RegisterUserView, self).form_valid(form)


# страница аутентификации пользователя
class LoginUserView(LoginView):
    template_name = 'manager/authentication.html'
    authentication_form = LoginUserForm
    next_page = 'main'

# главная старница
class MainView(TemplateView):
    template_name = 'manager/index.html'

# список контрагентов
class AllAgents(LoginRequiredMixin, TemplateView):
    template_name = 'manager/all_agents.html'

    def get_context_data(self, **kwargs):
        context = super(AllAgents, self).get_context_data(**kwargs)
        context['agents'] = Agent.objects.all
        return context

# создать контрагента
class AgentNew(LoginRequiredMixin ,CreateView):
    template_name = 'manager/new_agent.html'
    form_class = AgentForm
    success_url = '/all_agents/'

    def form_valid(self, form):
        return super().form_valid(form)

# редактировнае контрагента
class AgentEdit(LoginRequiredMixin, UpdateView):
    template_name = 'manager/new_agent.html'
    form_class = AgentForm
    success_url = '/all_agents/'

    def get_object(self, **kwargs):
        agent = Agent.objects.get(id=self.kwargs['pk'])
        return agent

    def form_valid(self, form):
        return super().form_valid(form)

# список накладных
class PackingLists(LoginRequiredMixin, TemplateView):
    template_name = 'manager/all_lists.html'

    def get_context_data(self, **kwargs):
        context = super(PackingLists, self).get_context_data(**kwargs)
        context['packing_lists'] = PackingList.objects.all().order_by('id')
        return context

# создание накладной
class PackingListNew(LoginRequiredMixin, CreateView, View):
    template_name = 'manager/new_list.html'
    form_class = PackingListForm
    success_url = '/packing_lists/'

    def form_valid(self, form):
        return super().form_valid(form)

# редактировнае накладной
class PackingListEdit(LoginRequiredMixin, UpdateView):
    template_name = 'manager/new_list.html'
    form_class = PackingListForm
    success_url = '/packing_lists/'

    def get_object(self, **kwargs):
        list = PackingList.objects.get(id=self.kwargs['pk'])
        return list

    def form_valid(self, form):
        return super().form_valid(form)

# печать PDF
class MyPDF(PDFView, DetailView):
    template_name = 'manager/print_pdf.html'
    context = {'title': 'List'}
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

# удалить накладную
class PackingListDelete(DeleteView):
    model = PackingList
    template_name = "manager/delite_list.html"
    success_url = '/packing_lists/'

    def delete(self, request, *args, **kwargs):
       self.object = self.get_object()
       self.object.delete()
       return redirect('packing_lists')

# страница о нас
class About(TemplateView):
    template_name = 'manager/about.html'

# хэндлеры ошибок
def custom_handler404(request, exception=None):
    return HttpResponseNotFound('Ресурс не найден!', status=404)
def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')