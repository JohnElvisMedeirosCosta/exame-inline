from django.urls import path
from .views import exam_list

app_name = 'exam'

urlpatterns = [
    path('', exam_list, name='exam_list'),
]