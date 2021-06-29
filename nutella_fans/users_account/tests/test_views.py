from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client
from django.urls import reverse


class BaseTest(TestCase):
    def setUp(self):
        self.login_url = reverse('login')
        self.signup_url = reverse('sign_up')
        self.user = User.objects.create_user(
            username='test', password='12test12', email='test@email.com')
        self.user = {
            'username': 'username',
            'password': 'password',
            'password2': 'password',
            'email': 'testemail@gmail.com'
        }
        self.user_unmatching_password = {
            'username': 'test',
            'password1': '12test12',
            'password2': '1test12',
            'email': 'testemail@email.com'
        }
        self.user_email_invalid = {
            'username': 'test',
            'password1': '12test12',
            'password2': '12test12',
            'email': 'testemail.com'
        }
        return super().setUp()


class SignUpTest(BaseTest):
    def test_view_ok(self):
        response = self.client.get(self.signup_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'users_account/registration/sign_up.html')

    def test_can_singup(self):
        response = self.client.post(
            self.signup_url, self.user, format='text/html')
        self.assertEquals(response.status_code, 200)

    def test_unmatching_password(self):
        response = self.client.post(
            self.signup_url, self.user, format='text/html')
        self.assertEquals(response.status_code, 400)

    def test_invalid_email(self):
        response = self.client.post(
            self.signup_url, self.user_email_invalid, format='text/html')
        self.assertEquals(response.status_code, 400)


class LoginTest(BaseTest):
    def test_can_view_page_correctly(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'users_account/registration/login.html')
