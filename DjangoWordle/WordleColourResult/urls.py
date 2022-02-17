from django.urls import path

from . import views

app_name='WordleColourResult'
urlpatterns=[
	#ex: /WordleColourResult/
	path('', views.index, name='index'),
	path('<int:result_id>', views.index, name='index'),
	#path('', views.IndexView.as_view(), name='index')
	#ex: /WordleColourResult/table/
	path('table/', views.table, name='table'),
	#path('<int:result_id>/saves/', views.saves, name='saves')
]