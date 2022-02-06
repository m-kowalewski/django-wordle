from django.urls import path

from . import views

app_name='WordleColourResult'
urlpatterns=[
	#ex: /WordleColourResult/
	path('', views.IndexView.as_view(), name='index')
]