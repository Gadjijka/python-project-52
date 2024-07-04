from django.test import TestCase
from task_manager.users.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model


class UserTestCase(TestCase):

    def setUp(self):
        self.new_user = {
            'first_name': 'Kirill',
            'last_name': 'Ushakov',
            'username': 'KiUs',
            'password1': '19gmr72lp24',
            'password2': '19gmr72lp24',
            }
        User.objects.create(
            id=110,
            first_name='Ivan',
            last_name='Ivanov',
            username='IvIv',
            password='19gmr72lp24'
            )

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
        last_user = User.objects.last()
        count_users = User.objects.count()
        self.assertEqual(last_user.first_name, 'Kirill')
        self.assertEqual(count_users, 2)

    def test_read(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'IvIv')

    def test_update(self):
        self.client.force_login(get_user_model().objects.get(id=110))
        response = self.client.post(reverse('user_update', kwargs={'pk': 110}),
                                    data=self.new_user, follow=True)
        self.assertRedirects(response, reverse('users'))
        self.assertEqual(User.objects.get(pk=110).username, 'KiUs')

    def test_delete(self):
        self.client.force_login(get_user_model().objects.get(id=110))
        response = self.client.post(reverse('user_delete',
                                    kwargs={'pk': 110}),
                                    follow=True
                                    )
        self.assertRedirects(response, reverse('users'))
        self.assertContains(response, 'User successfully deleted')
