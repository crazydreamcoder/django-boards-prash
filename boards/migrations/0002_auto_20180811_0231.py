# Generated by Django 2.0.7 on 2018-08-10 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='topic',
            name='subject',
            field=models.CharField(help_text='This is some helper text from MODEL!!.', max_length=255),
        ),
    ]