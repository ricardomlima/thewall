from rest_framework.test import APITestCase, APIRequestFactory
from model_mommy import mommy

from wall.models import Post


class PostTestCase(APITestCase):

    endpoint = '/api/v1/posts'

    def setUp(self):

        self.post = mommy.make(Post)
    
    def test_list_posts(self):
        """
        Test api post listing
        """

        response = self.client.get(self.endpoint)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.post.id)


    def test_create_post(self):
        """
        Test api post creation
        """
        new_post = {'message':'new post message'}
        create_request = self.client.post(self.endpoint, new_post)
        response = self.client.get(self.endpoint)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
