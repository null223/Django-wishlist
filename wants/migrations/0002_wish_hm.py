# Generated by Django 2.2.4 on 2019-08-18 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='hm',
            field=models.IntegerField(default=3747),
            preserve_default=False,
        ),
    ]
