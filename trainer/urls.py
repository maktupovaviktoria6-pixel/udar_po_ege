from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update_progress/<int:word_id>/', views.update_progress, name='update_progress'),
    path('learned/', views.learned_list, name='learned'),
]


