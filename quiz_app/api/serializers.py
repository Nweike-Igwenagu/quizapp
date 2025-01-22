from rest_framework import serializers
from django.utils.html import strip_tags
import html
from core.models import (
    Question,
    Category,
)

class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    
    class Meta:
        model = Question
        fields = ['id', 'question', 'options', 'correct_answer', 'category']

    def get_options(self, obj):
        return [obj.option_1, obj.option_2, obj.option_3, obj.option_4]
    
    def get_category(self, obj):
        return Category.objects.get(id=obj.Category.id).name