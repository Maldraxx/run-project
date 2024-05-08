import requests
from constants import GET, MAKE_QUESTION_URL, POST, SWAGGER_QUESTION_TAG
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import QuestionSerializer


class QuestionViewSet(viewsets.GenericViewSet):
    serializer_class = QuestionSerializer
    
    @swagger_auto_schema(tags=[SWAGGER_QUESTION_TAG])
    @action(detail=False, methods=[POST])
    def make_qustion(self, request):
        # serializer = QuestionSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # question_params = serializer.get_fields()
        
        category = request.data.get("category", "")
        difficulty = request.data.get("difficulty", "")

        data = {
            "difficulty": difficulty,
            "category": category
        }
        response = requests.post(MAKE_QUESTION_URL, json=data)
        response_data = response.json()
        print(response_data)
        return Response("Done : Create Question")