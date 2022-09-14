

from django.urls import path, include
from django.contrib.auth.views import LogoutView


from .views import About, AllAgents, AgentNew, AgentEdit, PackingLists, PackingListNew, PackingListEdit, \
        MyPDF, PackingListDelete, MainView

urlpatterns = [
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
    ]
