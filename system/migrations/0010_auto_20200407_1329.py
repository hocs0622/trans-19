# Generated by Django 3.0.5 on 2020-04-07 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0009_auto_20200407_0645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='visits',
        ),
        migrations.AddField(
            model_name='patient',
            name='visit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='system.Visit'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Location'),
        ),
    ]
