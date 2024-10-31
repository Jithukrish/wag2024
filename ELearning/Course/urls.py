from django.urls import path
from .api import CourseViewSet

urlpatterns = [
    path('', CourseViewSet.as_view({'get': 'list'}), name='course-list'),
    path('<slug:slug>/', CourseViewSet.as_view({'get': 'retrieve'}), name='course-detail'),
]