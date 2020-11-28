# Generated by Django 3.1.3 on 2020-11-27 07:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_auto_20201106_1458'),
        ('favorites', '0002_auto_20201025_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='substitute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='products.product'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='substituted',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='substituties', to='products.product'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ManyToManyField(related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]
