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
	TABLE = WordleResult.table_try
	SIMPLE_TABLE = WordleResult.simple_table
	LETTER_TABLE = WordleResult.letter_table
	if request.method == "POST":
		data = request.POST
		print(request.POST)
		print(list(request.POST.items()))
		#q = list(request.POST.items())
		p = data.get('button2')
		if p == None:
			p = data.get('button')
			val = data.get('result')
			print(p, val)
			result = WordleResult.objects.filter(pk=p)
			for a in result:
				print(a.answer)
				a.answer = str(val)
				a.save()
		else:
			print('jestem pięknie w else')
			val = data.get('letters_table')
			print('p: ', p)
			print('val: ', val)
			result = WordleResult.objects.filter(pk=p)
			for a in result:
				print(a.letter_table)
				a.letter_table = str(val)
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
	return render(request, 'WordleColourResult/index.html', {'ANSWERS':ANSWERS, 'names':ordered_result, 'n':range(5), 'table_try':TABLE, 'simple_table':SIMPLE_TABLE, 'letter_table':LETTER_TABLE })

def tabletest(request, result_id=None):
	ordered_result = WordleResult.objects.order_by('-result_date')
	ANSWERS = WordleResult.ANSWERS
	TABLE = WordleResult.table_try
	SIMPLE_TABLE = WordleResult.simple_table
	LETTER_TABLE = WordleResult.letter_table
	if request.method == "POST":
		data = request.POST
		print(request.POST)
		print(list(request.POST.items()))
		#q = list(request.POST.items())
		p = data.get('button2')
		if p == None:
			p = data.get('button')
			val = data.get('result')
			print(p, val)
			result = WordleResult.objects.filter(pk=p)
			for a in result:
				print(a.answer)
				a.answer = str(val)
				a.save()
		else:
			print('jestem pięknie w else')
			val = data.get('letters_table')
			print('p: ', p)
			print('val: ', val)
			result = WordleResult.objects.filter(pk=p)
			for a in result:
				print(a.letter_table)
				a.letter_table = str(val)
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
	return render(request, 'WordleColourResult/tabletest.html', {'ANSWERS':ANSWERS, 'names':ordered_result, 'n':range(5), 'table_try':TABLE, 'simple_table':SIMPLE_TABLE, 'letter_table':LETTER_TABLE })


def table(request):
	instance = GraphicTable()
	ordered_result = WordleResult.objects.order_by('-result_date')
	answer = GraphicTable.objects
	#answer = instance.
	return render(request, 'WordleColourResult/table.html', {'answer':answer, 'names':ordered_result, 'n':range(5)})#,{'answer':answer})#, 'table':table})

