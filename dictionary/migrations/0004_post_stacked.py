# Generated by Django 4.0.4 on 2023-02-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_post_is_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='stacked',
            field=models.BigIntegerField(default=0, null=True),
        ),
    ]
