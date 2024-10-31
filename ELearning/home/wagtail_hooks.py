from wagtail.admin.viewsets.pages import PageListingViewSet
from wagtail.admin.views.pages.create import CreateView
from wagtail.admin.views.pages.edit import EditView
from django.urls import path, reverse
from wagtail import hooks
from wagtail.admin.ui.tables import Column

from .models import HomePage

class HomePageCreateView(CreateView):
    pass

class HomePageEditView(EditView):
    pass

class HomePageViewSet(PageListingViewSet):
    model = HomePage
    icon = 'home'
    menu_label = 'Home Page'
    menu_order = 190
    add_to_settings_menu = False
    exclude_from_explorer = False
    add_to_admin_menu = True
    list_display = ('title', 'status_string')
    search_fields = ('title',)
    columns = PageListingViewSet.columns + [
        Column("locale", label="Locale", sort_key="locale"),
    ]

    create_view_class = HomePageCreateView
    edit_view_class = HomePageEditView

    def get_urlpatterns(self):
        urlpatterns = super().get_urlpatterns()
        return urlpatterns + [
            path('create/', self.create_view_class, name='create'),
            path('<int:page_id>/edit/', self.edit_view_class, name='edit'),
        ]

@hooks.register('register_admin_viewset')
def register_trading_page_viewset():
    return HomePageViewSet('home_page')