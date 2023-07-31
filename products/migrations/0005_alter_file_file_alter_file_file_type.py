# Generated by Django 4.2.3 on 2023-07-23 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_file_file_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(blank=True, upload_to='files/%y/%m/%d/', verbose_name='file'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'audio'), (2, 'video'), (3, 'pdf')], verbose_name='file type'),
        ),
    ]
