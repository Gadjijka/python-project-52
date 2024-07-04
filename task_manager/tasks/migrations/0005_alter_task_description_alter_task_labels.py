# Generated by Django 5.0.6 on 2024-07-04 20:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("labels", "0001_initial"),
        ("tasks", "0004_alter_task_labels"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="description",
            field=models.TextField(
                blank=True, max_length=500, verbose_name="Description"
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="labels",
            field=models.ManyToManyField(
                blank=True,
                related_name="labels",
                through="tasks.LabelTask",
                to="labels.label",
                verbose_name="Labels",
            ),
        ),
    ]