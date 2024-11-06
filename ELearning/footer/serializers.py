from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from wagtail.images.api.fields import ImageRenditionField
from wagtail.blocks.stream_block import StreamValue
from Navigation.models import SingleMenuBlock,MenuItemBlock
from wagtail import blocks
from wagtail.blocks import ListBlock, StructBlock
from wagtail.blocks.list_block import ListValue
from wagtail.blocks.struct_block import StructValue
# from wagtail.blocks.values import  StructValue 
from wagtail.blocks import ChoiceBlock
from wagtail.models import Page
from .models import FooterSnippet


class RightBlockSerializer(serializers.Serializer):
    heading = serializers.CharField()
    description = serializers.CharField()

    def to_representation(self, instance):
        return {
            'heading': instance.get('heading'), 
            'description': str(instance.get('description', '')),
        }
    
class MenuItemBlockSerializer(serializers.Serializer):
    title = serializers.CharField()
    link_type = serializers.ChoiceField(choices=[
        ('internal', 'Internal Page'),
        ('external', 'External URL'),
    ])
    internal_page = serializers.PrimaryKeyRelatedField(queryset=Page.objects.live(), required=False)
    tab_key = serializers.CharField(required=False)
    external_url = serializers.URLField(required=False)
    internal_page_model_name = serializers.CharField(required=False)
   
    def to_representation(self, instance):
        return {
            'title': instance.get('title'), 
            'link_type': instance.get('link_type'),
            'internal_page': instance.internal_page.id if instance.internal_page else None,
            'tab_key': instance.get('tab_key'),
            'external_url': instance.get('external_url'),
            'internal_page_model_name': instance.get('internal_page_model_name'),
        }
    
MENU_TYPE = [
	    ('text', _('Text Menu'),),
        ('bordered_button', _('Bordered Button Menu'),),
        ('filled_button', _('Filled Button Menu'),),
    ]

class SingleMenuBlockSerialzer(serializers.Serializer):
    title = serializers.CharField()
    menu_type = serializers.ChoiceField(choices=MENU_TYPE)
    menu_item = MenuItemBlockSerializer(many=True)
    
    def to_representation(self, instance):
        return {
            'title': instance.get('title'), 
            'menu_type': instance.get('menu_type'),
            'menu_items': [MenuItemBlockSerializer(menu_item).data for menu_item in instance.get('menu_item', [])],
        }
class MiddleBlockSerializer(serializers.Serializer):
    heading = serializers.CharField()
    menu_items = SingleMenuBlockSerialzer(many=True)
 
    def to_representation(self, instance):
        menu_list = []
        if isinstance(instance, ListValue):
            for item in instance:
                if isinstance(item, StructValue): 
                    menu_items = item.get('menu_items', None)
                    if isinstance(menu_items, ListValue):
                        for menu_item in menu_items:
                            if isinstance(menu_item, StructValue): 
                                try:
                                    nested_menu_item =menu_item.get('menu_item', None)
                                    # print("nested_menu_item -----------",nested_menu_item)
                                    if isinstance(nested_menu_item,StructValue):
                                        nested_serialized  = SingleMenuBlockSerialzer(nested_menu_item).data
                                        # print("nested_serialized:", nested_serialized) 
                                        serialized_data = {
                                            'title': menu_item.get('title', ''),
                                            'menu_type': menu_item.get('menu_type', ''),
                                            'menu_items': nested_serialized
                                        }
                                    # print("Serialized menu item data:", serialized_data)  
                                    menu_list.append(serialized_data)
                                except Exception as e:
                                    print("Error during serialization:",e)
                    else:
                        print("'menu_items' is not a ListValue:", menu_items)
                else:
                    print("Current item is not a StructValue:", item)
        else:
            print("Instance is not a ListValue or StreamValue.")  
        return {'menu_list': menu_list}
class SocialMediaLinkBlockSerializer(serializers.Serializer):
    platform = serializers.CharField()
    url = serializers.URLField()
 
    def to_representation(self, instance):
        # print("Debug: SocialMediaLinkBlock instance:", instance)  
        return {
            'platform': instance.get('platform', ''),  
            'url': instance.get('url', ''),
        }


class socialMediaListBlockSerializer(serializers.Serializer):
    icons = SocialMediaLinkBlockSerializer(many=True)

    def to_representation(self, instance):

        icons_list = []

        if isinstance(instance, ListValue):
            for item in instance:
                if isinstance(item, dict) and 'icons' in item:
                    icons = item['icons']
                    icons_list.extend(SocialMediaLinkBlockSerializer(icons, many=True).data)

        elif isinstance(instance, StreamValue):
            for block in instance:
                block_type, block_value = block  
                if block_type == 'social_media_list': 
                    icons = block_value.get('icons', [])
                    icons_list.extend(SocialMediaLinkBlockSerializer(icons, many=True).data)

        else:
            print("Instance is not a ListValue or StreamValue.")  

        return {'icons': icons_list}






      

class ContactBlockSerializer(serializers.Serializer):
    heading = serializers.CharField()
    street = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField()
    social_media = socialMediaListBlockSerializer()
    right_part = RightBlockSerializer()
    Middle_block =MiddleBlockSerializer()
 
    def to_representation(self, instance):
        # social_media_data = instance.get('social_media', [])
        # print("Debug social media data:", social_media_data)
        return {
            'heading': instance.get('heading', ''),  
            'street': instance.get('street', ''),
            'phone': instance.get('phone', ''),
            'email': instance.get('email', ''),
            # 'social_media': self.fields['social_media'].to_representation(social_media_data),
            # 'social_media': self.fields['social_media'].to_representation(instance.get('social_media')),
            'social_media': self.fields['social_media'].to_representation(instance.get('social_media', [])),
            'right_part': self.fields['right_part'].to_representation(instance.get('right_part')),
            'Middle_block': self.fields['Middle_block'].to_representation(instance.get('Middle_block', [])),
        }

class FooterSnippetSerializer(serializers.ModelSerializer): 
    name = serializers.CharField()
    copyright = serializers.CharField()
    content = serializers.SerializerMethodField(read_only=True)
   

    class Meta:
        model = FooterSnippet
        fields = ['id','name', 'copyright', 'content']


  
    def get_content(self, obj):
        content_data = []
        if isinstance(obj.content, StreamValue):
            for block in obj.content:
                # print(f"Block Type: {block.block_type}")  
                if block.block_type == 'contact_info':
                    contact_data = ContactBlockSerializer().to_representation(block.value)
                    # print("Contact Block Data:", contact_data)  
                    content_data.append(contact_data)
        return content_data

  
class FooterSnippetDetailSerializer(FooterSnippetSerializer):
    class Meta:
        model = FooterSnippet
        fields = ['id','name', 'copyright', 'content']  
                  
          
                
