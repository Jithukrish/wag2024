# Generated by Django 5.0.9 on 2024-10-30 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0004_courseindexpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseindexpage',
            name='intro',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='coursepage',
            name='course_title',
            field=models.CharField(blank=True, default='sdf', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coursepage',
            name='course_week',
            field=models.CharField(blank=True, default='12', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coursepage',
            name='student_count',
            field=models.CharField(blank=True, default='12', max_length=255),
            preserve_default=False,
        ),
    ]
