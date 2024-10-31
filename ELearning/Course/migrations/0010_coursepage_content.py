# Generated by Django 5.0.9 on 2024-10-30 09:24

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0009_alter_coursepage_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursepage',
            name='content',
            field=wagtail.fields.StreamField([('Body', 6)], blank=True, block_lookup={0: ('wagtail.images.blocks.ImageChooserBlock', (), {'help_text': 'Main image of the slider', 'required': True}), 1: ('wagtail.blocks.CharBlock', (), {'help_text': 'name of instructor', 'max_length': 255}), 2: ('wagtail.blocks.URLBlock', (), {'required': False}), 3: ('wagtail.blocks.CharBlock', (), {'help_text': 'name of topic', 'required': True}), 4: ('wagtail.blocks.StructBlock', [[('topic', 3)]], {}), 5: ('wagtail.blocks.ListBlock', (4,), {'help_text': 'Add key topics section', 'label': 'Add topics', 'max_num': 10, 'min_num': 0}), 6: ('wagtail.blocks.StructBlock', [[('image', 0), ('instructor', 1), ('link', 2), ('key_topic', 5)]], {})}, null=True),
        ),
    ]