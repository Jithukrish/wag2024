from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.utils.translation import gettext_lazy as _
from home.blocks import socialMediaListBlock
from Navigation.models  import SingleMenuBlock
from ELearning.constants import PAGE_TARGETS,BG_CHOICES,CARD_CHOICES,TOP_PADDING_CHOICES,BOTTOM_PADDING_CHOICES,IMAGE_LAYOUT,SOCIAL_MEDIA_CHOICES


class RightBlock(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=250, required=False, help_text=_("Heading add here"))
    description = blocks.RichTextBlock(editor='default',required=False, help_text=_("Add description"))
    class Meta:
        icon = "image"
        label = _("Right Block")
class MiddleBlock(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=250, required=False, help_text=_("Heading add here"))
    menu_items = blocks.ListBlock(SingleMenuBlock(),help_text=_("Add the social media platforms and URLs you want to display."))
    class Meta:
        icon = "edit"
        label =_("Middle Block")

class SocialMediaLinkBlock(blocks.StructBlock):
    platform = blocks.ChoiceBlock(choices=SOCIAL_MEDIA_CHOICES, required=True, help_text=_("Select the social media platform"))
    url = blocks.URLBlock(required=True, help_text=_("Enter the URL of the social media profile"))

    class Meta:
        # template = "blocks/text_block_with_links.html"
        icon = "doc-full"
        label = "Social media"
class socialMediaListBlock(blocks.StructBlock):
    icons = blocks.ListBlock(
        SocialMediaLinkBlock(),
        min_num=0,
        max_num=4,
        help_text=_("Add button/link information to this section"),
        label="Add link details"
    )
class ContactBlock(blocks.StructBlock):
    heading = blocks.CharBlock(max_length=250, required=False, help_text=_("Heading add here"))
    street = blocks.CharBlock(max_length=250, required=False,  help_text=_("street address"))
    phone = blocks.CharBlock(max_length=20, required= True, help_text=_("add footer phone number"))
    email = blocks.EmailBlock(required=True, help_text=_("add footer email address"))
    social_media = blocks.ListBlock(
        socialMediaListBlock(),
        help_text=_("Add the social media platforms and URLs you want to display.")
    )
    right_part = RightBlock()
    Middle_block =blocks.ListBlock(MiddleBlock(), 
                            label="Add menu items", 
                            help_text="Add multiple menu items cards.")
    
    class Meta:
        icon = "image"
        label = _("Contact Block")


