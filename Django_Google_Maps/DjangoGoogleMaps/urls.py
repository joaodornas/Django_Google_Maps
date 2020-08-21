"""DjangoGoogleMaps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from customers import views
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import SimpleRouter

schema_view = get_schema_view(
  validators=['ssv', 'flex'],
  public=True,
  permission_classes=(permissions.AllowAny,),
)

swagger_info = openapi.Info(
     title="Snippets API",
     default_version='v1',
     description="Description",
     terms_of_service="https://www.google.com/policies/terms/",
     contact=openapi.Contact(email="contact@snippets.local"),
     license=openapi.License(name="BSD License"),
)

app_name = 'customers'

router = SimpleRouter()
router.register('', views.CustomersViewSet)

urlpatternsCustomers = [
    url(r'^', include(router.urls)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('customers/', views.allCustomers, name = 'All Customers'),
    #path('customer/<int:_id>/', views.CustomerByID, name = 'Specific Customer'),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
] + urlpatternsCustomers
