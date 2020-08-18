from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from customers.models import Customers

# Create your views here.

def allCustomers(self):
    
    allData = Customers.objects.all()
    
    response = serializers.serialize('json', allData)
    
    return HttpResponse(response, content_type="text/json-comment-filtered")
    
def CustomerByID(self,_id):
    
    customer = Customers.objects.all().filter(id=_id)
    
    response = serializers.serialize('json', customer)
    
    return HttpResponse(response, content_type="text/json-comment-filtered")
    
