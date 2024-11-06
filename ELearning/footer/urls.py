from django.urls import path
from .api import FooterSnippetViewSet

urlpatterns = [
    path('', FooterSnippetViewSet.as_view({'get': 'list'}), name='course-list'),
    path('<slug:slug>/', FooterSnippetViewSet.as_view({'get': 'retrieve'}), name='course-detail'),
    # path('footer/', FooterSnippetViewSet.as_view({'get': 'retrieve'}), name='course-detail'),
]