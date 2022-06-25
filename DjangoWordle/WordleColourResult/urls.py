from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name='WordleColourResult'
urlpatterns=[
    #ex: /WordleColourResult/
    path('', views.index, name='index'),
    #path('<int:result_id>', views.index, name='index'),
    #ex: /WordleColourResult/table/
    #path('table/', views.table, name='table'),
    #path('TableTest/', views.tabletest, name='tabletest'),
    #path('usertable/', views.usertable, name='usertable'),
    path('realusers/', views.real_users, name='real_users'),
    path('favicon.ico',RedirectView.as_view(url='/static/WordleColourResult/images/favicon.ico')),

    #path('<int:result_id>/saves/', views.saves, name='saves')
]
