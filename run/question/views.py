from constants import GET, SWAGGER_QUESTION_TAG
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import QuestionSerializer


class QuestionViewSet(viewsets.GenericViewSet):
    serializer_class = QuestionSerializer
    
    @swagger_auto_schema(tags=[SWAGGER_QUESTION_TAG])
    @action(detail=False, methods=[GET])
    def test_url(self, request):
        return Response("Test URL")