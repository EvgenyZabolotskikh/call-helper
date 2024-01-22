# Generated by Django 5.0.1 on 2024-01-22 13:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breaks', '0006_replacementstatus'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='replacementstatus',
            name='id',
        ),
        migrations.AlterField(
            model_name='replacementstatus',
            name='code',
            field=models.CharField(max_length=16, primary_key=True, serialize=False, verbose_name='Код'),
        ),
        migrations.CreateModel(
            name='ReplacementEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replacements', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник')),
                ('replacement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='breaks.replacement', verbose_name='Смена')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replacement_employees', to='breaks.replacementstatus', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Смена - Работник',
                'verbose_name_plural': 'Смены - Работники',
            },
        ),
    ]
