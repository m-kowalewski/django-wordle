from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect

from .models import WordleResult

#class IndexView(generic.ListView):
#	template_name = 'WordleColourResult/index.html'
#	context_object_name = 'names'
#	
#	def get_queryset(self):
#		return WordleResult.objects.order_by('-result_date')

def index(request):
	ordered_result = WordleResult.objects.order_by('-result_date')
	return render(request, 'WordleColourResult/index.html', {'names':ordered_result, 'n':range(5)})