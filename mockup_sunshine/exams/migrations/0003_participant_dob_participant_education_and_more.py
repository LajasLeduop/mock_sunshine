# Generated by Django 4.2.5 on 2023-09-08 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_participant'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='dob',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='participant',
            name='education',
            field=models.CharField(default='+2', max_length=30),
        ),
        migrations.AddField(
            model_name='participant',
            name='university',
            field=models.CharField(default='Tribhuvan University', max_length=50),
        ),
    ]