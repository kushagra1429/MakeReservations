# Generated by Django 4.2.1 on 2023-06-22 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SeatAllocationAuthentication', '0002_user_last_login_alter_user_employeeemail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.CharField(default='', max_length=100),
        ),
    ]
