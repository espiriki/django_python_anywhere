# Generated by Django 3.1 on 2020-08-25 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeAcessed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formatted_date', models.CharField(max_length=200)),
            ],
        ),
    ]
