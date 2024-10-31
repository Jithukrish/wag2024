from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.ui.tables import UpdatedAtColumn
from wagtail.snippets.models import register_snippet
from wagtail import hooks
from django.core.cache import cache

from .models import  CoursePage


class CourseViewSet(SnippetViewSet):
    model = CoursePage
    icon = "crosshairs"
    menu_label = "Course"
    menu_name = "Course"
    menu_order = 216
    add_to_admin_menu = True
    list_display = ('course_title',  'locale')
    list_filter = ('locale',)

    

register_snippet(CourseViewSet)