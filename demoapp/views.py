from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        subject=request.POST['subject']
        # send an email
        Subject='Message Received (Contact Page)'
        messagem='NAME           : ' +name +'\n\n'+'EMAIL           : '+''+email +'\n\n'+'SUBJECT      : '+''+subject +'\n\n'+'MESSAGE     : '+message
        #messagem=(color.BOLD + messagem + color.END)
        sendfrom='settings.EMAIL_HOST_USER'
        toadress=['bathinamahesh5399@gmail.com',]
        send_mail(Subject,messagem,sendfrom,toadress)
    return render(request,"base.html")

