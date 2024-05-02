from rest_framework import serializers

from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'user_fk_id', 'description', 'created_at', 'updated_at', 'is_solved', 'difficulty', 'category', 'question_detail', 'example_input', 'example_output', 'fail_count', 'success_count']

class QuestionCreationSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    user_fk_id = serializers.IntegerField()
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    difficulty = serializers.IntegerField()
    category = serializers.CharField(max_length=20)

class GetQuestionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    user_fk_id = serializers.IntegerField()
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_solved = serializers.BooleanField(default=False)
    difficulty = serializers.IntegerField(default=0)
    category = serializers.CharField(max_length=20)
    question_detail = serializers.CharField(default='')
    example_input = serializers.CharField(default='')
    example_output = serializers.CharField(default='')
    fail_count = serializers.IntegerField(default=0)
    success_count = serializers.IntegerField(default=0)