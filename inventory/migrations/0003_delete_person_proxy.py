# Generated by Django 4.1.7 on 2023-03-15 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_person_proxy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person_Proxy',
        ),
    ]
