# Generated by Django 3.1.2 on 2020-10-22 08:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('favorites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ManyToManyField(help_text='User who saves a substitute product', related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]