from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User

class UserRegistrationAPIViewTestCase(APITestCase):
    def test_registration(self):
        url = reverse("user_view")
        user_data = {
            "username": "testuser",
            "fullname": "테스터",
            "email": "test@testuser.com",
            "password": "password",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.data['message'], "가입 완료!!")
        
    # def test_login(self):
    #     url = reverse("token_obtain_pair")
    #     user_data = {
    #         "username": "testuser",
    #         "fullname": "테스터",
    #         "email": "test@testuser.com",
    #         "password": "password",
    #     }
    #     response = self.client.post(url, user_data)
    #     self.assertEqual(response.status_code, 200)
    
# class LoginUserTest(APITestCase):
#     def setUp(self):
#         self.data = {'username': 'john', 'password': 'password'}
#         self.user = User.objects.create_user('john', 'password')
        
#     def test_login(self):
#         response = self.client.post(reverse('token_obtain_pair'), self.data)
#         self.assertEqual(response.status_code, 200)
        
#     def test_get_user_data(self):
#         access_token = self.client.post(reverse('token_obtain_pair'), self.data).data['access']
#         response = self.client.get(
#             path=reverse("user_view"),
#             HTTP_AUTHORIZATION=f"Bearer {access_token}"
#         )
#         # self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data['username'], self.data['username'])
        
        