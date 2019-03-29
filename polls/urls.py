from django.urls import path

from . import views

urlpatterns = [
    path('', views.polls_list, name='polls.index'),
    path('poll/<int:poll_id>', views.poll_page, name='polls.poll_page')
]