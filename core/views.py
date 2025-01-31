from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Question, Category
from datetime import datetime

def populate_db(request):
    # Fetch the Maths category (ensure it exists in your database)
    english = Category.objects.get(name="english")
    maths = Category.objects.get(name="maths")
    science = Category.objects.get(name="science")
    
    question_data = []
    
    # Insert questions into the database
    created_count = 0
    for data in question_data:
        if not Question.objects.filter(question=data['question']).exists():
            Question.objects.create(
                question=data['question'],
                option_1=data['option_1'],
                option_2=data['option_2'],
                option_3=data['option_3'],
                option_4=data['option_4'],
                correct_answer=data['correct_answer'],
                Category=data['Category'],
                last_modified=datetime.now(),
                date_added=datetime.now()
            )
            created_count += 1

    return HttpResponse(f"{created_count} questions added to the database.")
