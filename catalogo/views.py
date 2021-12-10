from django.shortcuts import render
from .models import Coche, Fabricante

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_coches = Coche.objects.all().count()

    # The 'all()' is implied by default.
    num_fabricantes = Fabricante.objects.count()

    context = {
        'numero de coches': num_coches,
        'numero de fabricantes': num_fabricantes,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)