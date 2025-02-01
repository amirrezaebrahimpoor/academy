from django.shortcuts import render
from django.http import *
# Create your views here.

courses_list=[
    {'id':1,'name':'python course','time-hours':100,'price':0},
    {'id':2,'name':'django course','time-hours':70,'price':2340000},
    {'id':3,'name':'front course','time-hours':50,'price':500000},
    {'id':4,'name':'js course','time-hours':120,'price':500000},
    {'id':5,'name':'c++ course','time-hours':300,'price':10000000}]


def lists(request):
    i=courses_list
    
    return HttpResponse(f'{i['id']}---> course:{i['name']} with pendding {i['time-hours']} hours.you can get with {i['price']}.<br>')