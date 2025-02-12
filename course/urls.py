from django.urls import path
from . import views
urlpatterns=[
    path('list/',views.lists),
    path('detail/<id>',views.corse_detail,name='corse-detail'),
    path('course_list',views.course_list),
    path('param/<str:name>',views.param_name),
    path('detail2/',views.detail2),
    path('search-detail/<search>',views.search_detail)
    ]