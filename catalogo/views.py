from django.shortcuts import render, redirect
from .models import Coche, Fabricante
from django.views.generic import ListView
from catalogo.forms import CocheForm, FabricanteForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.views import generic
import os # para construir las rutas con os.path
from django.conf import settings # para saber donde están los media
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

def todos_coches(request):
    coche = Coche.objects.all().order_by('marca')
    return render(request, 'todos_coches.html',
        context={'coches': coche})


    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

@login_required
def crear_coche(request):
    if request.method == 'POST':
        form = CocheForm(request.POST)
        if form.is_valid():
            form.save()
            # Mensaje para informar éxito redirección
            messages.add_message(request, 
                messages.SUCCESS, 
                'Autor creado.')
            return redirect('/')
    else:
        form = CocheForm()
    datos = {'form': CocheForm()}
    return render(request, 'crear_coche.html', 
        context=datos)

class CochesListView(generic.ListView):
    '''
    Vista genérica para nuestro listado de libros
    '''
    model = Coche
    paginate_by = 15

class FabricantesListView(generic.ListView):
    '''
    Vista genérica para nuestro listado de autores
    '''
    model = Fabricante
    paginate_by = 15
    queryset = Fabricante.objects.all().order_by('nombre_fabricante')

class SearchResultsListView(ListView):
    model = Coche
    context_object_name = 'coches'
    template_name = 'search_results.html'  # No usará la plantilla estándar del ListView
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        if query:
            return Coche.objects.filter(marca__icontains=query)
        return []

class CrearCoche(SuccessMessageMixin, generic.CreateView):
    model = Coche
    #fields = '__all__'
    template_name = 'crear_coche.html'
    success_url = '/'
    form_class = CocheForm
    success_message = "%(marca)s %(modelo)s se ha creado correctamente"


# Creación de autor con CreateVio. Añadimos SuccessMesaageMixin para mensaje de éxito.
class ModificarCoche(SuccessMessageMixin, generic.UpdateView):
    model = Coche
    fields = '__all__'
    template_name = 'modificar_coche.html'
    success_url = '/'
    success_message = "%(marca)s %(modelo)s se ha modificado correctamente"


# Creación de autor con CreateView. Añadimos SuccessMesaageMixin para mensaje de éxito.
class EliminarCoche(generic.DeleteView):
    model = Coche
    success_url = '/catalago/coches' #reverse('listado_autores')
    success_message = "El coche se ha borrado correctamente"
    template_name = 'coche_confirmar_borrado.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EliminarCoche, self).delete(
            request, *args, **kwargs)

class CrearFabricante(SuccessMessageMixin, generic.CreateView):
    model = Fabricante
    #fields = '__all__'
    template_name = 'crear_fabricante.html'
    success_url = '/'
    form_class = FabricanteForm
    success_message = "%(nombre_fabricante)s se ha creado correctamente"


# Creación de autor con CreateVio. Añadimos SuccessMesaageMixin para mensaje de éxito.
class ModificarFabricante(SuccessMessageMixin, generic.UpdateView):
    model = Fabricante
    fields = '__all__'
    template_name = 'modificar_fabricante.html'
    success_url = '/'
    success_message = "%(nombre_fabricante)s se ha modificado correctamente"


# Creación de autor con CreateView. Añadimos SuccessMesaageMixin para mensaje de éxito.
class EliminarFabricante(generic.DeleteView):
    model = Fabricante
    success_url = '/catalago/fabricantes' #reverse('listado_autores')
    success_message = "El fabricante se ha borrado correctamente"
    template_name = 'fabricante_confirmar_borrado.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EliminarCoche, self).delete(
            request, *args, **kwargs)

def subir_archivo(request):
    # Si método es POST (nos están enviando algo)
    if request.method == 'POST':
        # ruta del archivo
        nombre = request.FILES["archivo"].name
        save_path = os.path.join(
            settings.MEDIA_ROOT, nombre)

        # crear archivo con fragmentos
        with open(save_path, "wb") as output_file:
            for chunk in request.FILES["archivo"].chunks():
                output_file.write(chunk)

        return render(request,'subir-archivo.html',
            {'imagen':nombre})
        
    else:
        return render(request, 
            'subir-archivo.html')