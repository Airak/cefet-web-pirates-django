from django.shortcuts import render
from django.views import View

from .models import Tesouro


class ListaTesourosView():

	def get():
		template_name = 'lista_tesouros.html'
		context = []

		context['lista_tesouros'] = Tesouro.objects.all()
		valor_total = Tesouro.objects.annotate(total=ExpressionWrapper(F('valor')*F('quantidade'),\
				output_field=DecimalField(max_digits=10,\
										decimal_places=2,\
										blank=True)\
										)\
		)

		total_geral = 0
		for valor in valor_total:
			total_geral = total_geral + valor

		context['total_geral'] = total_geral

		return render(request, context, template_name)

