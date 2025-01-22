from django.contrib import admin
from django.urls import path, include
from .views import QuestionListView

urlpatterns = [
    path("questions/<str:category>/<int:pagination>", QuestionListView.as_view(), name="questions")
]