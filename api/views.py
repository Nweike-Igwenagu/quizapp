from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Question
from .serializers import QuestionSerializer
from rest_framework.exceptions import NotFound
import random

# Create your views here.

class QuestionListView(APIView):
    def get(self, request, category, pagination):
        try:
            queryset = Question.objects.filter(Category__name=category).order_by('date_added')[:pagination]
        except Question.DoesNotExist:
            raise NotFound("Questions not found.")

        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)
