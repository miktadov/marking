# Generated by Django 3.1.7 on 2021-08-13 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('decoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AfterDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Дата формирования')),
                ('username', models.CharField(max_length=50, verbose_name='Логин пользователя')),
                ('type', models.CharField(max_length=20, verbose_name='Тип файла')),
                ('count', models.IntegerField(verbose_name='Количество КМ')),
                ('first', models.IntegerField(verbose_name='Первый КМ')),
                ('last', models.IntegerField(verbose_name='Последний КМ')),
                ('comment', models.TextField(verbose_name='Дополнительное инфо')),
                ('file', models.FileField(upload_to='', verbose_name='Файл')),
                ('arg1', models.CharField(blank=True, max_length=250)),
                ('arg2', models.CharField(blank=True, max_length=250)),
                ('arg3', models.CharField(blank=True, max_length=250)),
                ('arg4', models.CharField(blank=True, max_length=250)),
                ('arg5', models.CharField(blank=True, max_length=250)),
                ('fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decoder.pdffiles')),
            ],
        ),
    ]