from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from ELearning.constants import PAGE_TARGETS,BG_CHOICES,CARD_CHOICES,TOP_PADDING_CHOICES,BOTTOM_PADDING_CHOICES,IMAGE_LAYOUT,SOCIAL_MEDIA_CHOICES


class LinkBlock(blocks.StructBlock):
    label = blocks.CharBlock(required=False, help_text=_("Enter the label of the link"))
    link_type = blocks.ChoiceBlock(
        choices = [
            ('internal', _('Internal Page')),
            ('external', _('External URL')),
        ],
        default='internal',
        help_text=_("Select the type of link"),
    )
    internal_page = blocks.PageChooserBlock(
        required=False, 
        help_text=_("Select an internal page"),
        target_model = PAGE_TARGETS
    )
    external_url = blocks.URLBlock(
        required=False, 
        help_text=_("Enter an external URL"),
    )

    def clean(self, value):
        """
        Custom validation to ensure that only one type of link (internal or external) is provided,
        and that the appropriate fields are filled based on the selected link type.
        """
        cleaned_data = super().clean(value)
        link_type = cleaned_data.get('link_type')
        internal_page = cleaned_data.get('internal_page')
        external_url = cleaned_data.get('external_url')

        # Validation logic based on link type
        if link_type == 'internal' and not internal_page:
            raise ValidationError(_('An internal page must be selected when "Internal Page" is chosen.'))
        elif link_type == 'external' and not external_url:
            raise ValidationError(_('A URL must be provided when "External URL" is chosen.'))

        if link_type == 'internal' and external_url:
            raise ValidationError(_('An external URL should not be provided when linking to an internal page.'))
        if link_type == 'external' and internal_page:
            raise ValidationError(_('An internal page should not be provided when linking to an external URL.'))

        return cleaned_data
    
    class Meta:
        label = _("Link Information")
        icon = 'link'

class LinkBlock(blocks.StructBlock):
    label = blocks.CharBlock(required=False, help_text=_("Enter the label of the link"))
    link_type = blocks.ChoiceBlock(
        choices = [
            ('internal', _('Internal Page')),
            ('external', _('External URL')),
        ],
        default='internal',
        help_text=_("Select the type of link"),
    )
    internal_page = blocks.PageChooserBlock(
        required=False, 
        help_text=_("Select an internal page"),
        target_model = PAGE_TARGETS
    )
    external_url = blocks.URLBlock(
        required=False, 
        help_text=_("Enter an external URL"),
    )

    def clean(self, value):
      
        cleaned_data = super().clean(value)
        link_type = cleaned_data.get('link_type')
        internal_page = cleaned_data.get('internal_page')
        external_url = cleaned_data.get('external_url')

        # Validation logic based on link type
        if link_type == 'internal' and not internal_page:
            raise ValidationError(_('An internal page must be selected when "Internal Page" is chosen.'))
        elif link_type == 'external' and not external_url:
            raise ValidationError(_('A URL must be provided when "External URL" is chosen.'))

        # Prevent both internal and external links from being filled
        if link_type == 'internal' and external_url:
            raise ValidationError(_('An external URL should not be provided when linking to an internal page.'))
        if link_type == 'external' and internal_page:
            raise ValidationError(_('An internal page should not be provided when linking to an external URL.'))

        return cleaned_data
    
    class Meta:
        label = _("Link Information")
        icon = 'link'
class ImageSliderBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, help_text="Title for the image slider (Please add the '&lt;/br&gt;' tag where you want to break the line.)")
    description = blocks.RichTextBlock(editor='default',required=False, help_text=_("Add additional text"))    
    main_image = ImageChooserBlock(required=True, help_text="Main image of the slider")
    # related_images = blocks.ListBlock(
    #     ImageChooserBlock(),
    #     max_num=10,  # Limit to 10 images
    #     required=False,  # Make the field optional
    #     help_text="Up to 10 small images"
    # )
    links = blocks.ListBlock(
        LinkBlock(),
        min_num=0,  # No minimum requirement
        max_num=2,  # Maximum of two links
        help_text=_("Add button/link information to this section"),
        label="Add link details"
    )

    class Meta:
        icon = 'image'
        label = "Image Slider"


class HomePageSharesListBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text=_("Add your heading"))
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add sub heading"))
    description = blocks.RichTextBlock(editor='default',required=False, help_text=_("Add additional text"))
    class Meta:
        template = "blocks/base_text_block.html"
        icon = "table"
        label = "Home Page Shares List Block"

class HomePagesectionsecondBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text=_("Add your heading"))
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add sub heading"))
    description = blocks.RichTextBlock(editor='default',required=False, help_text=_("Add additional text"))
    main_image = ImageChooserBlock(required=True, help_text="Main image of the slider")
    links = blocks.ListBlock(
        LinkBlock(),
        min_num=0,  # No minimum requirement
        max_num=2,  # Maximum of two links
        help_text=_("Add button/link information to this section"),
        label="Add link details"
    )

    class Meta:
        template = "blocks/base_section_second_block.html"
        icon = "table"
        label = "Home Page section second Block"


class BaseImageTextCardBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text=_("Add your heading"))
    image = ImageChooserBlock(required=True) 
    description  = blocks.RichTextBlock(editor='default',required=False, help_text=_("Add description"))

    class Meta:
        # template = "blocks/text_block_with_links.html"
        icon = "image"
        label = "Base Image Text Card Block"
class ImageTextCardBlockWithLinks(BaseImageTextCardBlock):
    links = blocks.ListBlock(
        LinkBlock(),
        min_num=0,
        max_num=2,
        help_text=_("Add button/link information to this section"),
        label="Add link details"
    )

    class Meta:
        # template = "blocks/text_block_with_links.html"
        icon = "doc-full"
        label = "Image Text Card Block with Links"

class TextOverlayImageCardBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text=_("Add your heading"))  
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add sub heading"))
    card_count = blocks.ChoiceBlock(max_length=20, choices=CARD_CHOICES,  null=True, blank=True, default="3", help_text=_("Number of cards"))
    background = blocks.ChoiceBlock(max_length=50, choices=BG_CHOICES,  null=True, blank=True, default="transparent", help_text=_("Block Backgound"))
    top_padding = blocks.ChoiceBlock(max_length=50, choices=TOP_PADDING_CHOICES,  null=True, blank=True, default="big", help_text=_("Top padding"))
    bottom_padding = blocks.ChoiceBlock(max_length=50, choices=BOTTOM_PADDING_CHOICES,  null=True, blank=True, default="big", help_text=_("Bottom padding"))      
    points = blocks.ListBlock(ImageTextCardBlockWithLinks(), 
                              label="Add image card", 
                              help_text="Add multiple image cards to this section. The image alignment is at the top.")
    
    class Meta:
        icon = "image"
        label = _("Text Overlay Image Card Block")

class BaseImageTextCardBlockone(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text=_("Add your heading"))
    students_amount = blocks.CharBlock(required=True, help_text=_("students count"))
    hour = blocks.CharBlock(required=True, help_text=_("total hour"))
    rating = blocks.CharBlock(required=True, help_text=_("total rating"))
    price = blocks.CharBlock(required=True, help_text=_("price tag"))
    image = ImageChooserBlock(required=True) 
    description  = blocks.RichTextBlock(editor='default',required=False, help_text=_("Add description"))

    class Meta:
        # template = "blocks/text_block_with_links.html"
        icon = "image"
        label = "Base Image Text Card Block"
class ImageTextCardBlockWithLinksone(BaseImageTextCardBlockone):
    links = blocks.ListBlock(
        LinkBlock(),
        min_num=0,
        max_num=2,
        help_text=_("Add button/link information to this section"),
        label="Add link details"
    )

    class Meta:
        # template = "blocks/text_block_with_links.html"
        icon = "doc-full"
        label = "Image Text Card Block with Links"
class SectionThreeCardBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text=_("Add your heading"))  
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add sub heading"))
    card_count = blocks.ChoiceBlock(max_length=20, choices=CARD_CHOICES,  null=True, blank=True, default="3", help_text=_("Number of cards"))
    background = blocks.ChoiceBlock(max_length=50, choices=BG_CHOICES,  null=True, blank=True, default="transparent", help_text=_("Block Backgound"))
    top_padding = blocks.ChoiceBlock(max_length=50, choices=TOP_PADDING_CHOICES,  null=True, blank=True, default="big", help_text=_("Top padding"))
    bottom_padding = blocks.ChoiceBlock(max_length=50, choices=BOTTOM_PADDING_CHOICES,  null=True, blank=True, default="big", help_text=_("Bottom padding"))      
    points = blocks.ListBlock(ImageTextCardBlockWithLinksone(), 
                              label="Add image card", 
                              help_text="Add multiple image cards to this section. The image alignment is at the top.")
    
    class Meta:
        icon = "image"
        label = _("Section Card Block three")


class PointBlock(blocks.StructBlock):
    heading_point = blocks.CharBlock(required=True, help_text=_("Add your points heading"))
    class Meta:
        # template = "blocks/text_block_with_links.html"
        icon = "tag"
        label = "point blocks"

class SectionFourCardBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text=_("Add your heading"))  
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add sub heading"))
    description  = blocks.RichTextBlock(editor='default',required=False, help_text=_("Add description"))
    background_image = ImageChooserBlock() 
    points = blocks.ListBlock(PointBlock(), 
                              label="Add points", 
                              help_text="Add multiple pointsd")
    
    class Meta:
        icon = "image"
        label = _("Section Card Block Four")

class BaseImageTextCardBlockFive(blocks.StructBlock):
    name = blocks.CharBlock(required=True, help_text=_("Add Name of teachers"))
    domain = blocks.CharBlock(required=True, help_text=_("domain"))
    image = ImageChooserBlock(required=True) 

    class Meta:
        # template = "blocks/text_block_with_links.html"
        icon = "image"
        label = "Base Image Text Card Block Five"
class ImageTextCardBlockWithLinksFive(BaseImageTextCardBlockFive):
    links = blocks.ListBlock(
        LinkBlock(),
        min_num=0,
        max_num=2,
        help_text=_("Add button/link information to this section"),
        label="Add link details"
    )

    class Meta:
        # template = "blocks/text_block_with_links.html"
        icon = "doc-full"
        label = "Image Text Card Block with Links"


class SocialMediaLinkBlock(blocks.StructBlock):
    platform = blocks.ChoiceBlock(choices=SOCIAL_MEDIA_CHOICES, required=True, help_text=_("Select the social media platform"))
    url = blocks.URLBlock(required=True, help_text=_("Enter the URL of the social media profile"))

    class Meta:
        # template = "blocks/text_block_with_links.html"
        icon = "doc-full"
        label = "Image Text Card Block with social media"
class socialMediaListBlock(BaseImageTextCardBlockFive):
    icons = blocks.ListBlock(
        SocialMediaLinkBlock(),
        min_num=0,
        max_num=3,
        help_text=_("Add button/link information to this section"),
        label="Add link details"
    )

    class Meta:
        # template = "blocks/text_block_with_links.html"
        icon = "doc-full"
        label = "Image Text Card Block with Links"
class SectionFiveCardBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text=_("Add your heading"))  
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add sub heading"))
    card_count = blocks.ChoiceBlock(max_length=20, choices=CARD_CHOICES,  null=True, blank=True, default="3", help_text=_("Number of cards"))
    background = blocks.ChoiceBlock(max_length=50, choices=BG_CHOICES,  null=True, blank=True, default="transparent", help_text=_("Block Backgound"))
    top_padding = blocks.ChoiceBlock(max_length=50, choices=TOP_PADDING_CHOICES,  null=True, blank=True, default="big", help_text=_("Top padding"))
    bottom_padding = blocks.ChoiceBlock(max_length=50, choices=BOTTOM_PADDING_CHOICES,  null=True, blank=True, default="big", help_text=_("Bottom padding"))      
    points = blocks.ListBlock(ImageTextCardBlockWithLinksFive(), 
                              label="Add image card", 
                              help_text="Add multiple image cards to this section. The image alignment is at the top.")
    social_media = blocks.ListBlock(
        socialMediaListBlock(),
        help_text=_("Add the social media platforms and URLs you want to display.")
    )
    
    class Meta:
        icon = "image"
        label = _("Section Card Block Five")
#section 7 start
class BaseImageTextCardBlockslider(blocks.StructBlock):
    client_name = blocks.CharBlock(required=True, help_text=_("Add your heading"))
    profession = blocks.CharBlock(required=True, help_text=_("Add your heading"))
    image = ImageChooserBlock(required=True) 
    description  = blocks.RichTextBlock(editor='default',required=False, help_text=_("Add description"))

    class Meta:
        # template = "blocks/text_block_with_links.html"
        icon = "image"
        label = "Base Image Text Card Block"
class FullImageTextCardBlock(BaseImageTextCardBlockslider):
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add sub heading"))
    links = blocks.ListBlock(
        LinkBlock(),
        min_num=0,
        max_num=2,
        help_text=_("Add button/link information to this section"),
        label="Add link details"
    )

    class Meta:
        # template = "blocks/full_text_block.html"
        icon = "image"
        label = "Full Image Text Card Block"
class CircleSwiperBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=False, help_text=_("Add your heading"))
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add sub heading"))
    background = blocks.ChoiceBlock(max_length=50, choices=BG_CHOICES,  null=True, blank=True, default="transparent", help_text=_("Block Backgound"))
    top_padding = blocks.ChoiceBlock(max_length=50, choices=TOP_PADDING_CHOICES,  null=True, blank=True, default="big", help_text=_("Top padding"))
    bottom_padding = blocks.ChoiceBlock(max_length=50, choices=BOTTOM_PADDING_CHOICES,  null=True, blank=True, default="big", help_text=_("Bottom padding"))      
    points = blocks.ListBlock(FullImageTextCardBlock(),label="Add circle card", help_text="Add circled cards to this section")

    class Meta:
        icon = "sliders"
        label = _("Circle Swiper")


#section 8


class BaseImageTextCardBlockEight(blocks.StructBlock):
    date = blocks.DateTimeBlock(required=True, help_text=_("date section"))
    image = ImageChooserBlock(required=True) 
    description  = blocks.RichTextBlock(editor='default',required=False, help_text=_("Add description"))

    class Meta:
        # template = "blocks/text_block_with_links.html"
        icon = "image"
        label = "Base Image Text Card Block eight"
class ImageTextCardBlockWithLinksEight(BaseImageTextCardBlockEight):
    links = blocks.ListBlock(
        LinkBlock(),
        min_num=0,
        max_num=2,
        help_text=_("Add button/link information to this section"),
        label="Add link details"
    )

    class Meta:
        # template = "blocks/text_block_with_links.html"
        icon = "doc-full"
        label = "Image Text Card Block with Links"
class SectionEightCardBlock(blocks.StructBlock):
    heading = blocks.CharBlock(required=True, help_text=_("Add your heading"))  
    sub_heading = blocks.CharBlock(required=False, help_text=_("Add sub heading"))
    card_count = blocks.ChoiceBlock(max_length=20, choices=CARD_CHOICES,  null=True, blank=True, default="3", help_text=_("Number of cards"))
    background = blocks.ChoiceBlock(max_length=50, choices=BG_CHOICES,  null=True, blank=True, default="transparent", help_text=_("Block Backgound"))
    top_padding = blocks.ChoiceBlock(max_length=50, choices=TOP_PADDING_CHOICES,  null=True, blank=True, default="big", help_text=_("Top padding"))
    bottom_padding = blocks.ChoiceBlock(max_length=50, choices=BOTTOM_PADDING_CHOICES,  null=True, blank=True, default="big", help_text=_("Bottom padding"))      
    points = blocks.ListBlock(ImageTextCardBlockWithLinksEight(), 
                              label="Add image card", 
                              help_text="Add multiple image cards to this section. The image alignment is at the top.")
    
    class Meta:
        icon = "image"
        label = _("Section Card Block Eight")

