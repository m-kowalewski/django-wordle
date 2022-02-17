from django.db import models

from django.db import models
from django.utils import timezone
from django.contrib import admin


class WordleResult(models.Model):
	user_name = models.CharField(max_length=100)
	result_date = models.DateTimeField('date solved')
	table_text = 'there will be a table'
	ANSWERS = (
		('G', 'Green'),
		('Y', 'Yellow'),
		('B', 'Black'),
	)
	answer = models.CharField(max_length=1, choices=ANSWERS, default='B')
	def __str__(self):
		return self.user_name

class GraphicTable(models.Model):
	wordleresult = models.ForeignKey(WordleResult, on_delete=models.CASCADE)
	
	table = 'there will be a table'