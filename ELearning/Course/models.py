from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from django.utils.translation import gettext_lazy as _
# from Course.blocks  import CategoryBlocks,LevelBlock
from Course.blocks  import LevelBlock,BodyBlock
from wagtail.fields import StreamField,RichTextField
from wagtail.fields import RichTextField

class Category(models.Model):
    Category_name = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.Category_name

class CoursePage(Page):
    course_title = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True, blank=True)
    course_week = models.CharField(max_length=255, blank=True)
    student_count = models.CharField(max_length=255, blank=True)
    course_description = RichTextField(blank=True)
    content = StreamField(
        [('Body', BodyBlock())],  
        null=True,
        blank=True,
    )
    levels = StreamField(
        [('level', LevelBlock())],
        null=True,
        blank=True,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('course_title'),
        FieldPanel('course_week'),
        FieldPanel('student_count'),
        FieldPanel('course_description'),
        FieldPanel('category'),
        FieldPanel('content'), 
        FieldPanel('levels'),
        FieldPanel('images'),
        FieldPanel('price'),
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = ['Course.CoursePage'] 

    max_count = 100 #this count used to create how many course pages 

    class Meta:
        verbose_name = _("Course Page")
        verbose_name_plural = _("Course Pages")

    def get_locale_display(self):
        return str(self.locale)

