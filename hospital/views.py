from django.shortcuts import render,redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView
from .models import Doctor
# from django.conf import settings

class hospitalView(TemplateView):
    template_name = 'index.html'


class DoctorListView(ListView):
    queryset = Doctor.objects.all()
    template_name = 'doctor-team.html'



class ContactView(TemplateView):
    template_name = 'contact.html'
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email_from = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if subject == '':
            subject = 'Healthcae Contact'     

        if name and message and email_from:
            send_mail(
                subject+ " - " + name,
                message+ 
                email_from,
                ['yourname@gmail.com',],
                fail_silently=False,
            )
            messages.success(request, f'Your message has been sent. Thank you {name}!')

        return redirect('contact')








# def contact(request):
#     return render(request, 'contact.html')


# def about(request):
#     return render(request, 'about.html')
    
# def testimonial(request):
#     return render(request, 'testimonial.html')