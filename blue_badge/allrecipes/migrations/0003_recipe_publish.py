# Generated by Django 2.1.7 on 2019-03-11 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allrecipes', '0002_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
