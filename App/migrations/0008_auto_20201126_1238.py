# Generated by Django 3.1.3 on 2020-11-26 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20201126_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='previous_score_num',
            old_name='manager1',
            new_name='manager',
        ),
    ]
