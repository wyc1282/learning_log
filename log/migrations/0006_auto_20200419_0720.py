# Generated by Django 3.0.5 on 2020-04-18 23:20

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0005_auto_20200418_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='内容'),
        ),
    ]
