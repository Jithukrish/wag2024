from rest_framework import serializers
from .models import CurriculamPage
from wagtail.images.api.fields import ImageRenditionField
from wagtail.blocks.stream_block import StreamValue
from Course.serializers import CoursePageSerializer


class lessonBlockListSerializer(serializers.Serializer):
    title = serializers.CharField()
    video = serializers.URLField()
class lessonsBlockSerializer(serializers.Serializer):
    title = serializers.CharField()
    lessons_count = serializers.CharField()
    lessons_name = lessonBlockListSerializer(many=True)


    def to_representation(self, instance):
        return {
            # 'lessons_name': [{'lessons': lessons['lessons']} for lessons in instance['lessons_name']],
            # 'lessons_name': [lesson for lesson in instance['lessons_name']],
            'title': instance['title'],
            'lessons_count': instance['lessons_count'],
            'lessons_name': [lessonBlockListSerializer(lesson).data for lesson in instance['lessons']],
            
        }

class VideoSessionBlockSerializer(serializers.Serializer):
    lessons = lessonsBlockSerializer(many=True)
    def to_representation(self, instance):
        return {
            # 'lessons': [lessons_block for lessons_block in instance['lessons']],
            'lessons': [lessonsBlockSerializer(lesson).data for lesson in instance['lessons']],  # Serialize each lessons block
        }

class CurriculamPageSerializer(serializers.ModelSerializer):
    course = serializers.SerializerMethodField(read_only=True)
    video = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CurriculamPage
        fields = ['id','slug','course', 'video']

    def get_video(self, obj):
        video_data = []
        for block in obj.video:
            if block.block_type == 'videosession':
                video_data.append(VideoSessionBlockSerializer().to_representation(block.value))
                # video_data.append(VideoSessionBlockSerializer(block.value).data)
        return video_data

    def get_course(self, obj):
        return CoursePageSerializer(obj.course).data if obj.course else None
   
    
class CurriculamPageDetailSerializer(CurriculamPageSerializer):
    class Meta:
        model = CurriculamPage
        fields = ['id','slug','course', 'video']                  
          
                
