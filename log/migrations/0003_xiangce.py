# Generated by Django 3.0.5 on 2020-04-16 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_auto_20200412_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='XiangCe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='标题')),
                ('img', models.ImageField(upload_to='pic/', verbose_name='图片')),
                ('fenlei', models.CharField(default='', max_length=50, verbose_name='分类')),
                ('time', models.TimeField(auto_now=True, verbose_name='上传时间')),
            ],
            options={
                'verbose_name': '图片',
                'verbose_name_plural': '图片',
            },
        ),
    ]
