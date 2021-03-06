from django.urls import path
from . import views

urlpatterns = [
	path('', views.ListaTesourosView.as_view(), name='lista'),
	path('inserir', views.SalvarTesouroView.as_view(), name='inserir'),
	path('deletar/<int:pk>', views.DeletarTesouroView.as_view(), name='deletar'),
	path('editar/<int:pk>', views.SalvarTesouroView.as_view(), name='editar'),
]