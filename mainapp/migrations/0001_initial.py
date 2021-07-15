# Generated by Django 3.2.5 on 2021-07-15 16:13

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
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_organizer', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=64, verbose_name='Название файла')),
                ('option_one', models.CharField(max_length=64)),
                ('option_two', models.CharField(max_length=64)),
                ('option_three', models.CharField(max_length=64)),
                ('option_four', models.CharField(max_length=64)),
                ('option_five', models.CharField(max_length=64)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.userprofile', verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('description', models.TextField(verbose_name='Описание')),
                ('status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.status', verbose_name='Статус')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.userprofile', verbose_name='Пользователь')),
            ],
        ),
    ]