from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Question
from .serializers import QuestionSerializer
from rest_framework.exceptions import NotFound
from django.db.models.functions import Random

class QuestionListView(APIView):
    def get(self, request, category, pagination):
        # Get the list of previously returned question IDs from the session (if any)
        previous_questions = request.session.get('previous_questions', [])

        # Fetch random questions, excluding those previously returned
        try:
            queryset = Question.objects.filter(
                Category__name=category
            ).exclude(id__in=previous_questions).order_by(Random())[:pagination]

            if not queryset:
                raise NotFound("Questions not found.")

        except Question.DoesNotExist:
            raise NotFound("Questions not found.")

        # Update the session with the new list of returned question IDs
        new_question_ids = [question.id for question in queryset]
        request.session['previous_questions'] = previous_questions + new_question_ids

        # Serialize the questions and return the response
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)
