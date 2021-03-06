from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    path('topic/<int:topic_id>/records/', views.records_for_topic, name='record_for_topic'),
    path('topic/<int:topic_id>/records/<int:offset>/', views.records_for_topic_offset, name='record_for_topic_offset')
]
