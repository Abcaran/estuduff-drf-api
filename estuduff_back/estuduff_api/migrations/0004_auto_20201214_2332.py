# Generated by Django 3.1.3 on 2020-12-14 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estuduff_api', '0003_auto_20201214_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='studyProfile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='estuduff_api.studyprofile'),
        ),
    ]
