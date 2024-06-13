from django.db import models
from task_manager.users.models import User
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name", unique=True)
    description = models.CharField(max_length=500, verbose_name="Description", blank=True)
    creator = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Creator', related_name='creator')
    executor = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Executor', related_name='executor')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Status', related_name='Status')
    labels = models.ManyToManyField(Label, blank=True, verbose_name='Label', related_name='labels')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
