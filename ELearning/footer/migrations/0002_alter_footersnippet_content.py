# Generated by Django 5.0.9 on 2024-10-30 05:27

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('footer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footersnippet',
            name='content',
            field=wagtail.fields.StreamField([('contact_info', 25)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Heading add here', 'max_length': 250, 'required': False}), 1: ('wagtail.blocks.CharBlock', (), {'help_text': 'street address', 'max_length': 250, 'required': False}), 2: ('wagtail.blocks.CharBlock', (), {'help_text': 'add footer phone number', 'max_length': 20, 'required': True}), 3: ('wagtail.blocks.EmailBlock', (), {'help_text': 'add footer email address', 'required': True}), 4: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('facebook', 'Facebook'), ('twitter', 'Twitter'), ('linkedin', 'LinkedIn'), ('instagram', 'Instagram'), ('youtube', 'YouTube')], 'help_text': 'Select the social media platform'}), 5: ('wagtail.blocks.URLBlock', (), {'help_text': 'Enter the URL of the social media profile', 'required': True}), 6: ('wagtail.blocks.StructBlock', [[('platform', 4), ('url', 5)]], {}), 7: ('wagtail.blocks.ListBlock', (6,), {'help_text': 'Add button/link information to this section', 'label': 'Add link details', 'max_num': 4, 'min_num': 0}), 8: ('wagtail.blocks.StructBlock', [[('icons', 7)]], {}), 9: ('wagtail.blocks.ListBlock', (8,), {'help_text': 'Add the social media platforms and URLs you want to display.'}), 10: ('wagtail.blocks.RichTextBlock', (), {'editor': 'default', 'help_text': 'Add description', 'required': False}), 11: ('wagtail.blocks.StructBlock', [[('heading', 0), ('description', 10)]], {}), 12: ('wagtail.blocks.CharBlock', (), {'help_text': 'enter title', 'required': False}), 13: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('text', 'Text Menu'), ('bordered_button', 'Bordered Button Menu'), ('filled_button', 'Filled Button Menu')], 'help_text': 'Menu type', 'max_length': 20, 'null': True}), 14: ('wagtail.blocks.CharBlock', (), {'required': True}), 15: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('internal', 'Internal Page'), ('external', 'External URL')]}), 16: ('wagtail.blocks.PageChooserBlock', (), {'page_type': [], 'required': False}), 17: ('wagtail.blocks.CharBlock', (), {'default': '', 'help_text': 'Enter a unique key for this tab. This key will be used to link the                                                                                             menu to the corresponding section of the page.', 'label': 'Tab Key', 'required': False}), 18: ('wagtail.blocks.URLBlock', (), {'required': False}), 19: ('wagtail.blocks.CharBlock', (), {'editable': False, 'help_text': 'This field can be avoided and will be set automatically.', 'label': 'Page name(internal)', 'max_length': 150, 'required': False}), 20: ('wagtail.blocks.StructBlock', [[('title', 14), ('link_type', 15), ('internal_page', 16), ('tab_key', 17), ('external_url', 18), ('internal_page_model_name', 19)]], {}), 21: ('wagtail.blocks.StructBlock', [[('title', 12), ('menu_type', 13), ('menu_item', 20)]], {}), 22: ('wagtail.blocks.ListBlock', (21,), {'help_text': 'Add the social media platforms and URLs you want to display.'}), 23: ('wagtail.blocks.StructBlock', [[('heading', 0), ('menu_items', 22)]], {}), 24: ('wagtail.blocks.ListBlock', (23,), {'help_text': 'Add multiple menu items cards.', 'label': 'Add menu items'}), 25: ('wagtail.blocks.StructBlock', [[('heading', 0), ('street', 1), ('phone', 2), ('email', 3), ('social_media', 9), ('right_part', 11), ('Middle_block', 24)]], {})}),
        ),
    ]
