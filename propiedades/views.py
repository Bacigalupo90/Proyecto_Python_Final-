

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Propiedad
from .forms import PropiedadForm, PropiedadSearchForm
import datetime 


class PropiedadBaseView:
   
    model = Propiedad
    context_object_name = 'propiedades'
    template_name = 'propiedades/propiedad_list.html' 

class PropiedadListView(PropiedadBaseView, ListView):
    
    template_name = 'propiedades/propiedad_list.html'
    paginate_by = 10 

    def get_queryset(self):
        queryset = super().get_queryset()
        form = PropiedadSearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            if query:
                queryset = queryset.filter(titulo__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = PropiedadSearchForm(self.request.GET)
        if not context['propiedades'] and self.request.GET.get('query'):
            context['no_results_message'] = "No se encontraron propiedades que coincidan con su búsqueda."
        elif not context['propiedades'] and not self.request.GET.get('query'):
            context['no_results_message'] = "Actualmente no hay propiedades publicadas."
        return context

class PropiedadDetailView(PropiedadBaseView, DetailView):
    
    template_name = 'propiedades/propiedad_detail.html'
    context_object_name = 'propiedad'

class PropiedadCreateView(LoginRequiredMixin, PropiedadBaseView, CreateView):
   
    template_name = 'propiedades/propiedad_form.html'
    form_class = PropiedadForm
    success_url = reverse_lazy('propiedades:propiedad_list')

    def form_valid(self, form):
        
        return super().form_valid(form)

class PropiedadUpdateView(LoginRequiredMixin, PropiedadBaseView, UpdateView):
   
    template_name = 'propiedades/propiedad_form.html'
    form_class = PropiedadForm
    success_url = reverse_lazy('propiedades:propiedad_list')

class PropiedadDeleteView(LoginRequiredMixin, PropiedadBaseView, DeleteView):
    
    template_name = 'propiedades/propiedad_confirm_delete.html'
    success_url = reverse_lazy('propiedades:propiedad_list')

def index(request):
    
    return render(request, 'propiedades/index.html')



def about(request):
   
    return render(request, 'propiedades/about.html')