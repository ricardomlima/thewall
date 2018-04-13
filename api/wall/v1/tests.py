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
        Feature: Post List

        Given:
            An existent Wall Post in the Database
        When:
            I make a GET request to the Post Endpoint
        Then:
            I should have a list with the existent Post
            identified by its primary key
        """

        response = self.client.get(self.endpoint)

        self.assertEqual(response.status_code, 200)

        json_result = response.json()
        self.assertEqual(json_result['count'], 1)
        self.assertEqual(json_result['results'][0]['id'], self.post.id)

    def test_create_post(self):
        """
        Feature: Post creation

        Given:
            No existent Post
          AND
            An existent User
        When:
            I authenticate the User
          AND
            I make a POST request with a Post object as body
        Then:
            I should have a persisted Post object in the
            database with the attribute values as the request

        Force authentication headers on request
        """

        # delete all existent Post objects
        Post.objects.all().delete()

        # authenticate as the existent user
        self.client.force_authenticate(user=self.user)

        # create and make the request for a new Post
        new_post = {'message':'new post message'}
        create_request = self.client.post(self.endpoint, new_post, format='json')

        # check for 201 created status code
        self.assertEqual(create_request.status_code, 201)

        # check if a Post now exists in the database
        self.assertTrue(Post.objects.count() > 0)

        # check if the existent post has the same message
        # value as the request
        created_post = Post.objects.all()[0]
        self.assertEquals(created_post.message, new_post['message'])

    def test_create_post_not_authenticated(self):
        """
        Feature: Post Creation Permissions

        Given:
            No existent Posts in the database
          AND
            An existent User
        When:
            I make a POST request with no authentication credentials
            and a Post object as body
        Then:
            I should have no Post objects in the database

        Test api post creation without an authenticated user
        """

        # delete all existent Post objects
        Post.objects.all().delete()

        # create and make the request for a new Post
        new_post = {'message':'new post message'}
        create_request = self.client.post(self.endpoint, new_post, format='json')

        # checking for forbidden status code
        self.assertEqual(create_request.status_code, 403)

        # check if still there is no Post object in the database
        self.assertEquals(Post.objects.count(),  0)
