from django.urls import path
from . import views

urlpatterns = [
    path('populate-questions/', views.populate_db, name='populate_questions'),
]
