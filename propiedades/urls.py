

from django.urls import path
from . import views

app_name = 'propiedades' 

urlpatterns = [
    path('', views.index, name='index'), 
    path('about/', views.about, name='about'), 
    path('propiedades/', views.PropiedadListView.as_view(), name='propiedad_list'), 
    path('propiedades/<int:pk>/', views.PropiedadDetailView.as_view(), name='propiedad_detail'), 
    path('propiedades/nueva/', views.PropiedadCreateView.as_view(), name='propiedad_create'), 
    path('propiedades/<int:pk>/editar/', views.PropiedadUpdateView.as_view(), name='propiedad_update'), 
    path('propiedades/<int:pk>/eliminar/', views.PropiedadDeleteView.as_view(), name='propiedad_delete'), 
]
