from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User
import datetime

class UserResult(models.Model):
    ''' main class of project '''
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    date_update = models.DateField(default=datetime.date.today)
    time_update = models.TimeField(default=datetime.time(0,0,0))
    result_letters = models.CharField(max_length=35, default='BBBBBEBBBBBEBBBBBEBBBBBEBBBBBEBBBBB')
    def __str__(self):
        return str(self.owner)

class WordleResult(models.Model):
    ''' old class for testing '''
    user_name = models.CharField(max_length=100)
    result_date = models.DateTimeField('date solved')
    ANSWERS = (
        ('G', 'Green'),
        ('Y', 'Yellow'),
        ('B', 'Black'),
    )
    table_width = 5
    table_height = 6
    table_try = [[0 for x in range(5)] for y in range(6)]
    table_try[3][3] = 1
    #table_field_try = [[models.CharField(max_length=1, choices=ANSWERS, default='B') for x in range(2)] for y in range(3)]
    simple_field = models.CharField(max_length=1, choices=ANSWERS, default='B')
    simple_row = []
    for x in range(3):
        simple_row.append(simple_field)
    simple_table = []
    for y in range(2):
        simple_table.append(simple_row)
    letter_table = models.CharField(max_length=35, default='BBBBBEBBBBBEBBBBBEBBBBBEBBBBBEBBBBB')
    table_text = 'there will be a table'
    answer = models.CharField(max_length=1, choices=ANSWERS, default='B')
    def __str__(self):
        return self.user_name

class GraphicTable(models.Model):
    ''' class under work '''
    wordleresult = models.ForeignKey(WordleResult, on_delete=models.CASCADE)
    table = 'there will be a table'
