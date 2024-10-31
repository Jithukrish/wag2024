from django.db import models
from wagtail.models import Page
from django.utils.translation import gettext_lazy as _
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from .blocks import VideoSessionBlock
from Course.models import CoursePage


class CurriculamPage(Page):
    name = models.CharField(max_length=200,  blank=True, help_text=_("add name "))
    course = models.ForeignKey(CoursePage,on_delete=models.SET_NULL,  null=True, blank=True, help_text=_("Select Course"))
    video = StreamField(
        [('videosession', VideoSessionBlock())],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('course'),
        FieldPanel('video'),
          
    ]
    # max_count = 1
    parent_page_types = ['home.HomePage']
    subpage_types = []
    template = "subjects/sub_video.html"
    class Meta:
        verbose_name = _("Curriculam Page")
        verbose_name_plural = _("Curriculam Pages")

    def get_locale_display(self):
        return str(self.locale)

