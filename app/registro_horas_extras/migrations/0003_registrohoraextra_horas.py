# Generated by Django 3.1 on 2020-08-12 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_horas_extras', '0002_registrohoraextra_funcionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='horas',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]
