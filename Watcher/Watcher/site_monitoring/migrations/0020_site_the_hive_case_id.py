# Generated by Django 3.0.7 on 2020-06-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_monitoring', '0019_auto_20200522_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='the_hive_case_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]