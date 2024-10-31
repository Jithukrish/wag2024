# Generated by Django 5.0.9 on 2024-10-29 05:03

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_homepage_options_homepage_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('banner_text', 3), ('link_information', 8), ('section_section', 12), ('text_card_blocks_subject', 21)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': 'Add your heading', 'required': True}), 1: ('wagtail.blocks.CharBlock', (), {'help_text': 'Add sub heading', 'required': False}), 2: ('wagtail.blocks.RichTextBlock', (), {'editor': 'default', 'help_text': 'Add additional text', 'required': False}), 3: ('wagtail.blocks.StructBlock', [[('heading', 0), ('sub_heading', 1), ('description', 2)]], {'group': 'Card Blocks'}), 4: ('wagtail.blocks.CharBlock', (), {'help_text': 'Enter the label of the link', 'required': False}), 5: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('internal', 'Internal Page'), ('external', 'External URL')], 'help_text': 'Select the type of link'}), 6: ('wagtail.blocks.PageChooserBlock', (), {'help_text': 'Select an internal page', 'page_type': [], 'required': False}), 7: ('wagtail.blocks.URLBlock', (), {'help_text': 'Enter an external URL', 'required': False}), 8: ('wagtail.blocks.StructBlock', [[('label', 4), ('link_type', 5), ('internal_page', 6), ('external_url', 7)]], {'group': 'Card Blocks'}), 9: ('wagtail.images.blocks.ImageChooserBlock', (), {'help_text': 'Main image of the slider', 'required': True}), 10: ('wagtail.blocks.StructBlock', [[('label', 4), ('link_type', 5), ('internal_page', 6), ('external_url', 7)]], {}), 11: ('wagtail.blocks.ListBlock', (10,), {'help_text': 'Add button/link information to this section', 'label': 'Add link details', 'max_num': 2, 'min_num': 0}), 12: ('wagtail.blocks.StructBlock', [[('heading', 0), ('sub_heading', 1), ('description', 2), ('main_image', 9), ('links', 11)]], {'group': 'Card Blocks'}), 13: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('2', '2 cards per row'), ('3', '3 cards per row'), ('4', '4 cards per row')], 'help_text': 'Number of cards', 'max_length': 20, 'null': True}), 14: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('transparent', 'Transparent Background'), ('solid', 'Solid Background'), ('gradient', 'Gradient Background'), ('pattern', 'Pattern Background')], 'help_text': 'Block Backgound', 'max_length': 50, 'null': True}), 15: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('big', 'Big (120px/80px/40px)'), ('small', 'Small (64px)'), ('none', 'NO Padding')], 'help_text': 'Top padding', 'max_length': 50, 'null': True}), 16: ('wagtail.blocks.ChoiceBlock', [], {'blank': True, 'choices': [('big', 'Big (120px/80px/40px)'), ('small', 'Small (64px)'), ('none', 'NO Padding')], 'help_text': 'Bottom padding', 'max_length': 50, 'null': True}), 17: ('wagtail.images.blocks.ImageChooserBlock', (), {'required': True}), 18: ('wagtail.blocks.RichTextBlock', (), {'editor': 'default', 'help_text': 'Add description', 'required': False}), 19: ('wagtail.blocks.StructBlock', [[('heading', 0), ('image', 17), ('description', 18), ('links', 11)]], {}), 20: ('wagtail.blocks.ListBlock', (19,), {'help_text': 'Add multiple image cards to this section. The image alignment is at the top.', 'label': 'Add image card'}), 21: ('wagtail.blocks.StructBlock', [[('heading', 0), ('sub_heading', 1), ('card_count', 13), ('background', 14), ('top_padding', 15), ('bottom_padding', 16), ('points', 20)]], {'group': 'Base Blocks'})}),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image_slider',
            field=wagtail.fields.StreamField([('image_slider', 9)], blank=True, block_lookup={0: ('wagtail.blocks.CharBlock', (), {'help_text': "Title for the image slider (Please add the '&lt;/br&gt;' tag where you want to break the line.)", 'required': False}), 1: ('wagtail.blocks.RichTextBlock', (), {'editor': 'default', 'help_text': 'Add additional text', 'required': False}), 2: ('wagtail.images.blocks.ImageChooserBlock', (), {'help_text': 'Main image of the slider', 'required': True}), 3: ('wagtail.blocks.CharBlock', (), {'help_text': 'Enter the label of the link', 'required': False}), 4: ('wagtail.blocks.ChoiceBlock', [], {'choices': [('internal', 'Internal Page'), ('external', 'External URL')], 'help_text': 'Select the type of link'}), 5: ('wagtail.blocks.PageChooserBlock', (), {'help_text': 'Select an internal page', 'page_type': [], 'required': False}), 6: ('wagtail.blocks.URLBlock', (), {'help_text': 'Enter an external URL', 'required': False}), 7: ('wagtail.blocks.StructBlock', [[('label', 3), ('link_type', 4), ('internal_page', 5), ('external_url', 6)]], {}), 8: ('wagtail.blocks.ListBlock', (7,), {'help_text': 'Add button/link information to this section', 'label': 'Add link details', 'max_num': 2, 'min_num': 0}), 9: ('wagtail.blocks.StructBlock', [[('title', 0), ('description', 1), ('main_image', 2), ('links', 8)]], {})}),
        ),
    ]