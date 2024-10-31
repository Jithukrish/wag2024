# from wagtail.snippets.views.snippets import SnippetViewSet
# from wagtail.admin.ui.tables import UpdatedAtColumn
# from wagtail.snippets.models import register_snippet
# from wagtail import hooks
# from django.core.cache import cache

# from .models import  FooterSnippet


# class FooterViewSet(SnippetViewSet):
#     model = FooterSnippet
#     icon = "crosshairs"
#     menu_label = "Footer"
#     menu_name = "footer"
#     menu_order = 216
#     add_to_admin_menu = True
#     list_display = ('name',  'locale')
#     list_filter = ('locale',)

    

# register_snippet(FooterViewSet)