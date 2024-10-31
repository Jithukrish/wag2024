from wagtail.snippets.views.snippets import SnippetViewSet
from wagtail.admin.ui.tables import UpdatedAtColumn
from wagtail.snippets.models import register_snippet
from wagtail import hooks
from django.core.cache import cache

from .models import  CurriculamPage


class CurriculamViewSet(SnippetViewSet):
    model = CurriculamPage
    icon = "crosshairs"
    menu_label = "Curriculam"
    menu_name = "Curriculam"
    menu_order = 216
    add_to_admin_menu = True
    list_display = ('name',  'locale')
    list_filter = ('locale',)

    

register_snippet(CurriculamViewSet)