from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import FooterSnippetDetailSerializer,FooterSnippetSerializer
from django.shortcuts import get_object_or_404
from wagtail.models import Locale
from django.utils.translation import get_language_from_request
from .models import FooterSnippet
from django.core.cache import cache
from ELearning.constants import FOOTER_CACHE_TIMEOUT

class FooterSnippetViewSet(viewsets.ModelViewSet):
    serializer_class = FooterSnippetSerializer
    def get_serializer_class(self):
        group_serializer = {
            'list': FooterSnippetSerializer,
            'retrieve': FooterSnippetDetailSerializer,
            # 'related': WorkshopPageSerializer,
        }

        serializer_class = group_serializer.get(self.action, None)
        if serializer_class is None:
            raise ValueError(f"No serializer found for action: {self.action}")
        return serializer_class
    def get_queryset(self):
        lang = get_language_from_request(self.request)
        locale = get_object_or_404(Locale, language_code=lang)
        # return FooterSnippet.objects.live().exact_type(FooterSnippet).filter(locale=locale)
        return FooterSnippet.objects.filter(locale=locale)
    
    def list(self, request, *args, **kwargs):
        response ={}
        try:           
            querysets = self.get_queryset()   
            serializer = self.get_serializer(querysets, many=True, context={'request': request})
            response['result'] = 'success'
            response['records'] = serializer.data
        except Exception as e:
            response['result'] = 'failure'
            response['message'] = str(e)    
        return Response(response, status=status.HTTP_200_OK)
    def retrieve(self, request, *args, **kwargs):
        response = {}
        try:
        
            slug = kwargs.get('slug')
            
            lang = get_language_from_request(request)
            locale = get_object_or_404(Locale, language_code=lang)
            
            # queryset = FooterSnippet.objects.live().exact_type(FooterSnippet).filter(locale=locale)
            queryset = FooterSnippet.objects.filter(locale=locale)
            
            service_page = get_object_or_404(queryset, slug=slug)
            
            serializer = self.get_serializer(service_page, context={'request': request})
            
            response['result'] = 'success'
            response['records'] = serializer.data
        except Exception as e:
            response['result'] = 'failure'
            response['message'] = str(e)
        return Response(response, status=status.HTTP_200_OK)

