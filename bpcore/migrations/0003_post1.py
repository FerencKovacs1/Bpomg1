# Generated by Django 2.1.5 on 2019-05-17 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpcore', '0002_post_texttwo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=250, null=True)),
                ('draft', models.BooleanField(default=False)),
            ],
        ),
    ]
