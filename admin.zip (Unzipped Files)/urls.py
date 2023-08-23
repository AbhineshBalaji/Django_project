from django.urls import path
from . import views

urlpatterns = [
    path('page/',views.indexhtml, name='indexhtml'),
    path('page/page1/',views.indexhtml3, name='indexhtml3'),
    path('page/indexhtml1/',views.indexhtml1, name='indexhtml1'),
    path('page/indexhtml1/indexhtml2/',views.indexhtml2, name='indexhtml2'),
    path('page/page1/back/',views.back, name='back'),
    path('page/page1/createuser/',views.createuser, name='createuser'),
]