""" views file for WordleColourResult app """
import datetime
import operator
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import DateResult, WordleResult, GraphicTable, UserResult, RealUserResult

"""
class IndexView(generic.ListView):
    template_name = 'WordleColourResult/index.html'
    context_object_name = 'names'
    def get_queryset(self):
        return WordleResult.objects.order_by('-result_date')
"""


def real_users(request):
    """ Function for REAL USERS """
    # users_key = {'user1': '1', 'user2': '2', 'user3': '3'}
    # real_result = RealUserResult.objects.all()
    if request.method == "POST":
        data = request.POST
        button_2 = data.get('button2')
        val = data.get('new_result_letters')
        print('REQUESTED USER: ', request.user)
        print('REQUEST POST: ', request.POST)
        print('LIST REQUEST.POST.ITEMS: ', list(request.POST.items()))
        print('button_2: ', button_2)
        print('val: ', val)
        result = RealUserResult()
        result.owner = User.objects.get(username=button_2)
        result.result_date = datetime.date.today()
        result.result_time = datetime.datetime.now()
        result.result_letters = str(val)
        result.save()
    elif request.method == "GET":
        data = request.GET
        print(data)
        print(list(data.items()))
    real_result = RealUserResult.objects.all()
    unique_owners = []
    [
        unique_owners.append(item.owner)
        for item in real_result
        if item.owner not in unique_owners
    ]
    real_result_ordered = sorted(
        real_result, key=operator.attrgetter('result_date', 'result_time'), reverse=True
    )
    real_result_ordered_clean = []
    [
        real_result_ordered_clean.append(item)
        for item in real_result_ordered
        if str(item) not in str(real_result_ordered_clean)
    ]
    today_result = []
    for item in real_result_ordered_clean:
        if item.owner in unique_owners:
            today_result.append(item)
            unique_owners.remove(item.owner)
            if len(unique_owners) == 0:
                break
    return render(
        request,
        'WordleColourResult/real_users.html',
        {
            'TR': today_result, 'RR': real_result_ordered_clean, 'n': range(5)
        }
    )


def usertable(request):
    """ main part of project """
    user_result = UserResult.objects.all()
    date_result = DateResult.objects.all()
    if request.method == "POST":
        data = request.POST
        button_2 = data.get('button2')
        val = data.get('new_result_letters')  
        print('REQUESTED USER: ', request.user)
        print('REQUEST POST: ', request.POST)
        print('LISTA REQUEST.POST.ITEMS: ', list(request.POST.items()))
        print('button_2: ', button_2)
        print('val: ', val)
        result = UserResult.objects.filter(pk=button_2)[0]
        result.result_letters = str(val)
        result.date_update = datetime.date.today()
        result.time_update = datetime.datetime.now()
        result.save()
        result_d = DateResult()
        result_d.owner = result.owner
        result_d.result_date = result.date_update
        result_d.result_time = result.time_update
        result_d.result_letters = result.result_letters
        result_d.save()
    elif request.method == "GET":
        data = request.GET
        print(data)
        print(list(data.items()))
    date_result = DateResult.objects.all()
    date_result_ordered = sorted(date_result, key=operator.attrgetter('result_date', 'result_time'), reverse=True)
    date_result_ordered_clean = []
    [
        date_result_ordered_clean.append(item)
        for item in date_result_ordered
        if str(item) not in str(date_result_ordered_clean)
    ]
    return render(
        request,
        'WordleColourResult/usertable.html',
        {
            'UR': user_result, 'DR': date_result_ordered_clean, 'n': range(5)
        }
    )


def index(request, result_id=None):
    """ old function """
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
        button_2 = data.get('button2')
        if button_2 is None:
            button_2 = data.get('button')
            val = data.get('result')
            print(button_2, val)
            result = WordleResult.objects.filter(pk=button_2)
            for item in result:
                print(item.answer)
                item.answer = str(val)
                item.save()
        else:
            print('jestem pięknie w else')
            val = data.get('letters_table')
            print('button_2: ', button_2)
            print('val: ', val)
            result = WordleResult.objects.filter(pk=button_2)
            for item in result:
                print(item.letter_table)
                item.letter_table = str(val)
                item.save()
    elif request.method == "GET":
        data = request.GET
        print(request.GET)
        print(list(request.GET.items()))
        #q = list(request.POST.items())
        button_2 = data.get('button')
        val = data.get('result')
        print(button_2, val)
        result = WordleResult.objects.filter(pk=button_2)
        for item in result:
            print(item.answer)
            item.answer = str(val)
            item.save()
    return render(
        request,
        'WordleColourResult/index.html',
        {
            'ANSWERS': ANSWERS,
            'names': ordered_result,
            'n': range(5),
            'table_try': TABLE,
            'simple_table': SIMPLE_TABLE,
            'letter_table': LETTER_TABLE
        }
    )


def tabletest(request, result_id=None):
    """ function for testing """
    ordered_result = WordleResult.objects.order_by('-result_date')
    ANSWERS = WordleResult.ANSWERS
    TABLE = WordleResult.table_try
    SIMPLE_TABLE = WordleResult.simple_table
    LETTER_TABLE = WordleResult.letter_table
    if request.method == "POST":
        data = request.POST
        print(request.POST)
        print(list(request.POST.items()))
        button_2 = data.get('button2')
        if button_2 is None:
            button_2 = data.get('button')
            val = data.get('result')
            print(button_2, val)
            result = WordleResult.objects.filter(pk=button_2)
            for item in result:
                print(item.answer)
                item.answer = str(val)
                item.save()
        else:
            print('jestem pięknie w else')
            val = data.get('letters_table')
            print('button_2: ', button_2)
            print('val: ', val)
            result = WordleResult.objects.filter(pk=button_2)
            for item in result:
                print(item.letter_table)
                item.letter_table = str(val)
                item.save()
    elif request.method == "GET":
        data = request.GET
        print(request.GET)
        print(list(request.GET.items()))
        button_2 = data.get('button')
        val = data.get('result')
        print(button_2, val)
        result = WordleResult.objects.filter(pk=button_2)
        for item in result:
            print(item.answer)
            item.answer = str(val)
            item.save()
    return render(
        request,
        'WordleColourResult/tabletest.html',
        {
            'ANSWERS': ANSWERS,
            'names': ordered_result,
            'n': range(5),
            'table_try': TABLE,
            'simple_table': SIMPLE_TABLE,
            'letter_table': LETTER_TABLE
        }
    )


def table(request):
    """ generate only table """
    #instance = GraphicTable()
    ordered_result = WordleResult.objects.order_by('-result_date')
    answer = GraphicTable.objects
    #answer = instance.
    return render(
            request,
            'WordleColourResult/table.html',
            {
                'answer': answer,
                'names': ordered_result,
                'n': range(5)
            }
        )#,{'answer':answer})#, 'table':table})
