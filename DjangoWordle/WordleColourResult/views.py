from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect

from .models import WordleResult, GraphicTable

#class IndexView(generic.ListView):
#	template_name = 'WordleColourResult/index.html'
#	context_object_name = 'names'
#	
#	def get_queryset(self):
#		return WordleResult.objects.order_by('-result_date')

def index(request, result_id=None):
	ordered_result = WordleResult.objects.order_by('-result_date')
	ANSWERS = WordleResult.ANSWERS
	if request.method == "POST":
		data = request.POST
		print(request.POST)
		print(list(request.POST.items()))
		#q = list(request.POST.items())
		p = data.get('button')
		val = data.get('result')
		print(p, val)
		result = WordleResult.objects.filter(pk=p)
		for a in result:
			print(a.answer)
			a.answer = str(val)
			a.save()
	elif request.method == "GET":
		data = request.GET
		print(request.GET)
		print(list(request.GET.items()))
		#q = list(request.POST.items())
		p = data.get('button')
		val = data.get('result')
		print(p, val)
		result = WordleResult.objects.filter(pk=p)
		for a in result:
			print(a.answer)
			a.answer = str(val)
			a.save()		
	return render(request, 'WordleColourResult/index.html', {'ANSWERS':ANSWERS, 'names':ordered_result, 'n':range(5)})


def table(request):
	instance = GraphicTable()
	ordered_result = WordleResult.objects.order_by('-result_date')
	answer = GraphicTable.objects
	#answer = instance.
	return render(request, 'WordleColourResult/table.html', {'answer':answer, 'names':ordered_result, 'n':range(5)})#,{'answer':answer})#, 'table':table})

