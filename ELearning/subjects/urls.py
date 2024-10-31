from django.urls import path
from .api import CurriculumViewSet

urlpatterns = [
    path('', CurriculumViewSet.as_view({'get': 'list'}), name='curriculum-list'),
    path('<slug:slug>/', CurriculumViewSet.as_view({'get': 'retrieve'}), name='curriculum-detail'),
]