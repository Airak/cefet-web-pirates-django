from django.shortcuts import render
from django.views import View
from django.db.models import F, ExpressionWrapper, DecimalField

from .models import Tesouro

class ListaTesourosView(View):
	def get(self, request):
		template_name = 'lista_tesouros.html'

		lista_tesouros = Tesouro.objects.annotate(total=ExpressionWrapper(F('preco')*F('quantidade'), output_field=DecimalField(max_digits=10, decimal_places=2,blank=True)))

		total_geral = 0
		for tesouro in lista_tesouros:
			total_geral = total_geral + tesouro.total

		context = {
			'lista_tesouros': lista_tesouros,
			'total_geral': total_geral
		}

		return render(request, template_name, context)