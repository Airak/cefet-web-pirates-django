from django.urls import path
from . import views

urlpatterns = [
	path('', views.ListaTesourosView.as_view()),
]