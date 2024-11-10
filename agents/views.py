from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .mixins import OrganizorAndLoginRequiredMixin
from .forms import AgentModelForm
from leads.models import Agent, UserProfile
# Create your views here.


class AgentListView(OrganizorAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/agent_list.html'
    
    def get_queryset(self) -> QuerySet[Any]:
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    

class AgentCreateView(OrganizorAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        user_profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        agent.organization = user_profile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)
    

class AgentDetailView(OrganizorAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = 'agent'
    
    def get_queryset(self) -> QuerySet[Any]:
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)
    
    
class AgentUpdateView(OrganizorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")
    
    def get_queryset(self) -> QuerySet[Any]:
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)


class AgentDeleteView(OrganizorAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agent_delete.html'
    queryset = Agent.objects.all()

    def get_success_url(self) -> str:
        return reverse('agents:agent-list')
    
    def get_queryset(self) -> QuerySet[Any]:
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)