from django.db import models


# Create your models here.
class Status(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name',
                            unique=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Date of Creation')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'
