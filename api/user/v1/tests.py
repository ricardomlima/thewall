from allauth.account.models import EmailAddress, EmailConfirmationHMAC
from rest_framework.test import APITestCase
from model_mommy import mommy

from user.models import WallUser


class AuthTestCase(APITestCase):

    endpoint = '/api/v1/auth/'

    def setUp(self):
        self.user = {
            'email':'mock@gmail.com',
            'password1':'12345abc',
            'password2':'12345abc',
        }

    def test_user_exists_after_registration_request(self):
        """
        Feature: User Registration

        Given: 
            A correct user registration request
        When:
            The request is sent to the registration endpoint
        Then:
            I expect to have one user in the database
        """

        r = self.client.post(self.endpoint+'registration/', self.user, format='json')
        self.assertTrue(WallUser.objects.count() > 0)

    def test_user_is_verified_after_email_verification_request(self):
        """
        Feauture: User Email Verification

        Given:
            A user with an Auth token and not verified email
          AND
            UserObject.is_verified == False
          And
            A correct request with this users token as key parameter
        When:
            The request is sent to the email verification endpoint
        Then:
            UserObject.is_verified == True
        """

        # register user
        res = self.client.post(self.endpoint+'registration/', self.user, format='json')
        self.assertTrue(WallUser.objects.count() > 0)

        # verify if recently created user's email is not verified
        wall_user = WallUser.objects.all()[0]
        self.assertFalse(wall_user.is_verified())

        # get the users key and make the email verification request
        key = EmailConfirmationHMAC(EmailAddress.objects.filter(user=wall_user).first()).key
        postData = {'key':key}
        res = self.client.post(self.endpoint+'registration/verify-email/', postData, format='json')

        # assert if user's email is verified
        # through the is_verified attribute
        self.assertTrue(wall_user.is_verified())
