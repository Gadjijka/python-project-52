from django.test import TestCase, Client
from django.urls import reverse
from task_manager.users.models import User
#from rest_framework.test import APIClient
#from rest_framework import status


class Test_User(TestCase):
    def setUp(self):
        self.user = {'first_name': 'Ilya',
                     'last_name': 'Ivanov',
                     'username': 'IlIv',
                     'password': '12345'}

    def test_registration(self):
        response = self.client.get(reverse('user_create'))
        self.assertTemplateUsed(response, 'registration/form.html')
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('user_create'), data=self.user)
        self.assertEqual(response.status_code, 200)

    def test_updating(self):
        pass


class Test_Label(TestCase):
    pass

class Test_Task(TestCase):
    pass

class Test_Status(TestCase):
    pass
