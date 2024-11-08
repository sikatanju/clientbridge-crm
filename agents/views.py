from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AgentModelForm
from leads.models import Agent, UserProfile
# Create your views here.


class AgentListView(LoginRequiredMixin, generic.ListView):
    template_name = 'agents/agent_list.html'
    
    def get_queryset(self) -> QuerySet[Any]:
        return Agent.objects.all()
    

class AgentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        # print(self.request.user.userprofile)

        # print('Validating Form with: ', self.request.user.pk)
        # print(UserProfile.objects.get())
        user_profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        agent.organization = user_profile
        # agent.save()
        return super(AgentCreateView, self).form_valid(form)
    
    