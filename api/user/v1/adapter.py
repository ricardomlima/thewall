from django.http import HttpResponse

from allauth.account.adapter import DefaultAccountAdapter

class CustomAdapter(DefaultAccountAdapter):
    
    def respond_email_verification_sent(self, request, user):
        return HttpResponse('Email sent!')
