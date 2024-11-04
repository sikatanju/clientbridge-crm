from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

# Create your views here.

def landing_page(request):
    return render(request, 'landing.html')


def lead_list(request):
    leads = Lead.objects.all()
    # return HttpResponse('Hello World')
    return render(request, 'leads/lead_list.html', { 'leads': leads})


def lead_detail(request, pk):
    lead = Lead.objects.get(pk=pk)

    return render(request, 'leads/lead_detail.html', { 'lead' : lead })


def lead_create(request):
    form = LeadModelForm()
    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')


    return render(request, "leads/lead_create.html", {'form': form})


def lead_update(request, pk):
    lead = Lead.objects.get(pk=pk)
    form = LeadModelForm(instance=lead)
    
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            lead.save()
            return redirect('/leads')
        
    return render(request, 'leads/lead_update.html', { 'lead' : lead, 'form': form})

def lead_delete(request, pk):
    lead = Lead.objects.get(pk=pk)
    lead.delete()
    return redirect('lead-list')

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