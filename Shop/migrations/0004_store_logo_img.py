# Generated by Django 3.1.3 on 2020-12-09 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_remove_store_logo_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='logo_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
