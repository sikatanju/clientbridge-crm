from typing import Any
import random

from django.core.mail import send_mail
from django.db.models.query import QuerySet
from django.urls import reverse
from django.views import generic

from .mixins import OrganizorAndLoginRequiredMixin
from .forms import AgentModelForm
from leads.models import Agent
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
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organizer = False
        user.set_password(f'{random.randint(100000, 999999)}')
        user.save()

        Agent.objects.create(
            user=user,
            organization=self.request.user.userprofile
        )   

        send_mail(subject='You are invited to be an agent', 
                  message='You were added as an agent on DJCRM. Please login to start.',
                  from_email='admin@gmail.com', recipient_list=[user.email])
        
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
        user = self.request.user
        return Agent.objects.filter(organization=user.userprofile)


class AgentDeleteView(OrganizorAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'agents/agent_delete.html'
    queryset = Agent.objects.all()

    def get_success_url(self) -> str:
        return reverse('agents:agent-list')
    
    def get_queryset(self) -> QuerySet[Any]:
        organization = self.request.user.userprofile
        return Agent.objects.filter(organization=organization)