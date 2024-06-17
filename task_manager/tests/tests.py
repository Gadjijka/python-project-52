from django.test import TestCase
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.urls import reverse
import json
from django.contrib.auth import get_user_model


class UserTestCase(TestCase):
    def setUp(self):
        self.new_user = {
                         'pk': 1,
                         'first_name': 'Ivan',
                         'last_name': 'Ivanov',
                         'username': 'IvIv',
                         'password': '19gmr72lp24'
                        }
        self.update_user = {
                            'pk': 2,
                            'first_name': 'Kirill',
                            'last_name': 'Ushakov',
                            'username': 'KiUs',
                            'password': '19gmr72lp24',
                           }

    def test_create(self):
        response = self.client.post(reverse('user_create'),
                                    data=json.dumps(self.new_user),
                                    content_type='application/json'
                                   )
        self.assertTemplateUsed(response, 'registration/form.html')
        self.assertEqual(response.status_code, 200)


    def test_users_list(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/index.html')
        self.assertContains(response, 'Ivan')

#    def test_update(self):
#        self.client.force_login(get_user_model().objects.get(pk=1))
#        response = self.client.post(reverse('user_update'),
#                                    data=json.dumps(self.update_user),
#                                    content_type='application/json'
#                                   )
#        self.assertEqual(response.status_code, 200)
