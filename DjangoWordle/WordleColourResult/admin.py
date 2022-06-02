from django.contrib import admin

from .models import WordleResult, GraphicTable, UserResult

admin.site.register(WordleResult)
admin.site.register(GraphicTable)
admin.site.register(UserResult)