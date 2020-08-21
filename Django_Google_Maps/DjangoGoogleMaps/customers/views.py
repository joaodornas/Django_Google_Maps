import datetime

from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.response import Response

from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from customers.models import Customers

from drf_yasg import openapi
from drf_yasg.app_settings import swagger_settings
from drf_yasg.inspectors import CoreAPICompatInspector, FieldInspector, NotHandled, SwaggerAutoSchema
from drf_yasg.utils import no_body, swagger_auto_schema

from rest_framework.decorators import action

# Create your views here.

class DjangoFilterDescriptionInspector(CoreAPICompatInspector):
    def get_filter_parameters(self, filter_backend):
        if isinstance(filter_backend, DjangoFilterBackend):
            result = super(DjangoFilterDescriptionInspector, self).get_filter_parameters(filter_backend)
            for param in result:
                if not param.get('description', ''):
                    param.description = "Filter the returned list by {field_name}".format(field_name=param.name)

            return result

        return NotHandled
 
class NoSchemaTitleInspector(FieldInspector):
    def process_result(self, result, method_name, obj, **kwargs):
        # remove the `title` attribute of all Schema objects
        if isinstance(result, openapi.Schema.OR_REF):
            # traverse any references and alter the Schema object in place
            schema = openapi.resolve_ref(result, self.components)
            schema.pop('title', None)

            # no ``return schema`` here, because it would mean we always generate
            # an inline `object` instead of a definition reference

        # return back the same object that we got - i.e. a reference if we got a reference
        return result
    
class NoTitleAutoSchema(SwaggerAutoSchema):
    field_inspectors = [NoSchemaTitleInspector] + swagger_settings.DEFAULT_FIELD_INSPECTORS
    
class NoPagingAutoSchema(NoTitleAutoSchema):
    def should_page(self):
        return False

class CustomersViewSet(viewsets.ModelViewSet):
    
    queryset = Customers.objects.all()
    
    swagger_schema = NoTitleAutoSchema
    
    @swagger_auto_schema(auto_schema=swagger_schema, filter_inspectors=[DjangoFilterDescriptionInspector])
    @action(detail=False, methods=['get'])
    def allCustomers(self,request):
    
        allData = Customers.objects.all()
    
        response = serializers.serialize('json', allData)
    
        return HttpResponse(response, content_type="text/json-comment-filtered")
    
    id_param = openapi.Parameter('_id', openapi.IN_QUERY, description="customer id", type=openapi.TYPE_INTEGER)
    @swagger_auto_schema(method='get', manual_parameters=[id_param])
    @action(detail=False, methods=['get'])
    def customerByID(self,request,_id):
    
        customer = Customers.objects.all().filter(id=_id)
    
        response = serializers.serialize('json', customer)
    
        return HttpResponse(response, content_type="text/json-comment-filtered")

    
