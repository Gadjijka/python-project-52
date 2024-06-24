from django.test import TestCase
from task_manager.users.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model


class UserTestCase(TestCase):
    def setUp(self):
        self.new_user = {
                         'first_name': 'Ivan',
                         'last_name': 'Ivanov',
                         'username': 'IvIv',
                         'password1': '19gmr72lp24',
                         'password2': '19gmr72lp24',
                        }
        self.update_user = {
                            'first_name': 'Kirill',
                            'last_name': 'Ushakov',
                            'username': 'KiUs',
                            'password': '19gmr72lp24',
                           }

    def test_user_create(self):
        response = self.client.get(reverse('user_create'))
        self.assertTemplateUsed(response, 'registration/form.html')
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('user_create'),
                                    data=self.new_user,
                                    follow=True
                                   )
        self.assertRedirects(response, reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'User is successfully registered')


    def tests_user_update(self):
        response = self.client
