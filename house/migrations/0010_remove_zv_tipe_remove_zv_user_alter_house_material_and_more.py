# Generated by Django 4.1.6 on 2023-02-15 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0009_zv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zv',
            name='tipe',
        ),
        migrations.RemoveField(
            model_name='zv',
            name='user',
        ),
        migrations.AlterField(
            model_name='house',
            name='material',
            field=models.CharField(choices=[('дерево', 'дерево'), ('кирпич', 'кирпич'), ('керамические блоки', 'керамические блоки'), ('газобетон', 'газобетон')], max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='type',
            field=models.CharField(choices=[('дом', 'дом'), ('квартира', 'квартира'), ('земельный участок', 'земельный участок')], max_length=25),
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
        migrations.DeleteModel(
            name='ZV',
        ),
    ]