from email.message import EmailMessage
from http.client import HTTPResponse
import socket
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail

from home.models import Contact, Project
from portfolio import settings

def index(request):
    projects = Project.objects.all()
    return render(request, 'home/index.html', {'projects': projects})

# View for project details
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'home/project_detail.html', {'project': project})

def contact_view(request):
    projects = Project.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the contact form details to the database
        contact = Contact(name=name, email=email, message=message)
        contact.save()

        # Send a success message to the template
        return render(request, 'home/index.html', {'projects': projects, 'success': True})

    return render(request, 'home/index.html', {'projects': projects})