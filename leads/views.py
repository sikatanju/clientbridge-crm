from typing import Any
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse

from agents.mixins import OrganizorAndLoginRequiredMixin

from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm

# Create your views here.

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self) -> str:
        return reverse('login')


class LandingPageView(generic.TemplateView):
    template_name = 'landing.html'


def landing_page(request):
    return render(request, 'landing.html')


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/lead_list.html'
    # queryset = Lead.objects.all() 
    # # object_list -- default for context_object_name
    context_object_name = 'leads'

    def get_queryset(self) -> QuerySet[Any]:
        user =  self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent__user=self.request.user)

        return queryset


class LeadDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'leads/lead_detail.html'
    # queryset = Lead.objects.all() # object_list -- default
    context_object_name = 'lead'

    def get_queryset(self) -> QuerySet[Any]:
        user =  self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent__user=self.request.user)

        return queryset


class LeadCreateView(OrganizorAndLoginRequiredMixin, generic.CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self) -> str:
        return reverse('leads:lead-list')
    
    def form_valid(self, form):
        # Todo send email
        send_mail(subject='Lead has been created',
                  message="Go to site to see the lead",
                  from_email='test@test.com',
                  recipient_list=['test@recipient.com'])
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(OrganizorAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    
    def get_queryset(self) -> QuerySet[Any]:
        user =  self.request.user

        if user.is_organizer:
            return Lead.objects.filter(organization=user.userprofile)


    def get_success_url(self) -> str:
        return reverse('lead-list')


class LeadDeleteView(OrganizorAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_queryset(self) -> QuerySet[Any]:
        user =  self.request.user

        if user.is_organizer:
            return Lead.objects.filter(organization=user.userprofile)

    def get_success_url(self) -> str:
        return '/leads'



"""
def lead_create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            return redirect('/leads')


    return render(request, "leads/lead_create.html", {'form': form})




def lead_update(request, pk):
    form = LeadForm()
    lead = Lead.objects.get(pk=pk)
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            lead.first_name = form.cleaned_data['first_name']
            lead.last_name = form.cleaned_data['last_name']
            lead.age = form.cleaned_data['age']
            lead.agent = Agent.objects.first()
            lead.save()
            return redirect('/leads')
    return render(request, 'leads/lead_update.html', { 'lead' : lead, 'form': form})

"""