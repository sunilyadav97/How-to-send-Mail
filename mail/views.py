from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from sendmail import settings

# Create your views here.

def home(request):
    return render(request,'home.html')

def SendMail(request):
    if request.method == 'POST':
        email=request.POST['email']
        msg=request.POST['msg']
        subject='Welcome to Sunil Code'
        message=msg
        from_email=settings.EMAIL_HOST_USER
        recipent_list=[email]
        send_mail(subject,message,from_email,recipent_list,fail_silently=True)

        return HttpResponse('your message has been send successfully.')

