from django.shortcuts import render
from django.http import *
from django.urls import reverse

# Create your views here.

courses_list=[
    {'id':1,'name':'python','time':100,'price':0},
    {'id':2,'name':'django','time':70,'price':2340000},
    {'id':3,'name':'front','time':50,'price':500000},
    {'id':4,'name':'js','time':120,'price':500000},
    {'id':5,'name':'c++','time':300,'price':10000000},
    {'id':6,'name':'c#','time':400,'price':1500000}]

#تمرینات قبل از فایل 5 ام
def lists(request):
    data=""
    for items in courses_list:
        url=reverse('corse-detail',args=[items['id']])
        data=data + f"<a href='{url}' target='_blank'>{items['name']}</a>" + '<br>'
    return HttpResponse(data)

def corse_detail(request,id):
    return HttpResponse(f'this is corse with id {id}')


# تمرینات فایل 5 به بعد
def course_list(request):
    return render(request,'course/list.html',context={'data':courses_list})

def param_name(request,name):
    
    data=''
    for items in courses_list:
        if name==items['name']:
            url=reverse('corse-detail',args=[items['id']])
            data=data+f"<a href='{url}'>{items['name']}</a>" + '<br>'
            break
            

    return HttpResponse(data)
    
# تمرینات فایل 6
def detail2(request):
    req=request.GET.get('id')
    req=int()
    for item in courses_list:
        if req==item['id']:
            return reverse('<corse-detail>',args=[item['id']])
    return render(request,'course/404.html')
    
def search_detail(request,search):
    data={}
    for items in courses_list:
        if search==items['name']:
            data=items

    return render(request,'course/search.html',context={'data':data})