# Generated by Django 2.2.5 on 2019-11-26 17:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Anonymous', max_length=200, null=True)),
                ('created_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('show', models.BooleanField(blank=True, default=True, null=True)),
                ('user_desc', models.CharField(blank=True, default='Customer', max_length=200, null=True)),
                ('testimonial', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
