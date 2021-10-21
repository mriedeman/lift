from django.db import models


# Create your models here.


class Pipes(models.Model):
    
    #hazen-williams equation
    #pipe_length (feet)
    #flow_rate (gal/min)
    #inner diamter (inches)


    #PIPE_LENGTH

    pipe_length = models.DecimalField(max_digits = 8, decimal_places=2)


    MATERIALS =  [
        (140, 'Brass'),
        (140, 'Copper'),
        (140, 'Aluminum'),
        (140, 'PE'),
        (150, 'PVC'),
        (130, 'Cast Iron'),
        (100, 'Galvanized Iron'),
        (120, 'Bituminous Iron'),
        (120, 'Welded Steel'),
        (110, 'Riveted Steel'),
        (130, 'Concrete'),
        (120, 'Wood'),
]
    material = models.CharField(max_length = 100, choices = MATERIALS, default = 'Aluminum')

    inner_diameter = models.DecimalField(max_digits = 8, decimal_places=2)
    
    LINE = [
        ('suc', 'Suction'),
        ('dis', 'Discharge')
    ]

    line_type = models.CharField(max_length = 100, choices = LINE, default = 'dis')
    
    name = f"{inner_diameter} {material} pipe" 


    def __str__(self):
        return self.name

class Valves(models.Model):

    size = models.FloatField(blank=False)

    VALVES =  [ #CERM Reference values, may be copyrighted update later 
        (5, 'Angle'),
        ('''45.00* size''', 'Butterfly 2-8"'), #Can we reference the size value??
        ('''35.00* size''', 'Butterfly 10-14"'),
        ('''25.00* size''', 'Butterfly 16-24"'),
        (2.3, 'Check'),
        (0.19, 'Gate (Open)'),
        (1.15, 'Gate 3/4 Open'),
        (5.6, 'Gate 1/2 Open'),
        (24, 'Gate 1/4 Open'),
        (10, 'Globe'),
        (10, 'Rotary Meter'),
]    
    LINE = [
        ('suc', 'Suction'),
        ('dis', 'Discharge')
    ]

    line_type = models.CharField(max_length = 100, choices = LINE, default = 'dis')
    valve = models.CharField(max_length = 100, choices = VALVES, default = 'Angle')
    name = f"{valve} valve" 
    def __str__(self):
        return self.name

class Fittings(models.Model):

    size = models.FloatField(blank=False)

    FITTINGS =  [ #CERM Reference values, may be copyrighted update later 
        (.9, 'Elbow'),
        (.6, 'LR Elbow'), #Can we reference the size value??
        (0.42, '45 Deg Bend"'),
        (1.6, 'Tee'),
]
    fitting = models.CharField(max_length = 100, choices = FITTINGS, default = 'Angle')
    LINE = [
        ('suc', 'Suction'),
        ('dis', 'Discharge')
    ]

    line_type = models.CharField(max_length = 100, choices = LINE, default = 'dis')
    name = f"{fitting} fitting" 
    def __str__(self):
        return self.name
#processsing a form from a field
#from django.http import HttpResponseRedirect
#from django.shortcuts import render

#from .forms import NameForm

# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, 'name.html', {'form': form})