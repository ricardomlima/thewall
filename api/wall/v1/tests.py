from rest_framework.test import APITestCase, APIRequestFactory
from model_mommy import mommy

from user.models import WallUser
from wall.models import Post


class PostTestCase(APITestCase):

    endpoint = '/api/v1/posts'

    def setUp(self):

        self.post = mommy.make(Post)
        self.user = mommy.make(WallUser)
    
    def test_list_posts(self):
        """
        Test api post listing
        """

        response = self.client.get(self.endpoint)

        self.assertEqual(response.status_code, 200)

        json_result = response.json()
        self.assertEqual(json_result['count'], 1)
        self.assertEqual(json_result['results'][0]['id'], self.post.id)


    def test_create_post(self):
        """
        Test api post creation

        Force authentication headers on request
        """

        self.client.force_authenticate(user=self.user)
        new_post = {'message':'new post message'}

        create_request = self.client.post(self.endpoint, new_post, format='json')

        self.assertEqual(create_request.status_code, 201)

        response = self.client.get(self.endpoint)

        self.assertEqual(response.status_code, 200)
        json_result = response.json()
        self.assertEqual(json_result['count'], 2)
