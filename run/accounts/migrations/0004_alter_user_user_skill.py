# Generated by Django 5.0.3 on 2024-03-25 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_user_location_user_user_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_skill',
            field=models.IntegerField(default=0),
        ),
    ]
