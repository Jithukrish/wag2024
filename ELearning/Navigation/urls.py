from django.urls import path
from .api import NavigationSnippetViewSet

urlpatterns = [
    path('', NavigationSnippetViewSet.as_view({'get': 'list'}), name='navigation-list'),
    path('<slug:slug>/', NavigationSnippetViewSet.as_view({'get': 'retrieve'}), name='navigation-detail'),
    # path('footer/', FooterSnippetViewSet.as_view({'get': 'retrieve'}), name='course-detail'),
]