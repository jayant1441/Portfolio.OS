# Generated by Django 2.2.5 on 2019-11-28 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.CharField(blank=True, default='https://res.cloudinary.com/raghavdhingra/image/upload/v1574935065/pc_bg9yoh.jpg', max_length=500, null=True),
        ),
    ]