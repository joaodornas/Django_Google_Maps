import graphene
from graphene_django import DjangoObjectType

from customers.models import Customers

class CustomerType(DjangoObjectType):
    class Meta:
        model = Customers
        fields = ("id", "first_name", "last_name", "email", "gender", "company", "city", "title", "latitude", "longitude")

class Query(graphene.ObjectType):
    all_customers = graphene.List(CustomerType)
    customer_by_id = graphene.Field(CustomerType, id=graphene.Int(required=True))
    
    def resolve_all_customers(root, info):
        
        return Customers.objects.all()
    
    def resolve_customer_by_id(root, info, id):
        try:
            return Customers.objects.get(id=id)
        except Customers.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)