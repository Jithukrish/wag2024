from django.db import models
from wagtail.models import TranslatableMixin
from django.utils.translation import gettext_lazy as _
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from .blocks import ContactBlock
from wagtail.models import Page

class FooterSnippet(TranslatableMixin, models.Model):
    name = models.CharField(max_length=250,help_text=_("Please enter name"))
    copyright = RichTextField(blank=True, editor='default' , help_text=_("Please enter copyright"))  # copyright text


    content = StreamField([
        ('contact_info', ContactBlock()),  
    ],use_json_field=True, blank=True )
    max_count = 1
    panels =[
        FieldPanel('name'),
        FieldPanel('copyright'),
        FieldPanel('content'),   
    ]

    def __str__(self):
        return self.name
   