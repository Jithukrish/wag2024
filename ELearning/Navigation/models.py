from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.blocks import StructBlock,CharBlock,ChoiceBlock,PageChooserBlock,URLBlock,ListBlock
from ELearning.constants import PAGE_TARGETS,BG_CHOICES,CARD_CHOICES,TOP_PADDING_CHOICES,BOTTOM_PADDING_CHOICES,IMAGE_LAYOUT,SOCIAL_MEDIA_CHOICES
from wagtail.admin.panels import FieldPanel
from django.core.exceptions import ValidationError
from wagtail.fields import StreamField
from wagtail.models import TranslatableMixin
NAV_TYPE = [
	    ('header', _('Header Navigation'),),
        ('footer', _('Footer Navigation'),),
        ('footer_links', _('Footer Links'),),
    ]

MENU_TYPE = [
	    ('text', _('Text Menu'),),
        ('bordered_button', _('Bordered Button Menu'),),
        ('filled_button', _('Filled Button Menu'),),
    ]


class MenuItemBlock(StructBlock):
    title = CharBlock(required=True)
    link_type = ChoiceBlock(choices=[
        ('internal', 'Internal Page'),
        ('external', 'External URL'),
    ])

    internal_page = PageChooserBlock(required=False, target_model=PAGE_TARGETS)
    tab_key = CharBlock(required=False, default="", label="Tab Key",  help_text="Enter a unique key for this tab. This key will be used to link the \
                                                                                            menu to the corresponding section of the page.")
    external_url = URLBlock(required=False)
    internal_page_model_name = CharBlock(required=False, max_length=150, label="Page name(internal)", help_text="This field can be avoided and will be set automatically.", editable=False) 
    class Meta:
        icon = "list-ul"
        label = "Menu Item"  


class TabBlock(StructBlock):
    title = CharBlock(required=False, help_text=_("Please enter tab name"))
    slug = CharBlock(required=False, help_text=_("Please provide unique slug name for url"))
    menu_items = ListBlock(MenuItemBlock())
    class Meta:
        icon = "list-ul"
        label = "Tabbed Menu with Multiple Menu Items"
class SingleMenuBlock(StructBlock):
    title = CharBlock(required=False, help_text=_("enter title"))
    menu_type = ChoiceBlock(max_length=20, choices=MENU_TYPE,null=True, blank=True, default="text", help_text=_("Menu type"))
    menu_item = MenuItemBlock()
    class Meta:
        icon = "list-ul"
        label = "Single Menu"

class MultipleMenuBlock(StructBlock):
    title = CharBlock(required=False, help_text=_("enter title"))
    menu_type = ChoiceBlock(max_length=20, choices=MENU_TYPE,null=True, blank=True, default="text", help_text=_("Menu type"))
    menu_item = ListBlock(MenuItemBlock())
    class Meta:
        icon = "list-ul"
        label = "Multiple Menu"


class TabbedMenuBlock(StructBlock):
    title = CharBlock(required=True, help_text=_("Please enter tab name"))
    tabs = ListBlock(TabBlock())
    class Meta:
        icon = "list-ul"
        label = "Tabbed Menu"

class NavigationSnippet(TranslatableMixin, models.Model):
    name = models.CharField(max_length=255, help_text=_("Please enter name"))
    nav_type = models.CharField(
        max_length=20,
        choices=NAV_TYPE,
        null=True,
        blank=True,
        default="top",
        help_text=_("Navigation type")
    )
    menus = StreamField([
        ('single_menu', SingleMenuBlock()),
        ('multiple_menu', MultipleMenuBlock()),
        ('tabbed_menu', TabbedMenuBlock()),
    ], use_json_field=True)
    panels = [
        FieldPanel('name'),
        FieldPanel('nav_type'),
        FieldPanel('menus'),
      ]
    
    def __str__(self):
        return self.name
    


