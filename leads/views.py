from django.core.mail import send_mail
# from django.contrib.auth.forms import UserCreationForm
from django.forms import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse

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

class LeadListView(generic.ListView):
    template_name = 'leads/lead_list.html'
    queryset = Lead.objects.all() # object_list -- default
    context_object_name = 'leads'


# def lead_list(request):
#     leads = Lead.objects.all()
#     # return HttpResponse('Hello World')
#     return render(request, 'leads/lead_list.html', { 'leads': leads})


class LeadDetailView(generic.DetailView):
    template_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all() # object_list -- default
    context_object_name = 'lead'


# def lead_detail(request, pk):
#     lead = Lead.objects.get(pk=pk)

#     return render(request, 'leads/lead_detail.html', { 'lead' : lead })

class LeadCreateView(generic.CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self) -> str:
        return reverse('lead-list')
    
    def form_valid(self, form):
        # Todo send email
        send_mail(subject='Lead has been created',
                  message="Go to site to see the lead",
                  from_email='test@test.com',
                  recipient_list=['test@recipient.com'])
        return super(LeadCreateView, self).form_valid(form)


# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/leads')


#     return render(request, "leads/lead_create.html", {'form': form})


class LeadUpdateView(generic.UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self) -> str:
        return reverse('lead-list')



# def lead_update(request, pk):
#     lead = Lead.objects.get(pk=pk)
#     form = LeadModelForm(instance=lead)
    
#     if request.method == 'POST':
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             lead.save()
#             return redirect('/leads')
        
#     return render(request, 'leads/lead_update.html', { 'lead' : lead, 'form': form})


class LeadDeleteView(generic.DeleteView):
    template_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self) -> str:
        return '/leads'


# def lead_delete(request, pk):
#     lead = Lead.objects.get(pk=pk)
#     lead.delete()
#     return redirect('lead-list')

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