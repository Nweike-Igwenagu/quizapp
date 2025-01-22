from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    last_modified = models.DateTimeField(auto_now=True, editable=False)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self):
        return self.name

    
class Question(models.Model):
    question = models.CharField(max_length=225)
    option_1 = models.CharField(max_length=225)
    option_2 = models.CharField(max_length=225)
    option_3 = models.CharField(max_length=225)
    option_4 = models.CharField(max_length=225)
    correct_answer = models.CharField(max_length=225)
    Category = models.ForeignKey('Category', related_name='category', on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True, editable=False)
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self):
        return self.question