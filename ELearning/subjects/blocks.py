from wagtail.models import Page
from wagtail import blocks
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class lessonBlockList(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text=_("name of lesson"))
    video = blocks.URLBlock(required=False)
    class Meta:
        template = "blocks/lesson_block.html"
        icon = "media"
        label = "Lesson Blocks"
class lessonsBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text=_("name of the course"))
    lessons_count = blocks.CharBlock(required=False)
    lessons = blocks.ListBlock(
        lessonBlockList(),
        help_text=_("Add lessons to this course"),
        label="Add lessons" 
    )
    class Meta:
        icon ="media"
        label = "lesson block"


class VideoSessionBlock(blocks.StructBlock):
    lessons = blocks.ListBlock(
       lessonsBlock(),
       help_text=_("Add lessons to this session"),
       label="Add lessons" 
    )
