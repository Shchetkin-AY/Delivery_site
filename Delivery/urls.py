"""Delivery URL Configuration

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib.auth.views import LogoutView

from manager.views import About, AgentNew, AgentEdit, AllAgents, MainView, PackingListNew, PackingLists, PackingListDelete, PackingListEdit, MyPDF, LoginUserView, RegisterUserView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name="main"),
    path('about/', About.as_view(), name="about"),
    path('all_agents/', AllAgents.as_view(), name="all_agents"),
    path('all_agents/new', AgentNew.as_view(), name="agent_new"),
    path('all_agents/<int:pk>/edit', AgentEdit.as_view(), name="agent_edit"),

    path('packing_lists/', PackingLists.as_view(), name="packing_lists"),
    path('packing_lists/new', PackingListNew.as_view(), name="pack_list"),
    path('packing_lists/<int:pk>/edit', PackingListEdit.as_view(), name="list_edit"),
    path('packing_lists/<int:pk>/print', MyPDF.as_view(), name="list_print"),
    path('packing_lists/<int:pk>/delete/', PackingListDelete.as_view(), name="delete_list"),

    path('registration/', RegisterUserView.as_view(), name='registration'),
    path('authentication/', LoginUserView.as_view(), name='authentication'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

