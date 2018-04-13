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
