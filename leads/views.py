from typing import Any
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse

from agents.mixins import OrganizorAndLoginRequiredMixin

from .models import Lead, Category
from .forms import LeadCategoryUpdateForm, LeadModelForm, CustomUserCreationForm, AssignAgentForm, CategoryModelForm

# Create your views here.

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self) -> str:
        return reverse('login')


class LandingPageView(generic.TemplateView):
    template_name = 'landing.html'


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/lead_list.html'
    # # object_list -- default for context_object_name
    context_object_name = 'leads'

    def get_queryset(self) -> QuerySet[Any]:
        user =  self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile, agent__isnull=False)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization, agent__isnull=False)
            queryset = queryset.filter(agent__user=user)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(LeadListView, self).get_context_data(**kwargs)
        user =  self.request.user
        queryset = None
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile, agent__isnull=True)
        
        if queryset:
            context.update({
                "unassigned_leads": queryset
            })
        
        return context


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
        lead = form.save(commit=False)
        lead.organization = self.request.user.userprofile
        lead.save()
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
        return reverse('leads:lead-list')


class LeadDeleteView(OrganizorAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_queryset(self) -> QuerySet[Any]:
        user =  self.request.user

        if user.is_organizer:
            return Lead.objects.filter(organization=user.userprofile)

    def get_success_url(self) -> str:
        return '/leads'
    

class AssignAgentView(OrganizorAndLoginRequiredMixin, generic.FormView):
    template_name = 'leads/assign_agent.html'
    form_class = AssignAgentForm

    def get_form_kwargs(self, **kwargs) -> dict[str, Any]:
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            'request': self.request
        })
        return kwargs
    
    def form_valid(self, form: Any) -> HttpResponse:
        agent = form.cleaned_data['agent']
        lead = Lead.objects.get(pk=self.kwargs['pk'])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)

    def get_success_url(self) -> str:
        return reverse('leads:lead-list')


class CategoryListView(LoginRequiredMixin, generic.ListView):
    template_name = 'leads/category_list.html'
    context_object_name = 'category_list'

    def get_queryset(self) -> QuerySet[Any]:
        user =  self.request.user
        if user.is_organizer:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = Category.objects.filter(organization=user.agent.organization)

        return queryset
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(CategoryListView, self).get_context_data(**kwargs)
        user =  self.request.user

        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)

        context.update({
            'unassigned_lead_count': queryset.filter(category__isnull=True).count()
        })
        
        return context


class CategoryDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'leads/category_detail.html'
    context_object_name = 'category'

    def get_queryset(self) -> QuerySet[Any]:
        user =  self.request.user
        if user.is_organizer:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = Category.objects.filter(organization=user.agent.organization)

        return queryset
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        leads = self.get_object().leads.all()
        context.update({'leads': leads})
    
        return context
    

class LeadCategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'leads/lead_category_update.html'
    form_class = LeadCategoryUpdateForm
    
    def get_queryset(self) -> QuerySet[Any]:
        user =  self.request.user
        if user.is_organizer:
            queryset = Lead.objects.filter(organization=user.userprofile)
        else:
            queryset = Lead.objects.filter(organization=user.agent.organization)
            queryset = queryset.filter(agent__user=self.request.user)

        return queryset


    def get_success_url(self) -> str:
        return reverse('leads:lead-detail', kwargs={'pk': self.get_object().pk})


class CategoryCreateView(OrganizorAndLoginRequiredMixin, generic.CreateView):
    template_name = "leads/category_create.html"
    form_class = CategoryModelForm

    def get_success_url(self):
        return reverse("leads:category-list")

    def form_valid(self, form):
        category = form.save(commit=False)
        category.organization = self.request.user.userprofile
        category.save()
        return super(CategoryCreateView, self).form_valid(form)


class CategoryUpdateView(OrganizorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "leads/category_update.html"
    form_class = CategoryModelForm

    def get_success_url(self):
        return reverse("leads:category-list")

    def get_queryset(self):
        user = self.request.user

        if user.is_organizer:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = Category.objects.filter(organization=user.agent.organization)

        return queryset


class CategoryDeleteView(OrganizorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "leads/category_delete.html"

    def get_success_url(self):
        return reverse("leads:category-list")

    def get_queryset(self):
        user = self.request.user

        if user.is_organizer:
            queryset = Category.objects.filter(organization=user.userprofile)
        else:
            queryset = Category.objects.filter(organisation=user.agent.organisation)
        
        return queryset