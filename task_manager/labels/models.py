from django.db import models

# Create your models here.
class Label(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50, unique=True)
    created_at = models.DateTimeField(verbose_name='Date of creation', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Label'
        verbose_name_plural = 'Labels'
