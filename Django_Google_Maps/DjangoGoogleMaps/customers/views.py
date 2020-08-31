from django.http import HttpResponse
from django.core import serializers
from customers.models import Customers

def allCustomers(self):
    
    allData = Customers.objects.all()
    
    response = serializers.serialize('json', allData)
    
    return HttpResponse(response, content_type="text/json-comment-filtered")
    
def customerByID(self,_id):
    
    customer = Customers.objects.all().filter(id=_id)
    
    response = serializers.serialize('json', customer)
    
    return HttpResponse(response, content_type="text/json-comment-filtered")

    
