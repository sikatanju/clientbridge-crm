from django.shortcuts import render
from django.http import HttpResponse

from .models import Lead

# Create your views here.
def lead_list(request):
    leads = Lead.objects.all()
    # return HttpResponse('Hello World')
    return render(request, 'leads/lead_list.html', { 'leads': leads})


def lead_detail(request, pk):
    lead = Lead.objects.get(pk=pk)

    return render(request, 'leads/lead_detail.html', { 'lead' : lead })