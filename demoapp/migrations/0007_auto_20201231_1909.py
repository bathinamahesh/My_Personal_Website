# Generated by Django 3.1.4 on 2020-12-31 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0006_auto_20201231_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]