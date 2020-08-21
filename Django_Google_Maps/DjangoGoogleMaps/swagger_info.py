from drf_yasg import openapi

swagger_info = openapi.Info(
     title="Snippets API",
     default_version='v1',
     description="Description",
     terms_of_service="https://www.google.com/policies/terms/",
     contact=openapi.Contact(email="contact@snippets.local"),
     license=openapi.License(name="BSD License"),
)