from django.http import HttpResponse

from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.models import EmailAddress, EmailConfirmationHMAC

class CustomAdapter(DefaultAccountAdapter):
    
    def respond_email_verification_sent(self, request, user):
        key = EmailConfirmationHMAC(EmailAddress.objects.filter(user=user).first()).key
        return HttpResponse(key)
