# Generated by Django 5.0.4 on 2024-04-17 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_speciality_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='create_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='last_update',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='position',
            name='create_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='position',
            name='last_update',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='create_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='last_update',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='create_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_update',
            field=models.DateField(),
        ),
    ]
