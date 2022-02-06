from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import WordleResult

class IndexView(generic.ListView):
	template_name = 'WordleColourResult/index.html'
	context_object_name = 'names'
	
	def get_queryset(self):
		return WordleResult.objects.order_by('-result_date')