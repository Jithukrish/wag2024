from wagtail import blocks
from django.utils.translation import gettext_lazy as _
from wagtail.images.blocks import ImageChooserBlock



PREDEFINED_LEVELS = [
    ('beginner', 'Beginner'),
    ('intermediate', 'Intermediate'),
    ('advanced', 'Advanced'),
]
class LevelBlock(blocks.ChoiceBlock):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = PREDEFINED_LEVELS
        super().__init__(*args, **kwargs)

    class Meta:
        template = "blocks/level_blocks.html"
        icon = "list-ul"
        label = "Level Blocks"

class KeytopicsBlock(blocks.StructBlock):
    topic = blocks.CharBlock(required=True, help_text=_("name of topic"))
    class Meta:
        template = "blocks/keytopics_block.html"
        icon = "list-ul"
        label = "Key topics Blocks"

class BodyBlock(blocks.StructBlock):
    # image = ImageChooserBlock(required=True, help_text="Main image of the slider")

    instructor = blocks.CharBlock(max_length=255,help_text=_("name of instructor"))
    link = blocks.URLBlock(required=False)
    key_topic = blocks.ListBlock(
        KeytopicsBlock(),
        min_num=0, 
        max_num=10,  
        help_text=_("Add key topics section"),
        label="Add topics"
    )

    class Meta:
        template = "blocks/base_text_block.html"
        icon = "table"
        label = "image blocks"


