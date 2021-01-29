from django.db import models
from datetime import datetime
class Product(models.Model):

          x=[
          ("phone","phone"),
          ("computer","computer"),
             ]
    
          name = models.CharField(max_length=25,verbose_name="title")
          content = models.TextField()
          price= models.DecimalField(max_digits=6, decimal_places=3)
          image = models.ImageField(upload_to="photos/%y/%m/%d",blank=True, null=True)
          active = models.BooleanField(default=True)
          category=models.CharField(max_length=100,null=True,blank=True,choices=x)
          
          def __str__(self):
                    return self.name
          
          class Meta:
                    ordering=["name"]
                    
class Test(models.Model):
          data=models.DateField()
          time=models.TimeField(null=True)
          created=models.DateTimeField(default=datetime.now)
          


          
          
          
