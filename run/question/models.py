from django.db import models


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    user_fk_id = models.ForeignKey('accounts.User', on_delete=models.CASCADE, to_field='id')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_solved = models.BooleanField(default=False)
    difficulty = models.IntegerField(default=0)
    category = models.CharField(max_length=20)
    question_detail = models.TextField(default='')
    example_input = models.TextField(default='')
    example_output = models.TextField(default='')
    fail_count = models.IntegerField(default=0)
    success_count = models.IntegerField(default=0)

    @classmethod
    def create_question(cls, title, user_fk_id, description, difficulty, category, question_detail, example_input, example_output):
        question = cls(title=title, user_fk_id=user_fk_id, description=description, difficulty=difficulty, category=category, question_detail=question_detail, example_input=example_input, example_output=example_output)
        question.save()
        return question