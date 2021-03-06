# Generated by Django 4.0.3 on 2022-06-01 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('body', models.TextField(help_text='post report content', max_length=500)),
                ('status', models.CharField(choices=[('Spam', 'Spam'), ('Harassment', 'Harassment'), ('Rules Violation', 'Rules Violation')], default='Spam', max_length=15)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_report', to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_report', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
