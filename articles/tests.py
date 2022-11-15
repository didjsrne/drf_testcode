from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from articles.models import Article
from django.urls import reverse


class ArticleCreateTest(APITestCase):
    @classmethod
    def setupTestData(cls):
        cls.user_data = {'username': 'john', 'password': 'password'}
        cls.article_data = {'title': 'some title', 'content': 'some content'}
        cls.user = User.objects.create_user('jonh', 'password')
    
    def setUp(self):
        self.access_token = self.client.post(reverse('token_obtain_pair'), self.user_data).data['access']
    
    def test_fail_if_not_logged_in(self):
        url = reverse("article_view")
        response = self.client.post(url, self.article_data)
        self.assertEqual(response.status_code, 401)
