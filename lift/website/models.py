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
        (130, 'Acrylonite Butadiene Styrene'),
        (190, 'Aluminum'),
        (140, 'Asbestos Cement')
]
    material = models.CharField(max_length = 100, choices = MATERIALS, default = 'Aluminum')

    inner_diameter = models.DecimalField(max_digits = 8, decimal_places=2)
    

    OUTLET = [
        ('suc', 'suction'),
        ('dis', 'discharge')
    ]

    outlet_type = models.CharField(max_length = 100, choices = OUTLET, default = 'dis')
    
    name = f"{inner_diameter} {material} pipe" 


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