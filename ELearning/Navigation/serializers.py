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
from .models import NavigationSnippet
from ELearning.constants import API_URLS
from Course.models import CoursePage 
from django.db.models import F

def get_api_urls(key):
   
    for item in API_URLS:
        if item[0] == key:
            return item[1]
    return None  
class MenuItemBlockSerializer(serializers.Serializer):
    title = serializers.CharField()
    link_type = serializers.ChoiceField(choices=[
        ('internal', 'Internal Page'),
        ('external', 'External URL'),
    ])
    internal_page = serializers.PrimaryKeyRelatedField(
        queryset=Page.objects.live(),
        required=False,
        allow_null=True
    )
    tab_key = serializers.CharField(required=False)
    external_url = serializers.URLField(required=False)
    internal_page_model_name = serializers.CharField(required=False)
    # link = serializers.Seri   alizerMethodField(read_only=True)

    def to_representation(self, instance):
        if isinstance(instance, dict):#to remove  "message": "'str' object has no attribute 'get'" this issue 
            return {
                'title': instance.get('title'), 
                'link_type': instance.get('link_type'),
                'internal_page': instance.get('internal_page'),
                'tab_key': instance.get('tab_key'),
                'external_url': instance.get('external_url'),
                # 'internal_page_model_name': instance.get('internal_page_model_name'),
            } 
        return {}
    # def get_link(self, obj):
    #     if obj.link_type == 'internal' and obj.internal_page:
    #         return obj.internal_page.get_url()  
    #     elif obj.link_type == 'external':
    #         return obj.external_url
    #     return None
       


class TabBlockSerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.CharField()
    menu_items = MenuItemBlockSerializer()
   
    def to_representation(self, instance):
        if isinstance(instance, dict):
            return {
                'title': instance.get('title'), 
                'slug': instance.get('slug'),
                'menu_items': instance.get('menu_items'),
            }
        return {}
class SingleMenuBlockSerializer(serializers.Serializer):
    MENU_TYPE = [
	    ('text', _('Text Menu'),),
        ('bordered_button', _('Bordered Button Menu'),),
        ('filled_button', _('Filled Button Menu'),),
    ]
    title = serializers.CharField()
    menu_type = serializers.ChoiceField(choices=MENU_TYPE)
    menu_item = MenuItemBlockSerializer(many =True)
    def to_representation(self, instance):
        if isinstance(instance, StructValue):
            menu_items_data = []
            menu_item = instance.get('menu_item')
            if isinstance(menu_item, StructValue):
                menu_items_data.append(MenuItemBlockSerializer(menu_item).data)
            return {
                'title': instance.get('title'), 
                'menu_type': instance.get('menu_type'),
                'menu_items': menu_items_data,
            }
        return {}
class MultipleMenuBlockSerializer(serializers.Serializer):
    MENU_TYPE = [
	    ('text', _('Text Menu'),),
        ('bordered_button', _('Bordered Button Menu'),),
        ('filled_button', _('Filled Button Menu'),),
    ]
    title = serializers.CharField()
    menu_type = ChoiceBlock(choices=MENU_TYPE)
    menu_item = MenuItemBlockSerializer(many=True)
    def to_representation(self, instance):
        if isinstance(instance, dict):
            return {
                'title': instance.get('title'), 
                'menu_type': instance.get('menu_type'),
                'menu_items': [MenuItemBlockSerializer(menu_item).data for menu_item in instance.get('menu_item', [])],
            }
        return {}

class TabbedMenuBlockSerializer(serializers.Serializer):
    title = serializers.CharField()
    tabs = TabBlockSerializer(many=True)
    def to_representation(self, instance):
        if isinstance(instance, dict):
            return {
                'title': instance.get('title'), 
                # 'menu_type': instance.get('menu_type'),
                'tabs': [TabBlockSerializer(tabs).data for tabs in instance.get('tabs', [])],
            }
        return {}

class NavigationSnippetSerializer(serializers.ModelSerializer):
    NAV_TYPE = [
	    ('header', _('Header Navigation'),),
        ('footer', _('Footer Navigation'),),
        ('footer_links', _('Footer Links'),),
    ] 
    name = serializers.CharField()
    nav_type = serializers.ChoiceField(choices=NAV_TYPE)
    menus = serializers.SerializerMethodField(read_only=True)
   

    class Meta:
        model = NavigationSnippet
        fields = ['id','name', 'nav_type', 'menus']


  
    def get_menus(self, obj):
        content_data = []
        if isinstance(obj.menus, StreamValue):
            for block in obj.menus:
                # print("Block Type:", block.block_type) 
                # print("Block Value:", block.value)  
                if block.block_type == 'single_menu':
                    single_data = SingleMenuBlockSerializer().to_representation(block.value)
                    # print("single_data Data:", single_data) 
                    # single_data.append(content_data)
                    content_data.append(single_data)
                elif block.block_type == 'multiple_menu':
                    multiple_data = MultipleMenuBlockSerializer().to_representation(block.value)
                    # print("multiple_data Data:", multiple_data) 
                    # multiple_data.append(content_data)
                    content_data.append(multiple_data)

                elif block.block_type == 'tabbed_menu':
                    tabbed_data = TabbedMenuBlockSerializer().to_representation(block.value)
                    # print("tabbed_data Data:", tabbed_data) 
                    # tabbed_data.append(content_data)
                    content_data.append(tabbed_data)

        return content_data

  
class NavigationSnippetDetailSerializer(NavigationSnippetSerializer):
    class Meta:
        model = NavigationSnippet
        fields = ['id','name', 'nav_type', 'menus']
                  
          
                
