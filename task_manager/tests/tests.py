from django.test import TestCase
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class UserTestCase(TestCase):
    def setUp(self):
        
