# Generated by Django 4.1.3 on 2023-02-27 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0014_remove_house_image1_remove_house_image10_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
