from rest_framework import serializers
from .models import CoursePage
# from Products.blocks import ProductBlock
from wagtail.images.api.fields import ImageRenditionField
from wagtail.blocks.stream_block import StreamValue


class KeytopicsBlockSerializer(serializers.Serializer):
    topic = serializers.CharField()
class BodyBlockSerializer(serializers.Serializer):
    key_topic = KeytopicsBlockSerializer(many=True)
    instructor = serializers.CharField()
    link = serializers.URLField()

    def to_representation(self, instance):
        return {
            'key_topic': [{'topic': topic['topic']} for topic in instance['key_topic']],
            'instructor': instance['instructor'],
            'link': instance['link'],
        }
class LevelBlockSerializer(serializers.Serializer):
    choices = serializers.ListField(child=serializers.CharField())
    def to_representation(self, instance):
        return {
            'level': instance,
        }

class CoursePageSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField(read_only=True)
    levels = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CoursePage
        fields = ['id','slug','course_title', 'category', 'course_week','student_count','course_description','content','levels']

    def get_content(self, obj):
        content_data = []
        for block in obj.content:
            if block.block_type == 'Body':
                content_data.append(BodyBlockSerializer().to_representation(block.value))
        return content_data

    def get_levels(self, obj):
        levels_data = []
        for block in obj.levels:
            if block.block_type == 'level':
                levels_data.append(LevelBlockSerializer().to_representation(block.value))
        return levels_data
    
class CoursePageDetailSerializer(CoursePageSerializer):
    class Meta:
        model = CoursePage
        fields = ['id','slug','course_title', 'category', 'course_week','student_count','course_description']  
                  
          
                
