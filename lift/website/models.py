from django.db import models
from django.db.models.fields import AutoField

# Create your models here.


class Pipes(models.Model):
    
   


    #frontend
    length = models.input_form   #find out how to define a input range
    material = MATERIAL_CHOICES = [ #double check this form input syntax
    ('pvc', '.09'), #ROUGHNESS
    ('copper', '.01'),
    ('carbon_steel', '.1'),
    ('carbon_steel', '.1'),
    ('carbon_steel', '.1'),
    ('carbon_steel', '.1'),
    ('carbon_steel', '.1'),
    ]

    diameter = DIAMETER_CHOICES = [
    ('pvc', '.75'), #DIAMETER IN INCHES  #determine how to make choices integers
    ('copper', '1'),
    ('carbon_steel', '3'),
    ('carbon_steel', '4'),
    ('carbon_steel', '6'),
    ('carbon_steel', '8'),
    ('carbon_steel', '10'),
    ('carbon_steel', '12'),
    ('carbon_steel', '16'),
    ('carbon_steel', '18'),
    ('carbon_steel', '24'),
    ('carbon_steel', '30'),
    ]


    schedule = [
          ('carbon_steel', '3'),
    ('schedule 40', '1'),
    ('schedule 40', '1'),
    ('schedule 40', '1'),
    ('schedule 40', '1'),
    ('schedule 40', '1'),
    ('schedule 40', '1'),
    ('schedule 40', '1'),
    ('schedule 40', '1'),
    ('schedule 40', '1'),
    ]


     #backend
    
    #need to learn how to call object from db and use its attributes/methods
    
    name = f"{diameter} + {material} pipe" #this is fine


    def __str__(self):
        return self.name

