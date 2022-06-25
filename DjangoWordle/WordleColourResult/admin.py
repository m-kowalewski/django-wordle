from django.contrib import admin

from .models import WordleResult, GraphicTable, UserResult, DateResult, RealUserResult

admin.site.register(WordleResult)
admin.site.register(GraphicTable)
admin.site.register(UserResult)
admin.site.register(DateResult)
admin.site.register(RealUserResult)
