
from django.core.management.base import BaseCommand
import csv
import os
import json
from django.apps import apps
from customers.models import Customers
import requests

class Command(BaseCommand):
    
    def getGEO(self, city, state):
        
        GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
        
        googleLink = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + city + '+' + state + '&key=' + GOOGLE_API_KEY
        
        response = requests.post(googleLink)
            
        data = json.loads(response.text)
        result = {}
        result["latitude"] = data["results"][0]["geometry"]["location"]["lat"]
        result["longitude"] = data["results"][0]["geometry"]["location"]["lng"]
        
        return result
        
        
    def handle(self, *args, **kwargs):

        PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
        reader = csv.DictReader(open(PROJECT_ROOT + '\customers.csv'))
        
        customers = list(reader)
        
        for i in range(len(customers)):
            
            if (i % 100 == 0):
                print(str(i) + ' GEO coordinates downloaded')
        
            row = dict(customers[i])
            
            customersGEO = Customers()
            customersGEO.id = row["id"]
            customersGEO.first_name = row["first_name"]
            customersGEO.last_name = row["last_name"]
            customersGEO.email = row["email"]
            customersGEO.gender = row["gender"]
            customersGEO.company = row["company"]
            customersGEO.city = row["city"]
            customersGEO.title = row["title"]
            
            location = row["city"].split(',')
            result = self.getGEO(location[0], location[1])
            
            customersGEO.latitude = result["latitude"]
            customersGEO.longitude = result["longitude"]
            
            customersGEO.save()
            
            
            

       
