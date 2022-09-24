# Generated by Django 3.1.14 on 2022-09-24 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.CharField(max_length=200, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('channel_title', models.CharField(max_length=400, null=True)),
                ('video_image', models.CharField(max_length=400, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200, null=True)),
                ('text', models.TextField(max_length=1000, null=True)),
                ('writer', models.TextField(max_length=200)),
                ('like_count', models.IntegerField()),
                ('reply_count', models.IntegerField()),
                ('writer_url', models.TextField(max_length=200, null=True)),
                ('writer_image', models.TextField(max_length=200, null=True)),
                ('zorbalık', models.TextField(max_length=200, null=True)),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='youtube_analiz.video')),
            ],
        ),
    ]
