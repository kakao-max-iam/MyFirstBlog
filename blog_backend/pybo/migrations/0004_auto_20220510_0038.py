# Generated by Django 3.1.3 on 2022-05-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0003_auto_20220510_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='owner_name',
            field=models.CharField(default='', max_length=30, null=True),
        ),
    ]