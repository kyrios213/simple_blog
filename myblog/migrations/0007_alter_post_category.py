# Generated by Django 3.2 on 2021-05-06 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_auto_20210506_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]